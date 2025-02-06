# System Components

The system consists of several key components that provide multi-tenant functionality, user management, session control, and subscription handling. Below is an overview of each component and their interactions.

---

## Partner Management

- Manages onboarding and configuration of partners (providers).  
- Stores partner-specific settings, including:  

  - User roles and feature toggles.  
  - Branding and operational limits.  
  - Subscription plan availability.  
  
- Ensures tenant isolation, preventing one partner’s configuration from affecting another.

---

## User Management

- Maintains user records across multiple partners.  
- Controls roles, statuses, and permissions based on partner-defined policies.  
- Enforces role-based access control (RBAC) for feature restrictions.  
- Tracks user subscription status, including transitions such as `signed` <-> `unsigned`.  
- Synchronizes user status with subscription states through the subscription management service.

---

## Session & Usage Policy Manager

- Monitors active sessions and usage limits.  
- Enforces session expiration policies, including:  
  - Guest session timeout (20-minute limit).  
  - Basic user inactivity timeouts (configurable per partner).  
  - Restricted state enforcement for users exceeding limits.  
- Ensures compliance with partner-specific session rules.

---

## Subscription & Plan Management

- Handles subscription lifecycle events, including:  

  - Plan creation, updates, and deletions.  
  - Subscription initiation and confirmation (`signing → signed`).  
  - Suspension due to non-payment or policy violations.  

- Limits plan availability to specific user roles as defined by the partner.  
- Synchronizes subscription status transitions.  
- Works with user management to update user status based on subscription changes.

---

## KYC & Verification Service

- Provides identity verification for user upgrades from `guest` to `basic` or `advanced`.  
- Integrates with internal and external verification sources.  
- Supports re-verification workflows when required.

---

## Data Storage & Isolation Layer

- Ensures partner data separation using tenant-aware schemas and row-level security (RLS).  
- Prevents data leakage between tenants.  
- Supports multi-region data storage for compliance with local regulations.

---

## Component Interaction Diagram

```plantuml
@startuml

skinparam rectangle {
  BackgroundColor #F5F5F5
  BorderColor #999999
}

actor "Partner Admin" as PA
actor "End User" as EU

rectangle "Partner Management" as PM
rectangle "User Management" as UM
rectangle "Session & Usage Policy Manager" as SM
rectangle "Subscription & Plan Management" as SUB
rectangle "KYC & Verification Service" as KYC
cloud "Data Storage & Isolation Layer" as DS

PA --> PM : Configure partner settings
PM --> UM : Provision partner config
PM --> SUB : Configure available plans

EU --> UM : Register / Log in / Update user profile
EU --> SUB : Subscribe / Manage plans

UM --> SM : Check session constraints & usage
SM --> UM : Session status & rate-limit feedback

SUB --> UM : Update user subscription status
UM --> DS : Store/retrieve user data
SM --> DS : Read/write session & usage data
SUB --> DS : Store subscription plan details

UM --> KYC : Initiate identity checks
KYC --> UM : Verification results

@enduml
```