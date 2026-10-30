# HARBOUR: 5-Month Plan for 8 Members

**Length:** 5 months, 21 active weeks, 62 meeting days, with a two-week festive break after Week 10.
**Team:** 8 members (Member 1 to Member 8). Replace the labels with names when the roster is confirmed.
**Sessions:** Monday (4 presenters), Wednesday (4 presenters), Friday (10:00–13:00 mini-project, 13:00–17:00 Harbour, all 8). Study happens over the weekend before each week.
**Tools:** Google Meet for sessions, Jupyter Notebooks for Python lessons, one Twitter Space each week for reflection.
**Harbour:** the capstone, in its own repository. Every Friday afternoon it applies that week's mini-project topic.

---

## 1. The five mini-projects

Each mini-project is a standalone project with its own name and its own domain. None of them is a piece of Harbour. Each one teaches a set of ideas, and the team applies those ideas to Harbour at the end of that month.

| # | Mini-project | Weeks | What the team builds | What it proves |
|---|---|---|---|---|
| 1 | **Library Loans API** | 1–4 | A small web API to borrow, return and list books, with fines for late returns | Python, SQL, FastAPI, tests, Docker, CI |
| 2 | **Inbox Triage Assistant** | 5–7 | Classifies incoming emails and drafts a reply for a human to review | LLM APIs, prompts, structured outputs, evaluation |
| 3 | **Campus Handbook Q&A** | 8–14 | Answers questions from a fictional university handbook, with citations and "not in the handbook" answers | Data preparation, chunking, embeddings, pgvector, hybrid search, reranking, RAG evaluation |
| 4 | **Conference Planner Agent** | 15–18 | An agent that checks venue availability and speaker lists, then drafts invitations that wait for approval | Tools, LangGraph, multi-agent patterns, approvals, budgets, tracing |
| 5 | **Ship It Lab** | 19–21 | Takes the Campus Handbook Q&A and makes it shippable: evaluation gate, red-teaming, observability, containers, a React interface | Evaluation gates, guardrails, logs and traces, Docker and Kubernetes basics, React UI, delivery |

**Repositories:** every project has its own repository, README and decision records. No project imports code from another. Each mini-project's task brief is its README, at `/home/user/mini-projects/<repository>/README.md`.

| Project | Repository | Weeks |
|---|---|---|
| Library Loans API | `library-loans-api` | 1–4 |
| Inbox Triage Assistant | `inbox-triage-assistant` | 5–7 |
| Campus Handbook Q&A | `campus-handbook-qa` | 8–14 |
| Conference Planner Agent | `conference-planner-agent` | 15–18 |
| Ship It Lab | `ship-it-lab` | 19–21 |
| Harbour | `harbour` | 1–21 |

**How the ideas reach Harbour:** every Friday, 13:00–17:00, the team applies that week's topic to Harbour. Because the two projects share most of their work, Harbour gets a weekly step, listed in Section 6. The idea is rewritten in Harbour's own code, and the Harbour README names the mini-project that taught it.

---

## 2. How each week runs

- **Every session:** opens with a short explanation of the day's task, then goes straight into teaching.
- **Weekend (study):** everyone studies the whole subtopic. Each presenter writes 20 questions for the class on their own chunk.
- **Monday (question round):** four members each ask the class their 20 questions on Google Meet. Laptops stay open and muted.
- **Wednesday (question round):** the other four members run their 20 questions.
- **Friday (build):** 10:00–13:00 all eight members build the mini-project piece that matches their chunk, then explain it to a reviewer before merge.
- **Friday (Harbour):** 13:00–17:00 the team applies the week's topic to Harbour, with the same explain-before-merge rule.
- **Twitter Space (weekly):** lessons, mistakes and open questions.

**Question round rule:** every member runs their 20 questions exactly once a week. Chunks 1 to 4 run on Monday and chunks 5 to 8 run on Wednesday. Rounds rotate every week, so nobody always goes on the same day.

**Chunk rule:** in week *w*, member *m* takes chunk *k* = ((m − 1) + (w − 1)) mod 8 + 1. Each member takes a different position every week.

**The "after the talk" column is the test.** Each of the 20 questions checks a point from that note. When the round ends, the class should be able to do what the note says.

**Week 1 exception:** the course starts midweek, so there is no Monday session. Members 1 to 4 run their question rounds on Wednesday, and Members 5 to 8 run theirs on Friday before the set-up.

**Language tracks (outside Python):**
- SQL: pgexercises.com, from Week 3
- TypeScript: TypeScript Handbook and Exercism's TypeScript track, from Week 16
- React: react.dev Learn section, from Week 19

---

## 3. Daily timetable

Sessions run on Google Meet with the whole team in one class. Everyone keeps their laptop open in front of them, muted. Nothing is recorded. The sessions are for explaining what we have learnt, not for long lectures.

**Monday and Wednesday (meeting window 09:00–18:00):**
- Each day opens with a short explanation of the task, then goes straight into the question rounds.
- Four presenters each run their question round: 20 questions for the class, drawn from the chunk's "after the talk" note. Four presenters at 20 questions each means 80 questions a day.
- The class answers by unmuting or in the chat. The presenter confirms or corrects each answer, and notes any question nobody could answer.
- **The rest of the window:** the class works through the notebook exercises together.

**Friday (10:00–17:00, about 7 hours):**
- **10:00–13:00 Mini-project:** a short explanation of the task, then each member builds their piece in the mini-project repository and explains it live before it merges.
- **13:00–17:00 Harbour:** a short explanation of the Harbour step, then the team applies the week's topic to the Harbour repository, with the same explain-before-merge rule.
- **Twitter Space (weekly):** Friday or Saturday, 20:00–22:00, outside the day.

**Week 1 is shorter:** Wednesday runs the question rounds for Members 1 to 4 and set-up. On Friday, Members 5 to 8 run their question rounds first, then the repositories are set up and the Harbour step begins.

**Weekly time in class:** Monday and Wednesday are both in the 09:00–18:00 window, and Friday runs 10:00–17:00, plus the weekend study.

---

## 4. Tools and libraries

Each library is introduced in a specific chunk, so it is taught, not just used. The table shows where.

| Tool or library | What it is for | Where it is taught |
|---|---|---|
| uv | Python environments, dependencies, lockfiles | Week 1 set-up |
| Jupyter Notebook | Lesson notebooks and experiments | Week 1 set-up, every question round |
| Git and GitHub | Branches, pull requests, review | Week 1 chunk 8 |
| PostgreSQL and psql | Relational database | Week 3 chunks 1 to 7 |
| Alembic | Versioned database migrations | Week 3 chunk 8 |
| psycopg 3 | Postgres driver used by SQLAlchemy | Week 4 chunk 3 |
| SQLAlchemy 2.0 | ORM and sessions | Week 4 chunk 3 |
| FastAPI and uvicorn | Web API and server | Week 4 chunk 1 |
| Pydantic and pydantic-settings | Validation and configuration | Week 4 chunks 2 and 7 |
| pytest and httpx | Tests and the FastAPI test client | Week 4 chunk 5 |
| Docker and Docker Compose | Containers for the API and Postgres | Week 4 chunk 6 |
| ruff, mypy | Linting and type checking | Week 4 chunk 8 |
| GitHub Actions | Continuous integration | Week 4 chunk 8 |
| tiktoken | Counting tokens | Week 5 chunk 1 |
| Provider SDK (one hosted LLM provider) | Model calls | Week 5 chunk 4 |
| Ollama | Local open-model runs | Week 5 chunk 5 |
| Presidio | PII detection and redaction | Week 8 chunk 6 |
| DVC | Versioning the corpus | Week 8 chunk 7 |
| sentence-transformers | Embedding models and cross-encoders | Week 9 chunk 6, Week 11 chunk 6 |
| pgvector | Vector search in Postgres | Week 10 chunk 5 |
| Postgres full-text search | Keyword search in Postgres | Week 11 chunk 3 |
| scikit-learn | Cross-checking ranking metrics | Week 13 chunk 3 |
| networkx | Entity graphs for GraphRAG | Week 14 chunk 1 |
| CLIP-style models | Image and text embeddings | Week 14 chunk 3 |
| k6 | Load testing the retrieval endpoint | Week 14 chunk 8 |
| LangGraph (with Postgres checkpointer) | Agent state machines | Weeks 16 and 17 |
| CrewAI | Role-based agent crews, compared with LangGraph | Week 17 chunk 7 |
| OpenTelemetry and Arize Phoenix | Traces and evaluation views | Week 20 chunks 2 and 3 |
| kind and kubectl | Local Kubernetes | Week 20 chunk 6 |
| React and Vite, TypeScript | Frontend | Week 21 chunks 1 and 2 |
| Postgres SKIP LOCKED | Safe job claiming | Week 21 chunk 6 |

**Concept-only references:** LangChain, LlamaIndex and RAGAS are discussed as concepts in the relevant weeks, so the team understands what they do. The code is written without them, so each step stays visible.

---

---

## 5. Team rules

1. **Explain before merge.** No pull request merges until its author can walk a reviewer through it live, without the screen.
2. **AI disclosure.** Each pull request states what AI helped with and how the author checked it.
3. **Hand-write the core first.** Each owner writes the core logic of their chunk (chunking, BM25, the classifier, the agent loop, the approval gate). AI can then review, suggest tests or explain errors.
4. **Break it on purpose.** Each chunk includes one failure experiment that the owner can explain.
5. **Fictional data only.** Every mini-project and Harbour use invented names, catalogues and customers. Real customer data stays out of the learning environment unless it is separately authorised and protected.
6. **Trade-offs in answers.** Every answer in a question round must include a trade-off where one applies.
7. **Honest limits.** Every release lists what it does not do, how it was tested, and what remains unknown.
8. **One repository per project.** The five mini-projects and Harbour each have their own repository. No project imports code from another. Ship It Lab starts from a tagged copy of Campus Handbook Q&A, and its README records the tag and the copy point.
9. **Project documentation.** Each README states the purpose, scope, what the project does not do, how to run it from a clean clone, how it was tested, measured results, known limits, the threat model for anything that takes text from users or calls tools, and an AI-use log.

---

## 6. Calendar overview

| Week | Month | Subtopic | Friday milestone (10:00–13:00) | Harbour step (13:00–17:00) |
|---|---|---|---|---|
| 1 | 1 | Python fundamentals and the problem-solving process | Repository created and first pull request merged | Harbour repository created with README, scope and known limits; first pull request merged. |
| 2 | 1 | HTTP, REST and core problem-solving patterns | API contract agreed by the team | Harbour API contract agreed and written as an OpenAPI file. |
| 3 | 1 | SQL and PostgreSQL basics | Schema v1 with migration script | Harbour schema v1 with an Alembic migration. |
| 4 | 1 | FastAPI, validation, tests, Docker and CI (Mini-project 1) | Mini-project 1 demo and Month 1 check. | Harbour core API skeleton: FastAPI, SQL, tests and Docker. |
| 5 | 2 | LLM APIs and prompt design | Service layer with two providers and call logging | Harbour service layer with two providers and call logging. |
| 6 | 2 | Structured outputs, validation and reliability | Validated ticket classification with safe retries | Harbour model outputs validated, with safe retries. |
| 7 | 2 | Evaluation and the Mini-project 2 report | Mini-project 2 delivered: Inbox Triage Assistant. | Harbour structured triage prototype with a small evaluation set. |
| 8 | 3 | Data preparation for retrieval | Versioned sample corpus v1 | Harbour sample corpus v1 (fictional content, versioned). |
| 9 | 3 | Chunking and embeddings | Chunking choice recorded with measurements | Harbour chunking choice recorded with measurements. |
| 10 | 3 | Vector indexes and pgvector | Index decision recorded in an ADR | Harbour vector index decision recorded in an ADR. |
| 11 | 3 | Hybrid search and reranking | Hybrid search with reranker beats vector-only on the test set | Harbour hybrid search with a reranker, compared against vector-only search. |
| 12 | 3 | Grounded answers, citations and access control | Document Q&A with citations and abstention | Harbour answers with citations and abstention. |
| 13 | 3 | Retrieval evaluation, query transformation and Mini-project 3 | Mini-project 3 delivered: Campus Handbook Q&A, with a retrieval evaluation report. | Harbour retrieval evaluation report. |
| 14 | 3 | Advanced retrieval and the production RAG service | Advanced retrieval demo with p95 measured. | Harbour versioned, cited knowledge service with a measured p95. |
| 15 | 4 | Agent fundamentals | Single agent with three tools and a step log | Harbour single agent with three tools and a step log. |
| 16 | 4 | LangGraph state machines | LangGraph workflow with approval and resume | Harbour workflow with approval and resume. |
| 17 | 4 | Multi-agent patterns and frameworks | Multi-agent crew (supervisor plus critic) running end to end | Harbour supervisor and critic added only where measurement shows they help. |
| 18 | 4 | Safe tools, budgets and agent tracing (Mini-project 4) | Mini-project 4 delivered: Conference Planner Agent. | Harbour approval gates and budgets on the agent. |
| 19 | 5 | Evaluation gate, red-teaming and guardrails | Eval gate blocks a deliberate regression | Harbour eval gate blocks a deliberate regression; red-team run recorded. |
| 20 | 5 | Observability and containers | Stack runs on kind with traces visible | Harbour stack runs on kind with traces visible. |
| 21 | 5 | Frontend, reliability and launch (Ship It Lab showcase) | Mini-project 5 showcase: Ship It Lab. | Harbour release candidate with eval gate, traces and known limitations. |

---

## 7. Week-by-week plan

Each week shows who runs a question round on Monday and Wednesday, what the class should understand after each round, and each member's Friday build task.

---

# Month 1: Library Loans API (Mini-project 1)


## Week 1: Python fundamentals and the problem-solving process

**Weekend before:** set up Git, uv, Jupyter and Python, then study the subtopic.  
**Wednesday question rounds:** Member 1, Member 2, Member 3, Member 4  
**Friday question rounds (Week 1):** Member 5, Member 6, Member 7, Member 8, then repository set-up and the Harbour step.  
**Harbour (Friday 13:00–17:00):** Harbour repository created with README, scope and known limits; first pull request merged.  
**Friday milestone:** Repository created and first pull request merged

| Member | Question round | Chunk | After the talk, the class should understand | Friday: build the mini-project |
|---|---|---|---|---|
| Member 1 | Wednesday | Variables, types and the Python data model | Understands that variables are names bound to objects, and can choose the right type for a fine amount, a book ID and a copy count. | Write a typed function that calculates loan due dates, with a docstring and three checks in a notebook |
| Member 2 | Wednesday | Functions, arguments and scope | Can write a function with clear inputs and outputs and no hidden state, and explains the default-argument trap. | Refactor a long fine-calculation function into small pure functions and explain each step |
| Member 3 | Wednesday | Lists and tuples: indexing, slicing and cost | Knows the cost of indexing, slicing, insert and remove, and when a tuple is the right choice. | Benchmark list vs set membership for checking book IDs across 100,000 items |
| Member 4 | Wednesday | Dicts and sets: lookups and hashing | Can explain why dictionary and set lookups are fast, and when to use each. | Count title words across a catalogue of 500 books and explain the data structure |
| Member 5 | Friday | Loops, comprehensions and readability | Knows when a comprehension helps and when a plain loop is clearer. | Rewrite one loop as a comprehension that lists overdue loans; argue which is clearer |
| Member 6 | Friday | Exceptions and reading tracebacks | Can read a traceback from the bottom up, and raise and handle a domain error. | Raise a custom error for an unknown book ID and handle it |
| Member 7 | Friday | Problem-solving: restate, examples, plan, test, reflect | Can turn a vague problem into examples, a plan, tests and a short reflection. | Write a problem-solving log for one exercise, step by step |
| Member 8 | Friday | Git basics: commits, branches and pull requests | Can explain commit, branch, merge and pull request, and why small pull requests are easier to review. | Create the mini-project repository and open the first pull request |


## Week 2: HTTP, REST and core problem-solving patterns

**Weekend before:** everyone studies the whole subtopic. Presenters write their 20 questions for the class.  
**Monday question rounds:** Member 1, Member 2, Member 3, Member 8  
**Wednesday question rounds:** Member 4, Member 5, Member 6, Member 7  
**Friday:** mini-project build for all eight members.  
**Harbour (Friday 13:00–17:00):** Harbour API contract agreed and written as an OpenAPI file.  
**Friday milestone:** API contract agreed by the team

| Member | Question round | Chunk | After the talk, the class should understand | Friday: build the mini-project |
|---|---|---|---|---|
| Member 1 | Monday | REST resources, methods and naming | Can design resource-based URLs and choose the right HTTP method for each action. | Write the status-code table for every endpoint, with reasons |
| Member 2 | Monday | Status codes and error response design | Knows when to return 400, 404, 409, 422 and 500, and why error bodies matter. | Analyse the Big-O of the book search function and name the bottleneck |
| Member 3 | Monday | Safe and idempotent methods | Can explain why repeating a PUT is safe and why repeating a POST may not be. | Solve a sliding-window problem on daily loan counts |
| Member 4 | Wednesday | Big-O notation with worked examples | Can estimate how a function's running time grows from its loops and data structures. | Detect duplicate loan IDs in one pass with a dictionary |
| Member 5 | Wednesday | Two pointers and sliding window | Can recognise when a sorted or contiguous problem can be solved in one pass. | Check that a shelf-layout configuration has balanced brackets |
| Member 6 | Wednesday | Hashing patterns: frequency counts and two-sum | Can explain the time-memory trade-off of hashing in a frequency problem. | Simulate a returns desk with a queue and measure wait times |
| Member 7 | Wednesday | Stacks and queues: bracket checks and level-order processing | Can explain LIFO versus FIFO, and solve bracket matching and level-by-level processing. | Write the API contract document and get it reviewed |
| Member 8 | Monday | Anatomy of an HTTP request and response | Can trace a request from client to server and back, naming each part. | Draft the endpoints for books, members and loans, with methods |


## Week 3: SQL and PostgreSQL basics

**Weekend before:** everyone studies the whole subtopic. Presenters write their 20 questions for the class.  
**Monday question rounds:** Member 1, Member 2, Member 7, Member 8  
**Wednesday question rounds:** Member 3, Member 4, Member 5, Member 6  
**Friday:** mini-project build for all eight members.  
**Harbour (Friday 13:00–17:00):** Harbour schema v1 with an Alembic migration.  
**Language track:** SQL practice on pgexercises.com, about one hour a week  
**Friday milestone:** Schema v1 with migration script

| Member | Question round | Chunk | After the talk, the class should understand | Friday: build the mini-project |
|---|---|---|---|---|
| Member 1 | Monday | SELECT, WHERE and NULL behaviour | Knows that NULL is not equal to anything, and writes correct filters with IS NULL. | Query books with no copies on the shelf |
| Member 2 | Monday | Joins: inner, left and anti-join | Can predict the rows produced by inner, left and anti-joins. | Write an anti-join: books never borrowed |
| Member 3 | Wednesday | Aggregates, GROUP BY and HAVING | Can write GROUP BY and HAVING, and explain why WHERE cannot filter aggregates. | Calculate fines per member; store money as integer cents and explain why |
| Member 4 | Wednesday | Indexes and reading EXPLAIN output | Can read an EXPLAIN plan and say why an index helps or hurts. | Add an index, run EXPLAIN before and after, and explain the change |
| Member 5 | Wednesday | Transactions and isolation basics | Can explain atomicity and isolation using a failed loan update. | Show a rollback when a loan update fails mid-transaction |
| Member 6 | Wednesday | Designing the library schema: books, copies, members, loans, fines, versioned with Alembic | Can justify each table and key in the library schema. | Write the first Alembic migration and apply it to Postgres |
| Member 7 | Monday | Tables, data types and primary keys | Can design a table with the right types and a primary key, and justify both. | Create books and members tables with constraints; explain each |
| Member 8 | Monday | Constraints and normalisation with a library example | Can explain first to third normal form with a library example, and why duplicated data causes bugs. | Add a foreign key and show a rejected bad insert |


## Week 4: FastAPI, validation, tests, Docker and CI (Mini-project 1)

**Weekend before:** everyone studies the whole subtopic. Presenters write their 20 questions for the class.  
**Monday question rounds:** Member 1, Member 6, Member 7, Member 8  
**Wednesday question rounds:** Member 2, Member 3, Member 4, Member 5  
**Friday:** mini-project build for all eight members.  
**Harbour (Friday 13:00–17:00):** Harbour core API skeleton: FastAPI, SQL, tests and Docker.  
**Friday milestone:** Mini-project 1 demo and Month 1 check.

| Member | Question round | Chunk | After the talk, the class should understand | Friday: build the mini-project |
|---|---|---|---|---|
| Member 1 | Monday | Layering: routers, services and repositories | Can say which code belongs in routers, services and repositories, and why. | Move borrowing rules into the service layer |
| Member 2 | Wednesday | pytest fixtures, the FastAPI test client (httpx) and a test database | Can write fixtures and tests that run against a real database. | Write tests for the loan endpoints, including invalid input |
| Member 3 | Wednesday | Dockerfile and Docker Compose for API and Postgres | Can explain the difference between an image and a container, and run the API and Postgres together. | Write the Compose file with a health check and verify it runs |
| Member 4 | Wednesday | Configuration with pydantic-settings and environment variables | Can load settings from environment variables and never commit secrets. | Load settings from environment variables and document them without secrets |
| Member 5 | Wednesday | GitHub Actions: ruff lint, mypy type-check and pytest on every pull request | Can read a CI workflow and explain why a failing test blocks a merge. | Set up the CI workflow with ruff, mypy and pytest, and get a green build on a pull request |
| Member 6 | Monday | FastAPI routing, path and query parameters, served with uvicorn | Can define routes with path and query parameters and explain the difference. | Implement book and loan CRUD endpoints |
| Member 7 | Monday | Pydantic models and validation errors | Can define a request model that rejects bad input with a useful error message. | Add Pydantic validation, including ISBN format and due-date rules |
| Member 8 | Monday | Database access: psycopg 3 driver and SQLAlchemy 2.0 sessions | Can explain what a database session is and when it is committed or closed. | Implement the loan repository with SQLAlchemy |


---

# Month 2: Inbox Triage Assistant (Mini-project 2)


## Week 5: LLM APIs and prompt design

**Weekend before:** everyone studies the whole subtopic. Presenters write their 20 questions for the class.  
**Monday question rounds:** Member 5, Member 6, Member 7, Member 8  
**Wednesday question rounds:** Member 1, Member 2, Member 3, Member 4  
**Friday:** mini-project build for all eight members.  
**Harbour (Friday 13:00–17:00):** Harbour service layer with two providers and call logging.  
**Friday milestone:** Service layer with two providers and call logging

| Member | Question round | Chunk | After the talk, the class should understand | Friday: build the mini-project |
|---|---|---|---|---|
| Member 1 | Wednesday | Provider abstraction: one interface, a hosted SDK and Ollama over HTTP (httpx) | Can explain why an interface between the app and the model protects against vendor lock-in. | Build one interface with a hosted adapter and an Ollama adapter |
| Member 2 | Wednesday | System instructions and roles | Can explain system versus user messages, and write scope rules for an assistant. | Write the triage assistant's system prompt with scope rules |
| Member 3 | Wednesday | Few-shot examples and example selection | Can explain when examples help, and how the choice of examples changes results. | Compare three-shot and zero-shot ticket classification |
| Member 4 | Wednesday | Uncertainty and refusal wording for triage | Can write behaviour for 'I don't know' and escalation, and test it. | Write the uncertainty rule and test it on five ambiguous emails |
| Member 5 | Monday | What LLMs do; counting tokens with tiktoken and context windows | Can count tokens and explain how context limits affect answers and cost. | Count tokens for 20 sample emails and estimate the context budget |
| Member 6 | Monday | Choosing a model and API: cost, latency and limits | Can compare models on cost, latency and limits for one specific task. | Compare two models on cost and latency using the same 10 emails |
| Member 7 | Monday | API keys and secrets management | Knows how to store API keys safely and rotate them. | Move keys to environment variables and add a secret-scanning check |
| Member 8 | Monday | A first model call with a provider SDK: record input, output and latency | Can make a model call and log its input, output, latency and token use. | Wrap the model call with timing and a JSON log record |


## Week 6: Structured outputs, validation and reliability

**Weekend before:** everyone studies the whole subtopic. Presenters write their 20 questions for the class.  
**Monday question rounds:** Member 4, Member 5, Member 6, Member 7  
**Wednesday question rounds:** Member 1, Member 2, Member 3, Member 8  
**Friday:** mini-project build for all eight members.  
**Harbour (Friday 13:00–17:00):** Harbour model outputs validated, with safe retries.  
**Friday milestone:** Validated ticket classification with safe retries

| Member | Question round | Chunk | After the talk, the class should understand | Friday: build the mini-project |
|---|---|---|---|---|
| Member 1 | Wednesday | Tool calling: schema, arguments and execution | Can describe the loop where the model proposes a tool call and the code executes it, and validate the arguments. | Expose a mocked lookup_calendar tool and log each call |
| Member 2 | Wednesday | Parsing streamed output safely | Can explain why partial JSON cannot be trusted until the stream is complete. | Parse a streamed reply only after it completes |
| Member 3 | Wednesday | Logging calls and cost per day | Can compute cost per request and per day from logged token counts. | Add daily cost totals to the log summary |
| Member 4 | Monday | Why free text breaks systems: the case for JSON output | Can explain why downstream code needs a predictable output shape. | Define a Pydantic model for a classified email |
| Member 5 | Monday | Pydantic schemas for category, urgency and sender type | Can model a classification result with typed fields. | Add enums for meeting request, invoice, complaint, newsletter, support request and spam |
| Member 6 | Monday | Enums and constrained values | Can restrict values with enums, and explain why free-text categories cause errors. | Reject an invalid urgency value and retry once with the error message |
| Member 7 | Monday | Validation failures and retry-with-feedback | Can explain when retrying with feedback helps, and how to bound the retries. | Implement backoff with a maximum number of attempts |
| Member 8 | Wednesday | Timeouts, retries and backoff: which errors to retry | Can name retryable and non-retryable errors, and justify a backoff schedule. | Add a timeout and a fallback to 'needs human review' |


## Week 7: Evaluation and the Mini-project 2 report

**Weekend before:** everyone studies the whole subtopic. Presenters write their 20 questions for the class.  
**Monday question rounds:** Member 3, Member 4, Member 5, Member 6  
**Wednesday question rounds:** Member 1, Member 2, Member 7, Member 8  
**Friday:** mini-project build for all eight members.  
**Harbour (Friday 13:00–17:00):** Harbour structured triage prototype with a small evaluation set.  
**Friday milestone:** Mini-project 2 delivered: Inbox Triage Assistant.

| Member | Question round | Chunk | After the talk, the class should understand | Friday: build the mini-project |
|---|---|---|---|---|
| Member 1 | Wednesday | Repeatable comparisons and regression runs | Can run the same evaluation before and after a change and compare the results. | Write a script that compares prompt v1 and v2 on the same cases |
| Member 2 | Wednesday | Failure analysis: grouping errors into a taxonomy | Can group errors into categories and prioritise fixes. | Group 10 failures into a taxonomy and write the Mini-project 2 report |
| Member 3 | Monday | Why fluent answers are not necessarily correct | Can give examples of fluent answers that are wrong, and how to catch them. | Label 50 emails: category, urgency and expected reply facts |
| Member 4 | Monday | Golden dataset design: 50 labelled emails | Can design a labelled dataset with coverage across categories and difficulty. | Write a reply rubric covering accuracy, tone and next step |
| Member 5 | Monday | Rubrics and scoring criteria | Can write a rubric with clear anchors for each score. | Implement an exact-match scorer for categories |
| Member 6 | Monday | Exact match vs rubric vs human review | Can choose the right scoring method for a given check. | Implement a rubric scorer for replies and check a human sample |
| Member 7 | Wednesday | LLM-as-judge: bias and calibration checks | Can explain judge bias, and check judge agreement against human labels. | Measure LLM-judge agreement with human labels on 20 items |
| Member 8 | Wednesday | Bootstrap confidence intervals on pass rates | Can compute and explain a bootstrap confidence interval for a pass rate. | Compute bootstrap intervals for each pass rate |


---

# Month 3: Campus Handbook Q&A (Mini-project 3)


## Week 8: Data preparation for retrieval

**Weekend before:** everyone studies the whole subtopic. Presenters write their 20 questions for the class.  
**Monday question rounds:** Member 2, Member 3, Member 4, Member 5  
**Wednesday question rounds:** Member 1, Member 6, Member 7, Member 8  
**Friday:** mini-project build for all eight members.  
**Harbour (Friday 13:00–17:00):** Harbour sample corpus v1 (fictional content, versioned).  
**Friday milestone:** Versioned sample corpus v1

| Member | Question round | Chunk | After the talk, the class should understand | Friday: build the mini-project |
|---|---|---|---|---|
| Member 1 | Wednesday | Idempotent ingestion and malformed-record handling | Can explain why re-running ingestion must not duplicate data. | Run ingestion twice and prove the second run changes nothing |
| Member 2 | Monday | Document formats: PDF, DOCX, Markdown and CSV | Can choose an extraction approach for PDF, DOCX, Markdown and CSV files. | Parse six sample handbook sections into clean text |
| Member 3 | Monday | Text cleaning and normalisation, including mixed-language text | Can explain why normalisation changes matching, and where it can change meaning. | Normalise text and show before-and-after examples |
| Member 4 | Monday | Exact deduplication with content hashes | Can explain content hashing and what counts as a duplicate. | Remove exact duplicates and report the counts |
| Member 5 | Monday | Near-duplicates: MinHash and LSH intuition | Can explain Jaccard similarity and why MinHash with LSH scales. | Find near-duplicate handbook versions and decide which to keep |
| Member 6 | Wednesday | Metadata design: document ID, faculty, version, access group, updated date | Can justify each metadata field and its use in filtering and access control. | Attach metadata to every document and validate required fields |
| Member 7 | Wednesday | PII detection and scrubbing in documents with Microsoft Presidio | Can detect and redact personal data, and explain false positives and false negatives. | Scrub phone numbers and student ID numbers from sample documents with Presidio |
| Member 8 | Wednesday | Versioned corpus with DVC and manifests | Can explain how versions and manifests make answers traceable. | Create corpus v1 with DVC tracking, content hashes and a manifest |


## Week 9: Chunking and embeddings

**Weekend before:** everyone studies the whole subtopic. Presenters write their 20 questions for the class.  
**Monday question rounds:** Member 1, Member 2, Member 3, Member 4  
**Wednesday question rounds:** Member 5, Member 6, Member 7, Member 8  
**Friday:** mini-project build for all eight members.  
**Harbour (Friday 13:00–17:00):** Harbour chunking choice recorded with measurements.  
**Friday milestone:** Chunking choice recorded with measurements

| Member | Question round | Chunk | After the talk, the class should understand | Friday: build the mini-project |
|---|---|---|---|---|
| Member 1 | Monday | Fixed-size chunking with overlap | Can explain how chunk size and overlap trade off context against recall. | Chunk handbook sections with fixed size and overlap; inspect five boundaries |
| Member 2 | Monday | Recursive and Markdown-aware splitting | Can explain why splitting on document structure keeps meaning intact. | Implement a recursive splitter that respects headings |
| Member 3 | Monday | Semantic chunking with similarity breakpoints | Can explain breakpoints, and when semantic chunking costs more than it gains. | Compare semantic and fixed chunking on one long handbook section |
| Member 4 | Monday | Parent-child (small-to-big) retrieval | Can explain retrieving small chunks but answering with their parent section. | Build a parent-child store and show a child returning its parent |
| Member 5 | Wednesday | Tables and fee schedules: row-to-text chunks | Can turn table rows into self-contained text that carries its headers. | Turn fee-schedule rows into text chunks with headers |
| Member 6 | Wednesday | Embedding models with sentence-transformers: how they are trained and how to choose | Can explain what an embedding captures, and how to choose an embedding model. | Compare two embedding models on 20 questions for quality, dimensions and cost |
| Member 7 | Wednesday | Similarity metrics: cosine, dot product and normalisation | Can explain cosine similarity versus dot product, and when they give the same ranking. | Show cosine vs dot product on normalised and unnormalised vectors |
| Member 8 | Wednesday | Chunk-size sweeps and boundary-loss measurement | Can measure boundary loss and choose a chunk size using evidence. | Sweep three chunk sizes and record boundary loss and hit rate |


## Week 10: Vector indexes and pgvector

**Weekend before:** everyone studies the whole subtopic. Presenters write their 20 questions for the class.  
**Monday question rounds:** Member 1, Member 2, Member 3, Member 8  
**Wednesday question rounds:** Member 4, Member 5, Member 6, Member 7  
**Friday:** mini-project build for all eight members.  
**Harbour (Friday 13:00–17:00):** Harbour vector index decision recorded in an ADR.  
**Friday milestone:** Index decision recorded in an ADR

| Member | Question round | Chunk | After the talk, the class should understand | Friday: build the mini-project |
|---|---|---|---|---|
| Member 1 | Monday | HNSW: layers, M, efConstruction and efSearch | Can explain how HNSW navigates a graph, and what M, efConstruction and efSearch control. | Build an HNSW index; compare latency and results with brute force |
| Member 2 | Monday | IVF clustering and nprobe | Can explain clustering-based search and what nprobe trades off. | Build an IVF index; tune nprobe and record recall |
| Member 3 | Monday | Product quantisation: memory vs accuracy | Can explain compressing vectors and the accuracy it costs. | Measure memory for float32 vectors and explain quantisation savings |
| Member 4 | Wednesday | pgvector and the psycopg adapter: storing vectors and running similarity queries | Can store vectors and run nearest-neighbour queries in Postgres. | Write the pgvector schema with faculty and access-group columns |
| Member 5 | Wednesday | HNSW vs IVFFlat indexes in pgvector | Can choose an index type using latency and recall evidence. | Compare HNSW and IVFFlat on latency and recall; write the decision |
| Member 6 | Wednesday | Metadata filters with vector search: pre- vs post-filtering | Can explain why pre-filtering and post-filtering can return different results. | Test faculty-filtered search before and after ranking; show the difference |
| Member 7 | Wednesday | When you do not need a vector database; Qdrant, Weaviate and Pinecone | Can justify when a dedicated vector database is needed and when it is not. | Write a one-page comparison of pgvector, Qdrant, Weaviate and Pinecone for the Campus Q&A service |
| Member 8 | Monday | Exact (brute-force) search and when it is enough | Can explain why exact search becomes expensive and when approximate search is needed. | Store chunks and embeddings in pgvector and run brute-force search |


## Week 11: Hybrid search and reranking

**Weekend before:** everyone studies the whole subtopic. Presenters write their 20 questions for the class.  
**Monday question rounds:** Member 1, Member 2, Member 7, Member 8  
**Wednesday question rounds:** Member 3, Member 4, Member 5, Member 6  
**Friday:** mini-project build for all eight members.  
**Harbour (Friday 13:00–17:00):** Harbour hybrid search with a reranker, compared against vector-only search.  
**Friday milestone:** Hybrid search with reranker beats vector-only on the test set

| Member | Question round | Chunk | After the talk, the class should understand | Friday: build the mini-project |
|---|---|---|---|---|
| Member 1 | Monday | Postgres full-text search: tsvector and ts_rank | Can use tsvector and explain what ts_rank measures. | Implement score-normalised hybrid fusion and test on 10 queries |
| Member 2 | Monday | Hybrid fusion: score normalisation | Can explain why raw scores from different systems cannot be added directly. | Implement RRF and compare it with normalised fusion |
| Member 3 | Wednesday | Reciprocal Rank Fusion (RRF) | Can explain rank-based fusion and why it is robust to score scales. | Time a bi-encoder against a cross-encoder and explain the gap |
| Member 4 | Wednesday | Bi-encoders vs cross-encoders (sentence-transformers) | Can explain the speed-versus-accuracy trade-off between bi-encoders and cross-encoders. | Add a reranker; measure latency and the effect of the top-k budget |
| Member 5 | Wednesday | Cross-encoder reranking and the top-k budget | Can explain the top-k budget and its latency cost. | Normalise test queries such as 'hostel' vs 'hostels' and 'CGPA' vs 'cumulative GPA' and check the matches |
| Member 6 | Wednesday | Query normalisation: abbreviations, spelling and informal phrasing | Can explain how abbreviations and informal phrasing affect matching, and how to handle them. | Compare hybrid with reranking against vector-only on the 20-query set |
| Member 7 | Monday | BM25 from scratch: term frequency and IDF | Can explain term frequency and inverse document frequency with a worked example. | Implement BM25 on the handbook corpus and check three queries |
| Member 8 | Monday | Length normalisation in BM25 | Can explain why BM25 penalises long documents and how length normalisation changes that. | Compare BM25 with Postgres full-text search on 10 queries |


## Week 12: Grounded answers, citations and access control

**Weekend before:** everyone studies the whole subtopic. Presenters write their 20 questions for the class.  
**Monday question rounds:** Member 1, Member 6, Member 7, Member 8  
**Wednesday question rounds:** Member 2, Member 3, Member 4, Member 5  
**Friday:** mini-project build for all eight members.  
**Harbour (Friday 13:00–17:00):** Harbour answers with citations and abstention.  
**Friday milestone:** Document Q&A with citations and abstention

| Member | Question round | Chunk | After the talk, the class should understand | Friday: build the mini-project |
|---|---|---|---|---|
| Member 1 | Monday | Abstention: saying 'not in the documents' correctly | Can design and test 'not in the documents' behaviour. | Test five unanswerable questions and enforce abstention |
| Member 2 | Wednesday | Access-aware retrieval enforced on the server | Can explain why access control must happen in the server and database, not in the prompt. | Enforce access groups in SQL and test a staff-only document from a student account |
| Member 3 | Wednesday | Indirect prompt injection in documents | Can explain how text inside a document can override the assistant's instructions. | Plant an injected instruction in a test document; show the effect and the fix |
| Member 4 | Wednesday | Spotlighting and delimiting untrusted text | Can explain how delimiting and labelling untrusted text helps, and where it falls short. | Add delimiters around retrieved text and rerun the injection test |
| Member 5 | Wednesday | Faithfulness checks: does the answer follow from the sources? | Can design a check that flags claims the sources do not support. | Build a faithfulness check that flags unsupported claims |
| Member 6 | Monday | Context assembly and token budgets | Can divide a token budget between system instructions, passages and the answer. | Assemble context from the top five passages within a token budget |
| Member 7 | Monday | Grounded answer prompting: answer only from the passages | Can write instructions that keep answers inside the retrieved passages. | Write the grounded-answer prompt and test five questions |
| Member 8 | Monday | Citations: linking claims to source spans | Can link each claim to a source span and check that the link holds. | Return citations with document ID and section |


## Week 13: Retrieval evaluation, query transformation and Mini-project 3

**Weekend before:** everyone studies the whole subtopic. Presenters write their 20 questions for the class.  
**Monday question rounds:** Member 5, Member 6, Member 7, Member 8  
**Wednesday question rounds:** Member 1, Member 2, Member 3, Member 4  
**Friday:** mini-project build for all eight members.  
**Harbour (Friday 13:00–17:00):** Harbour retrieval evaluation report.  
**Friday milestone:** Mini-project 3 delivered: Campus Handbook Q&A, with a retrieval evaluation report.

| Member | Question round | Chunk | After the talk, the class should understand | Friday: build the mini-project |
|---|---|---|---|---|
| Member 1 | Wednesday | HyDE: embedding a hypothetical answer | Can explain embedding a hypothetical answer, and its risk. | Implement HyDE and compare it with direct queries, including cost |
| Member 2 | Wednesday | Multi-query and RAG-Fusion | Can explain query expansion with fusion, and its cost. | Implement multi-query with fusion and measure the change |
| Member 3 | Wednesday | Query decomposition and self-querying into filters | Can explain multi-hop decomposition and turning language into metadata filters. | Turn 'hostel fees for level 200 in 2026' into metadata filters |
| Member 4 | Wednesday | Failure taxonomy and regression examples | Can classify retrieval failures and plan a fix for each category. | Write the Mini-project 3 report: metrics, failures and next fixes |
| Member 5 | Monday | Recall@k: definition and worked example | Can compute recall@k by hand. | Label 20 queries with relevant chunks as a team |
| Member 6 | Monday | MRR: reciprocal rank | Can compute MRR and explain what it rewards. | Implement recall@k and check three queries by hand |
| Member 7 | Monday | nDCG: graded relevance | Can explain graded relevance and why nDCG discounts lower ranks. | Implement MRR and nDCG and cross-check with scikit-learn's ndcg_score |
| Member 8 | Monday | Query rewriting and clarifying questions | Can explain how query rewriting changes retrieval, and when a clarifying question is better. | Add query rewriting and measure the change on the 20 queries |


## Week 14: Advanced retrieval and the production RAG service

**Weekend before:** everyone studies the whole subtopic. Presenters write their 20 questions for the class.  
**Monday question rounds:** Member 4, Member 5, Member 6, Member 7  
**Wednesday question rounds:** Member 1, Member 2, Member 3, Member 8  
**Friday:** mini-project build for all eight members.  
**Harbour (Friday 13:00–17:00):** Harbour versioned, cited knowledge service with a measured p95.  
**Friday milestone:** Advanced retrieval demo with p95 measured.

| Member | Question round | Chunk | After the talk, the class should understand | Friday: build the mini-project |
|---|---|---|---|---|
| Member 1 | Wednesday | Versioned indexes: build, validate and swap an alias | Can explain building, validating, swapping and rolling back an index version. | Build index v2 next to v1 and swap the alias after validation |
| Member 2 | Wednesday | Incremental updates: upserts, tombstones and hash diffs | Can explain upserts, tombstones and content-hash diffs. | Apply a changed handbook section: upsert changed chunks and tombstone removed ones |
| Member 3 | Wednesday | Query analytics and latency budgets (p50, p95, p99) | Can read p50, p95 and p99 and set a latency budget. | Log query analytics and load-test the retrieval endpoint to the p95 target with k6 |
| Member 4 | Monday | GraphRAG: entities, relations and when structure matters | Can explain entities and relations, and when a graph beats vector search. | Build a small entity graph with networkx from 10 handbook sections and query one relation |
| Member 5 | Monday | GraphRAG vs plain RAG: cost and when not to use it | Can justify when GraphRAG's extra cost is not worth it. | Compare a GraphRAG answer with a RAG answer on five structural questions |
| Member 6 | Monday | Multimodal retrieval: CLIP-style image and text embeddings for campus map images | Can explain shared image-text embeddings and their limits. | Index 10 campus map images with captions and retrieve them with text |
| Member 7 | Monday | Semantic caching: thresholds and wrong-hit risk | Can explain similarity thresholds, and why wrong cache hits are dangerous. | Add a semantic cache and demonstrate a wrong hit on near-miss queries |
| Member 8 | Wednesday | Exact caching: query keys and TTLs | Can design cache keys and expiry times that avoid stale answers. | Add an exact cache with a hashed key and a TTL |


---

# Month 4: Conference Planner Agent (Mini-project 4)


## Week 15: Agent fundamentals

**Weekend before:** everyone studies the whole subtopic. Presenters write their 20 questions for the class.  
**Monday question rounds:** Member 3, Member 4, Member 5, Member 6  
**Wednesday question rounds:** Member 1, Member 2, Member 7, Member 8  
**Friday:** mini-project build for all eight members.  
**Harbour (Friday 13:00–17:00):** Harbour single agent with three tools and a step log.  
**Friday milestone:** Single agent with three tools and a step log

| Member | Question round | Chunk | After the talk, the class should understand | Friday: build the mini-project |
|---|---|---|---|---|
| Member 1 | Wednesday | Reflection and self-critique: when it helps and when it loops | Can explain when self-critique helps and when it causes loops. | Add one reflection pass and measure whether it fixes errors |
| Member 2 | Wednesday | When not to use an agent: workflow vs single call vs agent | Can choose between a workflow, a single model call and an agent for a task, with reasons. | Write the decision tree: which conference tasks should not be agents |
| Member 3 | Monday | An agent is an LLM, a loop, tools and memory | Can explain the loop, tools and memory in an agent, and build a minimal one. | Build a 100-line agent loop with a fake LLM and two tools |
| Member 4 | Monday | Read tools vs write tools | Can explain why write tools need more control than read tools. | Add a third tool and log every step as a trace line |
| Member 5 | Monday | ReAct: reason, act, observe | Can explain the reason-act-observe cycle and parse an action from model output. | Parse ReAct-style actions and handle a malformed action |
| Member 6 | Monday | Planning: plan-then-execute and task decomposition | Can explain plan-then-execute and when planning helps. | Build plan-then-execute for 'check venue availability, then check speaker list' |
| Member 7 | Wednesday | Short-term memory: windows and summaries | Can explain what message windows and summaries keep and what they lose. | Keep a 30-turn conversation within a window using a summary |
| Member 8 | Wednesday | Long-term and episodic memory: what to store and retrieve | Can design a write policy for long-term memory. | Store organiser preferences with a policy for what must not be stored |


## Week 16: LangGraph state machines

**Weekend before:** everyone studies the whole subtopic. Presenters write their 20 questions for the class.  
**Monday question rounds:** Member 2, Member 3, Member 4, Member 5  
**Wednesday question rounds:** Member 1, Member 6, Member 7, Member 8  
**Friday:** mini-project build for all eight members.  
**Harbour (Friday 13:00–17:00):** Harbour workflow with approval and resume.  
**Language track:** TypeScript Handbook and Exercism's TypeScript track, about one hour a week  
**Friday milestone:** LangGraph workflow with approval and resume

| Member | Question round | Chunk | After the talk, the class should understand | Friday: build the mini-project |
|---|---|---|---|---|
| Member 1 | Wednesday | Testing graphs with stubbed LLM nodes | Can test transitions without calling a real model. | Write graph tests with stubbed LLM nodes |
| Member 2 | Monday | Nodes, edges and typed state | Can model a workflow as a graph with typed state. | Port the Week 15 agent into a LangGraph graph |
| Member 3 | Monday | Reducers: how state updates merge | Can explain how state updates merge, and why that matters. | Define state for messages, venue ID and approval status |
| Member 4 | Monday | Conditional edges and routing in one place | Can route on state in one place, using conditional edges. | Route between venue, speaker and invitation paths |
| Member 5 | Monday | Postgres checkpointing and resuming a case | Can explain resuming a run from a stored checkpoint. | Add a Postgres checkpointer; stop and resume a run |
| Member 6 | Wednesday | Interrupts for human-in-the-loop approval | Can pause a run for human approval and resume it with a decision. | Interrupt for approval before any invitation is sent |
| Member 7 | Wednesday | Loop guards: maximum iterations and graceful stops | Can add a maximum-steps guard and a graceful stop. | Add a max-steps guard and test a deliberately looping case |
| Member 8 | Wednesday | Streaming node events to a client | Can stream node events and explain what the client receives. | Stream node events to the console |


## Week 17: Multi-agent patterns and frameworks

**Weekend before:** everyone studies the whole subtopic. Presenters write their 20 questions for the class.  
**Monday question rounds:** Member 1, Member 2, Member 3, Member 4  
**Wednesday question rounds:** Member 5, Member 6, Member 7, Member 8  
**Friday:** mini-project build for all eight members.  
**Harbour (Friday 13:00–17:00):** Harbour supervisor and critic added only where measurement shows they help.  
**Friday milestone:** Multi-agent crew (supervisor plus critic) running end to end

| Member | Question round | Chunk | After the talk, the class should understand | Friday: build the mini-project |
|---|---|---|---|---|
| Member 1 | Monday | Supervisor pattern: routing and delegation | Can design a supervisor that routes work and delegates it. | Build a supervisor graph that routes between venue and speaker agents |
| Member 2 | Monday | Swarm and handoffs: passing control directly | Can explain direct handoffs and their trade-off in traceability. | Build a handoff version and compare trace lengths |
| Member 3 | Monday | Hierarchical teams: sub-supervisors and budgets | Can explain sub-supervisors and how a budget is split between them. | Build a hierarchical version with one sub-supervisor |
| Member 4 | Monday | Researcher, writer and critic pipeline | Can explain the critic's role and when a review loop should stop. | Build researcher, writer and critic with a rejection loop |
| Member 5 | Wednesday | Shared-state contracts and typed inter-agent messages | Can define contracts between agents and validate messages against them. | Define a typed message schema and validate it at each hop |
| Member 6 | Wednesday | Failure modes: loops, role drift and false agreement | Can name loops, role drift and false agreement, and detect each one. | Inject role drift and add detection for it |
| Member 7 | Wednesday | CrewAI concepts: roles, tasks and crews, mapped to LangGraph | Can map roles and tasks onto graph nodes, and compare the control each approach gives. | Rebuild one agent in CrewAI and compare the code and the control |
| Member 8 | Wednesday | Memory across agents: shared vs private | Can decide between shared and private memory for agents, with reasons. | Decide shared vs private memory for the crew and write an ADR |


## Week 18: Safe tools, budgets and agent tracing (Mini-project 4)

**Weekend before:** everyone studies the whole subtopic. Presenters write their 20 questions for the class.  
**Monday question rounds:** Member 1, Member 2, Member 3, Member 8  
**Wednesday question rounds:** Member 4, Member 5, Member 6, Member 7  
**Friday:** mini-project build for all eight members.  
**Harbour (Friday 13:00–17:00):** Harbour approval gates and budgets on the agent.  
**Friday milestone:** Mini-project 4 delivered: Conference Planner Agent.

| Member | Question round | Chunk | After the talk, the class should understand | Friday: build the mini-project |
|---|---|---|---|---|
| Member 1 | Monday | Tool design: narrow purpose, typed errors and idempotency | Can design narrow, typed and idempotent tools. | Refactor tools to be narrow, typed and return error codes |
| Member 2 | Monday | Write actions behind approval gates | Can explain why consequential actions wait for a human decision. | Gate the send-invitation tool behind human approval |
| Member 3 | Monday | Idempotency keys for invitations and bookings | Can prevent a double booking when a request is retried. | Add an idempotency key and test a double submission |
| Member 4 | Wednesday | Step and cost budgets with graceful stops | Can enforce step and cost limits with a graceful stop. | Add a step budget and a cost budget per run |
| Member 5 | Wednesday | Indirect prompt injection through tool outputs | Can explain how tool output can carry instructions that hijack the agent. | Plant instructions in a venue description and show the agent ignores them |
| Member 6 | Wednesday | Audit trails: who, what, when and result | Can produce a who, what and when record for every tool call. | Write an audit record for every tool call |
| Member 7 | Wednesday | Agent traces: spans for each step and tool call | Can explain spans, and read a full run trace. | Emit a trace per step and view a full run |
| Member 8 | Monday | Read-only database roles, parameterised queries and row limits | Can prove that a database role cannot write, and explain least privilege. | Create a read-only database role and prove that writes fail |


---

# Month 5: Ship It Lab (Mini-project 5)


## Week 19: Evaluation gate, red-teaming and guardrails

**Weekend before:** everyone studies the whole subtopic. Presenters write their 20 questions for the class.  
**Monday question rounds:** Member 1, Member 2, Member 7, Member 8  
**Wednesday question rounds:** Member 3, Member 4, Member 5, Member 6  
**Friday:** mini-project build for all eight members.  
**Harbour (Friday 13:00–17:00):** Harbour eval gate blocks a deliberate regression; red-team run recorded.  
**Friday milestone:** Eval gate blocks a deliberate regression

| Member | Question round | Chunk | After the talk, the class should understand | Friday: build the mini-project |
|---|---|---|---|---|
| Member 1 | Monday | Agent evals: tool correctness, task completion and path efficiency | Can score tool correctness, task completion and path efficiency. | Score agent runs for tool correctness and completion |
| Member 2 | Monday | Regression tests in CI: baselines and tolerances | Can explain baselines and tolerances, and why they block merges. | Add the eval gate to GitHub Actions with a baseline file |
| Member 3 | Wednesday | Attack suite: direct and indirect prompt injection | Can design direct and indirect injection tests. | Build a 50-case attack suite and run it against the Campus Q&A service |
| Member 4 | Wednesday | Jailbreak, PII-leak and excessive-agency tests | Can design tests for data leakage and excessive agency. | Run PII-leak and excessive-agency tests and log the results |
| Member 5 | Wednesday | Input and output guardrails and their false-positive rate | Can measure guardrail false positives and explain the trade-off. | Add an output PII filter and measure false positives on benign messages |
| Member 6 | Wednesday | Red-team report: severity, reproduction, fix and retest | Can write a red-team report with severity, reproduction, fix and retest. | Write the red-team report with severity levels and retest results |
| Member 7 | Monday | Eval design: error analysis before metrics | Can read failures and group them into categories before choosing metrics. | Write error-analysis notes from Mini-projects 1 to 4 |
| Member 8 | Monday | Eval types: unit, integration, human, LLM-judge and benchmark | Can choose between unit, integration, human, judge and benchmark evaluations. | Write 25 eval cases for your chunk's topic (200 in total) |


## Week 20: Observability and containers

**Weekend before:** everyone studies the whole subtopic. Presenters write their 20 questions for the class.  
**Monday question rounds:** Member 1, Member 6, Member 7, Member 8  
**Wednesday question rounds:** Member 2, Member 3, Member 4, Member 5  
**Friday:** mini-project build for all eight members.  
**Harbour (Friday 13:00–17:00):** Harbour stack runs on kind with traces visible.  
**Friday milestone:** Stack runs on kind with traces visible

| Member | Question round | Chunk | After the talk, the class should understand | Friday: build the mini-project |
|---|---|---|---|---|
| Member 1 | Monday | Metrics: latency histograms, error rates and token usage | Can choose useful metrics and explain what a histogram shows. | Export latency and token metrics and draft a one-page dashboard |
| Member 2 | Wednesday | Multi-stage Docker images for each service | Can explain why multi-stage builds produce smaller and safer images. | Build images for the API and retrieval services |
| Member 3 | Wednesday | Kubernetes basics on kind with kubectl: Deployments, Services and probes | Can explain Deployments, Services and probes. | Deploy the stack to kind with Deployments, Services and probes |
| Member 4 | Wednesday | Secrets and configuration in Kubernetes | Can keep secret values out of manifests and out of git. | Move secrets into Kubernetes Secrets; confirm none are in git |
| Member 5 | Wednesday | Rollback: one-command revert and a timed drill | Can roll back a deployment and measure how long it takes. | Run a rollback drill and time it |
| Member 6 | Monday | Structured logs (logging module or structlog): what to log and what must never be logged | Can decide what to log, and what must never be logged. | Add structured logs to one service and check for PII |
| Member 7 | Monday | OpenTelemetry tracing across API, retrieval, LLM and tools | Can instrument a multi-step request with spans. | Add OpenTelemetry spans to the retrieval and agent code |
| Member 8 | Monday | Arize Phoenix: viewing traces and evaluations | Can read a trace and an evaluation in Phoenix. | Send traces to Phoenix and capture one full run |


## Week 21: Frontend, reliability and launch (Ship It Lab showcase)

**Weekend before:** everyone studies the whole subtopic. Presenters write their 20 questions for the class.  
**Monday question rounds:** Member 5, Member 6, Member 7, Member 8  
**Wednesday question rounds:** Member 1, Member 2, Member 3, Member 4  
**Friday:** mini-project build for all eight members.  
**Harbour (Friday 13:00–17:00):** Harbour release candidate with eval gate, traces and known limitations.  
**Language track:** react.dev Learn section, self-paced, about one hour a week  
**Friday milestone:** Mini-project 5 showcase: Ship It Lab.

| Member | Question round | Chunk | After the talk, the class should understand | Friday: build the mini-project |
|---|---|---|---|---|
| Member 1 | Wednesday | Retries, timeouts and idempotency across services | Can explain how retries interact with idempotency. | Add a timeout and idempotency key to one endpoint and test a retry |
| Member 2 | Wednesday | Background jobs with Postgres SKIP LOCKED | Can explain how SKIP LOCKED allows safe job claiming in Postgres. | Demonstrate a background job with SKIP LOCKED and two workers |
| Member 3 | Wednesday | Explaining one design decision in two minutes | Can explain one design decision and its trade-off in two minutes. | Run a mock interview on your chunk with a peer |
| Member 4 | Wednesday | Final demo script, README and known limitations | Can present the demo and state the known limitations honestly. | Write the README and limitations; run a live three-minute demo |
| Member 5 | Monday | TypeScript essentials for React developers (self-paced track) | Can read and write typed functions and interfaces. | Write typed client types for the Q&A endpoints |
| Member 6 | Monday | React and Vite: components, props and state | Can explain props and state, and when to lift state up. | Build a chat component that calls the Q&A service |
| Member 7 | Monday | Calling the API from React: loading and error states | Can design interfaces for loading, error and empty states. | Build a review panel with approve and reject for flagged answers |
| Member 8 | Monday | Streaming chat UI and a trace list | Can display streamed output and a trace list. | Add a trace list fed by the API |

---

## 8. Checkpoints

- **End of Month 1 (end of Week 4):** the Library Loans API runs from a fresh clone, with tests and CI passing. Each member can explain one request from input to database and back. Harbour has its core API skeleton.
- **End of Month 2 (end of Week 7):** the Inbox Triage Assistant returns validated data, handles failures and keeps secrets out of git. The team can show a fluent-but-wrong answer caught by evaluation. Harbour has a structured triage prototype.
- **End of Month 3 (end of Week 14):** the Campus Handbook Q&A retrieves passages, answers from them, shows sources, and says so when evidence is missing. Harbour has a versioned knowledge service with a measured p95.
- **End of Month 4 (end of Week 18):** the Conference Planner Agent blocks unapproved invitations and stops looping runs. A full trace can be read. Harbour has approval gates and budgets.
- **End of Month 5 (end of Week 21):** the Ship It Lab showcase. The team runs the eval gate, shows traces, describes known limitations, and each member explains their chunk and one trade-off. Harbour has a release candidate.

---

## 9. What to decide before Week 1 ends

1. Monday and Wednesday after the question rounds: decided, the class works through the notebook exercises together.
2. Member names for the roster.
3. Confirm the five mini-project domains: Library Loans API, Inbox Triage Assistant, Campus Handbook Q&A, Conference Planner Agent and Ship It Lab.
4. Which Nigerian public holidays fall during the 21 active weeks, so the question-round rotation can be adjusted.
5. The LLM provider and budget, and whether a local Ollama model is used for the labs.
6. Twitter Space: decided, Friday or Saturday, 20:00–22:00. Confirm which of the two days.
7. Local Docker on each laptop, or a shared server for Jupyter and Postgres.