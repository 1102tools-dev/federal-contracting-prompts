# Federal contracting MCP prompts

**September 2026 · Copy, paste, adapt.**

Practical questions for federal opportunities, competitor research, teaming, pricing, and regulations, built for free, open-source MCP servers. Choose the work, install and connect the required MCPs, and replace the bracketed details.

[Browse the readable website](https://1102tools.com/#prompts) · [Download the printable guide](docs/1102tools-mcp-prompt-guide.pdf) · [MCP setup instructions](https://github.com/1102tools-dev/federal-contracting-mcps#install)

## Start here

1. Choose a prompt and check its **Required MCPs** line.
2. Use the Claude and ChatGPT directory links below where available, or follow the individual server READMEs for your MCP client. Configure any required API keys outside chat and confirm that your client can see the tools.
3. Replace the bracketed details, then ask your assistant to run the prompt. Check source links, dates, and missing information before using the results.

The print guide and the online library contain the same 56 prompts for all nine MCP sources. These examples describe available source tools; this edition is not a claim that every prompt has been re-run against live APIs.

## Available in Claude and ChatGPT

All nine MCPs install and run locally today; the **Local** column links to each setup guide. Four are also published in the Claude directory and three in ChatGPT, where installs need no user API key or local Python setup. The rest are coming soon to the directories.

| MCP | Claude | ChatGPT | Local |
|---|---|---|---|
| SAM.gov | Coming soon | Coming soon | [Install](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp#installation) (free key) |
| USAspending | [Install](https://claude.ai/directory/usaspending-by-1102tools) | [Install](https://chatgpt.com/plugins/plugin_asdk_app_6a9ee668cc248191a0bdb9911b546799) | [Install](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp#installation) |
| GSA CALC+ | [Install](https://claude.ai/directory/gsa-calc-by-1102tools) | [Install](https://chatgpt.com/plugins/plugin_asdk_app_6a9eeeebfa8c81918945df0945276cb1) | [Install](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/gsa-calc-mcp#installation) |
| BLS OEWS | Coming soon | Coming soon | [Install](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/bls-oews-mcp#installation) (free key) |
| GSA Per Diem | Coming soon | Coming soon | [Install](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/gsa-perdiem-mcp#installation) (free key) |
| eCFR | [Install](https://claude.ai/directory/ecfr-by-1102tools) | [Install](https://chatgpt.com/plugins/plugin_asdk_app_6a9ef0341b04819192935fd4e5cd9b34) | [Install](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/ecfr-mcp#installation) |
| Acquisition.gov | Coming soon | Coming soon | [Install](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/acquisition-gov-mcp#install) |
| Federal Register | [Install](https://claude.ai/directory/federal-register-by-1102tools) | Coming soon | [Install](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/federal-register-mcp#installation) |
| Regulations.gov | Coming soon | Coming soon | [Install](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/regulations-gov-mcp#installation) (free key) |

**Directory install or local install?**

- **Claude and ChatGPT:** Install from the directory listing. No API key and no setup. The MCP runs on Cloudflare at its own 1102tools.com address, such as `usaspending.1102tools.com`, and your AI app connects to it over the internet. The hosted servers don't store your queries, results, or conversations, and request logging is turned off, so no one at 1102tools sees what you look up. The server code and Cloudflare setup are public in [federal-contracting-mcps](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/deploy). Cloudflare still handles connection data such as IP addresses, and Claude or ChatGPT handles your conversation under its own privacy policy.
- **Local:** The MCP runs on your own computer and works with any MCP-compatible app. Requests go straight from your computer to the government source, and nothing passes through 1102tools.com. SAM.gov, BLS OEWS, GSA Per Diem and Regulations.gov need a free API key from the agency. Each setup guide shows how to get one.

A prompt does not install an MCP. Connect every source listed under **Required MCPs** before running it; if two are listed, both are required. Other sources and MCP clients use the individual server setup instructions below.

## Browse by task

| Task | Prompts |
|---|---|
| [Combine sources](#combination-plays) | 5 |
| [Find opportunities](#catching-opportunities) | 5 |
| [Research competitors](#competitor-intelligence) | 4 |
| [Track potential recompetes](#recompete-radar) | 2 |
| [Vet companies and find teammates](#vetting-and-teaming) | 7 |
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
| [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp) | Opportunities, entity registrations, exclusions, and contract-award records. | Free SAM.gov key for the full local edition; keyless hosted edition coming soon |
| [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp) | Awards, obligations, recipients, agencies, and reported subawards. | No user API key |
| [GSA CALC+](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/gsa-calc-mcp) | Awarded labor-category ceiling rates and comparison data. | No user API key |
| [BLS OEWS](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/bls-oews-mcp) | Occupational wages by geography and data year. | Optional key; limited keyless access |
| [GSA Per Diem](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/gsa-perdiem-mcp) | Lodging and meals-and-incidental-expense rates by locality. | Personal key recommended; shared fallback |
| [eCFR](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/ecfr-mcp) | Codified regulatory text, dates, and version comparisons. | No user API key |
| [Acquisition.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/acquisition-gov-mcp) | FAR Overhaul model text, posted agency deviations, and guidance. | No user API key |
| [Federal Register](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/federal-register-mcp) | Published rules, notices, comment periods, and FAR cases. | No user API key |
| [Regulations.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/regulations-gov-mcp) | Rulemaking dockets, documents, and public comments. | Personal key recommended; shared fallback |

The individual server READMEs contain installation instructions, configuration examples, access requirements, and testing records. A prompt does not install an MCP.

<a id="combination-plays"></a>
## Combine sources

Use multiple MCPs to connect award history, company records, and pricing context.

<a id="p01"></a>
### Size up a competitor

```text
Size up [COMPANY] as a competitor: their last 24 months of awards and top agencies
from USAspending, then their registration status, socioeconomic categories, and any
exclusions from SAM.gov. If SAM returns multiple registrations, say so and list them
before picking. Finish with 2 sentences on where they are strong and where they are
exposed.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp) + [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="p02"></a>
### The graduation window

```text
Find firms with 8(a) set-aside awards under NAICS [NAICS] in USAspending. Check each
selected recipient's SBA certification dates in SAM.gov and the end dates of its
relevant awards. Flag documented program exit dates within 18 months that overlap
with contract end dates within 12 months. Show the dates and source records. Treat
missing certification data as unresolved, not proof of graduation; treat an
approaching award end as a research lead, not a confirmed recompete.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp) + [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="p03"></a>
### Vet a teammate

```text
Vet [COMPANY] as a teammate: exclusions and registration expiration from SAM.gov,
then their award history from USAspending, including whether they have primed work
at [AGENCY] before.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp) + [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

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
Find comparable federal contract awards for [REQUIREMENT] under NAICS [NAICS] in
USAspending. Distinguish obligations, current award value, and potential ceiling
wherever the source provides them; identify the field used for each amount. Show
performance dates and scope differences. Compare relevant CALC+ labor-category
ceiling rates separately. Do not convert a total award amount into an hourly price
without a documented staffing and performance-period basis.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp) + [GSA CALC+](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/gsa-calc-mcp)

<a id="catching-opportunities"></a>
## Find opportunities

Start with the requirement, deadline, and notice. Keep amendments and incomplete searches visible.

<a id="p06"></a>
### Open solicitations, deadline first

```text
Search SAM.gov for solicitations and combined synopses under NAICS [NAICS] with a
response deadline between today and [N] days out. Give me title, agency, deadline,
and set-aside type, and drop anything whose deadline has already passed even if SAM
still marks it active. The search filters 1 notice type per call, so expect 2
searches merged, not 1.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp)

<a id="p07"></a>
### Sources sought and RFIs

```text
Find sources sought notices under NAICS [NAICS] from the last 60 days, then
separately search notice titles for RFI. Identify the returned notice types and flag
response deadlines within two weeks. If I supply PSC [PSC], run a separate PSC
search, merge the results, and deduplicate by notice ID. Identify limits or missing
pages instead of treating a partial search as complete.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp)

<a id="p08"></a>
### Read one opportunity properly

```text
Retrieve opportunity [NOTICE ID] from SAM.gov, including the full description when
available. Summarize the requirement, response deadline, evaluation approach if
stated, and any explicit incumbent references. Cite the notice and distinguish
stated requirements from your interpretation. Identify attachments or amendments the
MCP did not retrieve.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp)

<a id="p09"></a>
### Fresh award notices

```text
Find contract award notices under NAICS [NAICS] posted to SAM.gov in the last [N]
days. Show the winner, reported amount, award date, posting date, notice ID, and
source link where available. Keep missing amounts or dates marked as missing. If few
results appear, report the search coverage and offer a wider window; do not infer
that no awards occurred or assume every award posts immediately.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp)

<a id="p10"></a>
### One agency's postings

```text
Search opportunities under NAICS [NAICS] from the last 90 days with the result limit
set high, then filter for [AGENCY] yourself from the agency path field in the
results. The agency filter only screens what was fetched, so if the total count is
much larger than what came back, page through before concluding anything.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp)

<a id="competitor-intelligence"></a>
## Research competitors

Confirm the recipient identity before comparing customers, awards, and subcontracting records.

<a id="p11"></a>
### Find the right recipient record

```text
Search USAspending recipients for [COMPANY] and list every match with its lifetime
award total and whether it is the parent rollup or a subsidiary record. The same
company appears several times and the totals differ by a lot, so name the record you
pick and use it in everything that follows. If the search returns only near-misses,
try the other recipient search tool before deciding the company is not in the data.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="p12"></a>
### Their last 12 months

```text
Pull [COMPANY]'s federal contract awards with activity in the last 12 months: award
ID, agency, amount, NAICS, and period of performance end date. Sort by amount. Add
"in NAICS [NAICS] only" if I want one code.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="p13"></a>
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

<a id="p14"></a>
### Who they sub to

```text
Retrieve [COMPANY]'s ten largest prime awards from USAspending using a confirmed
recipient identity. For each, search the reported subawards and list the prime
award, subaward recipient, amount, and date. Keep similarly named firms and joint
ventures separate unless identifiers establish the relationship. Empty subaward
results mean no matching reports were returned; they do not establish that the prime
self-performed everything.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="recompete-radar"></a>
## Track potential recompetes

Award end dates identify research leads. They do not guarantee a new solicitation.

<a id="p15"></a>
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

<a id="p16"></a>
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

<a id="p17"></a>
### Exclusion check

```text
Check whether [COMPANY / UEI] has any exclusion records. If records exist, tell me
whether any are currently active and what they are for.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp)

<a id="p18"></a>
### Untangle multiple registrations

```text
Search SAM.gov for [COMPANY]. List each matching entity's legal name, UEI, CAGE
code, address, and registration status before choosing a record. Group
related-looking records for review, but do not infer headquarters or corporate
ownership from a shared address alone. Identify which UEI best matches the company I
mean and explain any unresolved ambiguity.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp)

<a id="p19"></a>
### Registration status at a glance

```text
Look up [COMPANY] in SAM.gov and tell me: is the registration active, when does it
expire, what is its primary NAICS, and what socioeconomic categories does it hold?
If more than 1 active registration exists, say how many and name the UEI you picked
before answering.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp)

<a id="p20"></a>
### SBA certification dates

```text
Retrieve [COMPANY]'s SBA certification fields from its SAM.gov entity record. Report
each listed program, status, entry date, and exit date using the source's own
labels. Distinguish a documented date from an inferred current status. An empty
certification list or a historical set-aside award does not by itself prove present
eligibility, graduation, or ineligibility.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp)

<a id="p21"></a>
### Registration, exclusion, and integrity evidence

```text
For [UEI], retrieve the current SAM.gov registration status and exclusions, then
request the separately available entity integrity information. Report the source,
retrieval date, entity match, and any access restrictions or missing records.
Present the evidence and unresolved gaps without making a responsibility
determination.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp)

<a id="p22"></a>
### How far back they go

```text
Research [COMPANY]'s historical contract awards in SAM.gov for [START FY] through
[END FY], in manageable fiscal-year ranges supported by the server. Use a confirmed
entity identifier where the tool permits it. Show the earliest returned award,
counts by period, and query coverage. Separate unsupported date ranges, empty
responses, and sparse reporting; do not treat the earliest returned record as the
company's first-ever federal award.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp)

<a id="p23"></a>
### Build a teaming shortlist

```text
Build a teaming shortlist from active SAM.gov registrants in [STATE] with NAICS
[NAICS] anywhere on their records and [SOCIOECONOMIC STATUS]. Use the server's
appropriate business-type or SBA-certification filter. Report the total count and
returned page size, paginate within the agreed scope, and deduplicate by UEI. Show
each firm's name, UEI, relevant NAICS, registration expiration, and returned
certification status and dates. Flag missing evidence and explain search coverage.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp)

<a id="market-and-agency-intel"></a>
## Understand a market

Keep fiscal years, amount fields, and geography consistent when comparing spending.

<a id="p24"></a>
### Who an agency pays under your code

```text
Show [AGENCY]'s USAspending contract obligations under NAICS [NAICS] for the most
recently completed fiscal year. State the exact fiscal-year dates, show the
available sub-agency breakdown, and list the top ten recipients. Distinguish a
single returned category from complete organizational detail and identify any source
or filter limitations.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="p25"></a>
### Where the work is, by state

```text
Show federal contract obligations under NAICS [NAICS] by place-of-performance state
for the most recently completed fiscal year. State the exact period and geography
basis, sort the states by amount, and separate unknown locations. Do not describe
recipient headquarters spending as the location where work is performed.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="p26"></a>
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

<a id="p27"></a>
### The five-year trend

```text
Show [AGENCY]'s USAspending contract obligations under NAICS [NAICS] for the last
five completed fiscal years. Give the exact fiscal years, amounts, year-over-year
changes, and a short explanation of the trend. Keep any current partial fiscal year
separate. Treat past obligations as market context rather than a forecast of future
opportunities.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="p28"></a>
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

<a id="p29"></a>
### Find your NAICS

```text
What NAICS code covers [PLAIN-ENGLISH BUSINESS ACTIVITY]? Give me the code and the
closest alternates so I do not file under the wrong one.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="p30"></a>
### Retrieve the size standard

```text
Use the eCFR MCP to retrieve the currently available size-standard table in 13 CFR
121.201 for NAICS [CODE]. Return the matching industry, dollar or employee
threshold, and relevant exceptions or footnotes, with the source date and citation.
If the table, row, or notes cannot be retrieved completely, state that limitation
and do not supply a threshold from memory.
```

**Required MCPs:** [eCFR](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/ecfr-mcp)

<a id="p31"></a>
### Find your PSC

```text
What PSC codes cover [PLAIN-ENGLISH SERVICE]? Give me the codes and official names
so I can search with them.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="p32"></a>
### Decode a PSC

```text
Use the available PSC reference tools to retrieve PSC [CODE], its official
description, and related categories. Report active or retired status only if the
returned reference explicitly provides it. If status or a detailed definition is
unavailable, identify that gap instead of inferring it from a missing search result.
```

**Required MCPs:** [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="p33"></a>
### Codes to opportunities, one chain

```text
Find the PSC code for [PLAIN-ENGLISH SERVICE], then search SAM.gov opportunities
under that exact code with a response deadline still open. Codes first,
opportunities second, one chain.
```

**Required MCPs:** [SAM.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/sam-gov-mcp) + [USAspending](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/usaspending-gov-mcp)

<a id="gsa-calc"></a>
## Compare labor rates

CALC+ rates are awarded ceilings. Compare like categories and disclose differences.

<a id="p34"></a>
### Find the right labor category title

```text
I do not know GSA's exact labor category title for [ROLE]. Show me the closest
matching titles with how many rate records each carries, so I search the right
string.
```

**Required MCPs:** [GSA CALC+](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/gsa-calc-mcp)

<a id="p35"></a>
### The rate distribution

```text
Show CALC+ ceiling-rate distributions for labor-category titles matching [LABOR
CATEGORY]. Identify the exact titles, filters, record count, and available
percentile or summary statistics. Compare relevant education and experience groups
using supported filters. Explain whether results combine multiple titles, and do not
present calculated precision beyond what the source supports.
```

**Required MCPs:** [GSA CALC+](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/gsa-calc-mcp)

<a id="p36"></a>
### A company's rate card

```text
Pull [COMPANY]'s GSA rate card and every row whose labor category contains
[KEYWORD]. Ask for the total category count and page through until you have every
row; the card reports which rows came back and whether more remain. There is no
server-side vendor-plus-keyword search, so the keyword screen happens on the rows
you fetched.
```

**Required MCPs:** [GSA CALC+](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/gsa-calc-mcp)

<a id="p37"></a>
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

<a id="p38"></a>
### What the labor earns

```text
Use BLS OEWS to find median and 75th-percentile annual wages for [OCCUPATION] in
[METRO AREA]. Confirm the available data year, SOC code, and geographic match first.
Report missing, suppressed, or unavailable figures explicitly, along with the source
period; do not silently substitute a different year or location.
```

**Required MCPs:** [BLS OEWS](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/bls-oews-mcp)

<a id="p39"></a>
### Metro versus metro

```text
Compare wages for [OCCUPATION] across [METRO 1] and [METRO 2], then pull the
national median separately as the baseline. I am deciding where a position can
realistically be staffed.
```

**Required MCPs:** [BLS OEWS](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/bls-oews-mcp)

<a id="p40"></a>
### Raw wage, your burden math

```text
Give me the raw BLS wage for [OCCUPATION] in [METRO], median and 10th and 90th
percentile, current data year, with no loaded-rate estimate attached. The burden
math is mine.
```

**Required MCPs:** [BLS OEWS](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/bls-oews-mcp)

<a id="p41"></a>
### Market floor against awarded ceiling

```text
Compare the BLS OEWS wage for [OCCUPATION] in [METRO] with CALC+ ceiling rates for a
closely matched labor category. Keep raw wages and fully burdened ceiling rates
distinct. If showing a burdened-wage scenario, use [BURDEN MULTIPLIER] or ask me to
supply it, and show the formula. Explain occupation, experience, geography, and
pricing-basis differences.
```

**Required MCPs:** [GSA CALC+](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/gsa-calc-mcp) + [BLS OEWS](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/bls-oews-mcp)

<a id="p42"></a>
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

<a id="p43"></a>
### Lodging and M&IE

```text
Retrieve GSA lodging and M&IE rates for [CITY, STATE] in [FISCAL YEAR]. Show
seasonal lodging changes, the matched locality, and the rate period. Identify an
unmatched or fallback locality clearly before using the rates in an estimate.
```

**Required MCPs:** [GSA Per Diem](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/gsa-perdiem-mcp)

<a id="p44"></a>
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

<a id="p45"></a>
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

<a id="p46"></a>
### The FAR as it reads today

```text
Retrieve FAR [CITATION] using the eCFR MCP's latest available Title 48 date. Quote
the relevant text and provide the citation and source date. Inspect its version
history and compare relevant revisions before calling a change substantive;
distinguish publication, amendment, effective, and retrieval dates when the source
supplies them.
```

**Required MCPs:** [eCFR](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/ecfr-mcp)

<a id="p47"></a>
### What changed in a FAR part

```text
Find sections in FAR Part [PART] with eCFR version changes in the last year, then
compare before and after section by section for the changes relevant to [TOPIC].
State the dates used and distinguish substantive wording changes from editorial or
structural changes. Identify incomplete comparisons rather than claiming the entire
part was reviewed.
```

**Required MCPs:** [eCFR](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/ecfr-mcp)

<a id="p48"></a>
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

<a id="p49"></a>
### What's moving on a topic

```text
Search Federal Register documents on [TOPIC] from the last 6 months across all
document types, ordered by relevance; the live items are often notices and RFIs, not
just proposed rules. For anything with an open comment period, give me the deadline.
```

**Required MCPs:** [Federal Register](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/federal-register-mcp)

<a id="p50"></a>
### Which agencies are moving

```text
Count Federal Register documents on [TOPIC] by agency for the last twelve months
using the available facet tools. State the date range, search terms, document types,
and returned counts. Use the result to choose which agencies to examine next; a
count alone does not indicate the significance of a policy change.
```

**Required MCPs:** [Federal Register](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/federal-register-mcp)

<a id="p51"></a>
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

<a id="p52"></a>
### Open for comment right now

```text
What is open for comment right now on [TOPIC]? Use the Federal Register's open
comment periods with a term filter for this one; the Regulations.gov version filters
by agency only. Give me the docket ID, or the document number when a notice carries
no docket, and the closing date.
```

**Required MCPs:** [Federal Register](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/federal-register-mcp)

<a id="p53"></a>
### The real FAR and DFARS pipeline

```text
Find FAR and DFARS proposed rules with open comment periods using the
Regulations.gov MCP's available agency and document filters. Check the relevant FAR
and DARS agency codes, then distinguish actual proposed rule changes from routine
information-collection notices. Return the docket or document ID, title, closing
date, source link, and any filter or coverage limitations.
```

**Required MCPs:** [Regulations.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/regulations-gov-mcp)

<a id="p54"></a>
### Who's lobbying a docket

```text
For docket [DOCKET ID], search Regulations.gov comments for organizational
submitters, including terms such as association, chamber, coalition, or institute.
Retrieve details and attachment references for the relevant matches. Summarize each
identified organization's position with citations, distinguish names from verified
affiliations, and explain the selection method. Do not treat this keyword sample as
all comments or a measure of consensus.
```

**Required MCPs:** [Regulations.gov](https://github.com/1102tools-dev/federal-contracting-mcps/tree/main/servers/regulations-gov-mcp)

<a id="far-overhaul-and-agency-deviations"></a>
## FAR Overhaul and deviations

Keep codified text, FAR Overhaul model text, and agency deviations separate, with source dates.

These two examples have not been live-tested as part of this guide refresh.

<a id="p55"></a>
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

<a id="p56"></a>
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

MIT licensed. Built by James Jenrette. Independently developed and not affiliated with or endorsed by any federal agency.
