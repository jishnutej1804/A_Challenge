\# Day 24 — Web Development Core Concepts



\*\*Date:\*\* 2026-10-24  

\*\*Topics:\*\* JavaScript Event Loop, Promises, REST APIs, HTTP Status Codes  



\---



\## 1. JavaScript Event Loop



JavaScript executes synchronous code on a single call stack. The event loop coordinates asynchronous callbacks between runtime APIs and task queues.



\* \*\*Call stack:\*\* Executes currently running functions.

\* \*\*Web APIs / Runtime APIs:\*\* Handle operations such as timers, DOM events, and network requests.

\* \*\*Macrotask (Task) queue:\*\* Holds callbacks from sources like `setTimeout`, `setInterval`, and UI events.

\* \*\*Microtask queue:\*\* Holds Promise reactions (`.then()`, `.catch()`, `.finally()`) and `queueMicrotask()` callbacks.



\### Execution Order

1\. Run all synchronous code on the call stack until it is empty.

2\. Drain the entire microtask queue.

3\. Pick the next task from the macrotask queue, execute it, and repeat.



> \*\*Note:\*\* Microtasks queued by other microtasks are processed before moving to the next macrotask, provided the microtask queue continues to be drained.



\### Example



```javascript

console.log("A");



setTimeout(() => console.log("B"), 0);



Promise.resolve().then(() => console.log("C"));



console.log("D");

```



\*\*Output:\*\*

```text

A

D

C

B

```



\*\*Why?\*\*

\* `A` and `D` run synchronously.

\* The Promise callback runs as a \*\*microtask\*\* immediately after the synchronous stack clears.

\* The timer callback runs in the \*\*macrotask queue\*\* in a subsequent tick.

\* A zero-millisecond timer (`setTimeout(..., 0)`) queues a task; it does not execute immediately.



\---



\## 2. Promises \& Asynchronous JavaScript



A `Promise` represents the eventual completion (or failure) of an asynchronous operation and its resulting value.



\### States

\* `pending`: Initial state, neither fulfilled nor rejected.

\* `fulfilled`: The operation completed successfully.

\* `rejected`: The operation failed.



\### Core Methods

\* `.then(onFulfilled, onRejected)`: Handles fulfillment and enables chaining.

\* `.catch(onRejected)`: Handles rejections/errors.

\* `.finally(onFinally)`: Runs after settlement, regardless of outcome.



\### Fetch Example



```javascript

fetch("/api/users")

&#x20; .then(response => {

&#x20;   if (!response.ok) {

&#x20;     throw new Error(`HTTP error: ${response.status}`);

&#x20;   }

&#x20;   return response.json();

&#x20; })

&#x20; .then(users => console.log(users))

&#x20; .catch(error => console.error("Request failed:", error))

&#x20; .finally(() => console.log("Request finished"));

```



> \*\*Important:\*\* `fetch()` only rejects on network failures or blocked requests. It does \*\*not\*\* reject on HTTP error statuses (like `404` or `500`). Always verify `response.ok` or `response.status`.



\### Async / Await



`async` functions implicitly return a Promise. The `await` keyword pauses execution inside the async function until the Promise settles, without blocking the main browser thread.



```javascript

async function loadUsers() {

&#x20; try {

&#x20;   const response = await fetch("/api/users");



&#x20;   if (!response.ok) {

&#x20;     throw new Error(`HTTP error: ${response.status}`);

&#x20;   }



&#x20;   return await response.json();

&#x20; } catch (error) {

&#x20;   console.error("Unable to load users:", error);

&#x20;   throw error;

&#x20; }

}

```



\---



\## 3. REST API Conventions



Representational State Transfer (REST) is an architectural style for networked systems. RESTful APIs expose resources via standard URIs and use HTTP methods to denote actions.



\### HTTP Methods



| Method | Typical Purpose | Example |

| :--- | :--- | :--- |

| `GET` | Retrieve a resource representation | `GET /api/users` |

| `POST` | Create a new resource or submit an operation | `POST /api/users` |

| `PUT` | Replace an entire resource representation | `PUT /api/users/42` |

| `PATCH` | Apply partial modifications to a resource | `PATCH /api/users/42` |

| `DELETE` | Remove a resource | `DELETE /api/users/42` |



\### Best Practices

\* \*\*Use nouns for resource paths:\*\* Favor `/api/users` over `/api/getUsers`.

\* \*\*Resource identification:\*\* Use consistent identifiers (e.g., `/api/users/42`).

\* \*\*Plural naming:\*\* Keep collection endpoints consistent (e.g., `/items`, `/orders`).

\* \*\*Statelessness:\*\* Each request must carry all the context required for processing.

\* \*\*Payload formats:\*\* Standardize on formats like JSON (`application/json`).

\* \*\*Security:\*\* Protect sensitive routes using standard authorization headers.



\### Sample Request \& Response



\*\*Request:\*\*

```http

GET /api/users/42 HTTP/1.1

Host: example.com

Accept: application/json

```



\*\*Response:\*\*

```http

HTTP/1.1 200 OK

Content-Type: application/json



{

&#x20; "id": 42,

&#x20; "name": "Alex"

}

```



\---



\## 4. HTTP Status Codes



\### 2xx — Success



| Code | Status | Typical Use |

| :--- | :--- | :--- |

| \*\*200\*\* | OK | Standard successful response for `GET`, `PUT`, or `PATCH`. |

| \*\*201\*\* | Created | Resource successfully created (common response to `POST`). |

| \*\*202\*\* | Accepted | Request accepted for asynchronous processing. |

| \*\*204\*\* | No Content | Successful operation with no return payload (common for `DELETE`). |



\### 3xx — Redirection \& Caching



| Code | Status | Meaning |

| :--- | :--- | :--- |

| \*\*301\*\* | Moved Permanently | Target resource assigned a new permanent URI. |

| \*\*302\*\* | Found | Temporary redirect. |

| \*\*304\*\* | Not Modified | Client can reuse its cached representation. |



\### 4xx — Client Errors



| Code | Status | Meaning |

| :--- | :--- | :--- |

| \*\*400\*\* | Bad Request | Malformed syntax or invalid request payload. |

| \*\*401\*\* | Unauthorized | Authentication is missing or invalid. |

| \*\*403\*\* | Forbidden | Server understood credentials, but access is refused. |

| \*\*404\*\* | Not Found | Target resource does not exist. |

| \*\*405\*\* | Method Not Allowed | Request HTTP method is not supported for this URI. |

| \*\*409\*\* | Conflict | Request conflicts with current state of the resource. |

| \*\*415\*\* | Unsupported Media Type | Request payload format is not supported. |

| \*\*422\*\* | Unprocessable Content | Syntax is valid, but instructions cannot be processed. |

| \*\*429\*\* | Too Many Requests | Rate limit exceeded. |



> \*\*Key Distinction:\*\* `401 Unauthorized` means unauthenticated; `403 Forbidden` means authenticated but lacking permission.



\### 5xx — Server Errors



| Code | Status | Meaning |

| :--- | :--- | :--- |

| \*\*500\*\* | Internal Server Error | Generic server failure. |

| \*\*501\*\* | Not Implemented | Server lacks the ability to fulfill the request. |

| \*\*502\*\* | Bad Gateway | Invalid response received from an upstream gateway/proxy. |

| \*\*503\*\* | Service Unavailable | Server is temporarily overloaded or down for maintenance. |

| \*\*504\*\* | Gateway Timeout | Upstream server failed to respond in time. |



\---



\## 5. Quick Revision Flashcards



\* \*\*Q: What runs first, synchronous code or Promise callbacks?\*\*  

&#x20; \*\*A:\*\* Synchronous code executes first on the call stack; Promise callbacks execute afterward from the microtask queue.



\* \*\*Q: Is `setTimeout(callback, 0)` immediate?\*\*  

&#x20; \*\*A:\*\* No. It schedules a callback in the macrotask queue, running only after the current stack and all microtasks clear.



\* \*\*Q: Does `fetch()` reject on an HTTP 404 response?\*\*  

&#x20; \*\*A:\*\* No. `fetch()` only rejects on network failures. Check `response.ok` or `response.status`.



\* \*\*Q: What is the primary difference between `PUT` and `PATCH`?\*\*  

&#x20; \*\*A:\*\* `PUT` replaces the entire target resource; `PATCH` applies partial modifications.



\* \*\*Q: Which status code indicates successful resource creation?\*\*  

&#x20; \*\*A:\*\* `201 Created`.



\* \*\*Q: What is the difference between status codes 401 and 403?\*\*  

&#x20; \*\*A:\*\* `401` relates to authentication identity; `403` indicates an authorized client lacks sufficient permission.



\* \*\*Q: What does a 429 status code signify?\*\*  

&#x20; \*\*A:\*\* Too Many Requests (rate limiting).



\* \*\*Q: What does statelessness mean in REST architecture?\*\*  

&#x20; \*\*A:\*\* Every request must contain all necessary authentication and context data; the server stores no session state between calls.



\---



\## 6. Day 24 Completion Checklist



\- \[ ] Explain synchronous execution, microtasks, and macrotasks.

\- \[ ] Predict the output of an Event Loop code sample.

\- \[ ] Explain Promise states and chaining.

\- \[ ] Implement `async`/`await` with proper `try/catch` and `fetch()` error handling.

\- \[ ] Map RESTful HTTP methods to standard CRUD operations.

\- \[ ] Recall core `2xx`, `3xx`, `4xx`, and `5xx` status codes.

\- \[ ] Save this revision note to the study repository.

\- \[ ] Update the October progress tracker.

\- \[ ] Commit and push the Day 24 work.



> \*\*Key Takeaway:\*\* Understand execution order in the event loop, handle both network and HTTP application errors explicitly, and structure REST APIs around clear nouns, standard methods, and accurate status codes.

