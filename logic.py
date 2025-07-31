def get_recommendation(data):
    try:
        sip = int(data.get("sip") or 0)
        tenure = int(data.get("tenure") or 0)
        risk = (data.get("risk") or "").lower()

        if risk == "high" and tenure >= 7 and sip >= 10000:
            return {
                "fund": "Quant Flexicap Fund",
                "reason_en": "High risk profile, long tenure and good SIP size. Flexicap gives exposure to multi-cap opportunities.",
                "reason_hi": "हाई रिस्क प्रोफाइल, लंबी अवधि और अच्छा SIP. फ्लेक्सीकैप फंड मल्टीकैप अवसर देता है।"
            }
        elif risk == "medium":
            return {
                "fund": "ICICI Prudential Balanced Advantage Fund",
                "reason_en": "Balanced fund suited for medium risk profiles.",
                "reason_hi": "मीडियम रिस्क प्रोफाइल के लिए संतुलित फंड उपयुक्त है।"
            }
        else:
            return {
                "fund": "HDFC Short Term Debt Fund",
                "reason_en": "Lower risk and short-term investment horizon. Safer option.",
                "reason_hi": "कम जोखिम और कम अवधि के लिए सुरक्षित विकल्प।"
            }
    except Exception as e:
        return {
            "fund": "Error",
            "reason_en": f"Something went wrong: {str(e)}",
            "reason_hi": "सर्वर में कोई समस्या आई है। कृपया बाद में प्रयास करें।"
        }
