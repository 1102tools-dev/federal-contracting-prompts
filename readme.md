# Federal contracting MCP prompts

[![price: free](https://img.shields.io/badge/price-free-007a59)](https://1102tools.com/#why) [![license: MIT](https://img.shields.io/badge/license-MIT-007a59)](license) [![prompts](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2F1102tools.com%2Fprompts.json&query=%24.prompts.length&label=prompts&color=007a59)](https://1102tools.com/#prompts) [![regression tests](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/1102tools-dev/federal-contracting-mcps/main/badges/tests-total.json)](https://github.com/1102tools-dev/federal-contracting-mcps#testing)

**October 2026 · Copy, paste, adapt.**

Practical questions for federal opportunities, competitor research, teaming, pricing, and regulations, built for free, open-source MCP servers. Choose the work, install and connect the required MCPs, and replace the bracketed details.

[Browse the readable website](https://1102tools.com/#prompts) · [Download the printable guide](docs/1102tools-mcp-prompt-guide.pdf) · [Local setup guide](https://github.com/1102tools-dev/federal-contracting-mcps#local-setup) · [Demo videos on YouTube](https://www.youtube.com/@1102tools)

## Start here

1. Choose a prompt and check its **Required MCPs** line.
2. Set up the required MCPs locally from their setup guides, or install the hosted versions from the Claude and ChatGPT directories. Configure any required API keys outside chat and confirm that your client can see the tools.
3. Replace the bracketed details, then ask your assistant to run the prompt. Check source links, dates, and missing information before using the results.

The print guide and the online library contain the same 56 prompts for all nine MCP sources. These examples describe available source tools; this edition is not a claim that every prompt has been re-run against live APIs.

<a id="available-in-claude-and-chatgpt"></a>
## Local or hosted

Every MCP works in Claude or ChatGPT two ways. **Local** runs it on your computer, inside the Claude or ChatGPT desktop app or another AI app. **Hosted** runs it on Cloudflare, so it works anywhere you use Claude or ChatGPT. Local is the better setup for daily work, and you don't have to set it up by hand: give your AI the [local setup guide](https://github.com/1102tools-dev/federal-contracting-mcps#local-setup) and ask it to set it up or walk you through it.

All nine are in the Claude and ChatGPT directories as hosted installs.

| MCP | Local setup (desktop) | Claude (hosted) | ChatGPT (hosted) |
|---|---|---|---|
| SAM.gov | [Setup guide](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp#installation) (full 20-tool edition, free key) | [Install](https://claude.ai/directory/sam-gov-by-1102tools) (6-tool edition, no key) | [Install](https://chatgpt.com/plugins/plugin_asdk_app_6ad986ea765081919a8856a5b5233f40) (6-tool edition, no key) |
| USAspending | [Setup guide](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp#installation) | [Install](https://claude.ai/directory/usaspending-by-1102tools) | [Install](https://chatgpt.com/plugins/plugin_asdk_app_6a9ee668cc248191a0bdb9911b546799) |
| GSA CALC+ | [Setup guide](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/gsa-calc-mcp#installation) | [Install](https://claude.ai/directory/gsa-calc-by-1102tools) | [Install](https://chatgpt.com/plugins/plugin_asdk_app_6a9eeeebfa8c81918945df0945276cb1) |
| BLS OEWS | [Setup guide](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/bls-oews-mcp#installation) | [Install](https://claude.ai/directory/bls-oews-by-1102tools) | [Install](https://chatgpt.com/plugins/plugin_asdk_app_6ab872bf5360819186af0917c923e57e) |
| GSA Per Diem | [Setup guide](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/gsa-perdiem-mcp#installation) (free key only for city names its bundled Census and county data can't place, or years before FY2021) | [Install](https://claude.ai/directory/gsa-perdiem-by-1102tools) | [Install](https://chatgpt.com/plugins/plugin_asdk_app_6ab85f56d4ec8191970ab75fdeddd2f9) |
| eCFR | [Setup guide](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/ecfr-mcp#installation) | [Install](https://claude.ai/directory/ecfr-by-1102tools) | [Install](https://chatgpt.com/plugins/plugin_asdk_app_6a9ef0341b04819192935fd4e5cd9b34) |
| Federal Register | [Setup guide](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/federal-register-mcp#installation) | [Install](https://claude.ai/directory/federal-register-by-1102tools) | [Install](https://chatgpt.com/plugins/plugin_asdk_app_6ad989cff4d4819187ca95781427b399) |
| Regulations.gov | [Setup guide](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/regulations-gov-mcp#installation) (free key) | [Install](https://claude.ai/directory/regulations-gov-by-1102tools) | [Install](https://chatgpt.com/plugins/plugin_asdk_app_6ad988bee41c8191a72c0b0e94d84eb9) |
| Acquisition.gov | [Setup guide](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/acquisition-gov-mcp#install) | [Install](https://claude.ai/directory/acquisition-gov-by-1102tools) | [Install](https://chatgpt.com/plugins/plugin_asdk_app_6ab2757102e08191887f75cc506c2333) |

| | Local | Hosted |
|---|---|---|
| **Why use it** | Your own full rate limits, so you skip any congestion on hosted | Always up to date. No keys, and it works in Claude or ChatGPT anywhere |
| **Works in** | Claude or ChatGPT desktop apps and other AI apps, on a desktop or laptop | Claude or ChatGPT on web, desktop, and phone |
| **Setup** | Ask your AI to set it up from the setup guide. Free keys for SAM.gov, Regulations.gov, and GSA Per Diem | Install from the Claude or ChatGPT directory. No keys |
| **Rate limits** | Your own, in full | Pooled across all users. Your lookups stay private |
| **Relies on** | Government sources | Government sources and Cloudflare |
| **Privacy** | Runs on your computer. Nothing passes through 1102tools | No tracking. Searches aren't logged and IP addresses aren't kept |
| **CUI** | Depends on your AI app, not 1102tools. The server only pulls public data, straight from the government site | Depends on your AI app, not 1102tools. The server gets only the search your AI sends, never your chat or files |
| **Updates** | Manual. Local installs don't update themselves. Ask your AI to update them | Automatic. Always runs the latest release |
| **SAM.gov** | Full edition: 20 tools, free key | 6 tools, no key |

**Use hosted if** you're on your phone, your work computer blocks installs, or you want SAM.gov opportunity, public registration, or exclusion research without a key.

Hosted services temporarily cache some public government responses. Some responses are cached in bounded memory; no conversations or query/result logs are retained. Their code and Cloudflare setup are public in [federal-contracting-mcps](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/deploy). Cloudflare still handles connection data such as IP addresses, and Claude or ChatGPT handles your conversation under its own privacy policy.

A prompt does not install an MCP. Connect every source listed under **Required MCPs** before running it; if two are listed, both are required. Other sources and MCP clients use the individual server setup instructions below.

## Browse by task

| Task | Prompts |
|---|---|
| [Combine sources](#combination-plays) | 5 |
| [Find opportunities](#catching-opportunities) | 6 |
| [Research competitors](#competitor-intelligence) | 4 |
| [Track potential recompetes](#recompete-radar) | 2 |
| [Vet companies and find teammates](#vetting-and-teaming) | 6 |
| [Understand a market](#market-and-agency-intel) | 5 |
| [Find the right codes](#speaking-the-governments-codes) | 5 |
| [Compare labor rates](#gsa-calc) | 4 |
| [Research wages](#bls-oews) | 5 |
| [Estimate travel](#gsa-per-diem) | 3 |
| [Read the regulations](#ecfr) | 3 |
| [Follow published changes](#federal-register) | 3 |
| [Explore dockets and comments](#regulationsgov) | 3 |
| [FAR Overhaul and deviations](#far-overhaul-and-agency-deviations) | 2 |

## MCPs and setup

| Source | What it provides | Access |
|---|---|---|
| [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp) | Contract opportunities, entity registrations, SBA certifications, and exclusions. | Local full edition: free SAM.gov key. Hosted: no key |
| [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp) | Contracts, grants, loans, recipients, agencies, and subawards. | No user API key |
| [GSA CALC+](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/gsa-calc-mcp) | Awarded labor-category ceiling rates and comparison data. | No user API key |
| [BLS OEWS](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/bls-oews-mcp) | Occupational wages by geography and data year from the Bureau of Labor Statistics. | No user API key |
| [GSA Per Diem](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/gsa-perdiem-mcp) | Lodging and meals-and-incidental-expense rates by locality. | Local: free key only for city names its bundled Census and county data can't place, or years before FY2021. Hosted: no key |
| [eCFR](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/ecfr-mcp) | The FAR, DFARS, and agency supplements: clause text, definitions, and what changed and when. | No user API key |
| [Federal Register](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/federal-register-mcp) | Published rules, notices, comment periods, and FAR cases. | No user API key |
| [Regulations.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/regulations-gov-mcp) | Rulemaking dockets, documents, and public comments. | Local: free key. Hosted: no key |
| [Acquisition.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/acquisition-gov-mcp) | FAR Overhaul model text, posted agency deviations, and guidance. The only known MCP server for this source. | No user API key |

The individual server READMEs contain installation instructions, configuration examples, access requirements, and testing records. A prompt does not install an MCP.

<a id="combination-plays"></a>
## Combine sources

Use multiple MCPs to connect award history, company records, and pricing context.

<a id="p01"></a>
### Size up a competitor

```text
Size up [COMPANY]: use USAspending to show contract obligations over the last 24
months, top agencies, and main work. Confirm the company's name and UEI. With
SAM.gov, add registration status, returned certification evidence, and exclusions.
If Hosted SAM.gov is connected, report its source file dates, distinguish
certification codes from detailed certification dates, and confirm current
registration on SAM.gov; flag missing evidence. Finish with two sentences on
strengths and exposure.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp) + [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

**Edition:** Hosted SAM.gov supplies dated public registration, certification codes with any listed exit dates, and exclusions; use Local full for live API details and certification entry dates.

<a id="p02"></a>
### The graduation window

```text
Find firms with 8(a) set-aside awards under NAICS [NAICS] in USAspending. Check each
selected recipient's SBA certification dates in SAM.gov and the end dates of its
relevant awards. Flag documented program exit dates within 18 months that overlap
with contract end dates within 12 months. Show the dates and source records. Treat
missing certification data as unresolved, not proof of graduation; treat an
approaching award end as a research lead, not a confirmed recompete.
If SBA exit dates aren't available from the connected SAM.gov server, list the
award-end leads and mark the 8(a) exit date as a check to do on SAM.gov.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp) + [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

**Edition:** Hosted SAM.gov supplies monthly public certification codes and any listed 8(a) exit dates, and flags exit dates that have passed; confirm current certification with SBA.

<a id="p03"></a>
### Vet a teammate

```text
Vet [COMPANY] as a teammate: check exclusions and registration expiration with
SAM.gov, then use USAspending to show whether they have primed work for [AGENCY],
including purchases funded there but awarded elsewhere. List other recent federal
work. If Hosted SAM.gov is connected, report its source file dates and confirm
current registration on SAM.gov. Flag missing evidence; opted-out entities are not
included in the hosted public mirror.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp) + [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

**Edition:** Hosted SAM.gov supplies dated public registration and exclusion checks; confirm current registration on SAM.gov.

<a id="p04"></a>
### Opportunity evidence screen

```text
Build an opportunity evidence screen for [NOTICE ID]. Pull the opportunity from
SAM.gov, then use USAspending to find comparable work at that agency under the same
NAICS, including award sizes, end dates, and evidence of a current incumbent. Keep
public facts separate from assumptions. List the internal capability, vehicle, past
performance, staffing, pricing, and risk-tolerance facts we still need; do not make
the company's bid/no-bid decision from public data alone.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp) + [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="p05"></a>
### What did the government actually pay?

```text
Find comparable federal contracts for [REQUIREMENT] under NAICS [NAICS] in
USAspending, skipping ones with a different scope. For each, show how it was
competed, obligations, current value, potential value with all options, and outlays
(money actually paid out) where reported, naming the field behind each number, plus
performance dates. Then show CALC+ ceiling rates for the matching labor categories
separately. Don't turn a total award amount into an hourly rate without a documented
staffing and period of performance basis.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp) + [GSA CALC+](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/gsa-calc-mcp)

<a id="catching-opportunities"></a>
## Find opportunities

Start with the requirement, deadline, and notice. Keep amendments and incomplete searches visible.

<a id="p06"></a>
### What federal IT work is coming that isn't out for bid yet?

```text
Using the SAM.gov tool, show me federal IT work that's coming but not out for bid
yet:
- NAICS starting with 5415 (all computer and IT services)
- Only Sources Sought and Presolicitation notices
- Still open for responses

First, count them by agency so I can see who's planning the most IT buying.
Then list the most interesting ones in a table with response due date, title,
agency, set-aside (if any), and sam.gov link.
Pick the 5 biggest or most strategic opportunities and say in one line each why a
company should respond now.
Keep notices with no stated deadline; flag sole-source intent, and only call an
opportunity big when its notice states a value.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp)

<a id="p07"></a>
### Open solicitations, deadline first

```text
Find current SAM.gov Solicitation and Combined Synopsis/Solicitation notices for
NAICS [NAICS] due between today and [N] days from now. Fetch all matches, remove
duplicate notice IDs, and sort by deadline. Show title, agency, deadline and time
zone, set-aside, and SAM.gov link. Exclude expired deadlines. Note snapshot date,
active-file coverage, missing fields, and attachment limits.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp)

<a id="p08"></a>
### Sources sought and RFIs

```text
Find sources sought notices under NAICS [NAICS] from the last 60 days, then
separately search notice titles for RFI. Identify the returned notice types and flag
response deadlines within two weeks. If I supply PSC [PSC], run a separate PSC
search, merge the results, and deduplicate by notice ID. Identify limits or missing
pages instead of treating a partial search as complete.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp)

<a id="p09"></a>
### Read one opportunity properly

```text
Retrieve opportunity [NOTICE ID] from SAM.gov, including the full description when
available. Summarize the requirement, response deadline, evaluation approach if
stated, and any explicit incumbent references. Cite the notice and distinguish
stated requirements from your interpretation. Identify attachments or amendments the
MCP did not retrieve.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp)

<a id="p10"></a>
### Fresh award notices

```text
Find contract award notices under NAICS [NAICS] posted to SAM.gov in the last [N]
days. Show the winner, reported amount, award date, posting date, notice ID, and
source link where available. Keep missing amounts or dates marked as missing. If few
results appear, report the search coverage and offer a wider window; do not infer
that no awards occurred or assume every award posts immediately.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp)

<a id="p11"></a>
### One agency's postings

```text
Find current SAM.gov notices for NAICS [NAICS] posted in the last 90 days by
[AGENCY]. Show title, agency path, notice type, posting date, response deadline, and
SAM.gov link, including postings with past deadlines. List the department, sub-tier,
and office names matched by the agency filter; command names may miss subordinate
field offices.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp)

<a id="competitor-intelligence"></a>
## Research competitors

Confirm the recipient identity before comparing customers, awards, and subcontracting records.

<a id="p12"></a>
### Find the right recipient record

```text
Search USAspending recipients for [COMPANY] and list every match with its lifetime
award total and whether it is the parent rollup or a subsidiary record. The same
company appears several times and the totals differ by a lot, so name the record you
pick and use it in everything that follows. If the search returns only near-misses,
try the other recipient search tool before deciding the company is not in the data.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="p13"></a>
### Their last 12 months

```text
Pull [COMPANY]'s federal contract activity over the last 12 months. For each award,
show award ID, agency, NAICS, performance end date, obligations added minus removals
during that window, and cumulative award obligations separately. Sort by obligations
added minus removals in the window, largest first. Add "in NAICS [NAICS] only" if I
want one code.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="p14"></a>
### Where their money comes from

```text
Retrieve [COMPANY]'s federal contract awards for the last two years from USAspending
using the selected recipient record. Summarize obligations by awarding agency, with
agency share and the underlying award count. Use compatible source filters and
paginate as needed. If only a sample is retrieved, state its size and selection
method and label the shares as sample shares, not the company's complete revenue
concentration.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="p15"></a>
### Who they sub to

```text
Find who [COMPANY] reports subcontracting work to. Confirm its recipient identity,
retrieve its ten largest contract prime awards by cumulative obligations, and search
all reported subaward pages for each. List prime ID, subcontract recipient, report
amount and action date. Explain that these are the company's subcontractors, not
primes it works under, and that absent reports do not establish self-performance.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="recompete-radar"></a>
## Track potential recompetes

Award end dates identify research leads. They do not guarantee a new solicitation.

<a id="p16"></a>
### An agency's expiring contracts

```text
Find [AGENCY]'s contract awards under NAICS [NAICS] above $[FLOOR] with recorded
performance end dates in the next nine months. Use USAspending's available filters
and paginate through the results; if end dates require local filtering, explain the
coverage. Flag implausible dates, possible follow-on awards, and option-period
uncertainty. Present the results as potential recompete leads, not confirmed future
solicitations.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="p17"></a>
### When a company's contracts end

```text
List [COMPANY]'s USAspending contract awards with recorded performance end dates
between today and [N] months from now. Sort the selected results by end date and
report the recipient identity, award ID, agency, amount field, and end date. If the
tool cannot filter directly by end date, paginate and filter the retrieved records.
State incomplete coverage and distinguish award end dates from confirmed recompete
plans.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="vetting-and-teaming"></a>
## Vet companies and find teammates

Use entity identifiers, registration records, and supporting evidence to build a useful shortlist.

<a id="p18"></a>
### Exclusion check

```text
Check whether [COMPANY / UEI] has any exclusion records. If records exist, tell me
whether any are currently active and what they are for.
If Hosted SAM.gov is connected, report the source file name and date. Entity records
are monthly snapshots; opted-out entities are not included in the hosted public
mirror. Confirm current registration and material exclusion findings on SAM.gov
before relying on them.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp)

**Edition:** Hosted SAM.gov supplies dated public exclusion records; verify current findings on SAM.gov.

<a id="p20"></a>
### Registration status at a glance

```text
Look up [COMPANY] in SAM.gov and tell me: is the registration active, when does it
expire, what is its primary NAICS, and what socioeconomic categories does it hold?
If more than 1 active registration exists, say how many and name the UEI you picked
before answering.
Do not infer corporate ownership from a shared address alone.
If Hosted SAM.gov is connected, report the source file name and date. Entity records
are monthly snapshots; opted-out entities are not included in the hosted public
mirror. Confirm current registration and material exclusion findings on SAM.gov
before relying on them.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp)

**Edition:** Hosted SAM.gov supplies monthly public registration records and certification codes; confirm current registration on SAM.gov.

<a id="p21"></a>
### SBA certification dates

```text
Retrieve [COMPANY]'s SBA certification fields from its SAM.gov entity record. Report
each listed program, status, entry date, and exit date using the source's own
labels. Distinguish a documented date from an inferred current status. An empty
certification list or a historical set-aside award does not by itself prove present
eligibility, graduation, or ineligibility.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp)

**Edition:** Hosted SAM.gov shows certification codes and any listed exit dates; entry dates and live status need the Local full SAM.gov edition.

<a id="p22"></a>
### Registration, exclusion, and integrity evidence

```text
For [UEI], retrieve the current SAM.gov registration status and exclusions, then
request the separately available entity integrity information. Report the source,
retrieval date, entity match, and any access restrictions or missing records.
Present the evidence and unresolved gaps without making a responsibility
determination.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp)

**Edition:** This prompt needs the Local full SAM.gov edition for live API or detailed certification/integrity fields.

<a id="p23"></a>
### Historical contract activity by fiscal year

```text
Using the confirmed recipient UEI for [COMPANY], retrieve USAspending dated contract
transactions for [START FY] through [END FY], one fiscal year at a time. Report
query coverage, transaction and distinct-award counts, and the earliest returned
action date. Page within a stated scope. Distinguish reporting gaps, unsupported
periods and empty responses; the earliest returned action is not proof of the
company's first federal award.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="p24"></a>
### Build a teaming shortlist

```text
Build a teaming shortlist from active SAM.gov registrants in [STATE] with NAICS
[NAICS] anywhere on their records and [SOCIOECONOMIC STATUS]. Use the server's
appropriate business-type or SBA-certification filter. Report the total count and
returned page size, paginate within the agreed scope, and deduplicate by UEI. Show
each firm's name, UEI, relevant NAICS, registration expiration, and returned
certification status and dates. Flag missing evidence and explain search coverage.
If Hosted SAM.gov is connected, report the source file name and date. Entity records
are monthly snapshots; opted-out entities are not included in the hosted public
mirror. Confirm current registration and material exclusion findings on SAM.gov
before relying on them.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp)

**Edition:** Hosted SAM.gov supplies monthly public registration records, certification codes, and any listed exit dates; entry dates and live details require Local full.

<a id="market-and-agency-intel"></a>
## Understand a market

Keep fiscal years, amount fields, and geography consistent when comparing spending.

<a id="p25"></a>
### Who an agency pays under your code

```text
Show [AGENCY]'s USAspending contract obligations under NAICS [NAICS] for the most
recently completed fiscal year. State the exact fiscal-year dates, show the
available sub-agency breakdown, and list the top ten recipients. Distinguish a
single returned category from complete organizational detail and identify any source
or filter limitations.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="p26"></a>
### Where the work is, by state

```text
Show federal contract obligations under NAICS [NAICS] by place-of-performance state
for the most recently completed fiscal year. State the exact period and geography
basis, sort the states by amount, and separate unknown locations. Do not describe
recipient headquarters spending as the location where work is performed.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="p27"></a>
### An agency's set-aside share

```text
Estimate the share of [AGENCY]'s contract obligations under NAICS [NAICS] associated
with small-business set-aside codes over the last two years. Use matching periods
and award filters for numerator and denominator, list the codes included, and show
the calculation. Keep unknown classifications separate where the source allows.
Explain that set-aside coding is not the same measure as all awards to small
businesses.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="p28"></a>
### The five-year trend

```text
Show [AGENCY]'s USAspending contract obligations under NAICS [NAICS] for the last
five completed fiscal years. Give the exact fiscal years, amounts, year-over-year
changes, and a short explanation of the trend. Keep any current partial fiscal year
separate. Treat past obligations as market context rather than a forecast of future
opportunities.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="p29"></a>
### The big vehicles

```text
Identify large IDVs under NAICS [NAICS] in USAspending, stating the amount field and
period used for ranking. For the vehicle I select, retrieve its detail and linked
child awards. Use additional searches only when their relationship to the vehicle
can be supported. Report missing links or incomplete coverage; do not conclude that
an active vehicle has no orders solely from an empty response.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="speaking-the-governments-codes"></a>
## Find the right codes

Use source references for NAICS, PSC, and size-standard research.

<a id="p30"></a>
### Find your NAICS

```text
What NAICS code covers [BUSINESS ACTIVITY]? Give me the code and the closest
alternates so I do not file under the wrong one.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="p31"></a>
### Retrieve the size standard

```text
Use the eCFR MCP to retrieve the currently available size-standard table in 13 CFR
121.201 for NAICS [CODE]. Return the matching industry, dollar or employee
threshold, and relevant exceptions or footnotes, with the source date and citation.
If the table, row, or notes cannot be retrieved completely, state that limitation
and do not supply a threshold from memory.
```

**Required MCPs:** [eCFR](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/ecfr-mcp)

<a id="p32"></a>
### Find your PSC

```text
Find PSC codes for [SERVICE AND DELIVERY MODEL], with official names. Check current
or retired status in the official PSC manual; mark unverified status unknown.
Separate codes for current opportunities from legacy codes for award history.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="p33"></a>
### Decode a PSC

```text
Use the available PSC reference tools to retrieve PSC [CODE], its official
description, and related categories. Report active or retired status only if the
returned reference explicitly provides it. If status or a detailed definition is
unavailable, identify that gap instead of inferring it from a missing search result.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="p34"></a>
### Codes to opportunities, one chain

```text
Find the PSC code for [SERVICE], then search SAM.gov opportunities under that exact
code with a response deadline still open. Codes first, opportunities second, one
chain.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp) + [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="gsa-calc"></a>
## Compare labor rates

CALC+ rates are awarded ceilings. Compare like categories and disclose differences.

<a id="p35"></a>
### Find the right labor category title

```text
I do not know GSA's exact labor category title for [ROLE]. Show me the closest
matching titles with how many rate records each carries, so I search the right
string.
```

**Required MCPs:** [GSA CALC+](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/gsa-calc-mcp)

<a id="p36"></a>
### The rate distribution

```text
Show CALC+ ceiling-rate distributions for labor-category titles matching [LABOR
CATEGORY]. Identify the exact titles, filters, record count, and available
percentile or summary statistics. Compare relevant education and experience groups
using supported filters. Explain whether results combine multiple titles, and do not
present calculated precision beyond what the source supports.
```

**Required MCPs:** [GSA CALC+](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/gsa-calc-mcp)

<a id="p37"></a>
### A company's rate card

```text
Pull [COMPANY]'s GSA rate card and every row whose labor category contains
[KEYWORD]. Ask for the total category count and page through until you have every
row; the card reports which rows came back and whether more remain. There is no
server-side vendor-plus-keyword search, so the keyword screen happens on the rows
you fetched.
```

**Required MCPs:** [GSA CALC+](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/gsa-calc-mcp)

<a id="p38"></a>
### Where does this rate sit?

```text
Position $[RATE]/hr for [LABOR CATEGORY] against relevant awarded CALC+ ceiling-rate
distributions. Show the comparison set, percentile band, geography, education and
experience differences, and data limitations. Do not call the rate defensible,
reasonable, fair, or acceptable; leave that determination to the authorized
official.
```

**Required MCPs:** [GSA CALC+](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/gsa-calc-mcp)

<a id="bls-oews"></a>
## Research wages

BLS wages describe a labor-market input. Show the occupation, location, and data year.

<a id="p39"></a>
### What the labor earns

```text
Use BLS OEWS to find median and 75th-percentile annual wages for [OCCUPATION] in
[METRO AREA]. Confirm the available data year, SOC code, and geographic match first.
Report missing, suppressed, or unavailable figures explicitly, along with the source
period; do not silently substitute a different year or location.
```

**Required MCPs:** [BLS OEWS](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/bls-oews-mcp)

<a id="p40"></a>
### Metro versus metro

```text
Compare wages for [OCCUPATION] across [METRO 1] and [METRO 2], then pull the
national median separately as the baseline. I am deciding where a position can
realistically be staffed.
```

**Required MCPs:** [BLS OEWS](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/bls-oews-mcp)

<a id="p41"></a>
### Raw wage, your burden math

```text
Give me the raw BLS wage for [OCCUPATION] in [METRO], median and 10th and 90th
percentile, current data year, with no loaded-rate estimate attached. The burden
math is mine.
```

**Required MCPs:** [BLS OEWS](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/bls-oews-mcp)

<a id="p42"></a>
### Market floor against awarded ceiling

```text
Compare the BLS OEWS wage for [OCCUPATION] in [METRO] with CALC+ ceiling rates for a
closely matched labor category. Keep raw wages and fully burdened ceiling rates
distinct. If showing a burdened-wage scenario, use [BURDEN MULTIPLIER] or ask me to
supply it, and show the formula. Explain occupation, experience, geography, and
pricing-basis differences.
```

**Required MCPs:** [GSA CALC+](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/gsa-calc-mcp) + [BLS OEWS](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/bls-oews-mcp)

<a id="p43"></a>
### The whole staffing picture

```text
Compare median wages for [OCCUPATION 1], [OCCUPATION 2], and [OCCUPATION 3] side by
side in [METRO]. I am pricing a mixed labor category task order and want the whole
staffing picture in one table, not separate lookups.
```

**Required MCPs:** [BLS OEWS](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/bls-oews-mcp)

<a id="gsa-per-diem"></a>
## Estimate travel

Name the location and travel dates before using lodging or M&IE rates.

<a id="p44"></a>
### Lodging and M&IE

```text
Retrieve GSA lodging and M&IE rates for [CITY, STATE] in [FISCAL YEAR]. Show
seasonal lodging changes, the matched locality, and the rate period. Identify an
unmatched or fallback locality clearly before using the rates in an estimate.
```

**Required MCPs:** [GSA Per Diem](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/gsa-perdiem-mcp)

<a id="p45"></a>
### Price a trip

```text
Estimate per-traveler lodging and M&IE for [N] nights in [CITY, STATE] during
[MONTH, YEAR]. Use the matching fiscal-year rates, identify the locality, show the
daily components, and apply the tool's first/last-day M&IE treatment explicitly.
State the assumed travel days and exclude airfare and other expenses unless
separately supplied. Ask for a date if it is missing instead of silently pricing
another season.
```

**Required MCPs:** [GSA Per Diem](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/gsa-perdiem-mcp)

<a id="p46"></a>
### The ZIP fallback

```text
Look up GSA per diem for ZIP [ZIP] in [FISCAL YEAR]. Report the locality actually
returned, lodging seasonality, and M&IE. If the ZIP lookup also falls back or fails
to match, keep that uncertainty visible rather than treating the location as
confirmed.
```

**Required MCPs:** [GSA Per Diem](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/gsa-perdiem-mcp)

<a id="ecfr"></a>
## Read the regulations

Retrieve the relevant codified text and its source date; check completeness before quoting.

<a id="p47"></a>
### The FAR as it reads today

```text
Retrieve FAR [CITATION] using the eCFR MCP's latest available Title 48 date. Quote
the relevant text and provide the citation and source date. Inspect its version
history and compare relevant revisions before calling a change substantive;
distinguish publication, amendment, effective, and retrieval dates when the source
supplies them.
```

**Required MCPs:** [eCFR](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/ecfr-mcp)

<a id="p48"></a>
### What changed in a FAR part

```text
Find sections in FAR Part [PART] with eCFR version changes in the last year, then
compare before and after section by section for the changes relevant to [TOPIC].
State the dates used and distinguish substantive wording changes from editorial or
structural changes. Identify incomplete comparisons rather than claiming the entire
part was reviewed.
```

**Required MCPs:** [eCFR](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/ecfr-mcp)

<a id="p49"></a>
### Chase a FAR definition

```text
Find the FAR definition of [TERM] using the eCFR MCP. Retrieve the relevant section
or complete matching definition, including numbered subparagraphs and exceptions.
Give the citation and source date. If a large section such as FAR 2.101 is
truncated, identify the missing portion and do not present a partial definition as
complete.
```

**Required MCPs:** [eCFR](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/ecfr-mcp)

<a id="federal-register"></a>
## Follow published changes

Separate direct rulemaking documents from related mentions and background notices.

<a id="p50"></a>
### What's moving on a topic

```text
Search Federal Register documents on [TOPIC] from the last 6 months across all
document types, ordered by relevance; the live items are often notices and RFIs, not
just proposed rules. For anything with an open comment period, give me the deadline.
```

**Required MCPs:** [Federal Register](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/federal-register-mcp)

<a id="p51"></a>
### Which agencies are moving

```text
Count Federal Register documents on [TOPIC] by agency for the last twelve months
using the available facet tools. State the date range, search terms, document types,
and returned counts. Use the result to choose which agencies to examine next; a
count alone does not indicate the significance of a policy change.
```

**Required MCPs:** [Federal Register](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/federal-register-mcp)

<a id="p52"></a>
### Track a FAR case

```text
Trace FAR Case [NUMBER] through Federal Register documents in date order. Separate
documents directly addressing the case from Unified Agenda entries or other notices
that merely mention it. Show proposed, final, withdrawn, and effective-date
information only where supported, with source links and any gaps in the retrieved
history.
```

**Required MCPs:** [Federal Register](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/federal-register-mcp)

<a id="regulationsgov"></a>
## Explore dockets and comments

Make the docket, deadline, sample, and supporting documents clear.

<a id="p53"></a>
### Open for comment right now

```text
What is open for comment right now on [TOPIC]? Use the Federal Register's open
comment periods with a term filter for this one; the Regulations.gov version filters
by agency only. Give me the docket ID, or the document number when a notice carries
no docket, and the closing date.
```

**Required MCPs:** [Federal Register](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/federal-register-mcp)

<a id="p54"></a>
### The real FAR and DFARS pipeline

```text
Find FAR and DFARS proposed rules with open comment periods using the
Regulations.gov MCP's available agency and document filters. Check the relevant FAR
and DARS agency codes, then distinguish actual proposed rule changes from routine
information-collection notices. Return the docket or document ID, title, closing
date, source link, and any filter or coverage limitations.
```

**Required MCPs:** [Regulations.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/regulations-gov-mcp)

<a id="p55"></a>
### Read organizational comments in a docket

```text
For docket [DOCKET ID], find organizational comments using terms such as
association, chamber, coalition, or institute. Group them by the document commented
on. Read full comment text or attachments before summarizing positions, and cite
each source. If attachments are unreadable, say so rather than infer positions from
snippets. Explain the keyword selection; it is not all comments or a measure of
consensus.
```

**Required MCPs:** [Regulations.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/regulations-gov-mcp)

<a id="far-overhaul-and-agency-deviations"></a>
## FAR Overhaul and deviations

Keep codified text, FAR Overhaul model text, and agency deviations separate, with source dates.

<a id="p56"></a>
### Find the model text and the agency's posted deviation

```text
Use the Acquisition.gov MCP to retrieve the FAR Overhaul model text for FAR Part
[PART] and find posted deviations for [AGENCY] and that part. Retrieve the relevant
indexed deviation documents. Report source links, retrieval dates, and any stated
effective dates or applicability language, with PDF page references. Keep the model
text separate from the agency's documented action, and clearly identify missing or
conflicting evidence. Do not decide which rule governs my procurement.
```

**Required MCPs:** [Acquisition.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/acquisition-gov-mcp)

<a id="p57"></a>
### Compare codified text, model text, and an agency deviation

```text
Compare the current codified text for FAR [CITATION] using eCFR with the relevant
FAR Overhaul model part and [AGENCY]'s posted deviation using Acquisition.gov. Show
the three sources separately, cite exact sections or PDF pages, and explain the
differences. Include retrieval dates and document-stated dates. Do not treat model
text as agency adoption or infer applicability from a filename.
```

**Required MCPs:** [eCFR](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/ecfr-mcp) + [Acquisition.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/acquisition-gov-mcp)

## Maintaining this library

Edit `catalog/prompts.json`, then run `python tools/build.py`. The README, PDF, and website are generated from that one file. `python tools/build.py --check` verifies that generated copies match. See [maintenance notes](MAINTAINING.md).

MIT licensed. Independently developed and not affiliated with or endorsed by any federal agency.
