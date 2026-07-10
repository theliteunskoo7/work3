# Environment Summary
Last updated: 2026-07-10 12:55:57

1. Main engine (Action 2) provides vertical thrust to counteract downward vertical velocity (`y_vel`).
2. Side engines (Actions 1 and 3) provide torque to control orientation (`angle`) and angular velocity (`ang_vel`).
3. The torque applied by side engines is orientation-dependent, meaning the sign of the resulting change in `ang_vel` depends on the current `angle`.
4. Leg contact is a binary state for each leg; contact can be asymmetric (only one leg at 1.0) or symmetric (both legs at 1.0).
5. Successful landings require the simultaneous minimization of `y_vel`, `ang_vel`, and `angle` at the moment of contact.
6. The episode can continue after the initial leg contact is detected, but high velocities during this phase trigger severe negative rewards.
7. Horizontal velocity (`x_vel`) drives lateral movement across the landing area.
8. Main engine thrust (Action 2) induces secondary angular velocity (`ang_vel`) whenever the lander's `angle` is non-zero.
9. High-magnitude negative rewards are strongly associated with non-zero `ang_vel` or `y_vel` during any period where `left_leg_contact` or `right_leg_contact` is 1.0.
10. Engine-applied actions immediately influence the subsequent linear and angular velocities in the next state.