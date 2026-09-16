# Additional illustrations

Fictional demonstrations of the [skill workflow](../SKILL.md#application).

**Situation:** A platform team is migrating internal API infrastructure. Stakeholder list: VP of Engineering (sponsor), three engineering leads (direct users), Legal (compliance review), the customer support team (their tooling depends on the APIs), and enterprise customers who won't see the change directly but whose uptime depends on it.

**Power × Interest grid placements:**
- VP of Engineering → Manage closely (high power, high interest)
- Engineering Leads → Manage closely (high power, high interest — direct builders)
- Legal → Keep satisfied (high power, low day-to-day interest)
- Customer Support → Keep informed (low power, high interest — their tools change)
- Enterprise Customers → Monitor (low power, low stated interest)

**Impact × Power grid placements:**
- VP of Engineering → Q2 (high impact, high power)
- Engineering Leads → Q2 (high impact, high power)
- Legal → Q4 (low impact, high power)
- Customer Support → **Q1** (high impact, low power — their tooling breaks if migration fails)
- Enterprise Customers → **Q1** (high impact, low power — uptime dependency)

**The gap the comparison reveals:** Customer Support and Enterprise Customers are "monitor" or "keep informed" on Grid 1, but Q1 on Grid 2. The migration team has been treating them as passive observers when they're actually the highest-risk stakeholders. Resolution: recruit support agents into UAT, create an enterprise customer communication plan with rollback triggers, and add both groups to the launch readiness criteria.
