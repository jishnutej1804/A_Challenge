# ⚡ A_Challenge

### Learn. Build. Solve. Improve. Repeat.

> A personal engineering challenge to build consistency, strengthen technical skills, solve problems, and create practical software — one day at a time.

---

## 🎯 About

**A_Challenge** is a daily learning and development journey that began on **October 1, 2026**.

The objective is not simply to maintain a GitHub contribution graph. It is to make meaningful progress through consistent practice, hands-on development, experimentation, testing, and documentation.

Throughout October, the challenge combined Data Structures and Algorithms, programming, databases, data analysis, web development, system design, and project deployment.

**The goal: turn daily learning into demonstrable engineering progress.**

---

## 🚀 October 2026 — Engineering Milestone

<details>
<summary><strong>October retrospective</strong></summary>

October focused on three major areas:

1. Strengthening problem-solving skills through DSA.
2. Building and improving EcoPulse, a sustainability-focused web application.
3. Developing practical knowledge of databases, data analysis, web technologies, and software deployment.

### Key outcomes

| Area | October outcome |
|---|---|
| Data Structures & Algorithms | Practised arrays, strings, two pointers, stacks, linked lists, binary search, trees, graphs, and dynamic programming |
| Web Development | Built and improved the EcoPulse frontend using HTML, CSS, and JavaScript |
| Backend Development | Integrated an Express backend with environmental data endpoints |
| SQL / DBMS | Designed database schemas and practised aggregation, joins, ranking, and window functions |
| Data Analysis | Used Python and Pandas for exploratory analysis and emission summaries |
| Machine Learning | Studied decision trees, random forests, impurity measures, and feature scaling |
| Web Fundamentals | Revised the JavaScript event loop, promises, REST, and HTTP status codes |
| Git & GitHub | Maintained a structured workflow using commits, repository documentation, and version control |
| Deployment | Deployed EcoPulse to Vercel and verified its production endpoints |

### Problem-solving practice

The DSA work covered a progression of common algorithmic patterns:

- **Arrays and Hashing:** Two Sum, Valid Anagram.
- **Two Pointers:** Valid Palindrome, Two Sum II.
- **Stacks:** Valid Parentheses, Queue using Stacks.
- **Linked Lists:** Reverse Linked List.
- **Binary Search:** Binary Search, Search Insert Position, Search in Rotated Sorted Array.
- **Trees:** DFS traversals, Maximum Depth, Invert Binary Tree, Validate Binary Search Tree.
- **Graphs:** Graph representation and BFS path finding.
- **Sorting and Greedy:** Merge Intervals, Maximum Subarray using Kadane's Algorithm.
- **Dynamic Programming:** Climbing Stairs.

The practice emphasised algorithm selection, boundary conditions, tracing, time complexity, and space complexity.

### EcoPulse — Sustainability Tracker

EcoPulse was developed as the main project workstream during the challenge.

**Project capabilities and engineering work:**

- Responsive sustainability-focused dashboard interface.
- Dark and light theme support.
- Carbon-emission calculation and saved-result functionality.
- Dashboard card improvements and responsive styling.
- SQL schema design and analytical queries.
- Python/Pandas-based emission analysis.
- Environmental data integration through the OpenWeather API.
- Express backend with input validation and error handling.
- Production deployment through Vercel.

**Live application:** https://ecopulse-tracker.vercel.app/

**Backend health endpoint:** https://ecopulse-tracker.vercel.app/api/health

**Production verification:** The homepage, styling, navigation, theme toggle, health endpoint, and air-quality API were tested after deployment.

### Database and data analysis

Database practice included:

- Relational table design and constraints.
- SQL `SELECT`, `INSERT`, and aggregation.
- `SUM()` and `GROUP BY`.
- `INNER JOIN` and `LEFT JOIN`.
- Ranking and window functions.
- Carbon-emission summaries by category and user.

Python and Pandas were used to explore sample sustainability data, calculate summary statistics, and analyse category-wise emissions.

### Technical learning

Additional study covered:

- Decision Trees and Random Forests.
- Gini impurity and entropy.
- Bagging and feature scaling.
- JavaScript event loop and asynchronous execution.
- Promises and microtasks versus macrotasks.
- REST concepts and HTTP status codes.
- BFS, DFS, recursion, and algorithmic complexity.

</details>

---

## 🌱 Main Project — EcoPulse

<details>
<summary><strong>Project overview and deployment</strong></summary>

**EcoPulse** is a sustainability-focused web application developed as part of A_Challenge.

| Component | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Node.js, Express |
| Environmental data | OpenWeather API |
| Database work | SQL / SQLite |
| Data analysis | Python, Pandas |
| Deployment | Vercel |
| Version control | Git and GitHub |

### Architecture

```text
                  EcoPulse
                      |
          +-----------+-----------+
          |                       |
       Frontend                 Backend
     HTML/CSS/JS             Node.js/Express
          |                       |
          |              +--------+--------+
          |              |                 |
       Dashboard       Health API      Air Quality API
          |                                |
          |                          OpenWeather API
          |
     User Interface
```

### Production links

- **Live application:** [ecopulse-tracker.vercel.app](https://ecopulse-tracker.vercel.app/)
- **API health:** [Check API status](https://ecopulse-tracker.vercel.app/api/health)

</details>

---

## 🧠 Learning Goals

| Area | Focus |
|---|---|
| DSA | Algorithms, problem-solving patterns, and complexity analysis |
| Programming | Python and JavaScript |
| SQL / DBMS | Database design, queries, joins, and analytical functions |
| AI / Data | Machine learning fundamentals and data analysis |
| Web Development | Frontend, backend, and API integration |
| Projects | Practical applications and deployment |
| Git & GitHub | Version control, documentation, and collaboration |

---

## 🗺️ Development Workflow

```text
       📚 LEARN
          ↓
       💻 BUILD
          ↓
       🧪 TEST
          ↓
       🔧 IMPROVE
          ↓
       📤 COMMIT
          ↓
       🚀 DEPLOY
          ↓
       🔁 REPEAT
```

---

## 🏗️ Repository Structure

```text
A_Challenge/
│
├── DSA/
│   ├── Arrays/
│   ├── Strings/
│   ├── Trees/
│   └── Notes/
│
├── Projects/
│   └── EcoPulse/
│       ├── public/
│       │   ├── index.html
│       │   ├── styles.css
│       │   ├── script.js
│       │   └── api/
│       ├── db/
│       │   ├── schema_and_queries.sql
│       │   └── window_functions.sql
│       ├── server.js
│       ├── package.json
│       └── package-lock.json
│
├── analysis/
│   └── carbon_eda.py
│
├── Progress/
│   └── October-2026.md
│
└── README.md
```

---

## 🛠️ Technologies & Tools

- **Languages:** Python, JavaScript, SQL
- **Frontend:** HTML5, CSS3
- **Backend:** Node.js, Express
- **Data Analysis:** Pandas
- **Database:** SQLite / SQL
- **APIs:** OpenWeather API
- **Deployment:** Vercel
- **Version Control:** Git, GitHub

---

## 📊 Progress Tracking

Daily activities, learning outcomes, and milestones are documented in:

**[October 2026 — Daily Progress](Progress/October-2026.md)**

The progress tracker records the work completed throughout the month and serves as a concise engineering log.

---

## 🌟 Key Takeaways

October reinforced several important engineering practices:

- Understanding a problem before writing code.
- Choosing appropriate algorithms and analysing their complexity.
- Testing functionality rather than relying only on visual appearance.
- Connecting frontend applications to backend services and external APIs.
- Structuring databases and analysing data.
- Using Git to track changes and maintain a development history.
- Debugging deployment issues through logs and configuration checks.
- Documenting work so that progress remains understandable and reproducible.

---

## 🌱 Guiding Principle

**Consistency over perfection. Progress over promises.**

One day at a time. One problem at a time. One commit at a time.