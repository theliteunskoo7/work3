# Environment Summary
Last updated: 2026-07-06 14:22:16

1. **Main Engine (Action 2) Multidimensionality**: Action 2 serves as the primary regulator for `y_pos` and `y_vel`, but its application is non-linearly coupled with the lander's orientation, inducing significant torque that alters both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal momentum but simultaneously induce rotation, acting as a double-edged tool for stability.
4. **Hierarchical Contact State Transitions**: The environment tracks contact through a sequence of states: airborne ($0,0$), single-leg contact ($1,0$ or $0,1$), and dual-leg contact ($1,1$).
5. **High-Magnitude Transition Rewards**: Significant positive rewards are triggered by transitioning into a contact state (e.g., moving from airborne to single-leg contact), with rewards observed as high as ~13.5.
6. **Severe Contact Loss Penalty**: Transitioning from a higher contact state (such as dual-leg $1,1$) to a lesser contact state (such as single-leg $1,0$ or $0,1$) triggers massive negative rewards.
7. **Low-Altitude Lateral Destabilization**: Applying lateral engines (Actions 1 or 3) while a leg is in contact or at very low altitude can induce extreme, catastrophic spikes in `ang_vel`, leading to rapid rotational divergence.
8. **Persistent Post-Landing Kinetic Oscillations**: Reaching a dual-leg contact state ($1,1$) does not result in a static equilibrium; the lander experiences continuous, non-dampened oscillations in `x_pos`, `y_pos`, `angle`, and `ang_vel` that persist for the remainder of the episode.
9. **Descent Velocity-Induced Instability**: High-magnitude downward `y_vel` (e.g., $|y\_vel| > 1.0$) during the approach to or during contact states is a critical precursor to terminal failure.
10. **Terminal Ground Collision Mechanics**: A massive terminal penalty (-100) is triggered when `y_pos` falls below zero, even if a leg contact state is currently active.