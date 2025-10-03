#!/usr/bin/python3
import xml.etree.ElementTree as ET
from datetime import datetime
import sys

def parse_dmarc_report(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    def ts_to_date(ts):
        return datetime.utcfromtimestamp(int(ts)).strftime('%A, %B %d, %Y')
    
    metadata = root.find('report_metadata')
    org_name = metadata.findtext('org_name')
    email = metadata.findtext('email')
    help_url = metadata.findtext('extra_contact_info')
    report_id = metadata.findtext('report_id')
    begin = ts_to_date(metadata.find('date_range').findtext('begin'))
    end = ts_to_date(metadata.find('date_range').findtext('end'))

    policy = root.find('policy_published')
    domain = policy.findtext('domain')
    adkim = policy.findtext('adkim')
    aspf = policy.findtext('aspf')
    p = policy.findtext('p')
    sp = policy.findtext('sp')
    pct = policy.findtext('pct')

    record = root.find('record')
    source_ip = record.find('row').findtext('source_ip')
    count = record.find('row').findtext('count')
    envelope_to = record.find('identifiers').findtext('envelope_to')
    disposition = record.find('row').find('policy_evaluated').findtext('disposition')
    dkim_result = record.find('row').find('policy_evaluated').findtext('dkim')
    spf_result = record.find('row').find('policy_evaluated').findtext('spf')
    header_from = record.find('identifiers').findtext('header_from')
    spf_domain = record.find('auth_results').find('spf').findtext('domain')
    spf_scope = record.find('auth_results').find('spf').findtext('scope')
    spf_auth_result = record.find('auth_results').find('spf').findtext('result')

    print(f"\n🧾 Report Metadata")
    print(f"- Reporting Organization: {org_name}")
    print(f"- Contact Email: {email}")
    print(f"- Help URL: {help_url}")
    print(f"- Report ID: {report_id}")
    print(f"- Date Range: {begin} to {end}")

    print(f"\n📜 Published DMARC Policy (for {domain})")
    print(f"- DKIM Alignment: {adkim}")
    print(f"- SPF Alignment: {aspf}")
    print(f"- Policy: {p}")
    print(f"- Subdomain Policy: {sp}")
    print(f"- Percentage Applied: {pct}%")

    print(f"\n📊 Record of Failed Authentication")
    print(f"- Source IP: {source_ip}")
    print(f"- Message Count: {count}")
    print(f"- Disposition: {disposition}")
    print(f"- DKIM Result: {dkim_result}")
    print(f"- SPF Result: {spf_result}")
    print(f"- Header From: {header_from}")
    print(f"- Envelope To: {envelope_to if envelope_to else 'Not provided'}")
    print(f"- SPF Auth Result: Domain={spf_domain}, Scope={spf_scope}, Result={spf_auth_result}")

if __name__ == "__main__":
    parse_dmarc_report(sys.argv[1])
