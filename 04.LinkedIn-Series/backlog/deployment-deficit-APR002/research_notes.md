# Research Notes: APR002 — The Deployment Deficit

## Case Study Evidence (12 Companies)

### 1. Air Canada (2024)

- Chatbot fabricated a bereavement fare refund policy that didn't exist
- Customer relied on it, booked flights, was denied refund
- Canadian tribunal ruled Air Canada liable for its chatbot's statements
- Remedy: refund + damages
- **Failure layer**: L2 (output filtering), L3 (human checkpoint)

### 2. Zillow (2021)

- Zestimate-powered iBuying algorithm systematically overvalued homes
- $881M inventory writedown
- ~2,000 employees laid off (25% of workforce)
- CEO admitted the algorithm "had a wider error rate than we were comfortable with"
- **Failure layer**: L5 (monitoring), L4 (rollback), L6 (governance)

### 3. Amazon (2018, disclosed)

- Internal AI recruiting tool trained on 10 years of resumes (predominantly male)
- Systematically penalized resumes containing the word "women's"
- Downgraded graduates of two all-women's colleges
- Scrapped after 4 years of internal use
- **Failure layer**: L1 (input validation — biased training data), L6 (governance)

### 4. Google Gemini (2024)

- Image generation produced historically inaccurate results (diverse Nazis, etc.)
- Paused image generation feature entirely
- Stock dropped ~$90B in market cap in a single trading session
- **Failure layer**: L2 (output filtering), L6 (governance — launched without adequate review)

### 5. Chevrolet Dealership (2023)

- Watsonville Chevrolet deployed a ChatGPT-powered sales bot
- Users tricked it into agreeing to sell a 2024 Tahoe for $1
- Screenshots went viral on social media
- **Failure layer**: L1 (input validation), L2 (output filtering), L3 (human checkpoint)

### 6. DPD (2024)

- Parcel delivery company's AI chatbot swore at a customer
- Customer prompted it to "disregard previous instructions"
- Bot called DPD "the worst delivery firm in the world" and used profanity
- Made international news
- **Failure layer**: L1 (input validation — prompt injection), L2 (output filtering)

### 7. McDonald's (2024)

- AI-powered drive-through ordering system by IBM
- Misheard orders, added items customers didn't request
- Videos of failures went viral (bacon on ice cream, hundreds of chicken nuggets)
- Pulled from 100+ locations
- **Failure layer**: L1 (input validation — speech recognition), L3 (human checkpoint)

### 8. iTutorGroup (2023)

- AI hiring system automatically rejected applicants over age 55 (women) and 60 (men)
- EEOC sued and settled for $365,000
- Over 200 qualified applicants were illegally screened out
- **Failure layer**: L1 (input validation — discriminatory rules), L6 (governance)

### 9. Samsung (2023)

- Engineers on at least 3 separate occasions pasted proprietary source code into ChatGPT
- Included semiconductor testing sequences and internal meeting notes
- Samsung banned all generative AI tools company-wide
- **Failure layer**: L6 (governance — no usage policy), L1 (input validation — no DLP)

### 10. NEDA — National Eating Disorders Association (2023)

- Replaced human helpline counselors with AI chatbot "Tessa"
- Tessa gave harmful diet and weight loss advice to people with eating disorders
- Organization shut down the chatbot and the helpline entirely
- **Failure layer**: L2 (output filtering), L3 (human checkpoint), L6 (governance)

### 11. Microsoft Tay (2016)

- Twitter chatbot designed to learn from conversations
- Learned hate speech, racism, and extremist language within 16 hours
- Microsoft killed it in under 24 hours
- **Failure layer**: L1 (input validation), L2 (output filtering), L5 (monitoring)

### 12. Unity (2023)

- ML-driven per-install pricing model announced without adequate stakeholder input
- Developer community revolt: open letters, pulled games, boycott threats
- CEO John Riccitiello resigned
- Stock price cratered
- **Failure layer**: L6 (governance), L5 (monitoring — no feedback mechanism pre-launch)

## Cross-Cutting Pattern Analysis

**Common thread**: Not one failure was caused by poor model accuracy. Every failure was a systems integration problem at the deployment layer.

**Most common missing layers**:

- L1 (Input validation): 8 of 12 cases
- L2 (Output filtering): 7 of 12 cases
- L6 (Governance): 8 of 12 cases
- L3 (Human checkpoint): 6 of 12 cases

**Least common missing layer**:

- L4 (Rollback): only explicitly missing in 2 cases, but implicitly absent in most

## The 6-Layer Framework (L1-L6)

| Layer | Name | Question It Answers |
|-------|------|-------------------|
| L6 | Governance | Who owns the decision to ship? |
| L5 | Monitoring | Can you see it failing in real time? |
| L4 | Rollback | Can you pull it in under 60 seconds? |
| L3 | Human checkpoint | Does a human have override authority? |
| L2 | Output filtering | Does anything screen what it says? |
| L1 | Input validation | Did you test what users actually type? |
