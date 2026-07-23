"""
Insurance Knowledge Base

Static insurance information used by the assistant.
"""

INSURANCE_DATA = {
    "health": {
        "waiting_period":
            "Most health insurance policies have a 30-day initial waiting period.",

        "renewal":
            "Health insurance policies can usually be renewed online before expiry.",

        "claims":
            "Cashless claims require treatment at a network hospital. Reimbursement claims require submitting bills.",

        "cashless":
            "Cashless treatment is available only at network hospitals."
    },

    "motor": {
        "renewal":
            "Motor insurance can be renewed online before policy expiry.",

        "claims":
            "Motor claims require vehicle inspection and supporting documents.",

        "accident":
            "Report accidents immediately and inform the insurer."
    },

    "travel": {
        "medical":
            "Travel insurance covers emergency medical expenses abroad.",

        "baggage":
            "Coverage may include baggage delay or loss.",

        "visa":
            "Some countries require valid travel insurance for visa approval."
    }
}