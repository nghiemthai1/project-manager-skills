# Risk Workshop: software example

Fictional training scenario. Values and thresholds are examples, not defaults for real projects.

## Guided workshop before the pilot

**Facilitator:** "Which failure would make the pilot unacceptable even if SAML login works?"

**Lena:** "An administrator might lose access when the identity provider is unavailable."

**Theo:** "Support could be unable to recover service using the runbook."

## Worked response

Group the related concerns under recovery capability while preserving both security and operational consequences. Require a demonstrated recovery path, reviewable audit evidence, and operator validation. The response owner must be confirmed; Lena's acceptance role does not automatically make her the implementer.

No failure probability is available. Prioritize the concern because it threatens an explicit acceptance condition, not because someone invented a high score. The later 28 October missing demonstration is a readiness gap to manage, not proof that this workshop's hypothetical failure actually occurred.

## Repair

**Flawed:** "Risk score 90; mitigated because a runbook exists."

**Corrected:** "Likelihood unquantified; consequence threatens acceptance. Test the recovery path and operator use before claiming the response is effective."
