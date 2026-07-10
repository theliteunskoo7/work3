# Environment Summary
Last updated: 2026-07-10 02:45:20

1. **Gravity-Driven Descent**: Gravity provides continuous downward acceleration, increasing the magnitude of negative $y\_vel$ throughout the descent.

2. **Main Engine Vertical Control**: Action 2 is the primary mechanism for managing $y\_vel$; the lander is capable of achieving positive $y\_vel$ if the main engine thrust exceeds gravitational acceleration.

3. **Angular-Angular Velocity Feedback Loop**: A non-zero `angle` creates a rotational state that requires active torque to stabilize; without intervention, the tilt can become self-reinforcing.

4. **Main Engine Thrust Vector Coupling**: When the lander is at a non-zero `angle`, the thrust from Action 2 is vectorially distributed, contributing simultaneously to vertical lift ($y\_vel$), horizontal translation ($x\_vel$), and angular acceleration (`ang_vel`).

5. **Orientation-Dependent Side Engine Translation**: Actions 1 and 3 provide torque to manipulate `angle` and `ang_vel`, but they also exert direct translational forces in both $x$ and $y$ directions, with the direction of translation being strictly dependent on the lander's current `angle`.

6. **Lateral Momentum Persistence**: Establishing leg contact does not immediately nullify horizontal velocity; the lander can maintain significant lateral translation ($x\_vel$) and undergo sustained "skidding" while in a contact state.

7. **Torque-Momentum Competition**: The effectiveness of corrective side-engine actions is limited by the current magnitude of `ang_vel`; if angular momentum is too high, the available torque from Actions 1 or 3 may be insufficient to reverse or halt the rotation.

8. **Vertical Control Authority Degradation**: As the absolute value of `angle` increases, the effective vertical component of the main engine's thrust decreases, diverting more power into horizontal and angular acceleration.

9. **Contact-Velocity Penalty Coupling**: High magnitudes of $x\_vel$ or $y\_vel$ during contact transitions ($0.0 \leftrightarrow 1.0$) or while in a sustained contact state trigger severe negative rewards, penalizing "hard" or "sliding" landings.

10. **Post-Contact Engine Instability**: Achieving leg contact can yield positive rewards, but the lander enters a volatile state where $y\_pos$ can become negative (ground penetration). In this state, applying any engine thrust (Actions 1, 2, or 3) while `angle` or `ang_vel` are non-zero is highly likely to trigger a terminal failure (-100 reward) via rapid rotational tip-over.