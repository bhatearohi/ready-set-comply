# Ready Steady Comply

**Audit prep, without the panic.**

Cyber Essentials Plus prep shouldn't mean scrambling the week before your audit.
Ready Steady Comply generates a plain-English readiness checklist — what you need,
what auditors will ask for, and where SMEs usually get caught out — so you know
exactly where you stand before audit day arrives.

## What it does (v1)

Ready Steady Comply currently covers **Cyber Essentials Plus**, generating a
checklist across the five core control themes:

- Firewalls and Internet Gateways
- Secure Configuration
- Security Update Management (Patch Management)
- User Access Control
- Malware Protection

More standards — DCC, ISO 27001, ISO 42001 — are planned next, incorporating
feedback from this first version.

## Running it locally

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
streamlit run app.py
```

## Feedback

This is an early version, built to get real reactions from people who've
actually lived the audit-panic problem. Issues, comments and honest feedback
are very welcome.

## Roadmap

- [ ] DCC (Digital Cyber Compliance)
- [ ] ISO/IEC 27001
- [ ] ISO/IEC 42001
- [ ] Personalisation based on company profile (size, sector, tooling)

---

Built by Arohi Bhate, grounded in MSc dissertation research into cyber law
and compliance burden for SMEs.
