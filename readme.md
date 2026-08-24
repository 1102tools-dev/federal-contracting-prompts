# federal-contracting-prompts

> [!IMPORTANT]
> **Advanced MCP request library.** You do not need this repository to use a packaged 1102tools agent. Agents accept ordinary-language requests and open their own menus. Start at the [Agents page](https://1102tools.com/tools) and [How It Works](https://1102tools.com/examples) unless you deliberately maintain standalone MCP servers.

Sixty-four copy-paste prompts for federal contracting research: competitor intelligence, bid decisions, recompete timing, pricing, market research, and the regulatory checks in between. Written for small businesses chasing federal work first, and for the acquisition workforce second. The 60 original MCP patterns were executed against live government APIs before publishing. Four agent launch prompts have deterministic routing contracts; the two acquisition-policy patterns remain release-candidate patterns pending the clean-client matrix.

**These are not standalone prompts.** They depend on the appropriate [federal contracting MCP servers](https://github.com/1102tools-dev/federal-contracting-mcps), such as SAM.gov, USASpending, GSA CALC+, BLS OEWS, GSA Per Diem, eCFR, Federal Register, Regulations.gov, or Acquisition.gov. Without the required server, an AI may answer from memory instead of querying the named source. Standalone MCP installation is advanced and documented in each server directory.

Website: [1102tools.com](https://1102tools.com)

## What's in here

| Section | Prompts | The job |
|---|---|---|
| [Combination plays](#combination-plays) | 5 | Cross-database moves aimed at a bid decision |
| [Catching opportunities](#catching-opportunities) | 5 | Solicitations, sources sought, fresh award notices |
| [Competitor intelligence](#competitor-intelligence) | 4 | Who wins what, where, and who they sub to |
| [Recompete radar](#recompete-radar) | 2 | Contracts coming up for rebid |
| [Vetting and teaming](#vetting-and-teaming) | 7 | Exclusions, registrations, certifications, shortlists |
| [Market and agency intel](#market-and-agency-intel) | 5 | Sizing agencies, trends, set-aside shares, big vehicles |
| [Speaking the government's codes](#speaking-the-governments-codes) | 5 | NAICS and PSC, found and decoded |
| [What should it cost](#what-should-it-cost) | 12 | Awarded rates, market wages, travel |
| [Watching the rules](#watching-the-rules) | 9 | The FAR today, what's changing, who's fighting it |
| [Agent and skill workflows](#agent-and-skill-workflows-ten-launch-lines) | 10 | PWS, IGCE, OT, research, growth, and acquisition-policy workflows |

## How to use this library

Everything below is meant to be copied, pasted, and adapted. Square brackets mark the parts you replace: `[COMPANY]`, `[NAICS]`, `[STATE]`. If you do not know your NAICS or PSC code yet, the [codes prompts](#speaking-the-governments-codes) find them; run those first. They need no API key, USASpending answers both lookups, so a rate-limited SAM.gov key cannot stand between you and your own codes.

A lot of this library runs the same way: the research prompts live on key-free USASpending, and SAM.gov enters when you reach live opportunities and company vetting. Your AI will usually pick the right server on its own; if it reaches for the wrong one or answers from memory, name the one you want: "use the sam-gov MCP" or "use USASpending for this." When a number matters, ask for the raw value and where it came from, and when recency matters, 1 cheap call checks when USASpending last refreshed its award data.

Prompts are written for one job each, and every prompt names the MCPs it uses right under it, so you know what has to be installed before you paste. Chain them: run a competitor scan, then feed what came back into the next prompt. The combination plays below show what chaining looks like when it is aimed at a bid decision.

> [!NOTE]
> **If the acronyms are new, 30 seconds of vocabulary.** An MCP server is a source adapter for an official federal system. NAICS and PSC are the catalog codes for what you sell: NAICS names your industry, PSC names the service or product. A set-aside is a competition restricted to small businesses, sometimes to one SBA program: 8(a) for disadvantaged firms, HUBZone for firms in designated underutilized zones, SDVOSB for service-disabled-veteran-owned, WOSB for woman-owned. A UEI is a company's ID in SAM.gov. An IDV is an umbrella contract that task orders are placed under, and a recompete is the rebid when a contract ends. PWS, SOO, and IGCE are defined in [the agent and skill workflows](#agent-and-skill-workflows-ten-launch-lines), where they are used.

## Combination plays

SAM.gov and USASpending answer different halves of the same question, so the strongest prompts use both. Run these as one request; your AI will make several tool calls and stitch the answer. Four of the five run on the big two alone; the pricing play reaches into GSA CALC+, and its label says so.

#### Size up a competitor

```text
Size up [COMPANY] as a competitor: their last 24 months of awards and top agencies
from USASpending, then their registration status, socioeconomic categories, and any
exclusions from SAM.gov. If SAM returns multiple registrations, say so and list them
before picking. Finish with 2 sentences on where they are strong and where they are
exposed.
```

*MCPs used: USASpending + SAM.gov*

#### The graduation window

Finds 8(a) firms whose program exit and contract end dates line up. Those are the firms whose work is about to be in play.

```text
Find 8(a) firms winning work under NAICS [NAICS]: search USASpending for awards with
8(a) set-aside types, take the top recipients, then pull each one's SBA certification
dates and current contract end dates. Flag firms graduating within 18 months whose
contracts also end within 12; those are the real targets. If a firm shows no 8(a)
certification despite winning 8(a) work, or an exit date already past, read that as
graduated; lapsed entries can linger on the record with their dates intact.
```

*MCPs used: USASpending + SAM.gov*

#### Vet a teammate

```text
Vet [COMPANY] as a teammate: exclusions and registration expiration from SAM.gov,
then their award history from USASpending, including whether they have primed work
at [AGENCY] before.
```

*MCPs used: SAM.gov + USASpending*

#### Should I bid this?

```text
Should I bid [NOTICE ID]? Pull the opportunity description from SAM.gov, then use
USASpending to find who holds similar work at that agency under the same NAICS:
award sizes and end dates, biggest first. Check the end dates before calling anyone
the incumbent; an already-ended award usually means the work moved to a follow-on
order, so look for a newer award to the same recipient before concluding they exited.
```

*MCPs used: SAM.gov + USASpending*

#### What did the government actually pay?

```text
What did the government actually pay for work like [REQUIREMENT]? Find comparable
awards under NAICS [NAICS] in USASpending and label the values for what they are:
multi-year contract ceilings, not hourly prices. Then put awarded CALC+ ceiling
rates for the matching labor categories next to them as the per-hour benchmark.
Scale from one, rates from the other; do not divide one by the other without a
period of performance and staffing count you can defend.
```

*MCPs used: USASpending + GSA CALC+*

## The two databases that matter most

Most of the value, and most of the confusion, lives in SAM.gov and USASpending. They sound interchangeable and are not. SAM.gov is the government's front door: who is registered to do business, who is excluded, and what opportunities are posted right now. USASpending is the government's receipts: every award that has already happened, who got it, from which office, and for how much. Forward-looking versus backward-looking. You market with one and you research with the other.

| | SAM.gov | USASpending |
|---|---|---|
| What it is | Registration, exclusions, and posted opportunities | Award and spending history for every agency |
| API key | Required, free, rotates every 90 days | None |
| Rate limits | Tiered by account role; see the warning below | Generous; comfortable for deep research |
| Freshness | Opportunities and registrations are live | Fed by FPDS on a lag, and new DoD awards are withheld from public reporting for 90 days |
| What only it has | Exclusion records, registration status and expiration, SBA certification entry and exit dates, active solicitations, sources sought | Complete award history, subawards, recipient profiles, agency spending breakdowns, IDV structures |
| Best at | Vetting a specific company; catching opportunities | Sizing markets and competitors; timing recompetes |

**You may not need SAM.gov at all.** If the job is competitor research, market sizing, or finding out who buys what you sell, USASpending answers it with no key, no rotation, and no meaningful rate ceiling. A surprising amount of what people reach for SAM.gov to do is really an awards question, and awards live in USASpending.

**You need SAM.gov when the question is about a specific company's standing or about work that has not been awarded yet.** Exclusion and debarment checks before you team. Whether a registration is active and when it expires. Small business status and SBA certifications, including when a company entered a program like 8(a) and when it exits, which used to mean a separate trip to the SBA's Dynamic Small Business Search. And the forward pipeline: solicitations, sources sought, and RFIs are posted here and nowhere else.

> [!WARNING]
> **Check your SAM.gov key tier before you rely on it.** SAM.gov keys are rate-limited by the account behind them, and the API discloses the tiers when you hit the wall: 10 requests per day for an account holding no SAM role, 1,000 per day for a personal account with a role, 10,000 for a federal system account. A 10-a-day key dies inside a single combination play from this library. The tier rides the account, not the key: regenerating keys buys you nothing, I watched 3 keys from roleless accounts hit the same wall in one evening. Blowing the cap also costs more than the day; the lockout I measured ran past the next daily reset. So the fix is roles, not keys: log in, get a role on your account, then generate the key from there. Ignore the error text's advice to switch to a system account key; system accounts are issued to government systems, not vendors. No SAM.gov account at all? Registering is free at sam.gov and can take days to weeks, so plan for it. And know the one failure with no workaround: live opportunity search exists only on SAM.gov, so when that prompt stalls on a rate limit, wait for the reset instead of hunting a reroute that does not exist.

> [!IMPORTANT]
> **The DoD delay, checked against the live data.** New DoD awards are withheld from public FPDS reporting for 90 days for operational security, and USASpending inherits that. But the picture is messier than "everything is a quarter behind": modifications and obligation activity on existing DoD contracts show up within days, and award notices posted on SAM.gov are not delayed at all. Practical reading: treat a competitor's newest DoD awards as invisible for up to 90 days, trust the activity you can see on their existing contracts, and use SAM.gov award notices when you need the fresh wins.

## Catching opportunities

One behavior worth knowing first: SAM marks a notice active until its archive date, so "active" does not mean the response deadline has not passed; in live testing, half the notices marked active had deadlines already behind them. The prompts below filter on the deadline, which is the date you actually care about.

#### Open solicitations, deadline first

```text
Search SAM.gov for solicitations and combined synopses under NAICS [NAICS] with a
response deadline between today and [N] days out. Give me title, agency, deadline,
and set-aside type, and drop anything whose deadline has already passed even if SAM
still marks it active. The search filters 1 notice type per call, so expect 2
searches merged, not 1.
```

*MCPs used: SAM.gov*

#### Sources sought and RFIs

```text
Find sources sought notices under NAICS [NAICS] from the last 60 days, plus anything
titled RFI; RFI is a title word, not a notice type, so it rides on the sources sought
search as a title check. Flag which ones close within 2 weeks. Then run it again
under PSC [PSC] if I give you one; the filters combine as AND, so separate runs
cover more ground than one narrow query.
```

*MCPs used: SAM.gov*

#### Read one opportunity properly

```text
Pull the full description for opportunity [NOTICE ID] and summarize what they
actually want, the evaluation approach if stated, and anything that looks like
incumbent language.
```

*MCPs used: SAM.gov*

#### Fresh award notices

The one place new DoD wins show up without the 90-day wait.

```text
Show me contract award notices under NAICS [NAICS] from the last [N] days: who won,
how much, and the award date. These post to SAM immediately, including DoD awards
that will not hit USASpending for 90 days. Coverage is uneven by NAICS, though: a
narrow code over a short window can legitimately return 0 or 1 notice, so widen the
window before concluding nothing posted.
```

*MCPs used: SAM.gov*

#### One agency's postings

```text
Search opportunities under NAICS [NAICS] from the last 90 days with the result limit
set high, then filter for [AGENCY] yourself from the agency path field in the
results. The agency filter only screens what was fetched, so if the total count is
much larger than what came back, page through before concluding anything.
```

*MCPs used: SAM.gov*

## Competitor intelligence

One quirk to know: date-window filters here run on when an award was last touched, not when it was signed, so "last 12 months" means recent activity, which usually is what you want anyway.

#### Find the right recipient record

```text
Search USASpending recipients for [COMPANY] and list every match with its lifetime
award total and whether it is the parent rollup or a subsidiary record. The same
company appears several times and the totals differ by a lot, so name the record you
pick and use it in everything that follows. If the search returns only near-misses,
try the other recipient search tool before deciding the company is not in the data.
```

*MCPs used: USASpending*

#### Their last 12 months

```text
Pull [COMPANY]'s federal contract awards with activity in the last 12 months: award
ID, agency, amount, NAICS, and period of performance end date. Sort by amount. Add
"in NAICS [NAICS] only" if I want one code.
```

*MCPs used: USASpending*

#### Where their money comes from

```text
Pull [COMPANY]'s awards for the last 2 years sorted by amount, in batches of 25 to
30 rows so nothing overflows, then tally them by awarding agency yourself and show
me where the concentration is. There is no direct agency-breakdown-by-recipient
call; for a company with hundreds of awards, the top 25 to 30 by dollar shows the
real concentration, just say that is what the tally covers.
```

*MCPs used: USASpending*

#### Who they sub to

```text
Pull [COMPANY]'s 10 largest prime awards by amount, and check each recipient name
actually contains the company's name; name matching can pull in joint ventures under
a different display name. Then search subawards under each genuine award ID and
merge the results. Who do they sub to, and for how much? Expect some of the largest
primes to show 0 subawards on file; treat that as a reporting gap, not proof they
self-perform everything.
```

*MCPs used: USASpending*

> [!WARNING]
> **Subaward data is only as good as the prime's reporting.** Primes self-report subawards through FSRS, small subcontracts below the reporting threshold often never appear, and there is no lookup for "who does this company sub under" at all; the data only travels prime-downward. A thin subaward picture may be a reporting gap, not the whole story.

## Recompete radar

The date filters cannot select on period of performance end dates, so the working method is sort and scan, and it works well.

#### An agency's expiring contracts

```text
Pull [AGENCY]'s contracts under NAICS [NAICS] above $[FLOOR], sorted by end date
descending. Drop any row with an obviously corrupted end date; they occasionally
come back centuries off and tend to sit right at the top. Then keep paging past the
far-future awards until the end dates fall inside the next 9 months; those are my
recompete targets. For a broad agency and code that takes several pages, not the
first one.
```

*MCPs used: USASpending*

#### When a company's contracts end

What they will be defending, and when.

```text
When do [COMPANY]'s contracts end? List their awards sorted by end date descending,
dropping corrupted dates on sight. Their longest-remaining commitments come first;
keep paging until the dates cross today, and stop once they fall inside the next 12
to 24 months. That stretch is what they will be defending and when; no filter jumps
straight to it.
```

*MCPs used: USASpending*

## Vetting and teaming

One naming trap: SBA program certifications live in the entity record, not in the tool named for reps and certs, which returns FAR clause responses instead. The wording below steers around it.

#### Exclusion check

The standalone version of the check a contracting officer runs before award; as a vendor you run it before you put a company on your team.

```text
Check whether [COMPANY / UEI] has any exclusion records. If records exist, tell me
whether any are currently active and what they are for.
```

*MCPs used: SAM.gov*

#### Untangle multiple registrations

```text
Search SAM.gov entities for [COMPANY]. If more than one active registration comes
back, list every UEI, CAGE code, and address before picking one; large companies
register each location separately, and the answer changes depending on which record
you check. Group them by mailing address to spot the headquarters, and normalize the
punctuation first; the same address gets spelled several ways across records.
```

*MCPs used: SAM.gov*

#### Registration status at a glance

```text
Look up [COMPANY] in SAM.gov and tell me: is the registration active, when does it
expire, what is its primary NAICS, and what socioeconomic categories does it hold?
If more than 1 active registration exists, say how many and name the UEI you picked
before answering.
```

*MCPs used: SAM.gov*

#### SBA certification dates

```text
Pull [COMPANY]'s SBA certifications from their SAM entity record, with the entry and
exit date for each. If they are in the 8(a) program, the exit date is the graduation
date. Expect lapses: a firm found through its old set-aside wins can show an empty
list or an exit date already past, and the dates on the record are the authoritative
answer.
```

*MCPs used: SAM.gov*

#### Responsibility check with FAPIIS

A contracting officer's move: the responsibility determination file, in two pulls.

```text
Run a vendor responsibility check on [UEI] for registration status and exclusions,
then pull FAPIIS integrity records separately; the one-pass check does not include
those.
```

*MCPs used: SAM.gov*

#### How far back they go

```text
How far back does [COMPANY]'s federal award history actually go? Check SAM.gov
contract awards decade by decade, FY1970 forward; the data reaches back that far
even though most tools never look before 2008. Volumes thin out before 1980, so read
single-digit years as archival traces, not gaps in your search.
```

*MCPs used: SAM.gov*

#### Build a teaming shortlist

```text
Search SAM.gov for active registrants in [STATE] under NAICS [NAICS], counting any
NAICS on file rather than primary only, which surfaced 4x more firms in testing,
holding [woman-owned / SDVOSB] status. Ask for the total count first: results come
back 10 to a page, so tell me how many pages that implies and keep paging until done
or I say stop, deduping by UEI since a page can repeat a record. I am building a
teaming shortlist. For HUBZone or 8(a), name the program instead of a code: SBA
certifications filter through their own SBA parameter, separate from the plain
business type codes, added to the sam-gov server in August 2026, so update the
server if that search errors. Either way, confirm the certification entry and exit
dates on each firm's record; lapses are common.
```

*MCPs used: SAM.gov*

## Market and agency intel

#### Who an agency pays under your code

```text
How much did [AGENCY] obligate under NAICS [NAICS] in the most recently completed
fiscal year? Break it down by sub-agency and show the top 10 recipients. Some
agencies report as a single flat sub-agency here, VA included; a 1-row breakdown
means there is no further split, not that the query failed.
```

*MCPs used: USASpending*

#### Where the work is, by state

```text
Show me total federal spending under NAICS [NAICS] by state for the last fiscal
year. The geography tool returns states unsorted, so sort them by amount yourself
before showing me. I am deciding where the work actually is.
```

*MCPs used: USASpending*

#### An agency's set-aside share

```text
What percent of [AGENCY]'s dollars under NAICS [NAICS] in the last 2 years carried a
small business set-aside versus none? There is no direct breakdown call: run the
NAICS total twice, once with the full small-business set-aside code list applied and
once without, then divide. Break out [8(a) / SDVOSB / WOSB] specifically if I ask;
each set-aside type is its own query.
```

*MCPs used: USASpending*

#### The five-year trend

When I ran this one, the most recently completed year turned out to be the low point of the whole range; a single-year number would have hidden it.

```text
Show me [AGENCY]'s obligations under NAICS [NAICS] by fiscal year for the last 5
years. Growing, flat, or shrinking is the first bid decision, and a single-year
number hides it.
```

*MCPs used: USASpending*

#### The big vehicles

```text
List the largest IDVs under NAICS [NAICS]. For the one I pick, try the direct
children lookup first, then a keyword search on the IDV's contract number. Both can
come back empty on the same active vehicle; if they do, say so plainly instead of
concluding it has no orders, because the gap is usually in how USASpending links the
children, not in reality.
```

*MCPs used: USASpending*

## Speaking the government's codes

Nearly every prompt in this library wants a code. These find yours, and the lookups need no SAM.gov key; if a PSC search stalls on a rate limit, say "use USASpending to find the PSC code" and the same answer comes back key-free. The one exception is the chain at the end: its second half is a SAM.gov opportunity search, and that half does need the key.

#### Find your NAICS

```text
What NAICS code covers [PLAIN-ENGLISH BUSINESS ACTIVITY]? Give me the code and the
closest alternates so I do not file under the wrong one.
```

*MCPs used: USASpending*

#### The size standard

The one prompt in this library with no live source behind it: no tool in the suite returns the SBA size standard table, so the answer comes from your AI's training data. Confirm the current threshold at sba.gov before you rely on it.

```text
Look up NAICS [CODE] and tell me the SBA small business size standard for it, in
dollars or employees, and say plainly that the figure comes from training data, not
a live lookup, so I know to confirm it at sba.gov.
```

*MCPs used: none; the answer is training data, confirm at sba.gov*

#### Find your PSC

```text
What PSC codes cover [PLAIN-ENGLISH SERVICE]? Give me the codes and official names
so I can search with them.
```

*MCPs used: USASpending or SAM.gov*

#### Decode a PSC

```text
Look up PSC [CODE] and tell me exactly what it covers and whether it is current or
retired.
```

*MCPs used: USASpending or SAM.gov*

#### Codes to opportunities, one chain

```text
Find the PSC code for [PLAIN-ENGLISH SERVICE], then search SAM.gov opportunities
under that exact code with a response deadline still open. Codes first,
opportunities second, one chain.
```

*MCPs used: USASpending + SAM.gov*

## What should it cost

GSA CALC+, BLS OEWS, and GSA Per Diem answer one question from three directions: what should this cost? CALC+ is what awarded GSA Schedule (MAS) contractors carry as ceiling rates, and only them; the big direct-agency contracts are bought outside the Schedule, so read CALC+ as the rate sanity check, not a price match for any specific contract. OEWS is what the labor underneath costs on the open market. Per diem is what the travel line is allowed to be. The IGCE skills chain all three automatically, but standalone prompts are how you sanity-check a price fast, whether the price is going into an IGCE or a proposal.

### GSA CALC+

#### Find the right labor category title

```text
I do not know GSA's exact labor category title for [ROLE]. Show me the closest
matching titles with how many rate records each carries, so I search the right
string.
```

*MCPs used: GSA CALC+*

#### The rate distribution

```text
What do awarded GSA schedule rates look like for [LABOR CATEGORY]? Give me the
percentile distribution and the education breakdown, then run it again filtered to
junior and senior experience bands so I can compare. Treat exact percentile figures
as approximate past whole dollars, and know the distribution runs on every title
containing the phrase, not the bare title alone; check the title-count prompt above
against it before quoting.
```

*MCPs used: GSA CALC+*

#### A company's rate card

```text
Pull [COMPANY]'s GSA rate card and every row whose labor category contains
[KEYWORD]. Ask for the total category count and page through until you have every
row; the card reports which rows came back and whether more remain. There is no
server-side vendor-plus-keyword search, so the keyword screen happens on the rows
you fetched.
```

*MCPs used: GSA CALC+*

#### Is this rate defensible?

```text
Is $[RATE]/hr defensible for [LABOR CATEGORY]? Run a price reasonableness check
against awarded CALC+ rates and tell me what percentile band it lands in.
```

*MCPs used: GSA CALC+*

### BLS OEWS

The built-in shortcut lists lean toward IT and professional titles; if your occupation or metro is missing from them, ask for the SOC and metro codes by name first, and read a "not in the built-in lookup" warning as not-on-the-shortlist, not wrong-number.

#### What the labor earns

```text
What does [OCCUPATION] earn in [METRO AREA]? Median and 75th percentile annual wage,
current data year. Confirm the data year first; a wrong year fails silently as empty
data, which is exactly why the confirmation comes first.
```

*MCPs used: BLS OEWS*

#### Metro versus metro

```text
Compare wages for [OCCUPATION] across [METRO 1] and [METRO 2], then pull the
national median separately as the baseline. I am deciding where a position can
realistically be staffed.
```

*MCPs used: BLS OEWS*

#### Raw wage, your burden math

```text
Give me the raw BLS wage for [OCCUPATION] in [METRO], median and 10th and 90th
percentile, current data year, with no loaded-rate estimate attached. The burden
math is mine.
```

*MCPs used: BLS OEWS*

#### Market floor against awarded ceiling

```text
Cross-check [OCCUPATION] in [METRO]: what burdened rate does the BLS wage imply at
standard multipliers, and where does that land against awarded CALC+ rates for the
closest labor category?
```

*MCPs used: BLS OEWS + GSA CALC+*

#### The whole staffing picture

```text
Compare median wages for [OCCUPATION 1], [OCCUPATION 2], and [OCCUPATION 3] side by
side in [METRO]. I am pricing a mixed labor category task order and want the whole
staffing picture in one table, not separate lookups.
```

*MCPs used: BLS OEWS*

### GSA Per Diem

#### Lodging and M&IE

```text
What are the current lodging and M&IE rates for [CITY, STATE]? Note any seasonal
rate changes inside the fiscal year, and confirm which locality the rate table
actually matched.
```

*MCPs used: GSA Per Diem*

#### Price a trip

```text
Estimate per-traveler travel cost for [N] nights in [CITY, STATE] in [MONTH],
including first and last day M&IE at 75 percent. Name the month; without it the
estimate prices the locality's most expensive one. I will multiply by headcount
myself; the estimator prices one traveler.
```

*MCPs used: GSA Per Diem*

#### The ZIP fallback

```text
Look up the per diem rate for ZIP [ZIP] instead of city and state. Use this whenever
a city lookup answers with an unmatched-locality warning; the ZIP path resolves the
same rate table cleanly.
```

*MCPs used: GSA Per Diem*

## Watching the rules

eCFR, Federal Register, and Regulations.gov are the compliance and pipeline layer. eCFR settles what the rule says today. The Federal Register shows what is changing. Regulations.gov shows who is fighting about it and what they said.

### eCFR

#### The FAR as it reads today

```text
Quote FAR [CITATION] as it reads today. Then pull its version history and give me
the latest substantive amendment date from there; the citation note baked into the
clause text can run behind it.
```

*MCPs used: eCFR*

#### What changed in a FAR part

```text
List the sections in FAR Part [PART] that changed in the last year, then compare
before and after on whichever look substantive. Whole-part comparisons do not work;
it is section by section.
```

*MCPs used: eCFR*

#### Chase a FAR definition

```text
Find where the FAR defines [TERM], then pull the full text of that section so I get
the complete definition with its citation, unless the term lives in FAR 2.101: that
section runs past 100,000 characters and the pull can fail outright. For 2.101
terms, list the matched paragraphs in order instead and tell me if the last one
looks cut off mid-list; multi-part definitions continue in clauses that never repeat
the term.
```

*MCPs used: eCFR*

### Federal Register

#### What's moving on a topic

```text
Search Federal Register documents on [TOPIC] from the last 6 months across all
document types, ordered by relevance; the live items are often notices and RFIs, not
just proposed rules. For anything with an open comment period, give me the deadline.
```

*MCPs used: Federal Register*

#### Which agencies are moving

```text
Before reading individual documents, give me the count of Federal Register activity
on [TOPIC] by agency for the last 12 months. 1 call, and it shows which agencies are
actually moving before I drill into anything.
```

*MCPs used: Federal Register*

#### Track a FAR case

```text
Track FAR Case [NUMBER]: every Federal Register document in its history, in order,
with where it stands now, including whether it was withdrawn. The full history comes
back padded with semiannual Unified Agenda notices that merely list the case among
hundreds; separate the documents whose title names the case from that background
noise before summarizing.
```

*MCPs used: Federal Register*

### Regulations.gov

#### Open for comment right now

```text
What is open for comment right now on [TOPIC]? Use the Federal Register's open
comment periods with a term filter for this one; the Regulations.gov version filters
by agency only. Give me the docket ID, or the document number when a notice carries
no docket, and the closing date.
```

*MCPs used: Federal Register; the Regulations.gov variant filters by agency only*

#### The real FAR and DFARS pipeline

```text
Show me FAR and DFARS proposed rules with an open comment period right now,
filtering out the routine paperwork notices, and check both the FAR and DARS agency
codes; a case can sit under either. This is the clean pipeline view; the raw
open-comment feed buries the 2 or 3 real rulemakings under dozens of renewals.
```

*MCPs used: Regulations.gov*

#### Who's lobbying a docket

```text
On docket [DOCKET ID], search the comments for words like association, chamber,
coalition, or institute to surface the organizational submitters, then pull full
detail with attachments on the top hits. I want the industry positions with real
names, not a random page of individual filers.
```

*MCPs used: Regulations.gov*

## Agent and skill workflows: ten launch lines

Standalone [1102tools skills](https://github.com/1102tools-dev/federal-contracting-skills) and packaged [agents](https://github.com/1102tools-dev/federal-contracting-agents) are different from the MCP patterns above. A skill is launched, not prompted. Say the job and it takes over: it shows the applicable menu or asks the framing questions, walks the decision tree, pauses for approval, and produces the requested findings or artifact. An agent package brings the workflow and source connections together.

Contract types, if the shorthand is new: FFP is firm-fixed-price, T&M is time-and-materials, CPFF is cost-plus-fixed-fee, OT is an other transaction agreement. And the deliverables themselves: a PWS (performance work statement) and a SOO (statement of objectives) describe the work a contract will buy, and an IGCE (independent government cost estimate) is the government's own price estimate for it. If you are bidding rather than buying, these are still your tools; they build the scope and pricing backup behind a proposal.

#### Write me a PWS

```text
Write me a PWS for [REQUIREMENT].
```

*Runs: the sow-pws-builder skill*

#### SOO into PWS

```text
Convert this SOO into a PWS. [PASTE SOO]
```

*Runs: the sow-pws-builder skill*

#### The FFP estimate

```text
Build a firm-fixed-price IGCE for [REQUIREMENT].
```

*Runs: the igce-builder-ffp skill*

#### The T&M estimate

```text
Build a T&M IGCE for [REQUIREMENT], [N]-year period of performance.
```

*Runs: the igce-builder-lh-tm skill*

#### The CPFF estimate

```text
Build a CPFF IGCE for [N] researchers in [CITY], [N]-year period of performance.
```

*Runs: the igce-builder-cr skill*

#### The OT cost analysis

```text
Build an OT cost analysis for a [N]-milestone prototype effort.
```

*Runs: the ot-cost-analysis skill*

#### GovCon growth menu

```text
Help me find and evaluate federal growth opportunities.
```

*Runs: the GovCon Growth Agent and its govcon-growth-workflow skill. The first response is the complete nine-choice menu; no research starts until you select a mode and approve the plan.*

#### FAR Part 10 market research menu

```text
Help me conduct market research for [REQUIREMENT].
```

*Runs: the Market Research Agent and its market-research-workflow skill. The first response is the complete six-choice menu; the next stage asks separately for any existing acquisition documents.*

#### Acquisition policy menu

```text
Help me with federal acquisition policy.
```

*Stable behavior: the Acquisition Policy Agent `1.0.0` returns its complete ten-choice menu without retrieving a source. Explicitly select or invoke the installed agent first; ambient routing remains host-controlled and best effort.*

#### Agency RFO status, direct route

```text
Determine the documented RFO policy status for [AGENCY] and FAR Part [NUMBER] as of
[DATE]. The relevant procurement date is [SOLICITATION, AWARD, MODIFICATION, OR OPTION
DATE]. Use a [GOVERNMENT / INDUSTRY / NEUTRAL] lens and keep codified text, model text,
and the agency deviation separately classified.
```

*Stable behavior: the Acquisition Policy Agent routes directly to agency-status mode and must not call model text operative without a documented agency deviation.*

The pricing skills will check that the three pricing MCPs are connected before they start, and the scope skills end by handing their staffing table to the IGCE builders, so the chain from "write me a PWS" to a priced estimate is those prompts in sequence and nothing more.

## More info

- Beginner path: [choose a packaged agent](https://1102tools.com/tools) and follow the [agent setup guide](https://1102tools.com/downloads/1102tools-agent-setup-guide.pdf)
- Agent walkthroughs: [How It Works](https://1102tools.com/examples)
- The servers these prompts run on: [federal-contracting-mcps](https://github.com/1102tools-dev/federal-contracting-mcps)
- The standalone workflow packages: [federal-contracting-skills](https://github.com/1102tools-dev/federal-contracting-skills)
- Five stable packaged agents: [federal-contracting-agents](https://github.com/1102tools-dev/federal-contracting-agents)

---

Written August 2026 by James Jenrette / [1102tools](https://1102tools.com). The 60 original MCP prompt patterns were executed against the live servers before publishing (suite release 1.0.x, August 2026), and the wording reflects what that testing found, including the limits. The five packaged agents are now the stable beginner path; this repository remains the canonical advanced MCP-oriented request library. MIT licensed. Independently developed and not endorsed by any federal agency.
