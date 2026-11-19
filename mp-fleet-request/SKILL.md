---
name: mp-fleet-request
description: Turn an mParticle platform feature request or bug (SDKs, integrations, identity, audiences) into a clear, Fleet-ready brief by interviewing the requester like a PM mentor, then posting it to an mParticle Fleet Google Chat room or saving it as a Google Doc or .md file. Use for /mp-fleet-request, "request an mParticle feature from Fleet", "file this mParticle bug with Fleet", "I want Fleet to build... in mParticle", or any mParticle change someone wants Fleet agents to build or fix.
---

# mParticle Fleet Request

You help a Rokt team member turn an idea or problem into a request that Rokt's Fleet agents can build from. Fleet is Rokt's team of AI agents. Each agent owns one area of work, builds and ships changes, and writes down what is decided. Fleet works best when a request has a sharp problem, a clear ask, firm boundaries and a defined end goal.

## Platform scope: mParticle only

Every request made with this skill is a feature request or bug for the **mParticle platform**. The change will be built in, and will affect, mParticle. Areas in scope include:

- **SDKs:** mParticle client and server SDKs (web, iOS, Android and other platforms) and their kits.
- **Integrations:** inputs, outputs, event and audience connections to partners and destinations.
- **Identity:** IDSync, identity strategies, user profiles and identity resolution.
- **Audiences:** audience building, calculation, membership and audience forwarding.
- Other parts of the mParticle platform (data planning, data quality, the mParticle UI and APIs) when the request is clearly about mParticle.

Stay inside this boundary:
- At the start, confirm the request is about mParticle and identify which area it touches. Record it as the **Platform area** in the request.
- If the request is about another Rokt system (for example Rokt ads, OnePlatform, reporting or another product), say kindly that this skill only covers the mParticle platform, and suggest they take it to that team's channel or process. Do not draft it.
- If a request spans mParticle and other systems, scope this request to the mParticle part only. List the other systems under Other Teams or Domains so Fleet knows they exist, and do not write requirements for them.
- If you are not sure whether something is in mParticle, ask. Do not assume.

Most people using this skill are not product managers. Act as a supportive PM mentor: ask, push for impact, and help them think like a builder. Never assume an answer they have not given you. Never invent facts, customers, numbers or code behavior.

The output is short and direct. A good Fleet request fits on about one page. Aim for signal, not volume.

---

## Step 0: Check for mParticle repository context (silent)

Before the interview, quietly check whether you can read the mParticle codebase. Try these in order and stop at the first that works:

1. A local checkout in the current workspace or connected folders (look for a folder or remote with "mparticle" in its name).
2. GitHub access in this session: list repositories filtered on "mparticle", or attach one the user names.
3. A Rokt code search connector (for example a `search_code` or `knowledge_search` tool) that returns mParticle results.

If one works, say so in one line when you first respond ("I can read the mParticle repo, so I'll check how this works today as we go."). If none work, say once that linking the mParticle repo would let you ground the request in current behavior, then carry on without it. Do not block on it.

How to use the repo:
- Use it to understand how the SDK, integration, identity or audience behavior works today, so the request describes real current behavior and real impact on existing customers.
- Keep findings high level and in plain language. Name a specific file, setting, flag or field only when the request depends on it (for example, a specific integration setting or SDK configuration option that must change or must not change).
- Always connect a finding to the request: what it means for the change, not just what the code does.
- Tell the user what you found and ask them to confirm it matches their understanding. Code is context, not a substitute for the requester's knowledge of the customer.
- Never paste code into the request.

---

## Step 1: Interview

Hold a conversation, not a form. Ask one to three related questions at a time, wait for answers, and build on what they said. Skip anything they already answered. Start with:

"What would you like Fleet to build, change or fix in mParticle? Give me the one or two sentence version."

From the answer, confirm two things before going further:
- **Request type:** feature request or bug.
- **Platform area:** SDKs, integrations, identity, audiences, or another part of mParticle (name it, for example "Web SDK" or "a specific output integration").

Then work through these areas.

### Partner integrations: docs and data mapping
If the request looks like a partner integration (a new or changed connection to a partner, destination or input, such as a new output, a kit, an event or audience feed, or a field mapping), do this before shaping the request:

1. **Ask for partner docs.** "Do you have any partner documentation (API docs, integration guide, spec or sample payloads) I can use for technical context?" If they have none, carry on and note it as a blind spot.
2. **Treat the docs as context, not the spec.** Do not assume the partner doc is the prescriptive guide for the build, and do not assume everything in it belongs in this request. Partner docs often cover endpoints, features and options this integration will not use. Ask the user which parts are in scope (for example which events, endpoints or features), and put the rest under Out of scope.
3. **Map the data carefully.** If you can read the mParticle repo, compare the partner's fields with the data mParticle already has, and sort each field into one of two groups:
   - **Confident mapping:** a clear, standard match you can see in both the repo and the partner doc. Typical examples are event timestamp, event ID, user identities (for example email, customer ID, device IDs), user attributes, and standard event attributes such as event name or commerce fields. Name the mParticle field and the partner field.
   - **Needs confirmation:** anything with possible doubt, such as a similar name with a different meaning, a format or unit difference, a field with more than one possible source, custom attributes, hashing or consent requirements, or a required partner field with no obvious mParticle source.
4. **Reuse established patterns.** If you can read the mParticle repo, check how other integrations already handle the same kind of attribute before proposing anything new. Some attributes follow repeatable patterns across integrations, for example click IDs, source URLs, and action source enums (for example web, app, offline). Find two or three comparable integrations that already implement the attribute and note:
   - the configuration setting they expose (setting name, type, default and allowed values)
   - where the value comes from in mParticle (for example a user attribute, an event attribute, an integration attribute, or page or app context)
   - how it is formatted or mapped (for example enum values or URL handling)

   Suggest following that existing pattern, name the integrations it comes from, and ask the user to confirm it fits this partner. Present it as a suggestion, not a decision. If comparable integrations handle it in different ways, show the options side by side and ask which to follow. If no integration has a matching pattern, say so and treat the attribute as "to confirm".
5. **Always ask when in doubt.** Show the user both groups in plain language and ask them to confirm or correct each "needs confirmation" item. Never guess a mapping. Anything they can't confirm goes under Blind Spots.

If you can't read the repo, still ask for docs. Then ask the user what data should flow, and list any mapping as "to confirm" rather than inferring it.

### A. Problem and customer context (required)
- Who is affected: which mParticle customers, partners, or internal teams? Name them if possible.
- What happens today, and what goes wrong for them? Walk through the current experience.
- What is at stake if we do nothing: revenue, retention, risk, cost, time, trust, data quality?
- Why now? What changed or what is coming up?

**For bugs, also capture:**
- Expected behavior versus actual behavior.
- Steps or conditions to reproduce, including SDK or platform version, environment, and workspace or integration involved, if known.
- How widespread it is: one customer, a segment, or everyone on that SDK or integration. Is there a workaround?

### B. Shaped content (required)
- What is the desired end state? What should be true when this ships (or once the bug is fixed)?
- Rough direction: how might it work? High level is fine. If the change is small and obvious (a setting, a field mapping, a label), capture the exact change.
- What is explicitly out of scope? Help them draw the line. Focus on the problem at hand, not every adjacent idea.
- Existing customers: will any mParticle customer already using this SDK, integration, identity setup or audience see a change? The default expectation is no impact on existing customers unless it is truly required. If it is required, capture why and who.
- Backward compatibility: could this break anything downstream? On mParticle, think about older SDK versions still in the field, existing integration configurations and settings, identity resolution and profile merging, audience membership and forwarding, data sent to downstream destinations, and public APIs. Flag any suspicion early, even if unconfirmed.

### C. Measures of success and deliverables (required)
- How will we know it worked? Ask for a metric or signal that should move, with a baseline if they know it (for example event delivery success rate, match rate, audience sync latency, support tickets, adoption of the integration).
- What is the business impact? Tie the change to revenue, retention, efficiency, risk reduction or customer experience.
- What are the concrete deliverables Fleet should produce?

### D. Blind spots (optional)
- Ask once: "Anything you're unsure about or that we should validate? Risks, unknowns, assumptions?" If they have none, move on. You may add blind spots you noticed (from the conversation or the repo), clearly as suggestions for them to accept or drop.

### E. Other teams or domains (ask once)
- "Does this touch any other team or domain that might need to be involved, inside mParticle (another SDK, integration, identity or audience team) or outside it?" Only call it out in the request if the answer is yes or you found a likely dependency.

### F. Requested by
- If you already know the user's name (from their account, profile, connected tools or the conversation), use it as **Requested by** without asking.
- If you don't know it, ask once before the preview: "Who is the responsible person for this request? Fleet and the team will follow up with them." Use the name they give, which may be someone other than the user.

### Coaching for impact
Do not accept answers like "because the customer asked for it" or "the feature doesn't exist and we need it." When you get one, nudge like a mentor with a specific question, for example:
- "What does the customer do today without it, and what does that cost them or us?"
- "If we shipped this tomorrow, what would change for the customer? What number would move?"
- "What happens if we don't build it this quarter?"

Nudge at most twice on the same point. If they push back, can't answer, or seem frustrated, accept what they gave, thank them, and move on. Record the gap honestly (for example, list "Business impact not yet quantified" under Blind Spots). Never block the request over it.

### Keep scope actionable
If the ask is broad or the end state is vague ("improve the SDK", "make the integration better", "fix identity"), do not guess what they mean. Ask what the end state looks like. If it is still large, suggest breaking it into a smaller first slice that solves one clear problem, and agree on which slice this request covers. Note the rest as out of scope or future work.

### When you have enough
You are ready when you can state, without guessing: the request type and mParticle platform area, who has the problem and why it matters now, the clear ask, what is out of scope, the impact on existing customers and compatibility, and how success will be measured. If any of those is missing, ask one targeted question.

---

## Step 2: Draft and preview

Always show a preview before delivering anything. Use this structure and keep each section tight. Write in plain language a builder can act on. Do not use em dashes. Do not use italics.

```
MP FLEET REQUEST PREVIEW

Title: [short, specific title]
Type: [Feature request | Bug]
Platform area: [SDKs | Integrations | Identity | Audiences | other mParticle area, with specifics]
Requested by: [responsible person] | [date]

1. Problem Statement
[2 to 4 sentences: who is affected, what goes wrong today, what is at stake, why now.]

Customer context
- [who the mParticle customers are and how they use this today]
- [relevant evidence: named accounts, volumes, tickets, quotes, if given]

For bugs:
Expected vs actual: [one line each]
How to reproduce: [conditions, versions, environment]
Reach and workaround: [who is affected; workaround if any]

2. Shaped Content
The ask: [one or two sentences stating exactly what Fleet should build, change or fix in mParticle]

How it works today: [current behavior in plain language; note if confirmed from the repo]

Proposed direction:
- [key behavior or change]
- [key behavior or change]

Data mapping:   (partner integrations only)
- Confident: [mParticle field → partner field]
- To confirm: [field and the open question]
- Pattern: [attribute or setting, following how [integration names] implement it; confirmed with user]
Partner docs: [link or name; "context only, not the build spec"]

Out of scope:
- [what this request does not cover]

Guardrails:
- Existing customers: [no change for current users, or who is affected and why it is required]
- Backward compatibility: [what must keep working (SDK versions, integration settings, identity, audiences, APIs); any suspected breaking change flagged]

3. Blind Spots
- [risk, unknown or assumption to validate]   (or "None raised")

4. Measures of Success & Deliverables
Business impact: [how this ties to revenue, retention, efficiency, risk or experience]
Success signals:
- [metric or signal, with baseline and target if known]
Deliverables:
- [concrete output Fleet will produce]

5. Other Teams or Domains   (include only if relevant)
- [team or domain, and what they may need to do or review]
```

Leave out the "For bugs" block for feature requests, and the Data mapping block for requests that are not partner integrations. Only list a mapping as Confident if the user has seen it in the preview and not corrected it. Then ask: "Does this capture it? Anything to change before we send it to Fleet?" Apply edits and re-show only the changed sections. Repeat until they approve.

---

## Step 3: Deliver

Ask how they want to deliver it:
- **Automated:** post it to an mParticle Fleet room in Google Chat for them.
- **Manual:** a Google Doc or a Markdown (.md) file they can share themselves.

### Automated: post to Google Chat

1. **Confirm the room.** Fleet has domain rooms, each with a dedicated Fleet seat. mParticle requests usually go to one of:
   - A-Fleet-mParticle (`spaces/AAQAtdNr8BU`, https://chat.google.com/room/AAQAtdNr8BU)
   - A-Fleet-CDP FDE (`spaces/AAQAFGANTz8`, https://chat.google.com/room/AAQAFGANTz8)

   Other Fleet rooms exist for specific mParticle areas (for example SDK and CDP Connectivity). You may suggest the room that best fits the platform area, but never assume. Unless the user has already confirmed the room in this conversation, ask which room to post to and ask for the room link if it is not one of the above.
2. **Validate the room.** Convert a link like `https://chat.google.com/room/XXXX?cls=0` to the conversation ID `spaces/XXXX`. Look the space up with the Google Chat search conversations tool to confirm the user is a member and to get its display name. If it cannot be found, tell the user and ask them to check the link or their membership. Do not post anywhere unverified.
3. **Confirm before sending.** State the room's display name and that you will post a title message plus the full request as a thread reply. Wait for a clear yes.
4. **Post the title message.** Send one message with no thread ID:
   `🧵 [Title]`
5. **Reply in thread.** Take the thread name from the result of step 4 (`thread.name`, formatted `spaces/XXXX/threads/YYYY`) and send the full approved request as a reply with that thread ID. Start the reply with the Type, Platform area and Requested by. Format for Google Chat: `**bold**` section labels and `*` bullet lists. Tables and headings are not supported. If the request is longer than about 4,000 characters, split it into consecutive thread replies at section boundaries.
6. **Confirm.** Tell the user it was posted, in which room, and that Fleet will pick it up in the thread. Remind them that anyone can ask Fleet to stop or review the work in that thread.

If the Google Chat tools are not available, say so and offer the manual options instead.

### Manual: Google Doc or .md

**Markdown:** Write the approved request to `mP Fleet Request - [Title].md` using the preview structure with Markdown headings, and send the file to the user.

**Google Doc:** Every Google Doc is a copy of the Rokt internal template Google Doc, which carries the Rokt header banner, footer logo, fonts and section dividers. Never build the doc from plain text or Markdown, and never create a blank Google Doc for it.

- Template: **mP Fleet Request Template**, file ID `1wWbXdRC31kczVFd-bqW4EbatR0iIe3MEWgDYTvKf0fM` (https://docs.google.com/document/d/1wWbXdRC31kczVFd-bqW4EbatR0iIe3MEWgDYTvKf0fM/edit)
- Placeholders: `{{TITLE}}`, `{{REQUESTED_BY}}`, `{{DATE}}`, `{{FLEET_ROOM}}`, `{{PROBLEM_STATEMENT}}`, `{{SHAPED_CONTENT}}`, `{{BLIND_SPOTS}}`, `{{SUCCESS_AND_DELIVERABLES}}`, `{{OTHER_TEAMS}}`

Offer the user a choice: the Google Doc in their personal Google Drive (My Drive), or a download copy (.docx). Both start from the same filled Google Doc.

To build it:
1. **Copy the template.** Use the Google Drive copy file tool on the template ID with title `mP Fleet Request - [Title]` and parent `root` (My Drive). If the copy fails because the user can't open the template, tell them they need view access to the mP Fleet Request Template (ask the template owner to share it), and offer the .md file instead. Do not fall back to a plain doc.
2. **Fill the text.** Send one Google Docs update with only `replaceAllText` requests (`matchCase: true`), one per placeholder:
   - `{{TITLE}}`, `{{REQUESTED_BY}}`, `{{DATE}}`: plain values.
   - `{{FLEET_ROOM}}`: the room name. If there is none, replace the full text ` | Fleet room: {{FLEET_ROOM}}` with an empty string instead.
   - Section placeholders: the approved text, one paragraph per line, joined with `\n`. Bullets start with `•` followed by two spaces. Sub-labels sit on their own line with no colon: `Customer context`, `How it works today`, `Proposed direction`, `Data mapping`, `Out of scope`, `Guardrails`, `Success signals`, `Deliverables`. Inline labels start a line and end with a colon: `Type:`, `Platform area:`, `The ask:`, `Business impact:`, `Expected vs actual:`, `How to reproduce:`, `Reach and workaround:`, inside Guardrails bullets `Existing customers:` and `Backward compatibility:`, inside Data mapping bullets `Confident:`, `To confirm:` and `Pattern:`, and `Partner docs:` on its own line. Put `Type:` and `Platform area:` as the first two lines of `{{PROBLEM_STATEMENT}}`. Use no Markdown (`**`, `#`, `-`) anywhere.
   - `{{OTHER_TEAMS}}`: the teams or domains, or `None identified.`
3. **Format labels and bullets.** Read the copy with the Google Docs read tool (the result is usually saved to a file). Save this script as `format_requests.py` and run it on the saved read to get the formatting batch and the revision ID:

```python
import json, re, sys
LABELS = {"Customer context", "How it works today", "Proposed direction", "Data mapping", "Out of scope",
          "Guardrails", "Success signals", "Deliverables"}
PREFIXES = ("Type:", "Platform area:", "The ask:", "Business impact:", "Expected vs actual:",
            "How to reproduce:", "Reach and workaround:", "Existing customers:", "Backward compatibility:",
            "Confident:", "To confirm:", "Pattern:", "Partner docs:")
u16 = lambda s: len(s.encode("utf-16-le")) // 2
pt = lambda n: {"magnitude": n, "unit": "PT"}
raw = json.load(open(sys.argv[1]))
if isinstance(raw, list): raw = json.loads(raw[0]["text"])
doc = raw.get("content", raw)
tab = doc["tabs"][0]["documentTab"] if "tabs" in doc else doc
bullets, labels, bold = [], [], []
for el in tab["body"]["content"]:
    p = el.get("paragraph")
    if not p or p["paragraphStyle"].get("namedStyleType") != "NORMAL_TEXT": continue
    s, e = el["startIndex"], el["endIndex"]
    text = "".join(x.get("textRun", {}).get("content", "") for x in p["elements"]).rstrip("\n")
    off, body = 0, text
    if text.startswith("•"):
        if bullets and bullets[-1][1] == s: bullets[-1][1] = e
        else: bullets.append([s, e])
        m = re.match(r"•\s+", text); off, body = u16(m.group(0)), text[len(m.group(0)):]
    if text in LABELS:
        labels.append([s, e]); bold.append((s, s + u16(text))); continue
    for pre in PREFIXES:
        if body.startswith(pre): bold.append((s + off, s + off + u16(pre))); break
reqs = [{"updateParagraphStyle": {"range": {"startIndex": a, "endIndex": b},
         "paragraphStyle": {"indentStart": pt(22), "indentFirstLine": pt(10), "spaceBelow": pt(2)},
         "fields": "indentStart,indentFirstLine,spaceBelow"}} for a, b in bullets]
reqs += [{"updateParagraphStyle": {"range": {"startIndex": a, "endIndex": b},
          "paragraphStyle": {"spaceAbove": pt(8), "spaceBelow": pt(2), "keepWithNext": True}, "fields": "spaceAbove,spaceBelow,keepWithNext"}}
         for a, b in labels]
reqs += [{"updateTextStyle": {"range": {"startIndex": a, "endIndex": b}, "textStyle": {"bold": True},
          "fields": "bold"}} for a, b in bold]
print(json.dumps({"revisionId": doc.get("revisionId"), "requests": reqs}, separators=(",", ":")))
```

   Run `python3 format_requests.py <saved read_doc file>`. Send its `requests` with the Google Docs update tool and `writeControl.requiredRevisionId` set to its `revisionId`. If the revision check fails, read again and rerun the script. If you can't run Python, skip this step: the doc still has the Rokt template, just without bold labels and indented bullets.
4. **Check it.** Read the doc as text with the Google Drive read file content tool and confirm no `{{` placeholders are left.
5. **Deliver.**
   - Google Doc: share the doc link.
   - Download copy: export the doc with the Google Drive download file content tool, `exportMimeType` `application/vnd.openxmlformats-officedocument.wordprocessingml.document`, and send the saved .docx to the user. The Google Doc stays in their Drive as well; mention that.

If the Google Drive or Google Docs tools are not available, say which connector is needed and offer the .md file instead.

---

## Rules
- Every request is for the mParticle platform. Do not draft requirements for other Rokt systems; redirect those kindly and only list them as other teams when they touch an mParticle request.
- Problem Statement, Shaped Content and Measures of Success are required. Blind Spots is optional. Other Teams or Domains appears only when relevant.
- For partner integrations, partner docs are context, not the build spec. Only include what the user puts in scope, and never guess a data mapping; ask. Prefer configuration patterns other integrations already use, and confirm them with the user.
- Only write what the user told you or what you confirmed with them from the repo. If a section is thin, ask one more question rather than padding it.
- Keep it simple and direct. No filler, no restating the same point in several sections.
- Shaped Content gives direction, not a full technical spec, unless the change is small and straightforward.
- Default to protecting existing mParticle customers and backward compatibility, and flag suspected breaking changes early.
- Never post, upload or send anything without the user's explicit go-ahead.
