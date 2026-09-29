"""
Seed data for the M&A integration memory demo.

Company A = Orbital Labs (target): AWS, flexible PTO, Slack.
Company B = Vantage Corp (acquirer): Azure, fixed leave policy, Microsoft Teams.

Story arc encoded in these notes:
- Week 1-2: AWS vs Azure is flagged as an open, undecided conflict.
- Week 3: VP of Engineering Derek Huang explicitly decides infra migrates to Azure.
- Week 4-5: unrelated integration noise (PTO policy, tooling migration, systems).
- Week 6: team lead Priya Shah proposes keeping the AWS pipeline for Q1, contradicting
  the Week 3 decision without acknowledging it.
- PTO policy conflict (Orbital's flexible PTO vs Vantage's fixed leave) recurs across
  the timeline and is never resolved.
"""

SEED_MEETINGS = [
    # Week 1
    {
        "content": (
            "Kickoff meeting for the infrastructure integration workstream. Orbital Labs "
            "currently runs its entire production stack on AWS, while Vantage Corp standardizes "
            "on Azure. No decision was made on which cloud provider the combined company will "
            "use going forward; flagging this as an open conflict to resolve in a future session."
        ),
        "context": "open conflict",
        "timestamp": "2026-01-05T10:00:00",
    },
    {
        "content": (
            "HR integration sync. Orbital Labs offers employees flexible, unlimited PTO, while "
            "Vantage Corp uses a fixed accrual-based leave policy. Both HR teams acknowledged the "
            "mismatch but did not propose a resolution; legal will need to weigh in on compliance "
            "implications before any policy is chosen."
        ),
        "context": "HR policy",
        "timestamp": "2026-01-07T14:30:00",
    },
    {
        "content": (
            "Brief note from the collaboration tools working group. Orbital Labs teams communicate "
            "primarily over Slack, whereas Vantage Corp is fully on Microsoft Teams. Noted for future "
            "discussion once higher-priority infra and HR items are settled."
        ),
        "context": "tooling migration",
        "timestamp": "2026-01-08T09:15:00",
    },
    # Week 2
    {
        "content": (
            "Follow-up infra meeting. Engineering pulled a cost and workload breakdown of Orbital's "
            "AWS footprint, including EC2, RDS, and S3 usage, to inform a future migration decision. "
            "Still no consensus on AWS vs Azure; the group agreed to escalate to VP-level for a final call."
        ),
        "context": "infra decision",
        "timestamp": "2026-01-12T11:00:00",
    },
    {
        "content": (
            "HR policy follow-up. Legal is still reviewing whether Orbital's flexible PTO can be "
            "preserved for legacy employees or whether Vantage's fixed leave policy must apply "
            "company-wide post-close. No timeline given for a decision."
        ),
        "context": "HR policy",
        "timestamp": "2026-01-14T13:00:00",
    },
    {
        "content": (
            "Engineering leads from both companies raised concerns about the effort required to "
            "migrate Orbital's AWS-native services to Azure, citing tight coupling to AWS-managed "
            "services like Lambda and DynamoDB. The AWS vs Azure question remains unresolved heading "
            "into next week."
        ),
        "context": "open conflict",
        "timestamp": "2026-01-15T15:45:00",
    },
    # Week 3 - the decision
    {
        "content": (
            "Infrastructure decision meeting. Derek Huang, VP of Engineering, made the final call: "
            "all Orbital Labs infrastructure will migrate from AWS to Azure to align with Vantage "
            "Corp's standard stack. Derek asked engineering leadership to draft a migration plan "
            "and timeline by end of week."
        ),
        "context": "infra decision",
        "timestamp": "2026-01-20T10:00:00",
    },
    {
        "content": (
            "Follow-up to Monday's decision. Engineering leadership communicated Derek Huang's "
            "AWS-to-Azure migration decision to all Orbital team leads. A draft migration timeline "
            "targeting full cutover by end of Q2 was circulated for feedback."
        ),
        "context": "infra decision",
        "timestamp": "2026-01-22T09:30:00",
    },
    # Week 4 - noise
    {
        "content": (
            "PTO policy conflict revisited. HR proposed a temporary dual-policy approach where "
            "Orbital employees keep flexible PTO through the end of the fiscal year, but Vantage HR "
            "pushed back citing payroll system complexity. Still unresolved."
        ),
        "context": "HR policy",
        "timestamp": "2026-01-26T11:30:00",
    },
    {
        "content": (
            "Collaboration tools migration planning. The working group drafted a Slack-to-Teams "
            "timeline: pilot migration for the Orbital sales team in February, followed by a full "
            "company rollout by April. Data export and channel history retention are still open questions."
        ),
        "context": "tooling migration",
        "timestamp": "2026-01-27T10:00:00",
    },
    {
        "content": (
            "Benefits and payroll systems integration note. Orbital's benefits enrollment platform "
            "will be sunset in favor of Vantage's existing system. Open enrollment for Orbital "
            "employees is tentatively scheduled for March."
        ),
        "context": "systems integration",
        "timestamp": "2026-01-28T14:00:00",
    },
    {
        "content": (
            "Azure migration planning update. Engineering assigned migration owners for each Orbital "
            "service: the payments team will handle DynamoDB-to-Cosmos DB migration first, per Derek "
            "Huang's Q2 cutover target from the Week 3 decision."
        ),
        "context": "infra decision",
        "timestamp": "2026-01-29T13:00:00",
    },
    # Week 5 - noise
    {
        "content": (
            "Collaboration tools update. Slack deprecation for the pilot group is confirmed for "
            "February 16th. IT will export message history for compliance retention before shutting "
            "down the Orbital Slack workspace."
        ),
        "context": "tooling migration",
        "timestamp": "2026-02-02T09:00:00",
    },
    {
        "content": (
            "PTO policy conflict, third discussion. HR again failed to reach agreement on whether "
            "Orbital's flexible PTO will be grandfathered in. The topic was tabled again pending "
            "further legal review; no owner or deadline assigned."
        ),
        "context": "HR policy",
        "timestamp": "2026-02-03T15:00:00",
    },
    {
        "content": (
            "Facilities and systems note. Orbital's Bay Area office will consolidate into Vantage's "
            "existing lease starting in Q3. Payroll systems cutover for Orbital employees is on track "
            "for the same quarter."
        ),
        "context": "systems integration",
        "timestamp": "2026-02-04T11:00:00",
    },
    {
        "content": (
            "Azure migration status update. The payments team completed the first workload migration "
            "off AWS, validating the approach Derek Huang approved in Week 3. Remaining teams are on "
            "track for the Q2 cutover."
        ),
        "context": "infra decision",
        "timestamp": "2026-02-05T10:30:00",
    },
    # Week 6 - the contradiction
    {
        "content": (
            "Note from Priya Shah, team lead for the data platform group. Priya proposed keeping "
            "their pipeline on AWS through Q1 'since it's already working,' citing recent stability "
            "improvements. No mention was made of Derek Huang's Week 3 decision to migrate all infra "
            "to Azure."
        ),
        "context": "open conflict",
        "timestamp": "2026-02-09T10:00:00",
    },
    {
        "content": (
            "Collaboration tools rollout begins. The Orbital sales team's pilot migration to Microsoft "
            "Teams went live this week, ahead of the planned company-wide cutover in April."
        ),
        "context": "tooling migration",
        "timestamp": "2026-02-10T09:00:00",
    },
    {
        "content": (
            "PTO policy conflict, still open. HR leadership acknowledged the issue has now gone "
            "unresolved for six weeks and agreed to escalate to the joint integration steering "
            "committee, but no meeting has been scheduled yet."
        ),
        "context": "HR policy",
        "timestamp": "2026-02-12T14:00:00",
    },
]
