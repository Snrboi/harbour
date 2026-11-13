# Week 3: SQL & PostgreSQL Basics

**Harbour Learning Programme · Month 1 · Week 3: team briefing**

> **The whole week in one line:** Put the rules in the database where nothing can skip them, and version the database so you can move it forward and back.
> *(from the schema & Alembic notebook)*

| | |
|---|---|
| **Sources** | Harbour [README](../README.md) (`learn` branch) and the 7 notebooks in this `week-3/` folder |
| **Mini-project** | Library Loans API (Weeks 1–4) |
| **Friday milestone** | Schema v1 with a migration script |
| **Harbour step** | Harbour schema v1 with an Alembic migration |
| **Language track** | About 1 hour a week of SQL practice on pgexercises.com |

---

## Contents

1. [Where Week 3 fits](#1-where-week-3-fits)
2. [Week 3 at a glance](#2-week-3-at-a-glance)
3. [Part A: Designing the data](#3-part-a-designing-the-data)
4. [Part B: Querying the data](#4-part-b-querying-the-data)
5. [Part C: Keeping it fast and safe](#5-part-c-keeping-it-fast-and-safe)
6. [How Week 3 connects to the whole project](#6-how-week-3-connects-to-the-whole-project)
7. [Decisions the team must agree on before Friday](#7-decisions-the-team-must-agree-on-before-fridays-migration)
8. [The 10 rules to remember](#8-the-10-rules-to-remember)
9. [Quick-fire check for the team](#9-quick-fire-check-for-the-team)

---

## 1. Where Week 3 fits

Month 1 builds one small but complete backend, the Library Loans API, one layer per week. Week 3 is the **data layer**: the part that stores the truth and refuses bad data.

| Week | Layer we build | Question it answers |
|---|---|---|
| 1 | Python + Git | Can we write and review clean code together? |
| 2 | HTTP / REST API contract | What can clients **ask** our system to do? |
| **3** | **SQL + PostgreSQL schema + migrations** | **Where is the data kept, and what rules keep it correct?** |
| 4 | FastAPI + SQLAlchemy + tests + Docker + CI | How do the API and the database connect, get tested and ship? |

**Why it matters:** in Week 4 every endpoint from the Week 2 contract will read or write the tables we design this week. If the schema is wrong, every later layer inherits the bug.

---

## 2. Week 3 at a glance

| Owner / day | Topic | What the class must be able to do | Friday build |
|---|---|---|---|
| M1 · Mon | SELECT, WHERE, NULL | Filter correctly; know NULL ≠ anything; use `IS NULL` | Query books with no copies on the shelf |
| M2 · Mon | Joins (inner, left, anti) | Predict the rows each join returns | Anti-join: books never borrowed |
| M3 · Wed | Aggregates, GROUP BY, HAVING | Summarise per group; explain why WHERE can't filter aggregates | Fines per member, stored as integer cents |
| M4 · Wed | Indexes & EXPLAIN | Read a query plan; say why an index helps or hurts | Add an index, EXPLAIN before/after |
| M5 · Wed | Transactions & isolation | Explain atomicity and isolation with a failed loan | Show a rollback mid-transaction |
| M6 · Wed | Library schema + Alembic | Justify every table and key | First Alembic migration applied to Postgres |
| M7 · Mon | Tables, data types, primary keys | Pick the right types and key, and justify them | `books` + `members` tables with constraints |
| M8 · Mon | Constraints & normalisation | Explain 1NF to 3NF and why duplicate data causes bugs | Add a foreign key; show a rejected insert |

*The sections below group the 8 topics in the order that makes them easiest to understand: **design the data → query the data → keep it fast and safe.***

---

## 3. Part A: Designing the data

### 3.1 Tables, data types & primary keys
*Member 7 · Monday · notebook: `Tables_Data_Types_and_Primary_Keys_Week_3.ipynb`*

> **In one sentence:** Decide what **one row means** first, then choose types based on what the data means (not how it looks), and give every row a stable ID.

**Key concepts**
- **Six design steps:** row meaning → columns → types → primary key → constraints → test inserts.
- **Choose types by meaning:** phone numbers and ISBNs are `TEXT` (they keep leading zeros and `+`), a year is `SMALLINT` (not a DATE), a join date is `DATE`, an ingestion moment is `TIMESTAMPTZ`, and active/inactive is `BOOLEAN`.
- **NULL, `''`, `0` and `FALSE` are four different things.** `NOT NULL` does **not** block an empty string, so add a `CHECK` for that.
- **Primary key = unique + never NULL**, and Postgres builds an index for it automatically. We use `BIGINT GENERATED ALWAYS AS IDENTITY`.
- **Surrogate vs natural key:** emails and ISBNs can change or be missing, so they become `UNIQUE` columns, not the key.

**Watch out**
- Gaps in generated IDs are normal. Never use the largest ID as a row count.
- Don't pick a key just because today's sample data happens to be unique.
- A `CHECK` lets NULL through. If a value must exist, add `NOT NULL` as well.

**Friday build:** Create `books` and `members` with constraints and explain every choice using the sentence: *"I chose X for Y because Z. The trade-off is W."*

**Why it matters for the project:** This same reasoning designs Harbour's tables. The notebook proposes a Harbour `documents` table (`document_id`, `title`, `body`, `source_url`, `received_at TIMESTAMPTZ`) and an `ingestion_jobs` table as a design exercise.

---

### 3.2 Constraints & normalisation
*Member 8 · Monday · notebook: `Constraints_and_Normalisation_Library.ipynb`*

> **In one sentence:** **Normalisation decides where each fact lives (one home only). Constraints are rules that stop bad data from getting in.** Normalisation removes the *temptation* to store inconsistent data; constraints remove the *ability*.

**Key concepts**
- **Three bugs caused by duplicated data (U-I-D):**
  - **Update:** you change one copy and miss another, so the data contradicts itself.
  - **Insert:** you can't add a book without inventing a fake loan.
  - **Delete:** removing a loan also wipes the member's phone number.
- **Normal forms:**
  - **1NF:** one value per cell, and every row has an ID.
  - **2NF:** no column depends on only *part* of a composite key.
  - **3NF:** no non-key column depends on another non-key column (e.g. a city's postcode doesn't belong in `members`).
- **The five constraints:** `PRIMARY KEY`, `FOREIGN KEY` (the value must exist in the parent table), `UNIQUE`, `NOT NULL`, `CHECK` (a yes/no rule about one row). `DEFAULT` fills in missing values but doesn't validate anything.
- **Delete policies:** `RESTRICT` (the default) for history and money. Use `CASCADE` only for children that are truly owned by the parent. Use `SET NULL` only where NULL actually means something.
- **Validate in both places:** Pydantic gives friendly errors quickly. The database is the final gate that scripts, race conditions and psql sessions can't get past.

**Watch out**
- `CASCADE` from members to loans means one delete could erase years of fines.
- A `CHECK` can't look at other rows. A rule like "max 5 active loans" needs app logic plus a transaction, or a trigger.
- Over-normalising: every split adds a JOIN. Only split to fix real duplication bugs.
- Name your constraints (`CONSTRAINT due_after_loan …`) so the error messages make sense.

**Friday build:** Add a foreign key on `loans` and show the database **rejecting** a loan for member 9999 (a member who doesn't exist).

**Why it matters for the project:** Harbour will store documents, chunks and later agent state. Each fact should have one home, and the database should refuse orphans, such as a chunk that points to a missing document.

---

### 3.3 Designing the library schema, versioned with Alembic
*Member 6 · Wednesday · notebook: `schema-and-alembic.ipynb`*

> **In one sentence:** Five tables hold the library without letting bad data in, and **Alembic is "Git for the schema"**: numbered revisions, each with an `upgrade()` and a `downgrade()`.

**Key concepts**
- **Five tables:** `books` (a title) · `copies` (one physical object) · `members` · `loans` (one borrowing event) · `fines` (one charge on a loan).
- **A book is not a copy.** Three copies of one title means 1 row in `books` and 3 rows in `copies`. Without this split you can't tell which copy is out.
- **Shape:**
  ```text
  books 1──* copies 1──* loans *──1 members
                           │
                           1──* fines
  ```
- **Partial unique index:** a copy can be on only **one open loan** at a time, but it can still be borrowed again after it's returned:
  ```sql
  CREATE UNIQUE INDEX one_open_loan_per_copy
      ON loans (copy_id)
      WHERE returned_on IS NULL;
  ```
- **Money is stored as INTEGER cents/kobo, never FLOAT** (because `0.1 + 0.2 ≠ 0.3`).
- **Alembic workflow:**
  ```bash
  alembic init migrations
  # wire migrations/env.py: import Base, set target_metadata = Base.metadata, read DATABASE_URL
  alembic revision --autogenerate -m "library schema v1"
  # READ the generated file
  alembic upgrade head
  alembic downgrade -1   # prove it can go back
  ```

**Watch out**
- If `env.py` isn't wired up, autogenerate silently produces an **empty migration**. This is the most common Alembic mistake.
- Never edit a migration that has already been applied. Add a new one instead. One change per revision. Commit `versions/` to Git.
- Foreign keys are **not** indexed automatically. Add the index yourself.

**Friday build:** Write the first Alembic migration and apply it to Postgres.

**Why it matters for the project:** This is **exactly** the Harbour Friday step: "Harbour schema v1 with an Alembic migration." The notebook sketches `documents` + `chunks` with `content_sha256 UNIQUE`, so ingesting the same page twice is refused. That's the Week 2 idempotency rule enforced by the database. `chunks.embedding vector(384)` comes in Week 10 with pgvector.

---

## 4. Part B: Querying the data

### 4.1 SELECT, WHERE & NULL behaviour
*Member 1 · Monday · notebook: `SELECT, WHERE & NULL.ipynb`*

> **In one sentence:** `SELECT` picks columns, `WHERE` keeps rows where the condition is TRUE, and **NULL means "unknown"**, so you test it with `IS NULL`, never `= NULL`.

**Key concepts**
- SQL uses **three-valued logic:** TRUE, FALSE, UNKNOWN. Any comparison with NULL gives UNKNOWN, and WHERE drops those rows.
- `copies_on_shelf = 0` (a known zero) is different from `copies_on_shelf IS NULL` (never recorded).
- `SELECT *` is fine for exploring. In real code, name only the columns you need.

```sql
SELECT title FROM books WHERE copies_on_shelf IS NULL;   -- correct
SELECT title FROM books WHERE copies_on_shelf = NULL;    -- always returns nothing
```

**Watch out**
- `WHERE x = NULL` returns **nothing**, even for rows where x really is NULL.
- Never quietly treat missing data as zero. Agree as a team what "no copies" means.

**Friday build:** Query books with no copies on the shelf.

**Why it matters for the project:** Every API read endpoint in Week 4 is a SELECT/WHERE underneath. Getting NULL wrong causes silent bugs: wrong results and no error message.

---

### 4.2 Joins: inner, left and anti-join
*Member 2 · Monday · ⚠️ there is no notebook for this topic in the week-3 folder yet*

> **In one sentence:** Joins put normalised tables back together. The join type decides **which rows survive** when there's no match.

**Key concepts**
- **INNER JOIN:** only rows that match on both sides (e.g. loans *with* their member).
- **LEFT JOIN:** every row from the left table. Where there's no match, the right side's columns are NULL (e.g. all books, borrowed or not).
- **Anti-join:** rows on the left with **no** match:
  ```sql
  -- books never borrowed
  SELECT b.title
  FROM books b
  WHERE NOT EXISTS (
      SELECT 1 FROM copies c JOIN loans l ON l.copy_id = c.copy_id
      WHERE c.book_id = b.book_id
  );
  ```

**Watch out**
- Moving a condition from `ON` to `WHERE` in a LEFT JOIN can quietly turn it into an INNER JOIN.
- `NOT IN (subquery)` returns nothing if the subquery contains a NULL. `NOT EXISTS` is safer.

**Friday build:** Write an anti-join that returns books that have never been borrowed.

**Why it matters for the project:** Normalisation (3.2) splits data across tables, and joins bring it back together. Every Week 4 endpoint that returns "a loan with its book and member" depends on this.

---

### 4.3 Aggregates, GROUP BY & HAVING
*Member 3 · Wednesday · notebook: `aggregates_group_by_having_lesson.ipynb`*

> **In one sentence:** Aggregates (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`) summarise many rows. `GROUP BY` produces one summary per group. **WHERE filters rows before grouping; HAVING filters groups after.**

**Key concepts**
- Clause order: `SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY`.
- Every selected column must either appear in `GROUP BY` or sit inside an aggregate.
- `COUNT(*)` counts every row. `COUNT(col)` skips NULLs. `SUM` of nothing returns NULL, so use `COALESCE(SUM(x), 0)`.
- Without `ORDER BY`, the order of results is not guaranteed.

```sql
SELECT member_id, SUM(fine_cents) AS total_fines_cents
FROM loans
GROUP BY member_id
HAVING SUM(fine_cents) >= 200
ORDER BY member_id;
```

**Watch out**
- `WHERE SUM(fine_cents) >= 200` is an error, because the sums haven't been calculated yet at that point. Use `HAVING`.
- Store money as integer cents/kobo, not floats.

**Friday build:** Calculate fines per member, store money as integer cents, and explain why.

**Why it matters for the project:** This is how reports and metrics get built. The same pattern later powers evaluation summaries (e.g. accuracy per label in Month 2, retrieval metrics in Month 3).

---

## 5. Part C: Keeping it fast and safe

### 5.1 Indexes & reading EXPLAIN output
*Member 4 · Wednesday · notebook: `Indexes_and_EXPLAIN.ipynb`*

> **In one sentence:** An index is like the index at the back of a textbook. It helps **selective** searches, but it costs storage and slows down writes. `EXPLAIN` shows you the plan instead of leaving you to guess.

**Key concepts**
- `EXPLAIN` shows the plan **without running** the query. `EXPLAIN ANALYZE` **runs it** and shows actual rows and times.
- **Scan types:**
  - `Seq Scan`: reads every row (not always bad).
  - `Index Scan`: uses the index to find rows, then fetches them from the table.
  - `Bitmap Index Scan` + `Bitmap Heap Scan`: collects matching row locations first, then fetches them together.
  - `Index Only Scan`: the index alone holds every column the query needs.
- `cost=` values are estimates in internal units, not milliseconds. Compare estimated `rows` with `actual rows`.
- **Selectivity:** an index helps when the condition matches only a few rows (e.g. a unique email) and often doesn't help when it matches most of the table.
- **Composite index column order matters:** `(name, salary)` helps queries filtering on `name`, but not queries on `salary` alone.
- `ANALYZE table` refreshes the statistics the planner relies on. It's a different command from `EXPLAIN ANALYZE`.

**Watch out**
- Creating an index doesn't guarantee Postgres will use it. The planner chooses whatever it estimates is cheapest.
- Be careful running `EXPLAIN ANALYZE` on statements that change data: it really executes them.
- Don't index every column. Index the columns you filter and join on, starting with foreign keys.

**Friday build:** Add an index, run EXPLAIN before and after, and explain why the plan changed (or didn't).

**Why it matters for the project:** Harbour must meet a **measured p95** by Week 14. pgvector indexes (Week 10) and full-text search (Week 11) are both indexes inside Postgres, and they're judged the same way: read the plan, measure, then decide.

---

### 5.2 Transactions & isolation
*Member 5 · Wednesday · notebook: `Transactions_Isolation_Atomicity.ipynb`*

> **In one sentence:** A transaction groups several changes into **all or nothing** (atomicity). Isolation sets the rules for what other connections can see while that work is still in progress.

**Key concepts**
- `BEGIN` → changes → `COMMIT` (save everything) or `ROLLBACK` (undo everything that wasn't committed).
- **The demo:** mark a copy as loaned, then the loan insert fails (member 999 doesn't exist), then ROLLBACK, and the copy is available again.
- **Safe checkout pattern:** update only if the copy is still available, check that exactly 1 row changed, then insert the loan and commit:
  ```sql
  BEGIN;
  UPDATE copies SET status = 'loaned' WHERE id = 101 AND status = 'available';
  -- app checks: exactly 1 row changed, otherwise ROLLBACK
  INSERT INTO loans (copy_id, member_id) VALUES (101, 7);
  COMMIT;
  ```
- **Postgres isolation levels:**
  - **READ COMMITTED** (the default): each statement sees a fresh snapshot.
  - **REPEATABLE READ:** the whole transaction sees one snapshot.
  - **SERIALIZABLE:** may abort a transaction, in which case retry the **whole** transaction.
- In Postgres, an error inside a transaction leaves it failed until you roll back.

**Watch out**
- Checking with a SELECT first doesn't stop two people grabbing the last copy at once. You need a concurrency-safe write plus constraints.
- **A rollback can't unsend an email or undo an LLM call.** For outside side-effects, use an outbox pattern, idempotency keys and retryable workers.

**Friday build:** Show a rollback when a loan update fails partway through a transaction.

**Why it matters for the project:** This is the most forward-looking topic of the week. Harbour will call LLM providers (Month 2), write embeddings (Month 3), run agents with approval gates (Month 4), and claim jobs with `SKIP LOCKED` (Week 21). All of these need atomic writes and idempotency.

---

## 6. How Week 3 connects to the whole project

Postgres isn't a one-week topic. It's the **foundation Harbour stands on for all 21 weeks.** Here's where this week's ideas come back:

| When | What comes back | Week 3 idea it relies on |
|---|---|---|
| Week 4 | psycopg 3 + SQLAlchemy 2.0 sessions; Postgres in Docker Compose; tests against a real DB | Schema, transactions (session commit/close), Alembic |
| Week 4 | Pydantic validation (ISBN, due dates) | Validate in **both** layers: Pydantic + DB constraints |
| Weeks 6–7 | Safe retries of model calls; evaluation summaries | Idempotency, transactions, GROUP BY |
| Week 8 | Versioned sample corpus for Harbour | Unique content hash = no duplicate ingestion |
| Week 10 | pgvector: vector search **inside Postgres** | Indexes, EXPLAIN, choosing an index |
| Week 11 | Postgres full-text (keyword) search for hybrid search | Indexes, query plans |
| Week 14 | Production knowledge service with measured p95 | Index trade-offs, measuring rather than guessing |
| Weeks 16–17 | LangGraph with a **Postgres checkpointer** (agent state saved) | Schema design, transactions |
| Week 21 | `SKIP LOCKED` for safe job claiming | Isolation and concurrency |

> **Harbour this Friday (13:00–17:00):** Apply the same thinking to Harbour's own domain: design schema v1 (documents/ingestion, not books) and ship it as an Alembic migration. Team rule 8: **no copying library tables or code into Harbour.** Rewrite the idea in Harbour's own code.

---

## 7. Decisions the team must agree on before Friday's migration

The notebooks were written by different members and **don't fully agree.** These need one team answer before anything goes into a migration:

| # | Question | What the notebooks currently say |
|---|---|---|
| 1 | ID style | Schema/Alembic notebook: `TEXT` IDs (`BK-001`) + `SERIAL`. Types and constraints notebooks: `BIGINT GENERATED ALWAYS AS IDENTITY`. |
| 2 | Copy columns | One uses `status` (available / on_loan / lost). Another uses `condition` (new / good / worn / damaged) + `barcode`. We probably need both. |
| 3 | Due-date rule | `due_on >= borrowed_on` vs `due_date > loan_date`. Are same-day loans allowed? |
| 4 | Money column name/unit | `amount_cents`, `fine_cents` or `amount_kobo`. Pick one and state the unit clearly. |
| 5 | "No copies on the shelf" | Notebook 1 uses a `copies_on_shelf` column, but in the normalised schema it's a **count of available copies**, which is a query, not a stored column. |
| 6 | Harbour schema v1 | Option A: `documents` + `chunks` with unique `content_sha256`. Option B: a single `documents` table (`body`, `source_url`, `received_at`) + `ingestion_jobs`. |
| 7 | Delete policy | Recommended: `RESTRICT` on loans and fines (history), plus the partial unique index for one open loan per copy. |

---

## 8. The 10 rules to remember

1. **Define what one row means before you write any SQL.**
2. **NULL means unknown.** Test it with `IS NULL`. It's not zero and it's not an empty string.
3. **Every table has a stable surrogate primary key.** Natural values like email and ISBN become `UNIQUE`.
4. **One fact, one home** (normalise to 3NF). Every other table just points to it.
5. **Put rules in the database** (FK, UNIQUE, CHECK, NOT NULL) **and** in Pydantic.
6. **WHERE filters rows; HAVING filters groups.**
7. **Money is INTEGER cents/kobo**, formatted only when it's displayed.
8. **Index what you filter and join on** (foreign keys aren't indexed for you), and prove it with `EXPLAIN`.
9. **Related changes go in one transaction.** A rollback can't undo things outside the database.
10. **Every schema change is an Alembic revision.** Read it, test the downgrade, never edit an applied one.

---

## 9. Quick-fire check for the team

<details>
<summary><b>Click to reveal the answers</b> (try answering first)</summary>

| Question | Answer |
|---|---|
| Why doesn't `WHERE x = NULL` work? | Comparing with NULL gives UNKNOWN, and WHERE only keeps TRUE rows. |
| Does `NOT NULL` reject an empty title `''`? | No. You need a `CHECK` for blank text. |
| Why not use email as the primary key? | Emails change, and every foreign key pointing at it would have to change too. Make it UNIQUE instead. |
| Name the three anomalies caused by duplicated data. | Update, Insert, Delete. |
| Why are books and copies separate tables? | A title is one fact. Each physical copy has its own status, so you need to know which copy is out. |
| Why can't WHERE filter on `SUM(...)`? | WHERE runs before grouping, so the sums don't exist yet. Use HAVING. |
| Does creating an index guarantee it gets used? | No. The planner picks the plan it estimates is cheapest. Check with EXPLAIN. |
| What's the difference between EXPLAIN and EXPLAIN ANALYZE? | EXPLAIN only plans. EXPLAIN ANALYZE actually runs the query and shows real numbers. |
| Can ROLLBACK undo an LLM call or a sent email? | No. It only undoes uncommitted database work. Use an outbox and idempotency keys. |
| What's the most common Alembic mistake? | Not wiring `env.py` to your models, so autogenerate writes an empty migration. |

</details>

---

**Team rules that apply this week:**
- **Explain before merge:** walk through your PR without looking at the screen.
- **Break it on purpose:** every Friday build includes a rejected insert, a rollback or a plan comparison.
- **Trade-offs in every answer.**
- **Fictional data only.**
