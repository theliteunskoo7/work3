# Environment Summary
Last updated: 2026-07-02 13:16:17

1. Main engine (Action 2) is the primary tool for managing altitude (`y_pos`) and vertical descent velocity (`y_vel`).
2. Side engines (Actions 1 and 3) provide lateral force for horizontal movement (`x_pos`, `x_vel`) and torque for orientation control (`angle`, `ang_vel`).
3. The application of the main engine (Action 2) at non-zero `angle` generates significant rotational torque, which can exacerbate `ang_vel` and potentially make rotation unarrestable during descent.
4. The transition of a single leg from 0.0 to 1.0 (asymmetrical contact) triggers an immediate, high-magnitude spike in angular velocity (`ang_vel`).
5. The interval between the first leg making contact and the second leg establishing contact is a phase of extreme instability characterized by rapid, continuous acceleration of `ang_vel`.
6. The rotational impulse during contact is compounded by both the lander's `angle` and its pre-existing `ang_vel` at the moment of impact.
7. Dual-leg contact (1.0, 1.0) establishes a "grounded" state, but stability in this state is highly dependent on the ability to immediately arrest `ang_vel` using side engines.
8. If `ang_vel` is high at the moment of the second leg contact, the resulting rotational impulse can cause the lander to bounce or tip, even if both legs are technically engaged.
9. Leg contact is not a permanent state; significant rotational or vertical kinetic energy can cause a leg to transition from 1.0 back to 0.0, leading to a bouncing or tipping effect.
10. Maintaining stable dual-leg contact requires continuous management of `ang_vel` to prevent the buildup of energy that triggers leg-rebound events (transitions from 1.0 back to 0.0).