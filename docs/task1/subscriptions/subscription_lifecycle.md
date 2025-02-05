# **Subscription Lifecycle**

## **Overview**

The **Subscription Lifecycle** defines how users **subscribe to, modify, and cancel** subscription plans. Each partner can configure **plan availability, transition rules, and enforcement policies**, but the **core lifecycle states** are **system-wide and consistent**.

Subscription plans directly impact **user role eligibility** and **available features**. When a user **subscribes, upgrades, or cancels**, their subscription status changes accordingly.

---

## **Subscription States**

Each subscription follows a **state-driven process**, ensuring **proper validation and enforcement**. The possible states are:

| **State**     | **Description** |
|--------------|----------------|
| `unsigned`   | The user has **no active subscription**. |
| `signing`    | The user has **initiated a subscription** but is **awaiting confirmation**. |
| `signed`     | The subscription is **active**, and the user has full access to the plan's features. |
| `suspended`  | The subscription is **temporarily inactive** due to **payment issues, policy violations, or admin actions**. |

- **All Basic, Advanced, and Company users start in the `unsigned` state unless they already have an active subscription.**
- **Guest users are not eligible for subscriptions until they complete KYC and upgrade to Basic.**
- **Once a user subscribes**, they enter the `signing` state.
- **If confirmation succeeds**, the subscription transitions to `signed`.
- **If issues arise (e.g., payment failure, fraud detection, or admin suspension),** the subscription may enter `suspended`.

---

## **Subscription Flow**

The diagram below illustrates how users transition between subscription states.

```plantuml
@startuml
skinparam rectangle {
  BackgroundColor #F5F5F5
  BorderColor #999999
}

[*] --> "unsigned"

"unsigned" --> "signing" : User subscribes to a plan
"signing" --> "signed" : Subscription confirmed
"signing" --> "unsigned" : Subscription request failed / cancelled
"signed" --> "suspended" : Subscription suspended (e.g., payment failure)
"signed" --> "unsigned" : User cancels subscription
"suspended" --> "signed" : Issue resolved, subscription restored
"suspended" --> "unsigned" : Subscription fully terminated

@enduml
```

---

## **Subscription Confirmation (`signing → signed`)**

When a user **subscribes to a plan**, they transition to `signing` until the subscription is **validated and confirmed**. 

- The confirmation process may include:
  - **Payment verification** (if required by the partner).
  - **Manual approval or automated processing**.
  - **Fraud prevention checks**.
- If **successful**, the user transitions to `signed`.
- If **rejected**, the user **returns to `unsigned`**.

> **Note:** Partners may define additional conditions before a subscription is confirmed.

---

## **Subscription Suspension (`signed → suspended`)**

A subscription may enter the **`suspended` state** if any of the following occur:

- **Payment failure** (for paid plans).
- **Policy violations** (fraud detection, abuse, etc.).
- **Manual suspension by an admin**.
- **Partner-defined restrictions** (e.g., exceeding plan limits).

> While suspended, the user **loses access to subscription-based features** until the issue is resolved.

### **Restoring a Suspended Subscription (`suspended → signed`)**
- **If the issue is resolved** (e.g., payment is completed), the subscription **returns to `signed`**.
- **If not resolved within a partner-defined period**, the subscription **transitions to `unsigned`**.

---

## **Subscription Cancellation (`signed → unsigned`)**

A user may **cancel their subscription**, resulting in a transition to `unsigned`.

- **For immediate cancellations**, access is revoked **instantly**.
- **For scheduled cancellations**, the user retains access **until the end of the billing period**.
- **If a user downgrades to a role that does not support the plan**, their subscription is also canceled.

---

## **Downgrades & Subscription Impact**

Subscription plans are **mapped to user roles**. When a user **changes roles**, their subscription status may be affected:

| **Role Change**                  | **Subscription Impact** |
|----------------------------------|------------------------|
| **Basic → Advanced**  | May gain access to **additional plans**. |
| **Advanced → Basic**  | May lose access to **previously available plans**. |
| **Downgrade to Guest/Admin** | **Subscription is canceled** (forced transition to `unsigned`). |

---

## **Summary**

The **Subscription Lifecycle** ensures a **structured, enforceable process** for managing user subscriptions. 

- **Users transition between `unsigned`, `signing`, `signed`, and `suspended` states.**
- **Subscription confirmation requires validation (e.g., payment processing, approval).**
- **Suspensions occur due to payment failures, policy violations, or manual admin actions.**
- **Cancellations return the user to `unsigned`.**
- **Role changes can affect subscription eligibility.**

For more details on subscription availability, see:

- [Plan Availability & Partner Restrictions](../subscriptions/plan-restrictions.md)
