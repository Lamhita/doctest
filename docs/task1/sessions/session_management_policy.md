# **Session Management Policy**

## **Overview**

Session management policies define how the system controls **user sessions, operation limits, and enforcement mechanisms**. These policies are essential for:

- **Security & fraud prevention** → Protecting the system from abuse.
- **Resource management** → Ensuring fair usage across all users.
- **User experience** → Encouraging users to complete verification for a better experience.

The **session management approach differs by user role**:

- **Guest users** → Subject to **strict, system-wide restrictions** to **prevent abuse and drive KYC verification**.
- **Basic users** → Have **more flexible, partner-defined restrictions**, as they are **KYC-verified and lower risk**.

This section explains **why these differences exist** and the **rationale behind enforcement mechanisms**.

---

## **Why Guest Users Have Stricter System-Wide Restrictions**

Guest users are **unverified and potentially anonymous**, which presents **higher security risks**, such as:

- **Fraud & abuse prevention** → Limits **prevent spam account creation and system exploitation**.
- **Encouraging KYC verification** → Strong restrictions **incentivize users to upgrade to Basic status**.
- **Resource protection** → Restricting session length and operation count **prevents excessive system load**.
- **Universal enforcement across all partners** → Ensuring **consistent security measures** for all Guest users.

### **System-Wide Controls for Guest Users**

To address these risks, the system **applies strict, non-configurable policies** to all Guest users:

- **Short session duration** → Sessions expire **after 20 minutes**.
- **Limited operations per day and per week** → **5 daily, 20 weekly**.
- **Automatic transition to Idle State** when limits are exceeded.

> **Guest session policies are fixed across all partners and cannot be customized.**

---

## **Why Basic Users Have More Relaxed, Partner-Defined Restrictions**

Once a user **completes KYC verification**, they **upgrade to Basic status**, which lowers their risk profile. Basic users:

- **Have verified identities** → Reducing risks of fraudulent or anonymous activity.
- **Are more engaged with the platform** → Likely to be legitimate, returning users.
- **May have different needs depending on the partner** → Some partners prefer more flexibility in how restrictions apply.

### **Partner-Defined Controls for Basic Users**

Because Basic users **are verified**, the system **allows partners to define enforcement mechanisms** when limits are exceeded. These may include:

- **Session expiration based on inactivity** → Instead of a fixed 20-minute session, Basic users remain logged in until they are inactive beyond a **partner-defined timeout**.
- **Higher operation limits** → Partners can allow Basic users **20 daily operations, 50 weekly**.
- **Warnings and soft enforcement** → When a Basic user exceeds limits:
  - **The system does not immediately block access**.
  - The user **receives a warning notification**.
  - Some partners may apply **rate-limiting, temporary restrictions, or manual review requirements** before restoring access.
  - If **excessive usage persists**, further action may be taken **based on the partner's policies**.

This **balances security with usability**, allowing partners to **control their own risk management strategies** while maintaining **system-wide integrity**.

---

## **Session Management Flow Diagram**

The following diagram illustrates how session management policies apply to Guest and Basic users:

```plantuml
@startuml
skinparam rectangle {
  BackgroundColor #F5F5F5
  BorderColor #999999
}

[*] --> "Guest Session Active"

"Guest Session Active" --> "Idle State" : Exceeds limits (Auto-enforced)
"Guest Session Active" --> "Session Expired" : 20 min timeout

"Idle State" --> "Login Required" : Wait for reset period

"Basic Session Active" --> "Warning Issued" : Exceeds limits
"Warning Issued" --> "Restricted Access" : Partner-defined enforcement
"Restricted Access" --> "Session Continues" : Partial access restored
"Restricted Access" --> "Idle State" : If excessive usage persists (Partner-defined)

"Basic Session Active" --> "Session Expired" : Partner-defined timeout

@enduml
```

---

## **Summary**

The **difference in session management between Guest and Basic users** is based on:

| **Factor**                     | **Guest Users** (System-Wide) | **Basic Users** (Partner-Defined) |
|---------------------------------|--------------------------------|-----------------------------------|
| **Session Expiration**          | **20 min per session**        | **Expires on inactivity (partner-defined)** |
| **Operation Limits**            | **5 per day, 20 per week**    | **20 per day, 50 per week** |
| **Exceeding Limits Consequence** | **Idle State (No access until reset)** | **Warning or limited enforcement (Partner-defined policies apply)** |
| **Customization**               | **Fixed across all partners** | **Partners control restrictions** |

The system's session management policies are designed to:

✅ **Maintain security** for unverified users while allowing verified users more flexibility.  
✅ **Encourage user conversion** by nudging Guest users toward KYC completion.  
✅ **Give partners control** over restrictions applied to their verified users.  
✅ **Ensure consistency** by keeping Guest restrictions **global** and Basic restrictions **partner-specific**.  

---

## **Next Steps**

The following sections provide more details on how these policies are enforced:

- [Guest Session Management](../sessions/guest_session_management.md)  
- [Basic Session Management](../sessions/basic_session_management.md)  
