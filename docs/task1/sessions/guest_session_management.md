# Guest Session Management

## Overview

Guest users operate under system-wide session policies to ensure security, prevent abuse, and encourage KYC verification. These restrictions apply uniformly across all partners and cannot be modified.

The system enforces session duration limits, operation quotas, and idle state enforcement to:

- Prevent fraudulent or anonymous misuse of system resources.  
- Encourage users to verify their identities through KYC.  
- Ensure fair resource distribution among guest users.  

Because Guest users lack verified identities, these controls serve as protective measures for both the system and legitimate users.

---

## Session Duration Limit

- Each session for a Guest user is limited to 20 minutes.  
- After 20 minutes, the session automatically expires, requiring the user to log in again.  
- This prevents unverified users from maintaining persistent access, ensuring periodic re-authentication.  

---

## Operation Quotas

Guest users are subject to strict operation quotas:

- Maximum 5 operations per day.  
- Maximum 20 operations in a rolling 7-day period.  
- Operations include API requests, transactions, and key system interactions.  

If a Guest user exceeds any of these quotas, they immediately transition into `idle` state.

---

## Idle State Enforcement

Idle State is a system-wide restriction applied when a Guest user exceeds session or operation quotas:

- The user is blocked from further actions until the next reset period.  
- They are prompted to complete KYC verification to upgrade to `basic` and regain full access.  
- Idle State cannot be bypassed unless the user either waits for the reset period or upgrades to `basic`.  

---

## Guest Session Flow Diagram

The following diagram illustrates the lifecycle of a Guest session:

```plantuml
@startuml
skinparam rectangle {
  BackgroundColor #F5F5F5
  BorderColor #999999
}

start
:Guest user logs in;
:Session starts (Max 20 min);

repeat
    if (Session expires?) then (Yes)
        :User must reauthenticate;
        stop
        note left: Must log in again
    else (No)
        :User performs operations;
        if (Daily/Weekly quota exceeded?) then (Yes)
            :User transitions to idle state;
            :Prompt for KYC upgrade;
            stop
            note left: Idle State (Quota Exceeded)
        else (No)
            :Session continues;
        endif
    endif
repeat while (Session continues)

@enduml
```

---

## Enforcing KYC Completion

The Guest session model is intentionally restrictive to drive users toward KYC verification:

- Frequent session expirations encourage users to verify their identity and upgrade to `basic`.  
- Operation quotas prevent `guest` users from overusing the system while allowing limited interaction.  
- Idle State enforces a strong conversion incentive—users must either wait for quotas to reset or complete KYC to continue.  

By applying these policies, the system ensures that `guest` users do not remain unverified indefinitely.

---

## Related Sections

- [Basic Session Management](basic_session_management.md)
- [Session Management Overview](session_management_overview.md)

---

© 2025 CompanyName. Internal use only.
