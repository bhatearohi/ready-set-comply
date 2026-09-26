"""
Cyber Essentials Plus (CE+) control themes, structured as data.

This is the 'brain' of the runbook tool. Each of the five CE+ control
themes has: a plain-English description, what auditors typically want
to see as evidence, and the common panic points SMEs run into.

Edit the "panic_points" list for each theme based on your own
CE+ knowledge and, ideally, real feedback from SME owners — that's
what will make this genuinely useful rather than generic.
"""

CE_PLUS_CONTROLS = {
    "Firewalls and Internet Gateways": {
        "description": (
            "Every device connected to the internet must be protected by "
            "a correctly configured firewall or equivalent network device."
        ),
        "required_evidence": [
            "List of all boundary firewalls / gateway devices in scope",
            "Firewall rule configuration showing default-deny inbound rules",
            "Evidence that default admin passwords have been changed",
            "Confirmation that admin interfaces are not exposed to the internet",
        ],
        "panic_points": [
            # e.g. "Teams often don't know which cloud services count as 'in scope'",
        ],
    },
    "Secure Configuration": {
        "description": (
            "Computers and network devices must be configured to reduce "
            "vulnerabilities and provide only the services required."
        ),
        "required_evidence": [
            "Build standard / hardening checklist for devices in scope",
            "Evidence unnecessary software and accounts have been removed",
            "Screenshot or export of device configuration settings",
            "Autorun / autoplay disabled where applicable",
        ],
        "panic_points": [],
    },
    "Security Update Management (Patch Management)": {
        "description": (
            "All software must be kept up to date, with high-risk or "
            "critical vulnerabilities patched within 14 days of release."
        ),
        "required_evidence": [
            "Patch management policy or process document",
            "Evidence of patching cadence (screenshots, patch logs, tooling reports)",
            "List of software in scope, including versions",
            "Confirmation no unsupported/end-of-life software is in use",
        ],
        "panic_points": [],
    },
    "User Access Control": {
        "description": (
            "Access to data and services must be limited to those who "
            "need it, with accounts and admin rights properly managed."
        ),
        "required_evidence": [
            "User account list with role justification",
            "Evidence of a joiners/movers/leavers process",
            "Admin account list, separate from standard user accounts",
            "Password policy and MFA configuration evidence",
        ],
        "panic_points": [],
    },
    "Malware Protection": {
        "description": (
            "Devices must be protected from malware via anti-malware "
            "software, application allow-listing, or sandboxing."
        ),
        "required_evidence": [
            "Anti-malware software deployment evidence across all devices",
            "Confirmation signatures/definitions update automatically",
            "Scan configuration and scheduling evidence",
            "Web filtering / malicious site blocking evidence, if applicable",
        ],
        "panic_points": [],
    },
}
