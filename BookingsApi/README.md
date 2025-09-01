# BookingsAPI - DI & DRY Approach

- We use _Dependency Injection_ (DI) to provide services and repositories via interfaces (`IBookingService`, `IBookingRepository`).
- Services and repositories are registered in `Program.cs` and injected where needed, making the code flexible and testable.
- Controllers now depend on interfaces, not concrete classes, for loose coupling.
- All logic for checking booking overlap is centralized in `BookingService` (DRY).
- This structure makes the API easy to maintain, extend, and test.
