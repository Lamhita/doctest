# Session Management Overview

## Introduction

The system enforces role-based session policies to ensure security, resource efficiency, and compliance. Session management controls:

- Session expiration rules – When and how sessions end.
- Operation limits – The number of actions a user can perform.
- Enforcement mechanisms – How the system responds when limits are exceeded.

## Guest vs. Basic User Sessions

| Factor                         | Guest Users (System-Wide)  | Basic Users (Partner-Defined) |
|--------------------------------|---------------------------|--------------------------------|
| Session Expiration            | 20 min per session        | Expires on inactivity (partner-defined) |
| Operation Limits              | 5 per day, 20 per week    | 20 per day, 50 per week |
| Exceeding Limits Consequence  | `idle` user state (No access until reset) | `suspended` subscription state (partner-defined criteria) |
| Customization                 | Fixed across all partners | Partners control restrictions |

## How Partners Influence Basic User Sessions

- Unlike Guest users, who follow system-wide rules, partners can define:
    - Custom session expiration settings.
    - Enforcement actions when limits are exceeded.
    - Extended session benefits for subscribed users.

For detailed policies, see:

- [Guest Session Management](../sessions/guest_session_management.md)
- [Basic Session Management](../sessions/basic_session_management.md)

---

© 2025 CompanyName. Internal use only.
