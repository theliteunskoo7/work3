
---

## 2026-07-02 02:46:40

1. **Gravity-Driven Descent**: Gravity causes a continuous increase in downward vertical velocity ($y\_vel$). The main engine is required to counteract this, but vertical descent often accelerates despite engine use if the lander is not perfectly upright.
2. **Angular-Angular Velocity Coupling**: Any deviation in `angle` from zero tends to generate or exacerbate `ang_vel` (angular velocity), creating a feedback loop where rotational momentum becomes increasingly difficult to arrest as it accumulates.
3. **Horizontal Velocity as a Persistent Threat**: High $|x\_vel|$ is a primary indicator of imminent failure. Even if vertical descent is managed, high horizontal velocity often leads to a crash upon contact.
4. **Main Engine (Action 2) Dual-Role**: While the main engine provides necessary upward thrust to mitigate $y\_vel$, its application at non-zero `angle` values effectively converts vertical lift into horizontal momentum ($x\_vel$) and angular momentum (`ang_vel`).
5. **Side Engine (Action 1 & 3) Functional Constraints**: Side engines are the primary tools for manipulating `angle` and `ang_vel`, but they provide no vertical thrust and no direct horizontal translation correction, meaning they cannot arrest $y\_vel$ or $x\_vel$.
6. **Action 0 (Nothing) Inertia**: Choosing no action allows all existing velocities ($x\_vel, y\_vel, ang\_vel$) and the current `angle` to persist unchecked, allowing gravity and existing momentum to drive the lander toward a terminal state.
7. **The Stability Trade-off**: Attempts to correct `angle` using side engines often result in an uncorrected drift in $y\_vel$ or $x\_vel$, as the engines' primary purpose is angular stabilization rather than translational control.
8. **Angular Momentum Saturation**: If `ang_vel` reaches high magnitudes, the corrective torque from side engines may become insufficient to counteract the rotation, leading to an irrecoverable "death spiral."
9. **Control Authority Degradation**: As the magnitude of `angle` increases, the lander's ability to use the main engine for vertical lift diminishes, as a larger portion of the thrust is diverted into horizontal and angular instability.
10. **Terminal State Sensitivity**: High $x\_vel$, $y\_vel$, or `ang_vel` at the moment of contact (even if the lander is relatively upright) results in a failure state, meaning stabilization must be achieved well before ground contact.

---

## 2026-07-02 02:50:02

1. **Gravity-Driven Descent**: Gravity continuously increases downward vertical velocity ($y\_vel$). The main engine (Action 2) is the only mechanism to counteract this, but its ability to arrest descent is strictly dependent on the lander's orientation (`angle`).

2. **Angular-Angular Velocity Positive Feedback**: There is a strong coupling between `angle` and `ang_vel`. As seen in both episodes, once a deviation in `angle` occurs, `ang_vel` often increases in the same direction, creating a runaway effect where rotational momentum accelerates the tilt.

3. **Horizontal Velocity as a Terminal Threat**: High $|x\_vel|$ is a primary driver of failure. Once horizontal momentum accumulates through side engine use or tilted main engine thrust, it becomes increasingly difficult to arrest before ground contact.

4. **Main Engine (Action 2) Vectoring**: While Action 2 provides upward thrust, applying it at a non-zero `angle` diverts a portion of that thrust into horizontal acceleration ($x\_vel$). This creates a trade-off where fighting gravity can inadvertently increase horizontal drift.

5. **Side Engine (Action 1 & 3) Functional Limits**: Side engines are purely for angular control. They provide no vertical thrust to combat gravity and no direct horizontal thrust to combat $x\_vel$, meaning they cannot correct translational momentum.

6. **The "Runaway Tilt" Phenomenon**: If `angle` and `ang_vel` share the same sign and reach significant magnitudes, the lander enters a state of rapid angular acceleration. In this state, the torque provided by side engines becomes insufficient to arrest the rotation, leading to an unrecoverable tumble.

7. **Control Authority Degradation**: As the `angle` increases, the effective vertical component of the main engine's thrust ($\cos(\text{angle})$) decreases. This causes the lander to descend faster even while the main engine is firing, compounding the difficulty of the landing.

8. **Translational-Rotational Coupling**: Attempts to stabilize `angle` using side engines often result in unintended shifts in $x\_vel$ or $y\_vel$. This makes precise landing difficult, as angular corrections often destabilize the lander's translational trajectory.

9. **Action 0 (Nothing) Inertia**: Selecting no action allows existing $x\_vel$, $y\_vel$, and `ang_vel` to persist. In the presence of gravity and existing angular momentum, this typically leads to a simultaneous increase in descent speed and tilt.

10. **Terminal State Sensitivity**: Failure is frequently caused by high-magnitude $x\_vel$, $y\_vel$, or `ang_vel` at the moment of impact ($y\_pos \le 0$). Successful landing requires achieving low velocities and near-zero `angle` well before the lander reaches the ground.

---

## 2026-07-02 02:54:08

1. **Gravity-Driven Descent**: Gravity continuously increases the downward vertical velocity ($y\_vel$). The main engine (Action 2) is the primary mechanism to counteract this, but its ability to arrest descent is strictly dependent on the lander's orientation (`angle`).

2. **Angular-Angular Velocity Coupling**: There is a strong coupling between `angle` and `ang_vel`. As observed in both episodes, once a deviation in `angle` occurs, `ang_vel` often increases in the same direction, creating a momentum-driven feedback loop.

3. **Horizontal Velocity as a Terminal Threat**: High $|x\_vel|$ is a primary driver of failure. Once horizontal momentum accumulates (as seen in Episode 2's high initial $x\_vel$), it becomes increasingly difficult to arrest before ground contact, even when using the main engine.

4. **Main Engine (Action 2) Thrust Vectoring**: Applying the main engine at a non-zero `angle` decomposes the upward thrust into both vertical and horizontal components. This creates a critical trade-off: fighting gravity (increasing $y\_vel$ upward) while simultaneously increasing horizontal drift ($x\_vel$).

5. **Side Engine (Action 1 & 3) Functional Limits**: Side engines are dedicated purely to angular control (torque). They provide no vertical thrust to combat gravity and no direct horizontal thrust to combat $x\_vel$; they can only influence translation indirectly by changing the `angle` of the main engine's thrust vector.

6. **The "Runaway Tilt" Phenomenon**: If `angle` and `ang_vel` reach high magnitudes, the lander enters an unrecoverable tumble (as seen in Episode 1, Step 94). In this state, the torque provided by side engines becomes insufficient to arrest the rotational momentum.

7. **Control Authority Degradation**: As the `angle` increases, the effective vertical component of the main engine's thrust ($\cos(\text{angle})$) decreases. This causes the lander to descend faster even while the main engine is firing, compounding the difficulty of a controlled landing.

8. **Translational-Rotational Coupling**: Attempts to stabilize `angle` using side engines often result in unintended shifts in $x\_vel$ or $y\_vel$. This necessitates a complex balance where angular corrections must not destabilize the translational trajectory required for a soft touchdown.

9. **Action 0 (Nothing) Inertia**: Selecting no action allows existing $x\_vel$, $y\_vel$, and `ang_vel` to persist. In the presence of gravity and existing angular momentum, Action 0 typically allows descent speed and tilt to reach critical, unrecoverable levels.

10. **Terminal State Sensitivity**: Failure is frequently caused by high-magnitude $x\_vel$, $y\_vel$, or `ang_vel` at the moment of impact ($y\_pos \le 0$). Successful landing requires the simultaneous achievement of low velocities and near-zero `angle` before ground contact.

---

## 2026-07-02 02:59:07

1. **Gravity-Driven Descent**: Gravity provides a constant downward acceleration, necessitating continuous upward thrust to prevent $y\_vel$ from reaching critical descent speeds.

2. **Angular-Angular Velocity Coupling**: Changes in `angle` are inherently coupled with `ang_vel`; once a rotation begins, the resulting momentum creates a feedback loop that requires active torque to arrest.

3. **Horizontal Velocity Persistence**: High $|x\_vel|$ is a primary terminal threat that is difficult to reverse. As seen in Episode 2, significant horizontal momentum can persist and even increase in magnitude despite active control efforts.

4. **Main Engine (Action 2) Thrust Decomposition**: Applying the main engine at a non-zero `angle` decomposes upward thrust into both vertical and horizontal components. This means any attempt to fight gravity while tilted directly contributes to horizontal drift ($x\_vel$).

5. **Side Engine (Action 1 & 3) Functional Limits**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct vertical or horizontal thrust. Their impact on translation ($x\_vel, y\_vel$) is entirely indirect, occurring only by reorienting the main engine's thrust vector.

6. **Angular Dampening vs. Angle Correction**: Side engines can effectively reduce `ang_vel` (e.g., Episode 1, Step 63), but they do not immediately reset the `angle` to zero. The lander can exhibit low rotational velocity while still maintaining a high, problematic tilt.

7. **Control Authority Degradation**: The effective vertical component of the main engine's thrust is scaled by $\cos(\text{angle})$. As the tilt increases, the ability of the main engine to counteract gravity diminishes, causing faster descent.

8. **The Drift-Tilt Feedback Loop**: A dangerous cycle exists where using the main engine to arrest $y\_vel$ while at an angle increases $x\_vel$, which may necessitate angular corrections that further perturb the translational trajectory.

9. **Action 0 (Nothing) Inertia**: Selecting no action allows existing $x\_vel$, $y\_vel$, and `ang_vel` to persist under the influence of gravity, typically leading to unrecoverable descent velocities or uncontrolled rotation.

10. **Terminal State Sensitivity**: Failure is defined by the state at the moment of impact ($y\_pos \le 0$). A successful landing requires the simultaneous minimization of $|x\_vel|$, $|y\_vel|$, and `angle` before ground contact occurs.

---

## 2026-07-02 03:03:57

1. **Gravity-Driven Descent**: Gravity provides a constant downward acceleration, necessitating continuous upward thrust to prevent $y\_vel$ from reaching critical descent speeds.

2. **Angular-Angular Velocity Coupling**: Changes in `angle` are inherently coupled with `ang_vel`; once a rotation begins, the resulting momentum creates a feedback loop that requires active torque to arrest.

3. **Horizontal Velocity Persistence**: High $|x\_vel|$ is a primary terminal threat that is difficult to reverse. As seen in both episodes, horizontal momentum can persist or even change direction based on the tilt and engine application, but is difficult to nullify before impact.

4. **Main Engine (Action 2) Thrust Decomposition**: Applying the main engine at a non-zero `angle` decomposes upward thrust into both vertical and horizontal components. This means any attempt to fight gravity while tilted directly contributes to horizontal drift ($x\_vel$).

5. **Side Engine (Action 1 & 3) Functional Limits**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct vertical or horizontal thrust. Their impact on translation ($x\_vel, y\_vel$) is entirely indirect, occurring only by reorienting the main engine's thrust vector.

6. **Angular Dampening vs. Angle Correction**: Side engines can effectively reduce `ang_vel`, but they do not immediately reset the `angle` to zero. The lander can exhibit low rotational velocity while still maintaining a high, problematic tilt.

7. **Control Authority Degradation**: The effective vertical component of the main engine's thrust is scaled by $\cos(\text{angle})$. As the tilt increases, the ability of the main engine to counteract gravity diminishes, causing faster descent.

8. **The Drift-Tilt Feedback Loop**: A dangerous cycle exists where using the main engine to arrest $y\_vel$ while at an angle increases $x\_vel$, which may necessitate angular corrections that further perturb the translational trajectory.

9. **Critical Descent Velocity Threshold**: There exists a threshold for downward $y\_vel$ beyond which the maximum upward acceleration provided by the main engine is insufficient to counteract gravity. As observed in Episode 2, if $y\_vel$ is sufficiently negative, continuous application of the main engine cannot arrest the descent.

10. **Terminal State Sensitivity**: Failure is defined by the state at the moment of impact ($y\_pos \le 0$). A successful landing requires the simultaneous minimization of $|x\_vel|$, $|y\_vel|$, and `angle` before ground contact occurs.

---

## 2026-07-02 03:07:24

1. **Gravity-Driven Descent**: Gravity provides a constant downward acceleration, necessitating continuous upward thrust to prevent $y\_vel$ from reaching critical descent speeds.

2. **Angular-Angular Velocity Coupling**: Changes in `angle` are inherently coupled with `ang_vel`; once a rotation begins, the resulting momentum creates a feedback loop that requires active torque to arrest.

3. **Horizontal Velocity Persistence**: High $|x\_vel|$ is a primary terminal threat. Horizontal momentum can persist or be redirected, but it is difficult to nullify before ground contact.

4. **Main Engine (Action 2) Directional Vectoring**: The main engine's thrust decomposes into vertical and horizontal components based on the `angle`. A positive `angle` induces negative $x\_vel$ acceleration, while a negative `angle` induces positive $x\_vel$ acceleration.

5. **Side Engine (Action 1 & 3) Functional Limits**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct vertical or horizontal thrust; their impact on translation is entirely indirect via the reorientation of the main engine's thrust vector.

6. **Angular Dampening vs. Angle Correction**: Side engines can effectively reduce `ang_vel` (angular velocity), but they do not immediately reset the `angle` to zero, allowing the lander to maintain a significant tilt even with low rotational speed.

7. **Vertical Control Authority Degradation**: The effective vertical component of the main engine's thrust is scaled by $\cos(\text{angle})$. As the absolute value of the `angle` increases, the capacity of the main engine to counteract gravity diminishes.

8. **The Drift-Tilt Feedback Loop**: A cycle exists where using the main engine to arrest $y\_vel$ while at an angle increases $x\_vel$, which may necessitate angular corrections that further perturb the translational trajectory.

9. **Critical Descent Velocity Threshold**: There exists a threshold for downward $y\_vel$ (observed $\approx 1.4$) beyond which the maximum upward acceleration provided by the main engine is insufficient to counteract gravity and arrest the descent before impact.

10. **Terminal State Sensitivity**: Success is defined by the state at the moment of impact ($y\_pos \le 0$). A successful landing requires the simultaneous minimization of $|x\_vel|$, $|y\_vel|$, and `angle` before ground contact occurs.

---

## 2026-07-02 03:12:47

1. **Gravity-Driven Descent**: Gravity provides a constant downward acceleration, necessitating continuous upward thrust to prevent $y\_vel$ from reaching critical descent speeds.

2. **Angular-Angular Velocity Coupling**: Changes in `angle` are inherently coupled with `ang_vel`; once a rotation begins, the resulting momentum creates a feedback loop that requires active torque to arrest.

3. **Horizontal Velocity Persistence**: High $|x\_vel|$ is a primary terminal threat. Horizontal momentum can persist or be redirected, but it is difficult to nullify before ground contact.

4. **Main Engine (Action 2) Directional Vectoring**: The main engine's thrust decomposes into vertical and horizontal components based on the `angle`. A positive `angle` induces negative $x\_vel$ acceleration, while a negative `angle` induces positive $x\_vel$ acceleration.

5. **Side Engine (Action 1 & 3) Functional Limits**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct vertical or horizontal thrust; their impact on translation is entirely indirect via the reorientation of the main engine's thrust vector.

6. **Angular Dampening vs. Angle Correction**: Side engines can effectively reduce `ang_vel` (angular velocity), but they do not immediately reset the `angle` to zero, allowing the lander to maintain a significant tilt even with low rotational speed.

7. **Vertical Control Authority Degradation**: The effective vertical component of the main engine's thrust is scaled by $\cos(\text{angle})$. As the absolute value of the `angle` increases, the capacity of the main engine to counteract gravity diminishes.

8. **The Drift-Tilt Feedback Loop**: A cycle exists where using the main engine to arrest $y\_vel$ while at an angle increases $x\_vel$, which may necessitate angular corrections that further perturb the translational trajectory.

9. **Multi-Factor Velocity Thresholds**: While $|y\_vel| \approx 1.4$ represents a threshold where vertical arrest via the main engine becomes physically impossible, significant horizontal velocity ($|x\_vel|$) can also drive landing failure even when descent speeds are below this threshold.

10. **Terminal State Stability**: Success is defined by the state at the moment of impact ($y\_pos \le 0$). A successful landing requires the simultaneous minimization of $|x\_vel|$, $|y\_vel|$, and `angle`; failure to nullify horizontal momentum or angular tilt can result in high-velocity impact or asymmetric leg contact.

---

## 2026-07-02 03:16:21

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust to prevent $y\_vel$ from reaching critical descent speeds.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest.

3. **Horizontal Velocity Persistence**: High $|x\_vel|$ is a primary terminal threat; horizontal momentum persists throughout the descent and must be actively nullified before ground contact.

4. **Main Engine (Action 2) Vector Decomposition**: Main engine thrust decomposes into vertical and horizontal components based on `angle`. Increasing $|angle|$ decreases the vertical thrust component ($\cos(\text{angle})$) while increasing the horizontal thrust component.

5. **Side Engine (Action 1 & 3) Indirect Translation**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct translational thrust; their effect on $x\_vel$ and $y\_vel$ is entirely mediated by the reorientation of the main engine's thrust vector.

6. **Angular Dampening vs. Orientation Correction**: Side engines can effectively reduce `ang_vel`, but they do not immediately reset the `angle` to zero, allowing a significant tilt to persist even after the rotational speed has slowed.

7. **Vertical Control Authority Degradation**: The capacity of the main engine to counteract gravity is scaled by $\cos(\text{angle})$; as the absolute value of the `angle` increases, the engine's ability to arrest $y\_vel$ diminishes significantly.

8. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at an angle creates a feedback loop where correcting one velocity component inevitably perturbs the other.

9. **Critical Descent Velocity Threshold**: A $y\_vel$ approaching $\approx -1.4$ represents a critical threshold where the main engine's vertical component is insufficient to counteract gravity and prevent a high-velocity impact.

10. **Terminal State Stability**: Successful landing requires the simultaneous minimization of $|x\_vel|$, $|y\_vel|$, and `angle` at the moment of $y\_pos \le 0$; failure to synchronize these components results in high-velocity impact or asymmetric contact.

---

## 2026-07-02 03:20:43

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust to prevent $y\_vel$ from reaching critical descent speeds.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest.

3. **Horizontal Velocity Persistence**: High $|x\_vel|$ is a primary terminal threat; horizontal momentum persists throughout the descent and must be actively nullified before ground contact.

4. **Main Engine (Action 2) Vector Decomposition**: Main engine thrust decomposes into vertical and horizontal components based on `angle`. Increasing $|angle|$ decreases the vertical thrust component ($\cos(\text{angle})$) while increasing the horizontal thrust component.

5. **Side Engine (Action 1 & 3) Indirect Translation**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct translational thrust; their effect on $x\_vel$ and $y\_vel$ is entirely mediated by the reorientation of the main engine's thrust vector.

6. **Angular Dampening vs. Orientation Correction**: Side engines can effectively reduce `ang_vel`, but they do not immediately reset the `angle` to zero, allowing a significant tilt to persist even after the rotational speed has slowed.

7. **Vertical Control Authority Degradation**: The capacity of the main engine to counteract gravity is scaled by $\cos(\text{angle})$; as the absolute value of the `angle` increases, the engine's ability to arrest $y\_vel$ diminishes significantly.

8. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at an angle creates a feedback loop where correcting one velocity component inevitably perturbs the other.

9. **Asymmetric Landing Instability**: Trajectories indicate that failure is highly correlated with asymmetric leg contact (e.g., `left_leg_contact=0` and `right_leg_contact=1`). This suggests that landing on only one leg causes a loss of stability or tipping, regardless of whether the descent speed is moderate or high.

10. **Multi-Variable Terminal Failure**: Landing success is not solely governed by a $y\_vel$ threshold; while high descent speeds are dangerous, failures also occur at moderate speeds (e.g., $|y\_vel| \approx 0.8$) if the `angle` and leg contact are not simultaneously stabilized, indicating a complex coupling between velocity, orientation, and contact symmetry.

---

## 2026-07-02 03:24:21

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust to prevent $y\_vel$ from reaching critical descent speeds.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest.

3. **Horizontal Velocity Persistence**: High $|x\_vel|$ is a primary terminal threat; horizontal momentum persists throughout the descent and must be actively nullified before ground contact.

4. **Main Engine (Action 2) Vector Decomposition**: Main engine thrust decomposes into vertical and horizontal components based on `angle`. Increasing $|angle|$ decreases the vertical thrust component ($\cos(\text{angle})$) while increasing the horizontal thrust component.

5. **Side Engine (Action 1 & 3) Indirect Translation**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct translational thrust; their effect on $x\_vel$ and $y\_vel$ is entirely mediated by the reorientation of the main engine's thrust vector.

6. **Angular Dampening vs. Orientation Correction**: Side engines can effectively reduce `ang_vel`, but they do not immediately reset the `angle` to zero, allowing a significant tilt to persist even after the rotational speed has slowed.

7. **Vertical Control Authority Degradation**: The capacity of the main engine to counteract gravity is scaled by $\cos(\text{angle})$; as the absolute value of the `angle` increases, the engine's ability to arrest $y\_vel$ diminishes significantly.

8. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at an angle creates a feedback loop where correcting one velocity component inevitably perturbs the other.

9. **Asymmetric Landing Instability**: Trajectories confirm that asymmetric leg contact (e.g., `left_leg_contact=0` and `right_leg_contact=1`) is a primary driver of failure. Even when descent speeds are moderate, landing on only one leg leads to immediate instability and terminal failure.

10. **Tri-Factor Terminal Success**: Landing success is a multi-variable requirement. A successful landing necessitates the simultaneous stabilization of descent velocity ($y\_vel$), orientation (`angle`), and contact symmetry (both legs). Failure to achieve any one of these—such as landing with a significant tilt or asymmetric contact—results in failure, even if the descent velocity is relatively low.

---

## 2026-07-02 03:28:28

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust to prevent $y\_vel$ from reaching critical descent speeds that lead to terminal impact.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest.

3. **Horizontal Velocity Persistence**: High $|x\_vel|$ is a primary terminal threat; horizontal momentum persists throughout the descent and must be actively nullified before ground contact to prevent lateral crashes.

4. **Main Engine (Action 2) Vector Decomposition**: Main engine thrust decomposes into vertical and horizontal components based on `angle`. As the absolute value of `angle` increases, the vertical thrust component ($\cos(\text{angle})$) decreases while the horizontal component ($\sin(\text{angle})$) increases, making the main engine a dual-purpose tool for both altitude and lateral maneuvering.

5. **Side Engine (Action 1 & 3) Indirect Translation**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct translational thrust; their effect on $x\_vel$ and $y\_vel$ is entirely mediated by the reorientation of the main engine's thrust vector.

6. **Angular Dampening vs. Orientation Correction**: Side engines can effectively reduce `ang_vel` (rotational speed), but they do not immediately reset the `angle` to zero, allowing a state with low rotational velocity but significant tilt to persist.

7. **Vertical Control Authority Degradation**: The capacity of the main engine to counteract gravity is scaled by $\cos(\text{angle})$; as the absolute value of the `angle` increases, the engine's ability to arrest $y\_vel$ diminishes significantly.

8. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at an angle creates a feedback loop where correcting one velocity component inevitably perturbs the other.

9. **Asymmetric Landing Instability**: Asymmetric leg contact (e.g., `left_leg_contact=1` and `right_leg_contact=0`) is a primary driver of failure. This instability is frequently coupled with high `ang_vel` or significant `angle` at the moment of contact, leading to immediate terminal failure.

10. **Tri-Factor Terminal Success**: A successful landing requires the simultaneous stabilization of three critical variables: descent velocity ($y\_vel$), orientation (`angle`), and contact symmetry (both legs). Failure to satisfy any one of these—such as landing with excessive descent speed, significant tilt, or asymmetric contact—results in failure.

---

## 2026-07-02 03:31:54

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust to prevent $y\_vel$ from reaching critical descent speeds that lead to terminal impact.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest.

3. **Horizontal Velocity Persistence**: High $|x\_vel|$ is a primary terminal threat; horizontal momentum persists throughout the descent and must be actively nullified before ground contact to prevent lateral crashes.

4. **Main Engine (Action 2) Vector Decomposition**: Main engine thrust decomposes into vertical and horizontal components based on `angle`. As $|\text{angle}|$ increases, the vertical thrust component ($\cos(\text{angle})$) decreases while the horizontal component ($\sin(\text{angle})$) increases, making the main engine a dual-purpose tool for both altitude and lateral maneuvering.

5. **Side Engine (Action 1 & 3) Indirect Translation**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct translational thrust; their effect on $x\_vel$ and $y\_vel$ is entirely mediated by the reorientation of the main engine's thrust vector.

6. **Angular Dampening vs. Orientation Correction**: Side engines can effectively reduce `ang_vel` (rotational speed), but they do not immediately reset the `angle` to zero, allowing a state with low rotational velocity but significant tilt to persist.

7. **Vertical Control Authority Degradation**: The capacity of the main engine to counteract gravity is scaled by $\cos(\text{angle})$; as the absolute value of the `angle` increases (approaching $\pi/2$), the engine's ability to arrest $y\_vel$ diminishes significantly.

8. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at an angle creates a feedback loop where correcting one velocity component inevitably perturbs the other.

9. **Momentum-Induced Impact Failure**: Terminal success is contingent on the magnitude of kinetic energy at $y\_pos \approx 0$. Even if contact is established, excessive $|x\_vel|$, $|y\_vel|$, or $|ang\_vel|$ at the moment of impact results in a failure.

10. **Asymmetric Contact and Stability**: Leg contact is a binary state. Asymmetric contact (e.g., `left_leg_contact=1` and `right_leg_contact=0`) is a primary driver of failure, typically occurring when significant `angle` or `ang_vel` prevents a level landing.

---

## 2026-07-02 03:34:46

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust to prevent $y\_vel$ from reaching critical descent speeds that lead to terminal impact.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest the rotational velocity.

3. **Horizontal Velocity Persistence**: High $|x\_vel|$ is a primary terminal threat. Lateral momentum can accumulate significantly throughout the descent, and if not nullified early, it becomes increasingly difficult to arrest before ground contact.

4. **Main Engine (Action 2) Vector Decomposition**: Main engine thrust decomposes into vertical and horizontal components based on `angle`. As $|\text{angle}|$ increases, the vertical thrust component ($\cos(\text{angle})$) decreases while the horizontal component ($\sin(\text{angle})$) increases, making the main engine a dual-purpose tool for both altitude and lateral maneuvering.

5. **Side Engine (Action 1 & 3) Indirect Translation**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct translational thrust; their effect on $x\_vel$ and $y\_vel$ is entirely mediated by the reorientation of the main engine's thrust vector.

6. **Angular Dampening vs. Orientation Correction**: Side engines can effectively reduce `ang_vel` (rotational speed), but they do not immediately reset the `angle` to zero, allowing a state with low rotational velocity but significant tilt to persist.

7. **Vertical Control Authority Degradation**: The capacity of the main engine to counteract gravity is scaled by $\cos(\text{angle})$; as the absolute value of the `angle` increases (approaching $\pi/2$), the engine's ability to arrest $y\_vel$ diminishes significantly.

8. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at an angle creates a feedback loop where correcting one velocity component inevitably perturbs the other.

9. **Momentum-Induced Impact Failure**: Terminal success is contingent on low kinetic energy at $y\_pos \approx 0$. High magnitudes of $|x\_vel|$, $|y\_vel|$, or $|ang\_vel|$ at the moment of impact result in failure, even if the lander's `angle` is near zero.

10. **Asymmetric Contact and Tip-Over Risk**: Leg contact is a binary state. One-legged contact (e.g., `right_leg_contact=1`) in the presence of significant $|x\_vel|$ or $|ang\_vel|$ frequently leads to a tip-over or a secondary, catastrophic impact on the opposite leg.

---

## 2026-07-02 03:37:39

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust to prevent $y\_vel$ from reaching critical descent speeds that lead to terminal impact.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest the rotational velocity.

3. **Horizontal Velocity Persistence**: High $|x\_vel|$ is a primary terminal threat. Lateral momentum can accumulate significantly throughout the descent, and if not nullified early, it becomes increasingly difficult to arrest before ground contact.

4. **Main Engine (Action 2) Vector Decomposition**: Main engine thrust decomposes into vertical and horizontal components based on `angle`. As $|\text{angle}|$ increases, the vertical thrust component ($\cos(\text{angle})$) decreases while the horizontal component ($\sin(\text{angle})$) increases.

5. **Side Engine (Action 1 & 3) Indirect Translation**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct translational thrust; their effect on $x\_vel$ and $y\_vel$ is entirely mediated by the reorientation of the main engine's thrust vector.

6. **Angular Dampening vs. Orientation Correction**: Side engines can effectively reduce `ang_vel` (rotational speed), but they do not immediately reset the `angle` to zero, allowing a state with low rotational velocity but significant tilt to persist.

7. **Vertical Control Authority Degradation**: The capacity of the main engine to counteract gravity is scaled by $\cos(\text{angle})$; as the absolute value of the `angle` increases (approaching $\pi/2$), the engine's ability to arrest $y\_vel$ diminishes significantly.

8. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at an angle creates a feedback loop where correcting one velocity component inevitably perturbs the other.

9. **Ground-Contact Fulcrum Effect**: Leg contact (e.g., `left_leg_contact=1`) transforms the lander from a free-falling body into a constrained pivot. If $|x\_vel|$ or $|ang\_vel|$ are non-zero at the moment of contact, the ground acts as a fulcrum, inducing rapid and catastrophic angular acceleration (tip-over).

10. **Terminal Kinetic Energy Constraint**: Terminal success is contingent on the simultaneous minimization of $|x\_vel|$, $|y\_vel|$, and $|ang\_vel|$ at $y\_pos \approx 0$. High magnitudes in any single velocity component at impact will result in failure, even if the `angle` is near zero.

---

## 2026-07-02 03:41:59

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust to prevent $y\_vel$ from reaching critical descent speeds that lead to terminal impact.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest the rotational velocity.

3. **Horizontal Velocity Persistence**: High $|x\_vel|$ is a primary terminal threat. Lateral momentum can accumulate significantly throughout the descent, and if not nullified early, it becomes increasingly difficult to arrest before ground contact.

4. **Main Engine (Action 2) Vector Decomposition**: Main engine thrust decomposes into vertical and horizontal components based on `angle`. As $|\text{angle}|$ increases, the vertical thrust component ($\cos(\text{angle})$) decreases while the horizontal component ($\sin(\text{angle})$) increases, often exacerbating $x\_vel$ drift.

5. **Side Engine (Action 1 & 3) Indirect Translation**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct translational thrust; their effect on $x\_vel$ and $y\_vel$ is entirely mediated by the reorientation of the main engine's thrust vector.

6. **Angular Dampening vs. Orientation Correction**: Side engines can effectively reduce `ang_vel` (rotational speed), but they do not immediately reset the `angle` to zero, allowing a state with low rotational velocity but significant tilt to persist.

7. **Vertical Control Authority Degradation**: The capacity of the main engine to counteract gravity is scaled by $\cos(\text{angle})$; as the absolute value of the `angle` increases, the engine's ability to arrest $y\_vel$ diminishes significantly.

8. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at a significant `angle` creates a feedback loop where correcting one velocity component inevitably perturbs the other due to thrust vector decomposition.

9. **The Ground-Contact Fulcrum Effect**: Leg contact (`left_leg_contact` or `right_leg_contact` = 1) transforms the lander from a free-falling body into a constrained pivot. If $x\_vel$, $y\_vel$, or $ang\_vel$ are non-zero at the moment of contact, the ground acts as a fulcrum, causing an immediate and catastrophic conversion of translational or angular momentum into rapid, uncontrolled rotational acceleration (tip-over).

10. **The Multi-Component Terminal Constraint**: Success is contingent on the simultaneous minimization of $|x\_vel|$, $|y\_vel|$, $|ang\_vel|$, and $|angle|$ at or before $y\_pos \approx 0$. High magnitudes in any single velocity component or tilt at the moment of leg contact trigger the fulcrum effect, leading to failure even if the lander's center of mass is near the ground.

---

## 2026-07-02 03:43:57

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust to prevent $y\_vel$ from reaching critical descent speeds that lead to terminal impact.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest the rotational velocity.

3. **Horizontal Velocity Persistence**: High $|x\_vel|$ is a primary terminal threat. Lateral momentum can accumulate significantly, and if not nullified early, high $|x\_vel|$ at the moment of ground contact will prevent a successful landing, even if the lander's orientation is correct.

4. **Main Engine (Action 2) Vector Decomposition**: Main engine thrust decomposes into vertical and horizontal components based on `angle`. As $|\text{angle}|$ increases, the vertical thrust component ($\cos(\text{angle})$) decreases while the horizontal component ($\sin(\text{angle})$) increases, often exacerbating $x\_vel$ drift.

5. **Side Engine (Action 1 & 3) Indirect Translation**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct translational thrust; their effect on $x\_vel$ and $y\_vel$ is entirely mediated by the reorientation of the main engine's thrust vector.

6. **Angular Dampening vs. Orientation Correction**: Side engines can effectively reduce `ang_vel` (rotational speed), but they do not immediately reset the `angle` to zero, allowing a state with low rotational velocity but significant tilt to persist.

7. **Vertical Control Authority Degradation**: The capacity of the main engine to counteract gravity is scaled by $\cos(\text{angle})$; as the absolute value of the `angle` increases, the engine's ability to arrest $y\_vel$ diminishes significantly.

8. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at a significant `angle` creates a feedback loop where correcting one velocity component inevitably perturbs the other due to thrust vector decomposition.

9. **The Single-Leg Fulcrum Trigger**: The transition from a free-falling body to a constrained pivot occurs upon the contact of even a *single* leg. If $x\_vel$, $y\_vel$, or $ang\_vel$ are non-zero at the moment of initial leg contact, the ground acts as a fulcrum, causing an immediate and catastrophic conversion of momentum into rapid, uncontrolled angular acceleration (tip-over).

10. **The Multi-Component Terminal Constraint**: Success is contingent on the simultaneous minimization of $|x\_vel|$, $|y\_vel|$, $|ang\_vel|$, and $|angle|$ at or before $y\_pos \approx 0$. Maintaining low tilt is insufficient for success if translational velocities ($x\_vel, y\_vel$) are high at the point of contact.

---

## 2026-07-02 03:47:47

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust to prevent $y\_vel$ from reaching critical descent speeds that lead to terminal impact.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest the rotational velocity.

3. **Horizontal Velocity Persistence**: High $|x\_vel|$ is a primary terminal threat. Lateral momentum can accumulate significantly, and if not nullified early, high $|x\_vel|$ at the moment of ground contact will prevent a successful landing, even if the lander's orientation is correct.

4. **Main Engine (Action 2) Vector Decomposition**: Main engine thrust decomposes into vertical and horizontal components based on `angle`. As $|\text{angle}|$ increases, the vertical thrust component ($\cos(\text{angle})$) decreases while the horizontal component ($\sin(\text{angle})$) increases, often exacerbating $x\_vel$ drift.

5. **Side Engine (Action 1 & 3) Indirect Translation**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct translational thrust; their effect on $x\_vel$ and $y\_vel$ is entirely mediated by the reorientation of the main engine's thrust vector.

6. **Angular Dampening vs. Orientation Correction**: Side engines can effectively reduce `ang_vel` (rotational speed), but they do not immediately reset the `angle` to zero, allowing a state with low rotational velocity but significant tilt to persist.

7. **Vertical Control Authority Degradation**: The capacity of the main engine to counteract gravity is scaled by $\cos(\text{angle})$; as the absolute value of the `angle` increases, the engine's ability to arrest $y\_vel$ diminishes significantly.

8. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at a significant `angle` creates a feedback loop where correcting one velocity component inevitably perturbs the other due to thrust vector decomposition.

9. **The Fulcrum-Induced Momentum Conversion**: The transition from free-fall to a constrained pivot occurs upon the contact of any leg. Residual $x\_vel$, $y\_vel$, or $ang\_vel$ is instantaneously converted into rapid, escalating angular velocity. This ground-induced rotational acceleration can be high enough to overwhelm the corrective torque capacity of the side engines, leading to uncontrollable spinning.

10. **The Pre-Contact Stabilization Requirement**: Successful landing requires the simultaneous minimization of $|x\_vel|$, $|y\_vel|$, $|ang\_vel|$, and $|angle|$ *before* the onset of leg contact. Once the transition to a constrained pivot is triggered, the resulting rotational instability becomes the dominant physical driver, making recovery via engine thrust unlikely.

---

## 2026-07-02 03:49:41

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust (Action 2) to prevent $y\_vel$ from reaching terminal descent speeds.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest the rotational velocity.

3. **Horizontal Velocity Persistence**: High $|x\_vel|$ is a primary terminal threat; lateral momentum must be nullified early, as high $|x\_vel|$ at the moment of contact prevents a stable landing regardless of orientation.

4. **Main Engine (Action 2) Vector Decomposition**: Main engine thrust decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as $|\text{angle}|$ increases, vertical thrust decreases while horizontal drift increases.

5. **Side Engine (Action 1 & 3) Indirect Translation**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct translational thrust; their effect on $x\_vel$ and $y\_vel$ is entirely mediated by the reorientation of the main engine's thrust vector.

6. **Angular Dampening vs. Orientation Correction**: Side engines can effectively reduce `ang_vel` (rotational speed), but they do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **Vertical Control Authority Degradation**: The capacity of the main engine to counteract gravity is scaled by $\cos(\text{angle})$; as the absolute value of the `angle` increases, the engine's ability to arrest $y\_vel$ diminishes.

8. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at a significant `angle` creates a feedback loop where correcting one velocity component inevitably perturbs the other due to thrust vector decomposition.

9. **The Fulcrum-Induced Momentum Conversion**: The transition from free-fall to a constrained pivot occurs upon leg contact. Residual $x\_vel$, $y\_vel$, or $ang\_vel$ is instantaneously converted into rapid, escalating angular velocity that can overwhelm corrective torque.

10. **Post-Contact Dynamic Instability**: Establishing leg contact does not guarantee a static state; the lander remains susceptible to torque-induced tipping, transitions between single-leg and dual-leg contact, or complete loss of contact if angular and linear velocities are not minimized prior to and during the landing phase.

---

## 2026-07-02 03:52:00

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust (Action 2) to prevent $y\_vel$ from reaching terminal descent speeds.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest the rotational velocity.

3. **Horizontal Velocity Persistence**: High $|x\_vel|$ is a primary terminal threat; lateral momentum is highly persistent and, if not nullified early, becomes increasingly difficult to arrest as the lander descends and must prioritize vertical control.

4. **Main Engine (Action 2) Vector Decomposition**: Main engine thrust decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as $|\text{angle}|$ increases, vertical thrust decreases while horizontal drift increases.

5. **Side Engine (Action 1 & 3) Indirect Translation**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct translational thrust; their effect on $x\_vel$ and $y\_vel$ is entirely mediated by the reorientation of the main engine's thrust vector.

6. **Angular Dampening vs. Orientation Correction**: Side engines can effectively reduce `ang_vel` (rotational speed), but they do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **Vertical Control Authority Degradation**: The capacity of the main engine to counteract gravity is scaled by $\cos(\text{angle})$; as the absolute value of the `angle` increases, the engine's ability to arrest $y\_vel$ diminishes.

8. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at a significant `angle` creates a feedback loop where correcting one velocity component inevitably perturbs the other due to thrust vector decomposition.

9. **The Fulcrum-Induced Momentum Conversion**: The transition from free-fall to a constrained pivot occurs upon leg contact. Residual $x\_vel$, $y\_vel$, or $ang\_vel$ is instantaneously converted into rapid, escalating angular velocity that can overwhelm corrective torque.

10. **Post-Contact Multi-Phase Instability**: Establishing leg contact (e.g., `left_leg_contact=1.0`) does not terminate the descent or guarantee stability; the lander enters a highly unstable contact state where it may transition between single-leg and dual-leg contact, remaining susceptible to tipping or complete loss of contact if angular and linear velocities are not minimized.

---

## 2026-07-02 03:53:42

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust (Action 2) to manage $y\_vel$ and prevent terminal descent speeds.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest the rotational velocity.

3. **Horizontal Velocity Persistence**: High $|x\_vel|$ is a primary terminal threat; lateral momentum is highly persistent and, if not nullified early in the descent, becomes increasingly difficult to arrest as the lander must prioritize vertical control.

4. **Main Engine Vector Decomposition & Vertical Authority**: Main engine thrust decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute value of the `angle` increases, the engine's capacity to counteract gravity and arrest $y\_vel$ diminishes while horizontal drift increases.

5. **Side Engine Indirect Translation**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct translational thrust; their effect on $x\_vel$ and $y\_vel$ is entirely mediated by the reorientation of the main engine's thrust vector.

6. **Angular Dampening vs. Orientation Correction**: Side engines can effectively reduce `ang_vel` (rotational speed), but they do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at a significant `angle` creates a feedback loop where correcting one velocity component inevitably perturbs the other due to thrust vector decomposition.

8. **The Fulcrum-Induced Momentum Conversion**: The transition from free-fall to a constrained pivot occurs upon leg contact. Residual $x\_vel$, $y\_vel$, or $ang\_vel$ is instantaneously converted into rapid, escalating angular velocity that can overwhelm corrective torque.

9. **Post-Contact Multi-Phase Instability**: Establishing leg contact does not guarantee stability; the lander enters a highly unstable contact state where it may transition between single-leg and dual-leg contact, remaining susceptible to tipping if angular and linear velocities are not minimized.

10. **High-Energy State Sensitivity**: Massive negative rewards (e.g., -18 to -100) are state-dependent, triggered when the lander enters critical configurations of high angular or linear velocity. In these regimes, the environment may impose severe penalties regardless of the action taken (including Action 0), and applying side engines (Actions 1 or 3) often exacerbates instability, leading to even larger negative rewards.

---

## 2026-07-02 03:57:22

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust (Action 2) to manage $y\_vel$ and prevent terminal descent speeds.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest the rotational velocity.

3. **Horizontal Velocity Persistence**: High $|x\_vel|$ is a primary terminal threat; lateral momentum is highly persistent and, if not nullified early in the descent, becomes increasingly difficult to arrest as the lander must prioritize vertical control.

4. **Main Engine Vector Decomposition & Vertical Authority**: Main engine thrust decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute value of the `angle` increases, the engine's capacity to counteract gravity and arrest $y\_vel$ diminishes while horizontal drift increases.

5. **Side Engine Indirect Translation**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct translational thrust; their effect on $x\_vel$ and $y\_vel$ is entirely mediated by the reorientation of the main engine's thrust vector.

6. **Angular Dampening vs. Orientation Correction**: Side engines can effectively reduce `ang_vel` (rotational speed), but they do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at a significant `angle` creates a feedback loop where correcting one velocity component inevitably perturbs the other due to thrust vector decomposition.

8. **The Fulcrum-Induced Momentum Conversion**: The transition from free-fall to a constrained pivot occurs upon leg contact (transition of `leg_contact` from 0.0 to 1.0). This transition instantaneously converts residual linear or angular momentum into rapid, escalating angular velocity spikes.

9. **Contact-Phase Control Volatility**: Once leg contact is established, the lander enters a regime of extreme control sensitivity. In this state, any action (including Action 2 or side engines) that is not perfectly calculated to counteract the pivot-induced torque can trigger massive negative rewards by causing rapid, uncontrolled angular acceleration.

10. **Catastrophic Terminal Penalty**: The environment imposes a maximum negative reward (-100) for terminal failure. This is typically triggered by a "crash" state where angular or linear velocities exceed critical stability thresholds or when the lander's orientation becomes unrecoverable during the contact phase.

---

## 2026-07-02 03:59:38

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust (Action 2) to manage $y\_vel$ and prevent terminal descent speeds.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest the rotational velocity.

3. **Lateral Momentum Persistence**: High $|x\_vel|$ is a primary terminal threat. New data (Episode 2) confirms that even with a relatively controlled `angle`, high lateral velocity at the moment of impact facilitates a violent conversion of linear momentum into rotational energy.

4. **Main Engine Vector Decomposition**: Main engine thrust decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute value of the `angle` increases, the engine's capacity to counteract gravity and arrest $y\_vel$ diminishes while horizontal drift increases.

5. **Side Engine Indirect Translation**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct translational thrust; their effect on $x\_vel$ and $y\_vel$ is entirely mediated by the reorientation of the main engine's thrust vector.

6. **Angular Dampening vs. Orientation Correction**: Side engines can effectively reduce `ang_vel` (rotational speed), but they do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at a significant `angle` creates a feedback loop where correcting one velocity component inevitably perturbs the other due to thrust vector decomposition.

8. **Asymmetric Contact-Induced Pivot**: The transition of a single `leg_contact` from 0.0 to 1.0 transforms the lander from a free-falling body into a pivoting pendulum. This transition instantaneously converts residual linear momentum ($x\_vel$ and $y\_vel$) into rapid, escalating angular velocity spikes ($\text{ang\_vel}$) around the contact point.

9. **Contact-Phase Control Volatility**: Once any leg contact is established, the lander enters a regime of extreme control sensitivity. The moment-arm created by the contact point means that even the main engine (Action 2) can trigger massive uncontrolled angular acceleration if the thrust vector is not perfectly aligned to counteract the pivot-induced torque.

10. **Catastrophic Terminal Penalty**: The environment imposes a maximum negative reward (-100) for terminal failure. This is typically triggered by a "crash" state where angular or linear velocities exceed critical stability thresholds or when the lander's orientation becomes unrecoverable during the high-torque contact phase.

---

## 2026-07-02 04:01:22

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust (Action 2) to manage $y\_vel$ and prevent terminal descent speeds.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest the rotational velocity.

3. **Lateral Momentum Persistence**: High $|x\_vel|$ is a primary terminal threat. High lateral velocity at the moment of impact facilitates a violent conversion of linear momentum into rotational energy.

4. **Main Engine Vector Decomposition**: Main engine thrust decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute value of the `angle` increases, the engine's capacity to counteract gravity diminishes while horizontal drift increases.

5. **Side Engine Indirect Translation**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct translational thrust; their effect on $x\_vel$ and $y\_vel$ is entirely mediated by the reorientation of the main engine's thrust vector.

6. **Angular Dampening vs. Orientation Correction**: Side engines can effectively reduce `ang_vel` (rotational speed), but they do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at a significant `angle` creates a feedback loop where correcting one velocity component inevitably perturbs the other due to thrust vector decomposition.

8. **Asymmetric Contact-Induced Pivot**: The transition of a single `leg_contact` from 0.0 to 1.0 transforms the lander into a pivoting pendulum. This transition converts residual linear momentum into rapid, escalating angular velocity spikes ($\text{ang\_vel}$) around the contact point.

9. **Contact-Phase Control Volatility**: Once leg contact is established, the lander enters a regime of extreme control sensitivity. The moment-arm created by the contact point means that even the main engine (Action 2) can trigger massive uncontrolled angular acceleration, which is reflected in violent reward oscillations between high positive values and significant negative penalties.

10. **Two-Stage Terminal Instability**: Terminal failure follows a staged penalty structure. Before the final -100 crash penalty is triggered, the environment imposes heavy intermediate negative rewards (e.g., -10 to -30) when $x\_vel$, $y\_vel$, or $ang\_vel$ exceed stability thresholds while in contact, signaling a high-energy kinetic instability.

---

## 2026-07-02 04:05:23

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust (Action 2) to manage $y\_vel$ and prevent terminal descent speeds.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest the rotational velocity.

3. **Lateral Momentum Persistence**: High $|x\_vel|$ is a primary terminal threat. High lateral velocity at the moment of impact facilitates a violent conversion of linear momentum into rotational energy.

4. **Main Engine Vector Decomposition**: Main engine thrust decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute value of the `angle` increases, the engine's capacity to counteract gravity diminishes while horizontal drift increases.

5. **Side Engine Indirect Translation**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct translational thrust; their effect on $x\_vel$ and $y\_vel$ is entirely mediated by the reorientation of the main engine's thrust vector.

6. **Angular Dampening vs. Orientation Correction**: Side engines can effectively reduce `ang_vel` (rotational speed), but they do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at a significant `angle` creates a feedback loop where correcting one velocity component inevitably perturbs the other due to thrust vector decomposition.

8. **Asymmetric Contact-Induced Pivot**: The transition of a single `leg_contact` from 0.0 to 1.0 transforms the lander into a pivoting pendulum, converting residual linear momentum into rapid, escalating angular velocity spikes ($\text{ang\_vel}$) around the contact point.

9. **Contact-Phase Stability Thresholds**: During the contact phase, maintaining a high absolute `angle` (e.g., $|angle| \approx 0.3$) triggers severe intermediate negative rewards (e.g., -10 to -30), even if the angular velocity (`ang_vel`) is low.

10. **Terminal Kinetic Collapse**: The terminal -100 crash penalty is triggered by the convergence of high angular tilt and high angular velocity during contact, representing a catastrophic loss of attitude control where rotation and tilt amplify one another.

---

## 2026-07-02 04:07:37

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust (Action 2) to manage $y\_vel$ and prevent terminal descent speeds.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest the rotational velocity.

3. **Lateral Momentum Persistence**: High $|x\_vel|$ is a primary terminal threat. High lateral velocity at the moment of impact facilitates a violent conversion of linear momentum into rotational energy.

4. **Main Engine Vector Decomposition**: Main engine thrust decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute value of the `angle` increases, the engine's capacity to counteract gravity diminishes while horizontal drift increases.

5. **Side Engine Indirect Translation**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct translational thrust; their effect on $x\_vel$ and $y\_vel$ is entirely mediated by the reorientation of the main engine's thrust vector.

6. **Angular Dampening vs. Orientation Correction**: Side engines can effectively reduce `ang_vel` (rotational speed), but they do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at a significant `angle` creates a feedback loop where correcting one velocity component inevitably perturbs the other due to thrust vector decomposition.

8. **Asymmetric Contact-Induced Pivot**: The transition of a single `leg_contact` from 0.0 to 1.0 transforms the lander into a pivoting pendulum, converting residual linear momentum into rapid, escalating angular velocity spikes ($\text{ang\_vel}$) around the contact point.

9. **Contact-Phase Reward Duality**: Upon establishing `leg_contact`, the reward structure shifts from survival-based to stability-based; while tilt penalties remain, the environment provides high-magnitude positive bonuses (e.g., +10 to +23) for maintaining near-zero $x\_vel$, $y\_vel$, and `angle`.

10. **Instantaneous Terminal Collapse**: The catastrophic -100 penalty is an immediate terminal event that can trigger even from a seemingly stable contact state (`leg_contact` [1, 1]), representing a sudden threshold breach in kinetic or angular stability.

---

## 2026-07-02 04:09:01

---
1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust (Action 2) to manage $y\_vel$ and prevent terminal descent speeds.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest the rotational velocity.

3. **Lateral Momentum Persistence**: High $|x\_vel|$ is a primary terminal threat. High lateral velocity at the moment of impact facilitates a violent conversion of linear momentum into rotational energy.

4. **Main Engine Vector Decomposition**: Main engine thrust decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute value of the `angle` increases, the engine's capacity to counteract gravity diminishes while horizontal drift increases.

5. **Side Engine Indirect Translation**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct translational thrust; their effect on $x\_vel$ and $y\_vel$ is entirely mediated by the reorientation of the main engine's thrust vector.

6. **Angular Dampening vs. Orientation Correction**: Side engines can effectively reduce `ang_vel` (rotational speed), but they do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at a significant `angle` creates a feedback loop where correcting one velocity component inevitably perturbs the other due to thrust vector decomposition.

8. **Asymmetric Contact-Induced Pivot**: The transition of a single `leg_contact` from 0.0 to 1.0 transforms the lander into a pivoting pendulum, converting residual linear momentum into rapid, escalating angular velocity spikes ($\text{ang\_vel}$) around the contact point.

9. **Contact-Phase Reward Duality and Contact Maintenance**: Upon establishing `leg_contact`, the reward structure shifts from survival-based to stability-based. While [1, 1] contact yields high positive bonuses, transitions from [1, 1] to [0, 1] (losing a leg) or [0, 0] are associated with significant negative rewards, indicating that maintaining dual-leg contact is a distinct and precarious stability requirement.

10. **Instantaneous Terminal Collapse**: The catastrophic -100 penalty is an immediate terminal event that can be triggered from a seemingly stable contact state ([1, 1]) if kinetic or angular instability causes the lander to tip or bounce, resulting in a total loss of contact ([0, 0]).

---

## 2026-07-02 04:10:42

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust (Action 2) to manage $y\_vel$ and prevent terminal descent speeds.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest the rotational velocity.

3. **Lateral Momentum Persistence**: High $|x\_vel|$ is a primary terminal threat. High lateral velocity at the moment of impact facilitates a violent conversion of linear momentum into rotational energy.

4. **Main Engine Vector Decomposition**: Main engine thrust decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute value of the `angle` increases, the engine's capacity to counteract gravity diminishes while horizontal drift increases.

5. **Side Engine Indirect Translation**: Side engines provide torque to influence `angle` and `ang_vel` but offer no direct translational thrust; their effect on $x\_vel$ and $y\_vel$ is entirely mediated by the reorientation of the main engine's thrust vector.

6. **Angular Dampening vs. Orientation Correction**: Side engines can effectively reduce `ang_vel` (rotational speed), but they do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at a significant `angle` creates a feedback loop where correcting one velocity component inevitably perturbs the other due to thrust vector decomposition.

8. **Contact-Induced Angular Acceleration**: Upon establishing contact (transitioning to `leg_contact` [1, 1]), residual linear or angular momentum can trigger rapid, non-linear spikes in `ang_vel` as the lander pivots around its contact points.

9. **Contact-Phase Reward Duality**: While [1, 1] contact yields high positive bonuses, this can incentivize the agent to prioritize contact maintenance over orientation correction, allowing the `angle` to drift into unrecoverable ranges.

10. **Orientation-Based Terminal Failure**: The catastrophic -100 penalty is triggered by a tip-over event, occurring when `angle` or `ang_vel` exceeds a critical stability threshold, even if the lander is currently maintaining dual-leg contact ([1, 1]).

---

## 2026-07-02 04:13:32

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust (Action 2) to manage $y\_vel$ and prevent terminal descent speeds.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest the rotational velocity.

3. **Lateral Momentum Persistence**: High $|x\_vel|$ is a primary terminal threat. High lateral velocity at the moment of impact facilitates a violent conversion of linear momentum into rotational energy.

4. **Main Engine Vector Decomposition**: Main engine thrust decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute value of the `angle` increases, the engine's capacity to counteract gravity diminishes while horizontal drift increases.

5. **Side Engine-Induced Contact Disruption**: Side engines (Actions 1 and 3) provide torque but also act as impulsive forces during the contact phase; improper use while grounded can trigger skidding ([1, 0] or [0, 1]) or complete contact loss ([0, 0]).

6. **Angular Dampening vs. Orientation Correction**: Side engines can effectively reduce `ang_vel` (rotational speed), but they do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at a significant `angle` creates a feedback loop where correcting one velocity component inevitably perturbs the other due to thrust vector decomposition.

8. **Contact-Phase Kinetic Instability**: The transition to dual-leg contact ([1, 1]) is highly sensitive to momentum; residual linear or angular velocity can be amplified by thrust, causing rapid, non-linear spikes in $y\_vel$ and `ang_vel` that break ground contact.

9. **Contact-Phase Reward Duality**: While [1, 1] contact yields high positive bonuses, this can incentivize the agent to prioritize contact maintenance over orientation correction, allowing the `angle` to drift into unrecoverable ranges.

10. **Dual-Mode Terminal Failure**: The catastrophic -100 penalty is triggered by exceeding critical stability thresholds in `angle` or `ang_vel`. This can occur during the descent phase or as a consequence of high-energy kinetic instability (bouncing/skidding) triggered during the contact phase.

---

## 2026-07-02 04:16:04

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust (Action 2) to manage $y\_vel$ and prevent terminal descent speeds.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest the rotational velocity.

3. **Lateral Momentum Persistence**: High $|x\_vel|$ is a primary terminal threat, as high lateral velocity at the moment of impact facilitates a violent conversion of linear momentum into rotational energy.

4. **Main Engine Vector Decomposition**: Main engine thrust decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute value of the `angle` increases, the engine's capacity to counteract gravity diminishes while horizontal drift increases.

5. **Engine-Induced Contact Instability**: Using engines (Actions 1, 2, or 3) while in a contact state ([1, 1]) can trigger impulsive transitions to skidding ([1, 0] or [0, 1]) or total contact loss ([0, 0]).

6. **Angular Dampening vs. Orientation Correction**: Side engines can effectively reduce `ang_vel` (rotational speed), but they do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at a significant `angle` creates a feedback loop where correcting one velocity component inevitably perturbs the other due to thrust vector decomposition.

8. **Contact-Phase Kinetic Penalty Spikes**: Applying significant thrust (particularly Action 2) while grounded can trigger sudden, massive negative rewards (e.g., -10 to -20) due to rapid, non-linear transitions from contact to airborne states.

9. **Contact-Phase Reward Duality**: While [1, 1] contact yields high positive bonuses, this can incentivize the agent to prioritize contact maintenance over orientation correction, allowing the `angle` to drift into unrecoverable ranges.

10. **Dual-Mode Terminal Failure**: The catastrophic -100 penalty is triggered by exceeding critical stability thresholds in `angle` or `ang_vel`. This can occur during the descent phase or as a consequence of high-energy kinetic instability (bouncing/skidding) triggered during the contact phase.

---

## 2026-07-02 04:17:56

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust (Action 2) to manage $y\_vel$ and prevent terminal descent speeds.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest the rotational velocity.

3. **Lateral Velocity Accumulation**: High $|x\_vel|$ is often a cumulative byproduct of using the main engine (Action 2) to combat gravity while at a non-zero `angle`. This lateral drift persists and grows throughout the descent, significantly increasing the risk of impact instability.

4. **Main Engine Vector Decomposition**: Main engine thrust decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute value of the `angle` increases, the engine's capacity to counteract gravity diminishes while horizontal drift increases.

5. **Engine-Induced Contact Instability**: Using engines (Actions 1, 2, or 3) while in a contact state ([1, 1]) can trigger impulsive transitions to skidding ([1, 0] or [0, 1]) or total contact loss ([0, 0]).

6. **Angular Dampening vs. Orientation Correction**: Side engines can effectively reduce `ang_vel` (rotational speed), but they do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at a significant `angle` creates a feedback loop where correcting one velocity component inevitably perturbs the other due to thrust vector decomposition.

8. **Impact-Induced Rotational Spikes**: Establishing contact ([1, 1]) does not inherently stabilize the craft; if `ang_vel` is significant at the moment of impact, the transition from airborne to grounded can trigger massive spikes in rotational velocity, leading to immediate failure.

9. **Side-Engine Reward Volatility**: Side engine actions (1 and 3) exhibit extreme reward volatility; they can provide critical, high-reward orientation corrections during late-stage descent, but they can also trigger heavy negative rewards if they exacerbate the tilt-drift cycle.

10. **Terminal Stability Thresholds**: The catastrophic -100 penalty is triggered by exceeding critical stability thresholds in `angle` or `ang_vel`. Data shows this penalty can be triggered even if both legs have successfully achieved contact ([1, 1]), provided the rotational energy is too high.

---

## 2026-07-02 04:19:50

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust (Action 2) to manage $y\_vel$ and prevent terminal descent speeds.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest the rotational velocity.

3. **Lateral Velocity Accumulation**: High $|x\_vel|$ is a cumulative byproduct of using the main engine (Action 2) to combat gravity while at a non-zero `angle`. This lateral drift persists and grows throughout the descent, significantly increasing the risk of impact instability.

4. **Main Engine Vector Decomposition**: Main engine thrust decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute value of the `angle` increases, the engine's capacity to counteract gravity diminishes while horizontal drift increases.

5. **Side-Engine Reward Volatility**: Side engine actions (1 and 3) exhibit extreme reward volatility; while they can provide critical orientation corrections, frequent or uncoordinated use often results in significant negative rewards.

6. **Angular Dampening vs. Orientation Correction**: Side engines effectively reduce `ang_vel` (rotational speed), but they do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at a significant `angle` creates a feedback loop where correcting one velocity component inevitably perturbs the other due to thrust vector decomposition.

8. **Action Switching Instability**: Rapidly toggling between the main engine (Action 2) and side engines (Actions 1 or 3) induces high-frequency oscillations in both the `angle` and $y\_vel$ state variables, preventing the craft from achieving a steady descent state.

9. **Terminal Stability Thresholds**: The catastrophic -100 penalty is triggered by exceeding critical stability thresholds in `angle` or `ang_vel`; data indicates this penalty can be triggered mid-flight before contact is established.

10. **Cumulative Reward Erosion**: The reward structure heavily penalizes high-frequency, uncoordinated engine pulses; the summation of frequent negative rewards from side-engine "chatter" can significantly degrade the total episode reward even if the craft remains airborne.

---

## 2026-07-02 04:22:42

---
1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust (Action 2) to manage $y\_vel$ and prevent terminal descent speeds.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest the rotational velocity.

3. **Lateral Velocity Accumulation**: High $|x\_vel|$ is a cumulative byproduct of using the main engine (Action 2) to combat gravity while at a non-zero `angle`. This lateral drift persists and necessitates precise management to prevent excessive horizontal displacement during the landing phase.

4. **Main Engine Vector Decomposition**: Main engine thrust decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute value of the `angle` increases, the engine's capacity to counteract gravity diminishes while horizontal drift increases.

5. **Side-Engine Reward Volatility**: Side engine actions (1 and 3) exhibit extreme reward volatility; while they can provide critical orientation corrections, frequent or uncoordinated use often results in significant negative rewards.

6. **Angular Dampening vs. Orientation Correction**: Side engines effectively reduce `ang_vel` (rotational speed), but they do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at a significant `angle` creates a feedback loop where correcting one velocity component inevitably perturbs the other due to thrust vector decomposition.

8. **Action Switching Instability**: Rapidly toggling between the main engine (Action 2) and side engines (Actions 1 or 3) induces high-frequency oscillations in both the `angle` and $y\_vel$ state variables.

9. **Contact-Triggered Catastrophic Penalty**: The catastrophic -100 penalty is triggered when leg contact is established (`left_leg_contact` or `right_leg_contact` = 1.0) while the `angle` exceeds a critical stability threshold.

10. **Landing State Sensitivity**: Landing stability is critically dependent on the `angle` at the moment of touchdown; while $|x\_vel|$ and $|y\_vel|$ must be managed, failure to minimize `angle` during the transition to a contact state is the primary driver of terminal failure.

---

## 2026-07-02 04:29:39

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates continuous upward thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent speeds.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, the resulting angular momentum requires active torque (Actions 1 or 3) to arrest the rotational velocity.

3. **Lateral Velocity Accumulation**: Main engine thrust (Action 2) at non-zero angles produces horizontal displacement; this lateral drift persists even after the `angle` is later corrected, necessitating long-term management of $x\_vel$.

4. **Main Engine Vector Decomposition**: Main engine thrust decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute value of the `angle` increases, the engine's capacity to counteract gravity diminishes while horizontal drift increases.

5. **Torque-Orientation Coupling**: Side engines provide fixed torque (Action 1 = negative, Action 3 = positive); using a side engine to arrest `ang_vel` can inadvertently increase the magnitude of the absolute `angle` if the torque direction aligns with the current angular displacement.

6. **Side-Engine Reward Volatility**: Side engine actions (1 and 3) exhibit extreme reward volatility; while they can provide critical orientation corrections, uncoordinated or directionally incorrect use results in significant negative rewards.

7. **Angular Dampening vs. Orientation Correction**: Side engines effectively reduce `ang_vel` (rotational speed), but they do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

8. **The Drift-Tilt Feedback Loop**: Using the main engine to arrest $y\_vel$ or $x\_vel$ while at a significant `angle` creates a feedback loop where correcting one velocity component inevitably perturbs the other due to thrust vector decomposition.

9. **Action Switching Instability**: Rapidly toggling between the main engine (Action 2) and side engines (Actions 1 or 3) induces high-frequency oscillations in both the `angle` and $y\_vel$ state variables.

10. **Landing State Sensitivity**: Terminal stability is critically dependent on the state of all variables at the moment of touchdown; failure to simultaneously minimize `angle`, $|x\_vel|$, and $|y\_vel|$ during the transition to a contact state is the primary driver of catastrophic failure.

---

## 2026-07-02 04:32:15

---
1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained upward thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, active torque (Actions 1 or 3) is required to arrest angular velocity.

3. **Lateral Velocity Accumulation**: Main engine thrust (Action 2) applied at non-zero angles produces horizontal displacement; this lateral $x\_vel$ drift persists and must be managed to ensure terminal stability.

4. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute `angle` increases, the engine's capacity to counteract gravity decreases while lateral drift increases.

5. **Torque-Orientation Mismatch**: Applying side-engine torque (Actions 1 or 3) can inadvertently increase the magnitude of the absolute `angle` if the torque direction is misaligned with the current angular displacement.

6. **Side-Engine Reward Volatility**: Side engine actions (1 and 3) exhibit extreme reward volatility; uncoordinated use or applying torque to minor angular deviations often results in significant negative rewards.

7. **Angular Dampening vs. Orientation Correction**: Side engines effectively reduce `ang_vel` (rotational speed) but do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

8. **The Drift-Tilt Feedback Loop**: Using the main engine (Action 2) to arrest $y\_vel$ while at a significant `angle` creates a feedback loop where vertical correction inevitably perturbs the $x\_vel$ component.

9. **Landing State Sensitivity**: Terminal outcomes (SUCCESS vs. PARTIAL) are critically dependent on the simultaneous minimization of `angle`, $|x\_vel|$, and $|y\_vel|$ at the moment of leg contact.

10. **Contact-Phase Persistence**: The episode does not necessarily terminate immediately upon contact; a lander can maintain a contact state (both legs = 1.0) while still possessing non-zero lateral velocity or tilt.

---

## 2026-07-02 04:34:46

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained upward thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, active torque (Actions 1 or 3) is required to arrest angular velocity.

3. **Lateral Velocity Accumulation**: Main engine thrust (Action 2) applied at non-zero angles produces horizontal displacement; this lateral $x\_vel$ drift persists and must be managed to ensure terminal stability.

4. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute `angle` increases, the engine's capacity to counteract gravity decreases while lateral drift increases.

5. **Torque-Orientation Mismatch**: Applying side-engine torque (Actions 1 or 3) can inadvertently increase the magnitude of the absolute `angle` if the torque direction is misaligned with the current angular displacement.

6. **Phase-Dependent Reward Volatility**: Side-engine actions (1 and 3) exhibit extreme reward volatility; while typically penalized during descent, they can trigger massive positive reward spikes once leg contact is established.

7. **Angular Dampening vs. Orientation Correction**: Side engines effectively reduce `ang_vel` (rotational speed) but do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

8. **The Drift-Tilt Feedback Loop**: Using the main engine (Action 2) to arrest $y\_vel$ while at a significant `angle` creates a feedback loop where vertical correction inevitably perturbs the $x\_vel$ component.

9. **Landing State Sensitivity**: Terminal outcomes (SUCCESS vs. PARTIAL) are critically dependent on the simultaneous minimization of `angle`, $|x\_vel|$, and $|y\_vel|$ at the moment of leg contact.

10. **Contact-Phase Persistence and Reward Transition**: The episode does not necessarily terminate upon contact; a lander can maintain a contact state (legs = 1.0) for hundreds of steps, during which the reward signal shifts from descent penalties to high-magnitude positive values.

---

## 2026-07-02 04:37:07

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained upward thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, active torque (Actions 1 or 3) is required to arrest angular velocity.

3. **High-Inertia Lateral Velocity**: High $|x\_vel|$ exhibits significant momentum; reducing a high lateral velocity (as seen in Episode 2) is a slow, cumulative process that requires sustained, opposing thrust over an extended duration.

4. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute `angle` increases, the engine's capacity to counteract gravity decreases while lateral drift increases.

5. **Torque-Orientation Mismatch**: Applying side-engine torque (Actions 1 or 3) can inadvertently increase the magnitude of the absolute `angle` if the torque direction is misaligned with the current angular displacement.

6. **Phase-Dependent Reward Volatility**: Side-engine actions (1 and 3) exhibit reward volatility; while typically penalized during descent, they are critical for managing the state variables that dictate terminal success.

7. **Angular Dampening vs. Orientation Correction**: Side engines effectively reduce `ang_vel` (rotational speed) but do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

8. **The Drift-Tilt Feedback Loop**: Using the main engine (Action 2) to arrest $y\_vel$ while at a significant `angle` creates a feedback loop where vertical correction inevitably perturbs the $x\_vel$ component.

9. **Landing State Sensitivity**: Terminal outcomes are critically dependent on the simultaneous minimization of `angle`, $|x\_vel|$, and $|y\_vel|$ at the moment of leg contact.

10. **Extended Descent Dynamics**: The environment allows for very long-duration descents (1000+ steps) where the lander remains airborne at significant altitude, necessitating long-term management of accumulated lateral and angular deviations to reach a viable landing state.

---

## 2026-07-02 04:39:34

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained upward thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, active torque (Actions 1 or 3) is required to arrest angular velocity.

3. **High-Inertia Lateral Velocity**: High $|x\_vel|$ exhibits significant momentum; reducing lateral velocity is a slow, cumulative process that requires sustained, opposing thrust over an extended duration.

4. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute `angle` increases, the engine's capacity to counteract gravity decreases while lateral drift increases.

5. **Torque-Orientation Mismatch**: Applying side-engine torque (Actions 1 or 3) can inadvertently increase the magnitude of the absolute `angle` if the torque direction is misaligned with the current angular displacement.

6. **Side-Engine Reward Volatility**: Side-engine actions (1 and 3) exhibit reward volatility; while typically penalized during descent, they are critical for managing the state variables that dictate terminal success.

7. **Angular Dampening vs. Orientation Correction**: Side engines effectively reduce `ang_vel` (rotational speed) but do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

8. **The Drift-Tilt Feedback Loop**: Using the main engine (Action 2) to arrest $y\_vel$ while at a significant `angle` creates a feedback loop where vertical correction inevitably perturbs the $x\_vel$ component.

9. **Landing State Sensitivity**: Terminal outcomes are critically dependent on the simultaneous minimization of `angle`, $|x\_vel|$, and $|y\_vel|$ at the moment of leg contact.

10. **Post-Contact State Evolution**: Once leg contact is established (e.g., `left_leg_contact` and `right_leg_contact` both equal 1.0), the simulation continues to allow for state manipulation; the lander can continue to refine its $angle$ and $x\_vel$ while remaining in a grounded state.

---

## 2026-07-02 04:46:07

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained upward thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, active torque (Actions 1 or 3) is required to arrest angular velocity.

3. **High-Inertia Lateral Velocity**: High $|x\_vel|$ exhibits significant momentum; reducing lateral velocity is a slow, cumulative process that requires sustained, opposing thrust over an extended duration.

4. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute `angle` increases, the engine's capacity to counteract gravity decreases while lateral drift increases.

5. **Torque-Orientation Mismatch**: Applying side-engine torque (Actions 1 or 3) can inadvertently increase the magnitude of the absolute `angle` if the torque direction is misaligned with the current angular displacement.

6. **Side-Engine Reward Volatility**: Side-engine actions (1 and 3) exhibit reward volatility; while typically penalized during descent, they are critical for managing the state variables that dictate terminal success.

7. **Angular Dampening vs. Orientation Correction**: Side engines effectively reduce `ang_vel` (rotational speed) but do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

8. **The Drift-Tilt-Velocity Feedback Loop**: Using the main engine (Action 2) to arrest $y\_vel$ while at a significant `angle` creates a feedback loop where vertical correction inevitably perturbs the $x\_vel$ component.

9. **Landing State Sensitivity**: Terminal outcomes are critically dependent on the simultaneous minimization of `angle`, $|x\_vel|$, and $|y\_vel|$ at the moment of leg contact.

10. **Altitude-Lateral Velocity Decoupling**: Maintaining vertical stability ($y\_pos$ and $y\_vel$) through main engine modulation does not prevent the monotonic divergence of lateral position ($x\_pos$) and lateral velocity ($x\_vel$).

---

## 2026-07-02 04:49:09

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained upward thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, active torque (Actions 1 or 3) is required to arrest angular velocity.

3. **High-Inertia Lateral Velocity**: High $|x\_vel|$ exhibits significant momentum; reducing lateral velocity is a slow, cumulative process that requires sustained, opposing thrust over an extended duration.

4. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute `angle` increases, the engine's capacity to counteract gravity decreases while lateral drift increases.

5. **Torque-Orientation Mismatch**: Applying side-engine torque (Actions 1 or 3) can inadvertently increase the magnitude of the absolute `angle` if the torque direction is misaligned with the current angular displacement.

6. **Side-Engine Reward Volatility**: Side-engine actions (1 and 3) exhibit high reward volatility; while critical for managing orientation, they often incur heavy penalties during descent phases.

7. **Angular Dampening vs. Orientation Correction**: Side engines effectively reduce `ang_vel` (rotational speed) but do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

8. **The Drift-Tilt-Velocity Feedback Loop**: Using the main engine (Action 2) to arrest $y\_vel$ while at a significant `angle` creates a feedback loop where vertical correction inevitably perturbs the $x\_vel$ component.

9. **Landing State Sensitivity**: Terminal outcomes are critically dependent on the simultaneous minimization of `angle`, $|x\_vel|$, and $|y\_vel|$ at the moment of leg contact.

10. **Ground Boundary Criticality**: The $y\_pos$ zero-crossing is a high-sensitivity boundary; states where $y\_pos$ approaches or falls below zero are associated with extreme reward volatility and potential crash-induced penalties.

---

## 2026-07-02 04:51:54

---
1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained upward thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, active torque (Actions 1 or 3) is required to arrest angular velocity.

3. **High-Inertia Lateral Velocity**: Significant initial lateral momentum (as seen in the high $|x\_vel|$ of Episode 2) is slow to arrest, requiring sustained, opposing thrust over an extended duration to counteract the drift.

4. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while lateral drift increases.

5. **Torque-Orientation Mismatch**: Applying side-engine torque (Actions 1 or 3) can inadvertently increase the magnitude of the absolute `angle` if the torque direction is misaligned with the current angular displacement.

6. **Side-Engine Reward Volatility**: Side-engine actions (1 and 3) exhibit high reward volatility; while critical for managing orientation, they often incur heavy penalties during descent or stabilization phases.

7. **Angular Dampening vs. Orientation Correction**: Side engines effectively reduce `ang_vel` (rotational speed) but do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

8. **The Drift-Tilt-Velocity Feedback Loop**: Using the main engine (Action 2) to arrest $y\_vel$ while at a significant `angle` creates a feedback loop where vertical correction inevitably perturbs the $x\_vel$ component.

9. **Landing State Multi-Variate Sensitivity**: Terminal outcomes are critically dependent on the simultaneous minimization of `angle`, $|x\_vel|$, $|y\_vel|$, and $|x\_pos|$ at the moment of leg contact.

10. **Unstable Hovering Persistence**: The physics of the system permit "drifting hover" trajectories where the lander successfully stabilizes $y\_vel$, but unarrested lateral momentum and angular tilt lead to a continuous, cumulative drift away from the landing target.

---

## 2026-07-02 04:54:15

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained upward thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, active torque (Actions 1 or 3) is required to arrest angular velocity.

3. **High-Inertia Lateral Velocity**: Significant initial lateral momentum (e.g., high negative $x\_vel$ in Episode 2) is extremely difficult to arrest, requiring sustained, opposing thrust that often conflicts with the necessity for vertical stabilization.

4. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while lateral drift increases.

5. **Torque-Orientation Mismatch**: Applying side-engine torque (Actions 1 or 3) can inadvertently increase the magnitude of the absolute `angle` if the torque direction is misaligned with the current angular displacement.

6. **Side-Engine Reward Volatility**: Side-engine actions (1 and 3) exhibit high reward volatility; while critical for managing orientation, they often incur heavy penalties during descent or stabilization phases.

7. **Angular Dampening vs. Orientation Correction**: Side engines effectively reduce `ang_vel` (rotational speed) but do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

8. **The Drift-Tilt-Velocity Feedback Loop**: Using the main engine (Action 2) to arrest $y\_vel$ while at a significant `angle` creates a feedback loop where vertical correction inevitably perturbs the $x\_vel$ component.

9. **Landing State Multi-Variate Sensitivity**: Terminal outcomes are critically dependent on the simultaneous minimization of `angle`, $|x\_vel|$, $|y\_vel|$, and $|x\_pos|$ at the moment of leg contact; failure can occur even with low angular error if velocities are too high, or if the landing tilt is excessive (as seen in Episode 2).

10. **Rotational Runaway**: High angular velocity (`ang_vel`) can enter a runaway state where side-engine thrusts fail to arrest the rotation, leading to a rapid, uncontrollable increase in `angle` that results in a non-upright impact (as seen in the terminal phase of Episode 2).

---

## 2026-07-02 04:57:16

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent rapid, uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, active torque (Actions 1 or 3) is required to arrest the angular velocity.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Torque-Induced Angular Deviation**: Using side engines (Actions 1 or 3) to correct lateral drift or $x\_vel$ inherently produces torque, which frequently causes the `angle` to deviate significantly from zero.

5. **Side-Engine Reward Volatility**: Side-engine actions exhibit high reward volatility; while critical for managing orientation and lateral momentum, they often incur heavy penalties during descent due to the angular deviations they induce.

6. **Angular Dampening vs. Orientation Correction**: Side engines effectively reduce `ang_vel` (rotational speed) but do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **The Drift-Tilt-Velocity Feedback Loop**: Using the main engine (Action 2) to arrest $y\_vel$ while at a non-zero `angle` creates a feedback loop where vertical correction inevitably perturbs the $x\_vel$ component.

8. **Landing State Multi-Variate Sensitivity**: Terminal outcomes are critically dependent on the simultaneous minimization of $x\_pos$, $x\_vel$, $y\_vel$, and `angle` at the moment of leg contact; failure to converge all four parameters can result in a non-successful landing.

9. **The Velocity-Orientation Conflict**: In high-momentum scenarios (e.g., the high initial $x\_vel$ observed in Episode 2), correcting large lateral velocities through side-engine thrust creates a conflict where the lander can achieve translational stabilization only at the expense of significant angular error.

10. **Rotational Runaway**: High angular velocity (`ang_vel`) can enter a runaway state where side-engine thrusts become insufficient to arrest the rotation, leading to a rapid, uncontrollable increase in `angle` that results in a non-upright impact.

---

## 2026-07-02 05:02:02

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, active torque (Actions 1 or 3) is required to arrest the angular velocity.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Lateral-Torque Coupling**: Using side engines (Actions 1 or 3) to counteract lateral velocity ($x\_vel$) inherently produces torque, which causes the `angle` to deviate from zero.

5. **Momentum-Orientation Conflict**: In scenarios with high initial lateral velocity (e.g., $x\_vel \approx 0.7$ in Episode 2), correcting momentum through side-engine thrust creates a conflict where translational stabilization requires extreme angular deviations.

6. **Angular Dampening vs. Orientation Correction**: Side engines effectively reduce `ang_vel` (rotational speed) but do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **Contact-Event Reward Dependency**: Significant rewards are heavily contingent on the lander's $x\_vel$, $y\_vel$, and `angle` at the precise moment `left_leg_contact` or `right_leg_contact` transitions to 1.0.

8. **The Descent Feedback Loop**: Using the main engine (Action 2) to arrest $y\_vel$ while at a non-zero `angle` creates a feedback loop where vertical correction inevitably perturbs the $x\_vel$ component.

9. **Rotational Runaway**: High angular velocity (`ang_vel`) can enter a runaway state where side-engine thrusts become insufficient to arrest the rotation, leading to a rapid, uncontrollable increase in `angle`.

10. **Landing State Multi-Variate Sensitivity**: Terminal success is critically dependent on the simultaneous minimization of $x\_vel$, $y\_vel$, and `angle` at the moment of leg contact; failure to converge these parameters during the contact event results in failure.

---

## 2026-07-02 05:03:54

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, active torque (Actions 1 or 3) is required to arrest the angular velocity.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Lateral-Torque Coupling**: Using side engines (Actions 1 or 3) to counteract lateral velocity ($x\_vel$) inherently produces torque, which causes the `angle` to deviate from zero.

5. **Momentum-Orientation Conflict**: In scenarios with high initial lateral velocity (e.g., $x\_vel \approx -0.41$ in Episode 2), correcting momentum through side-engine thrust creates a conflict where translational stabilization requires extreme angular deviations.

6. **Angular Dampening vs. Orientation Correction**: Side engines effectively reduce `ang_vel` (rotational speed) but do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist (as seen in the partial success of Episode 1).

7. **Contact-Event Reward Dependency**: Significant rewards are heavily contingent on the lander's $x\_vel$, $y\_vel$, and `angle` at the precise moment `left_leg_contact` or `right_leg_contact` transitions to 1.0.

8. **The Descent Feedback Loop**: Using the main engine (Action 2) to arrest $y\_vel$ while at a non-zero `angle` creates a feedback loop where vertical correction inevitably perturbs the $x\_vel$ component.

9. **Rotational Runaway**: High angular velocity (`ang_vel`) can enter a runaway state where side-engine thrusts become insufficient to arrest the rotation, leading to a rapid, uncontrollable increase in `angle`.

10. **Landing State Multi-Variate Sensitivity**: Terminal success is critically dependent on the simultaneous minimization of $x\_vel$, $y\_vel$, and `angle` at the moment of leg contact; failure to arrest both `angle` and `ang_vel` (as seen in the failure of Episode 2) results in a failed landing.

---

## 2026-07-02 05:05:40

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; once rotation begins, active torque (Actions 1 or 3) is required to arrest the angular velocity.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Lateral-Torque Coupling**: Using side engines (Actions 1 or 3) to counteract lateral velocity ($x\_vel$) inherently produces torque, which causes the `angle` to deviate from zero.

5. **Momentum-Orientation Conflict**: Scenarios with high initial lateral velocity (e.g., $x\_vel \approx 0.65$ in Episode 2) create a conflict where correcting translational momentum through side-engine thrust leads to significant increases in `angle` and `ang_vel`.

6. **Angular Dampening vs. Orientation Correction**: Side engines effectively reduce `ang_vel` (rotational speed) but do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **Contact-Event Reward Dependency**: Significant rewards or penalties are determined by the specific values of $x\_vel$, $y\_vel$, and `angle` at the precise moment `left_leg_contact` or `right_leg_contact` transitions to 1.0.

8. **Cumulative Orientation Drift**: Long-duration flights (as seen in Episode 1) can experience a slow, cumulative increase in `angle` and `ang_vel` if the control strategy prioritizes managing $y\_vel$ and $x\_vel$ over strict orientation stabilization.

9. **Rotational Runaway**: High angular velocity (`ang_vel`) can enter a runaway state where side-engine thrusts become insufficient to arrest the rotation, leading to a rapid, uncontrollable increase in `angle`.

10. **Landing State Multi-Variate Sensitivity**: Terminal success is critically dependent on the simultaneous minimization of $x\_vel$, $y\_vel$, and `angle` at the moment of leg contact; failing to arrest even one component (such as the high `angle` and `ang_vel` observed in the Episode 2 failure) results in a failed landing.

---

## 2026-07-02 05:08:27

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque (Actions 1 or 3) is required to arrest the angular velocity once rotation begins.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Lateral-Torque Coupling**: Using side engines (Actions 1 or 3) to counteract lateral velocity ($x\_vel$) inherently produces torque, which causes the `angle` to deviate from zero.

5. **Momentum-Orientation Conflict**: Scenarios with high initial lateral velocity create a conflict where correcting translational momentum through side-engine thrust leads to significant increases in `angle` and `ang_vel`.

6. **Angular Dampening vs. Orientation Correction**: Side engines effectively reduce `ang_vel` (rotational speed) but do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **Post-Contact Velocity Attenuation**: Upon leg contact, all velocity components ($x\_vel, y\_vel, ang\_vel$) undergo rapid attenuation, indicating a physics transition from free-flight to ground-interaction/friction.

8. **Cumulative Orientation Drift**: Long-duration flights can experience a slow, cumulative increase in `angle` and `ang_vel` if the control strategy prioritizes managing $y\_vel$ and $x\_vel$ over strict orientation stabilization.

9. **Rotational Runaway**: High angular velocity (`ang_vel`) can enter a runaway state where side-engine thrusts become insufficient to arrest the rotation, leading to a rapid, uncontrollable increase in `angle`.

10. **Landing State Multi-Variate Sensitivity**: A successful landing is critically dependent on the simultaneous minimization of $x\_pos, y\_pos, x\_vel, y\_vel, angle,$ and $ang\_vel$ at the moment of contact; failing to converge on even one variable (such as the $x\_pos$ offset observed in the Episode 2 landing) results in a Partial outcome.

---

## 2026-07-02 05:10:49

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque (Actions 1 or 3) is required to arrest the angular velocity once rotation begins.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Lateral-Torque Coupling**: Using side engines (Actions 1 or 3) to counteract lateral velocity ($x\_vel$) inherently produces torque, which causes the `angle` to deviate from zero.

5. **Momentum-Orientation Conflict**: Scenarios with high initial lateral velocity create a conflict where correcting translational momentum through side-engine thrust leads to significant increases in `angle` and `ang_vel`.

6. **Angular Dampening vs. Orientation Correction**: Side engines effectively reduce `ang_vel` (rotational speed) but do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **Post-Contact Ground Constraint**: Upon leg contact (contact status = 1.0), the physics transitions from free-flight to a ground-interaction regime; while engine thrusts still exert influence, velocities ($x\_vel, y\_vel, ang\_vel$) are heavily attenuated by ground friction and contact constraints.

8. **Cumulative Orientation Drift**: Long-duration flights can experience a slow, cumulative increase in `angle` and `ang_vel` if the control strategy prioritizes managing $y\_vel$ and $x\_vel$ over strict orientation stabilization.

9. **Rotational Runaway**: High angular velocity (`ang_vel`) can enter a runaway state where side-engine thrusts become insufficient to arrest the rotation, leading to a rapid, uncontrollable increase in `angle`.

10. **Landing State Multi-Variate Sensitivity**: A successful landing is critically dependent on the simultaneous minimization of $x\_pos, y\_pos, x\_vel, y\_vel, angle,$ and $ang\_vel$ at the moment of contact; failing to converge on even one variable results in a Partial outcome.

---

## 2026-07-02 05:15:50

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque (Actions 1 or 3) is required to arrest the angular velocity once rotation begins.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Lateral-Torque Coupling**: Using side engines (Actions 1 or 3) to counteract lateral velocity ($x\_vel$) inherently produces torque, which causes the `angle` to deviate from zero.

5. **Momentum-Orientation Conflict**: Scenarios with high initial lateral velocity create a conflict where correcting translational momentum through side-engine thrust leads to significant increases in `angle` and `ang_vel`.

6. **Angular Dampening vs. Orientation Correction**: Side engines effectively reduce `ang_vel` (rotational speed) but do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **Uncontrolled Lateral Translation**: High initial $x\_vel$ or improper `angle` during main engine firing (Action 2) results in significant $x\_pos$ accumulation; the observed control strategies struggle to arrest this horizontal drift, leading to large lateral displacements.

8. **Cumulative Orientation Drift**: Long-duration flights can experience a slow, cumulative increase in `angle` and `ang_vel` if the control strategy prioritizes managing $y\_vel$ and $x\_vel$ over strict orientation stabilization.

9. **Rotational Runaway**: High angular velocity (`ang_vel`) can enter a runaway state where side-engine thrusts become insufficient to arrest the rotation, leading to a rapid, uncontrollable increase in `angle`.

10. **Landing State Multi-Variate Sensitivity**: A successful landing is critically dependent on the simultaneous minimization of $x\_pos, y\_pos, x\_vel, y\_vel, angle,$ and $ang\_vel$ at the moment of contact; failing to converge on even one variable results in a Partial outcome or terminal failure.

---

## 2026-07-02 05:17:53

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque (Actions 1 or 3) is required to arrest the angular velocity once rotation begins.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Lateral-Torque Coupling**: Using side engines (Actions 1 or 3) to counteract lateral velocity ($x\_vel$) inherently produces torque, which causes the `angle` and `ang_vel` to deviate from zero.

5. **Translational-Rotational Conflict**: High initial translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust to arrest momentum often induces significant increases in `angle` and `ang_vel`, potentially destabilizing the craft.

6. **Angular Dampening vs. Orientation Correction**: Side engines effectively reduce `ang_vel` (rotational speed) but do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **Lateral Drift Accumulation**: Even during controlled descent, small errors in `angle` during main engine firing (Action 2) lead to a continuous accumulation of $x\_pos$, making precise horizontal landing a long-term stability challenge.

8. **Cumulative Orientation Drift**: Long-duration flights can experience a slow, cumulative increase in `angle` and `ang_vel` if the control strategy prioritizes managing $y\_vel$ and $x\_vel$ over strict orientation stabilization.

9. **Rotational Runaway**: In high-energy states (high initial $ang\_vel$ or $x\_vel$), the magnitude of torque required to arrest rotation can cause `ang_vel` to diverge, leading to a runaway state where side-engine thrusts become insufficient to stabilize the `angle`.

10. **Landing State Multi-Variate Sensitivity**: A successful landing is critically dependent on the simultaneous minimization of $x\_pos, y\_pos, x\_vel, y\_vel, angle,$ and $ang\_vel$ at the moment of contact; failing to converge on even one variable (such as high lateral velocity or significant tilt) results in a Partial or Failure outcome.

---

## 2026-07-02 05:20:21

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque (Actions 1 or 3) is required to arrest the angular velocity once rotation begins.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Lateral-Torque Coupling**: Using side engines (Actions 1 or 3) to counteract lateral velocity ($x\_vel$) inherently produces torque, which causes the `angle` and `ang_vel` to deviate from zero.

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust to arrest momentum often induces significant increases in `angle` and `ang_vel`, potentially destabilizing the craft.

6. **Angular Dampening vs. Orientation Correction**: Side engines effectively reduce `ang_vel` (rotational speed) but do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **Lateral Drift Accumulation**: Even during controlled descent, small errors in `angle` during main engine firing (Action 2) lead to a continuous accumulation of $x\_pos$, making precise horizontal landing a long-term stability challenge.

8. **Cumulative Orientation Drift**: Long-duration flights can experience a slow, cumulative increase in `angle` and `ang_vel` if the control strategy prioritizes managing $y\_vel$ and $x\_vel$ over strict orientation stabilization.

9. **Rotational Runaway**: In high-energy states (high initial $ang\_vel$ or $x\_vel$), the magnitude of torque required to arrest rotation can cause `ang_vel` to diverge, leading to a runaway state where side-engine thrusts become insufficient to stabilize the `angle`.

10. **Impact-State Multi-Variate Sensitivity**: Landing outcomes (Success, Partial, or Failure) are critically dependent on the simultaneous minimization of $x\_pos, y\_pos, x\_vel, y\_vel, angle,$ and $ang\_vel$ at the moment of leg contact; high residual velocities or significant tilt at the moment of contact can result in failure or partial success even if leg contact is sustained.

---

## 2026-07-02 05:22:57

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque (Actions 1 or 3) is required to arrest the angular velocity once rotation begins.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Lateral-Torque Coupling**: Using side engines (Actions 1 or 3) to counteract lateral velocity ($x\_vel$) inherently produces torque, which causes the `angle` and `ang_vel` to deviate from zero.

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust to arrest momentum often induces significant increases in `angle` and `ang_vel`, potentially destabilizing the craft.

6. **Angular Dampening vs. Orientation Correction**: Side engines effectively reduce `ang_vel` (rotational speed) but do not immediately reset the `angle` to zero, allowing states with low rotational velocity but significant tilt to persist.

7. **Drift Accumulation**: Small errors in `angle` during main engine firing lead to continuous accumulation of $x\_pos$, while prioritizing $y\_vel$ management over orientation can lead to a slow, cumulative increase in `angle` and `ang_vel`.

8. **Rotational Runaway**: In high-energy states (high initial $ang\_vel$ or $x\_vel$), the magnitude of torque required to arrest rotation can cause `ang_vel` to diverge, leading to a runaway state where side-engine thrusts become insufficient to stabilize the `angle`.

9. **Ground-Contact Equilibrium**: Once leg contact is established (`leg_contact`=1), the environment is highly sensitive to any action that disrupts the contact state; actions that break contact (e.g., Action 1 causing a leg contact to drop to 0.0) result in extreme negative rewards, whereas actions that stabilize or restore contact can yield high positive rewards.

10. **Impact-State Multi-Variate Sensitivity**: Landing outcomes are critically dependent on the simultaneous minimization of $x\_pos, y\_pos, x\_vel, y\_vel, angle,$ and $ang\_vel$ at the moment of leg contact; high residual velocities or significant tilt at the moment of contact can result in failure or partial success even if contact is sustained.

---

## 2026-07-02 05:25:02

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque (Actions 1 or 3) is required to arrest the angular velocity once rotation begins.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Lateral-Torque Coupling**: Using side engines (Actions 1 or 3) to counteract lateral velocity ($x\_vel$) inherently produces torque, which causes the `angle` and `ang_vel` to deviate from zero.

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust to arrest momentum often induces significant increases in `angle` and `ang_vel`, potentially destabilizing the craft.

6. **Side-Engine Instability Penalty**: The application of side engines (Actions 1 or 3) frequently incurs immediate negative rewards due to the resulting increases in `ang_vel` and `angle`, even when intended for lateral correction.

7. **Rotational Runaway**: In high-energy states (high initial $ang\_vel$ or $x\_vel$), the magnitude of torque required to arrest rotation can cause `ang_vel` to diverge, leading to a runaway state where side-engine thrusts become insufficient to stabilize the `angle`.

8. **Post-Contact Equilibrium Sensitivity**: Once leg contact is established (`leg_contact`=1), the environment is sensitive to actions that disrupt the contact state; continued use of side engines (Actions 1 or 3) can induce instability or negative rewards if they disturb the established landing equilibrium.

9. **Terminal Velocity and Angular Thresholds**: Landing outcomes are not determined by contact alone; high residual $y\_vel$ or $ang\_vel$ at the moment of contact can trigger catastrophic failure penalties (e.g., -100 reward), even if `leg_contact` is sustained.

10. **Simultaneous State Minimization**: Successful landings depend on the concurrent minimization of $x\_pos, y\_pos, x\_vel, y\_vel, angle,$ and $ang\_vel$ at the moment of leg contact; high values in any single velocity or angular component can negate the benefits of established contact.

---

## 2026-07-02 05:28:48

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque (Actions 1 or 3) is required to arrest the angular velocity once rotation begins.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Lateral-Torque Coupling**: Using side engines (Actions 1 or 3) to counteract lateral velocity ($x\_vel$) inherently produces torque, which causes the `angle` and `ang_vel` to deviate from zero.

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust to arrest momentum often induces significant increases in `angle` and `ang_vel`, potentially destabilizing the craft.

6. **Side-Engine Instability Penalty**: The application of side engines (Actions 1 or 3) frequently incurs immediate negative rewards due to the resulting increases in `ang_vel` and `angle`, even when intended for lateral correction.

7. **Rotational Runaway**: In high-energy states (high initial $ang\_vel$ or $x\_vel$), the magnitude of torque required to arrest rotation can cause `ang_vel` to diverge, leading to a runaway state where side-engine thrusts become insufficient to stabilize the `angle`.

8. **Post-Contact Engine-Induced Instability**: Once leg contact is established (`leg_contact`=1), the application of side engines (Actions 1 or 3) acts as a primary destabilizing force. This can cause a rapid, uncontrolled increase in `ang_vel` that converts a grounded state into a catastrophic failure.

9. **Extended Terminal Failure Window**: The catastrophic failure penalty (-100) is not strictly limited to the instant of impact; the environment monitors stability for a duration after contact, where high residual or induced `ang_vel` and `angle` will trigger failure even if `leg_contact` remains 1.

10. **Simultaneous State Minimization**: Successful landings depend on the concurrent minimization of $x\_pos, y\_pos, x\_vel, y\_vel, angle,$ and $ang\_vel$ at the moment of leg contact; high values in any single velocity or angular component can negate the benefits of established contact.

---

## 2026-07-02 05:30:29

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque (Actions 1 or 3) is required to arrest the angular velocity once rotation begins.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical ($\cos(\text{angle})$) and horizontal ($\sin(\text{angle})$) components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Lateral-Torque Coupling**: Using side engines (Actions 1 or 3) to counteract lateral velocity ($x\_vel$) inherently produces torque, which causes the `angle` and `ang_vel` to deviate from zero.

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust to arrest momentum often induces significant increases in `angle` and `ang_vel`, potentially destabilizing the craft.

6. **Side-Engine Instability Penalty**: The application of side engines (Actions 1 or 3) frequently incurs immediate negative rewards due to the resulting increases in `ang_vel` and `angle`, even when intended for lateral correction.

7. **Rotational Runaway**: In high-energy states (high initial $ang\_vel$ or $x\_vel$), the magnitude of torque required to arrest rotation can cause `ang_vel` to diverge, leading to a runaway state where side-engine thrusts become insufficient to stabilize the `angle`.

8. **Post-Contact Grounding Transition**: Once a single leg establishes contact, the craft enters a transitional state where it must manage torque and lateral drift to successfully transition from single-leg contact to a dual-leg grounded state (`leg_contact` = [1, 1]).

9. **Dual-Leg Success Requirement**: The terminal success reward (+100) is strictly contingent upon both `left_leg_contact` and `right_leg_contact` being 1.0, achieved alongside the near-simultaneous minimization of $x\_vel, y\_vel, angle,$ and $ang\_vel$.

10. **Terminal Failure Modes**: The catastrophic failure penalty (-100) is triggered by either a high-velocity impact without established leg contact or by failing to maintain orientation and stability during the post-contact phase.

---

## 2026-07-02 05:32:25

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque (Actions 1 or 3) is required to arrest angular velocity once rotation begins.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Lateral-Torque Coupling**: Using side engines (Actions 1 or 3) to counteract lateral velocity ($x\_vel$) inherently produces torque, which causes the `angle` and `ang_vel` to deviate from zero.

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust to arrest momentum often induces significant increases in `angle` and `ang_vel`, potentially destabilizing the craft.

6. **Rotational Runaway**: In high-energy states, the magnitude of torque required to arrest rotation can cause `ang_vel` to diverge, leading to a runaway state where side-engine thrusts become insufficient to stabilize the `angle`.

7. **Side-Engine Instability Penalty**: The application of side engines (Actions 1 or 3) frequently incurs immediate negative rewards due to the resulting increases in `ang_vel` and `angle`, even when intended for lateral correction.

8. **Single-Leg Pivot Dynamics**: Once a single leg establishes contact (`leg_contact` = [1,0] or [0,1]), the craft transitions from free-flight to a pendulum-like state. This contact point acts as a pivot, significantly amplifying the angular torque generated by both side engines and the main engine.

9. **Post-Contact Angular Volatility**: The transition to single-leg contact can induce sudden, high-magnitude spikes in `ang_vel` due to the pivot-point physics. Successful landing requires immediate and precise damping of this new rotational energy to transition to a stable dual-leg state.

10. **Terminal Success and Failure Modes**: The terminal success reward (+100) is strictly contingent upon dual-leg contact (`leg_contact` = [1, 1]) achieved alongside near-simultaneous minimization of all velocities and orientation. Failure (-100) is triggered by high-velocity impact or an inability to stabilize the craft during the post-contact pivot phase.

---

## 2026-07-02 05:34:08

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Side-Engine Damping and Lateral Drift**: While side engines (Actions 1 or 3) can be used to dampen `ang_vel`, they simultaneously induce lateral velocity ($x\_vel$) and increase the magnitude of the `angle`.

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust to arrest momentum often induces significant increases in `angle` and `ang_vel`, potentially destabilizing the craft.

6. **Rotational Runaway**: In high-energy states, if `ang_vel` is not immediately arrested, the craft can enter a state where angular velocity diverges, making the orientation uncontrollable.

7. **Side-Engine Instability Penalty**: The application of side engines (Actions 1 or 3) frequently incurs immediate negative rewards due to the resulting increases in `ang_vel` and `angle`, even when intended for stabilization.

8. **Single-Leg Pivot Dynamics**: Once a single leg establishes contact (`leg_contact` = [1,0] or [0,1]), the craft transitions to a pendulum-like state. This contact point acts as a pivot, significantly amplifying the angular torque generated by both side engines and the main engine.

9. **Post-Contact Angular Divergence**: The transition to single-leg contact is a critical bifurcation point; if the craft possesses significant `ang_vel` at the moment of contact, the pivot dynamics can cause a rapid, catastrophic divergence in `angle` and `ang_vel`.

10. **Terminal Success and Failure Modes**: Terminal success (+100) is strictly contingent upon dual-leg contact (`leg_contact` = [1, 1]) achieved with near-simultaneous minimization of all velocities. Failure (-100) is triggered by high-velocity impact or an inability to arrest rotation during the post-contact pivot phase.

---

## 2026-07-02 05:38:04

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest rotation, though they often induce immediate angular changes.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Side-Engine Induced Drift**: The application of side engines (Actions 1 or 3) induces lateral velocity ($x\_vel$) and increases the magnitude of the `angle`.

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust to arrest momentum often induces significant increases in `angle` and `ang_vel`, potentially destabilizing the craft.

6. **Rotational Runaway**: In high-energy states, if `ang_vel` is not immediately arrested, the craft can enter a state where angular velocity diverges, making the orientation uncontrollable.

7. **Side-Engine Instability Penalty**: The application of side engines (Actions 1 or 3) frequently incurs immediate negative rewards due to the resulting increases in `ang_vel` and `angle`, even when intended for stabilization.

8. **Fulcrum Dynamics (Contact-Induced Torque)**: Once any leg establishes contact (`leg_contact` = [1,0] or [0,1]), the contact point acts as a pivot. Applying engines while grounded—especially side engines—generates extreme angular torque, causing a rapid and potentially catastrophic increase in `ang_vel`.

9. **Post-Contact Angular Divergence**: The transition to contact (single or dual leg) is a critical bifurcation point. Even after achieving dual-leg contact ([1,1]), the continued use of side engines can drive angular velocity to extreme levels due to the pivot effect.

10. **Terminal Success and Failure Modes**: Terminal success (+100) is achieved through dual-leg contact (`leg_contact` = [1, 1]). Failure (-100) is triggered by high-velocity impact or an inability to manage the rapid angular divergence that occurs during the post-contact phase.

---

## 2026-07-02 05:39:40

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest rotation, though they often induce immediate angular changes.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Side-Engine Induced Drift**: The application of side engines (Actions 1 or 3) induces lateral velocity ($x\_vel$) and increases the magnitude of the `angle`.

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust to arrest momentum often induces significant increases in `angle` and `ang_vel`, potentially destabilizing the craft.

6. **Rotational Runaway**: In high-energy states, if `ang_vel` is not immediately arrested, the craft can enter a state where angular velocity diverges, making the orientation uncontrollable.

7. **Grounded Side-Engine Penalty Scaling**: The negative reward incurred by side-engine use (Actions 1 or 3) scales significantly higher once any leg contact is established, penalizing the high-torque states created when thrust is applied against the terrain.

8. **Single-Leg Fulcrum Dynamics**: A single leg contact (`leg_contact` = [1,0] or [0,1]) creates a pivot point; applying side engines in this state transforms the lander into a lever, inducing rapid angular acceleration (`ang_vel`) that is much more aggressive than in free flight.

9. **Contact-Phase Divergence**: The transition to contact (single or dual leg) is a critical bifurcation point; the combination of residual angular momentum and the pivot effect often leads to rapid, non-linear divergence of `angle` and `ang_vel`.

10. **Terminal Success and Failure Modes**: Terminal success (+100) is achieved through dual-leg contact (`leg_contact` = [1, 1]). Failure (-100) is triggered by high-velocity impact or an inability to manage the rapid angular divergence that occurs during the post-contact phase.

---

## 2026-07-02 05:41:59

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest rotation, though they often induce immediate angular changes.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Side-Engine Induced Drift**: The application of side engines (Actions 1 or 3) induces lateral velocity ($x\_vel$) and increases the magnitude of the `angle`.

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust to arrest momentum often induces significant increases in `angle` and `ang_vel`, potentially destabilizing the craft.

6. **Rotational Runaway**: In high-energy states, if `ang_vel` is not immediately arrested, the craft can enter a state where angular velocity diverges, making the orientation uncontrollable.

7. **Non-Linear Reward Scaling in Contact**: Once contact is established (`leg_contact` = [1,1]), the reward magnitude scales significantly; side-engine applications that previously cost ~ -2.0 can now incur penalties exceeding -15.0, while successful stabilization can yield rewards exceeding +20.0.

8. **Grounded Torque Amplification**: Applying side engines (Actions 1 or 3) while in the contact phase generates much more violent angular acceleration than in free flight, rapidly inducing high-torque states that are difficult to arrest.

9. **Momentum-Contact Sensitivity**: The transition to a grounded state acts as a high-sensitivity bifurcation point where residual $x\_vel$, $y\_vel$, or $ang\_vel$ disproportionately increases the probability of catastrophic negative rewards.

10. **Post-Contact Stability Window**: Successful landing requires maintaining an extremely narrow equilibrium of near-zero angular velocity and vertical velocity; any thrusting that disrupts this state during the contact phase leads to immediate, high-magnitude reward divergence.

---

## 2026-07-02 05:43:38

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest rotation, though they often induce immediate angular changes.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Side-Engine Lateral Management**: Side engines (Actions 1 or 3) serve a dual purpose: they are used to manage angular velocity but are also the primary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust to arrest momentum often induces significant increases in `angle` and `ang_vel`, potentially destabilizing the craft.

6. **Rotational Runaway**: In high-energy states, if `ang_vel` is not immediately arrested, the craft can enter a state where angular velocity diverges, making the orientation uncontrollable.

7. **Extreme Reward Bifurcation in Contact**: Once leg contact is established (`leg_contact` = 1), the reward landscape shifts from gradual scaling to extreme divergence; corrective side-engine applications that fail to stabilize the craft can incur penalties exceeding -15.0, while successful orientation stabilization can trigger terminal rewards of +100.0.

8. **Grounded Torque Amplification**: Applying side engines (Actions 1 or 3) while in the contact phase generates significantly more violent angular acceleration than in free flight, rapidly inducing high-torque states.

9. **Momentum-Contact Sensitivity**: The transition to a grounded state acts as a high-sensitivity bifurcation point where residual $x\_vel$, $y\_vel$, or $ang\_vel$ disproportionately increases the probability of catastrophic negative rewards.

10. **Post-Contact Orientation Priority**: Following contact, the physics requirements shift from altitude/velocity management to the near-total elimination of `ang_vel` and `angle`; maintaining this narrow equilibrium is the sole determinant of a successful landing reward.

---

## 2026-07-02 05:45:29

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest rotation, though they often induce immediate angular changes.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Side-Engine Lateral Management**: Side engines (Actions 1 or 3) serve a dual purpose: they are used to manage angular velocity but are also the primary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust to arrest momentum often induces significant increases in `angle` and `ang_vel`, potentially destabilizing the craft.

6. **Rotational Runaway**: In high-energy states, if `ang_vel` is not immediately arrested, the craft can enter a state where angular velocity diverges, making the orientation uncontrollable.

7. **Grounded Torque Amplification**: Applying side engines (Actions 1 or 3) while in the contact phase generates significantly more violent angular acceleration than in free flight, rapidly inducing high-torque states.

8. **Contact-Induced Unseating**: Applying torque (Actions 1 or 3) while one leg is in contact (`leg_contact` = 1) frequently induces a "trip" effect, where the resulting angular momentum causes the craft to lose contact with the ground, transitioning `leg_contact` from 1 back to 0.

9. **Extreme Reward Bifurcation in Contact**: Upon establishing contact, the reward landscape shifts from gradual scaling to extreme divergence; the transition between grounded and unseated states, or the failure to arrest `ang_vel`, triggers massive penalties (ranging from approximately -15.0 to a terminal -100.0).

10. **Post-Contact Orientation Priority**: Following contact, the physics requirements shift from altitude/velocity management to the near-total elimination of `ang_vel` and `angle`; maintaining this narrow equilibrium is the sole determinant of a successful landing reward.

---

## 2026-07-02 05:53:06

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest rotation, though they often induce immediate angular changes.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Side-Engine Lateral Management**: Side engines (Actions 1 or 3) serve a dual purpose: they are used to manage angular velocity but are also the primary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust to arrest momentum often induces significant increases in `angle` and `ang_vel`, potentially destabilizing the craft.

6. **Rotational Runaway**: In high-energy states, if `ang_vel` is not immediately arrested, the craft can enter a state where angular velocity diverges, making the orientation uncontrollable.

7. **Grounded Torque Amplification**: Applying side engines (Actions 1 or 3) while in the contact phase generates significantly more violent angular acceleration than in free flight, rapidly inducing high-torque states.

8. **Contact-Induced Unseating**: Applying torque (Actions 1 or 3) while one leg is in contact (`leg_contact` = 1) frequently induces a "trip" effect, where the resulting angular momentum causes the craft to lose contact with the ground, transitioning `leg_contact` from 1 back to 0.

9. **Contact-Transition Volatility**: The transition into the contact phase triggers extreme reward swings; while initial contact (the transition to `leg_contact` = 1) can trigger large positive rewards, the immediate stabilization period is prone to massive, high-magnitude penalties (e.g., $\approx -18.0$) if the craft fails to maintain near-zero `ang_vel` during the transition from one-leg to two-leg contact.

10. **Grounded State Equilibrium**: Once both legs are grounded (`leg_contact` = [1, 1]), the physics requirement shifts to a high-frequency micro-correction mode. Maintaining a narrow equilibrium of near-zero `angle` and `ang_vel` through rapid, alternating side-engine pulses is the only way to prevent further instability and maintain the grounded state.

---

## 2026-07-02 05:55:17

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest rotation, though they often induce immediate angular changes.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Side-Engine Lateral Management**: Side engines (Actions 1 or 3) serve a dual purpose: they are used to manage angular velocity but are also the primary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust to arrest momentum often induces significant increases in `angle` and `ang_vel`, potentially destabilizing the craft.

6. **Rotational Runaway**: In high-energy states, if `ang_vel` is not immediately arrested, the craft can enter a state where angular velocity diverges, making the orientation uncontrollable.

7. **Grounded Torque Amplification**: Applying side engines (Actions 1 or 3) while in the contact phase generates significantly more violent angular acceleration than in free flight, rapidly inducing high-torque states.

8. **Contact-Induced Unseating**: Applying torque (Actions 1 or 3) while one leg is in contact (`leg_contact` = 1) frequently induces a "trip" effect, where the resulting angular momentum causes the craft to lose contact with the ground, transitioning `leg_contact` from 1 back to 0.

9. **Landing-Success Reward Impulse**: Successfully transitioning into a stable two-leg contact state (`leg_contact` = [1, 1]) triggers massive, sudden positive reward spikes (e.g., $\approx +12.0$ to $+20.0$), which are significantly higher in magnitude than standard flight rewards.

10. **Post-Contact Stability Collapse**: Following initial contact, the craft is highly susceptible to extreme reward volatility; improper torque application or failure to suppress `ang_vel` can cause the craft to bounce or trip, reverting `leg_contact` to [1, 0] or [0, 0] and triggering catastrophic penalties (e.g., $\approx -17.0$ to $-20.0$).

---

## 2026-07-02 05:56:29

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest rotation, though they often induce immediate angular changes.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Side-Engine Lateral Management**: Side engines (Actions 1 or 3) serve a dual purpose: they are used to manage angular velocity but are also the primary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust to arrest momentum often induces significant increases in `angle` and `ang_vel`, potentially destabilizing the craft.

6. **Rotational Runaway**: In high-energy states, if `ang_vel` is not immediately arrested, the craft can enter a state where angular velocity diverges, making the orientation uncontrollable.

7. **Grounded Torque Amplification**: Applying side engines (Actions 1 or 3) while in the contact phase generates significantly more violent angular acceleration than in free flight, rapidly inducing high-torque states.

8. **Sequential Contact Phases**: The transition to a landing is not binary; the environment transitions from free flight (`leg_contact` = [0, 0]) through transient single-leg contact states (`[1, 0]` or `[0, 1]`) before reaching a stable dual-leg contact state (`[1, 1]`).

9. **Hierarchical Success Rewards**: The reward structure is tiered to encourage landing progression: significant positive impulses are granted upon achieving initial leg contact ($\approx +13.0$), while a massive terminal reward ($\approx +100.0$) is awarded for successfully completing the episode in a stable, two-leg contact state.

10. **Terminal State Divergence**: The episode concludes with extreme reward magnitudes that distinguish mission outcomes; catastrophic failure (e.g., a crash) results in a terminal penalty of $\approx -100.0$, while a successful landing results in a terminal bonus of $\approx +100.0$.

---

## 2026-07-02 05:58:28

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest rotation, though they often induce immediate angular changes.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Side-Engine Lateral Management**: Side engines (Actions 1 or 3) serve a dual purpose: they are used to manage angular velocity but are also the primary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust to arrest momentum often induces significant increases in `angle` and `ang_vel`, potentially destabilizing the craft.

6. **Rotational Runaway**: In high-energy states, if `ang_vel` is not immediately arrested, the craft can enter a state where angular velocity diverges, making the orientation uncontrollable.

7. **Grounded Torque Amplification**: Applying side engines (Actions 1 or 3) while in a contact phase generates significantly more violent angular acceleration than in free flight, rapidly inducing high-torque states.

8. **Asymmetric Leg Contact Rewards**: The transition from free flight to landing is marked by significant positive reward impulses ($\approx +11.0$ to $+14.0$) upon achieving initial single-leg contact (`[1, 0]` or `[0, 1]`), and the sequence may involve multiple transient single-leg states before dual-leg contact.

9. **Terminal Reward Timing**: The terminal bonus ($\approx +100.0$) is awarded at the conclusion of the episode rather than immediately upon the achievement of a dual-leg contact state (`[1, 1]`).

10. **Landing Quality Distinction**: The distinction between SUCCESS and PARTIAL outcomes is determined by the precision of the final state (residual `angle` and `velocity`) at the time of episode conclusion, rather than the receipt of the terminal reward magnitude.

---

## 2026-07-02 06:04:06

---
1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Side-Engine Dual-Purpose Control**: Side engines (Actions 1 or 3) serve a dual purpose: they are used to manage angular velocity and are the primary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust to arrest momentum often induces significant increases in `angle` and `ang_vel`, potentially destabilizing the craft.

6. **Rotational Runaway**: In high-energy states, if `ang_vel` is not immediately arrested, the craft can enter a state where angular velocity diverges, making the orientation uncontrollable.

7. **Post-Contact Quasi-Static Stability**: Once dual-leg contact `[1, 1]` is achieved, the craft can maintain a stable equilibrium with minimal micro-adjustments via side engines (Actions 1 or 3) or no thrust (Action 0), effectively "hovering" on the ground.

8. **Ground-Plane Contact Depth**: The contact state `[1, 1]` remains valid even as $y\_pos$ transitions into slightly negative values, indicating the landing surface threshold is positioned at $y \approx 0$.

9. **Asymmetric Leg Contact Rewards**: The transition from free flight to landing is marked by significant positive reward impulses upon achieving initial single-leg contact (`[1, 0]` or `[0, 1]`).

10. **Landing Quality Distinction**: The distinction between SUCCESS and PARTIAL outcomes is determined by the precision of the final state (residual `angle` and `velocity`) at the time of episode conclusion, rather than the receipt of the terminal reward magnitude.

---

## 2026-07-02 06:06:03

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Side-Engine Dual-Purpose Control**: Side engines (Actions 1 or 3) serve a dual purpose: they are used to manage angular velocity and are the primary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust to arrest momentum often induces significant increases in `angle` and `ang_vel`, potentially destabilizing the craft.

6. **Rotational Runaway**: In high-energy states, if `ang_vel` is not immediately arrested, the craft can enter a state where angular velocity diverges, making the orientation uncontrollable.

7. **Post-Contact Micro-Stabilization**: Once dual-leg contact `[1, 1]` is achieved, the craft can maintain a stable equilibrium by using side engine micro-adjustments (Actions 1 or 3) to counteract residual angular velocity and maintain orientation.

8. **Ground-Plane Contact Depth**: The contact state `[1, 1]` remains valid even as $y\_pos$ transitions into slightly negative values, indicating the landing surface threshold is positioned at $y \approx 0$.

9. **Contact State Transition**: The landing process follows a sequence: moving from free flight to single-leg contact (`[1, 0]` or `[0, 1]`) before reaching the dual-leg contact state (`[1, 1]`).

10. **Landing Quality Distinction**: The distinction between SUCCESS and PARTIAL outcomes is determined by the precision of the final state (residual `angle` and `velocity`) at the time of episode conclusion, rather than the receipt of the terminal reward magnitude.

---

## 2026-07-02 06:08:47

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift increases.

4. **Side-Engine Dual-Purpose Control**: Side engines (Actions 1 or 3) serve a dual purpose: they are used to manage angular velocity and are the primary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust to arrest momentum often induces significant increases in `angle` and `ang_vel`, potentially destabilizing the craft.

6. **Rotational Runaway**: In high-energy states, if `ang_vel` is not immediately arrested, the craft can enter a state where angular velocity diverges, making the orientation uncontrollable.

7. **Post-Contact Micro-Stabilization**: Once dual-leg contact `[1, 1]` is achieved, the craft can maintain a stable equilibrium by using side engine micro-adjustments (Actions 1 or 3) to counteract residual angular velocity and maintain orientation.

8. **Ground-Plane Contact Depth**: The contact state `[1, 1]` remains valid even as $y\_pos$ transitions into slightly negative values, indicating the landing surface threshold is positioned at $y \approx 0$.

9. **Contact State Transition**: The landing process follows a sequence: moving from free flight to single-leg contact (`[1, 0]` or `[0, 1]`) before reaching the dual-leg contact state (`[1, 1]`).

10. **Landing Persistence and Terminal Precision**: The episode continues for a fixed duration after dual-leg contact `[1, 1]` is achieved; the final outcome (SUCCESS vs. PARTIAL) is determined by the precision of the terminal state, which includes residual `angle`, `velocity`, and the accumulated lateral displacement `x_pos`.

---

## 2026-07-02 06:10:29

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **Side-Engine Dual-Purpose Control**: Side engines (Actions 1 or 3) serve a dual purpose: they are the primary mechanism for managing angular velocity and are the secondary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust intended to arrest momentum often induces significant increases in `angle` and `ang_vel`, potentially destabilizing the craft.

6. **Rotational Runaway**: In high-energy states, if `ang_vel` is not immediately arrested, the craft can enter a state where angular velocity diverges, making orientation control increasingly difficult.

7. **Post-Contact Micro-Stabilization**: Once dual-leg contact `[1, 1]` is achieved, the craft can maintain a stable equilibrium by using side engine micro-adjustments (Actions 1 or 3) to counteract residual angular velocity and maintain orientation.

8. **Ground-Plane Contact Depth**: The contact state `[1, 1]` remains valid even as $y\_pos$ transitions into slightly negative values, indicating the landing surface threshold is positioned at $y \approx 0$.

9. **Contact State Transition**: The landing process typically follows a sequence: moving from free flight to single-leg contact (`[1, 0]` or `[0, 1]`) before reaching the dual-leg contact state (`[1, 1]`).

10. **Landing Persistence and Terminal Precision**: The episode continues for a fixed duration after dual-leg contact `[1, 1]` is achieved; the final outcome (SUCCESS vs. PARTIAL) is determined by the stability of the terminal state, specifically the precision of residual `angle`, `velocity`, and `x_pos`.

---

## 2026-07-02 06:12:39

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **Side-Engine Dual-Purpose Control**: Side engines (Actions 1 or 3) serve a dual purpose: they are the primary mechanism for managing angular velocity and the secondary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust intended to arrest momentum often induces significant increases in `angle` and `ang_vel`.

6. **Rotational Runaway**: In high-energy states, if `ang_vel` is not immediately arrested, the craft can enter a state where angular velocity diverges, making orientation control increasingly difficult.

7. **Post-Contact Thrust Instability**: Applying the main engine (Action 2) while in a contact state (`[0, 1]` or `[1, 1]`) can induce upward $y\_vel$ and significant negative rewards, suggesting a penalty for vertical instability or "bouncing" during ground contact.

8. **Post-Contact Lateral Drift**: Establishing dual-leg contact `[1, 1]` does not automatically arrest lateral momentum; $x\_pos$ and $x\_vel$ can continue to drift significantly post-contact if not actively managed.

9. **Contact State Transition**: The landing process follows a sequence: moving from free flight to single-leg contact (`[1, 0]` or `[0, 1]`) before reaching the dual-leg contact state (`[1, 1]`).

10. **Terminal Stability and Lateral Precision**: A SUCCESS outcome is contingent on the stability of the terminal state, requiring the craft to minimize residual `angle`, `velocity`, and specifically lateral displacement ($x\_pos$) after dual-leg contact is achieved.

---

## 2026-07-02 06:15:14

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **Side-Engine Dual-Purpose Control**: Side engines (Actions 1 or 3) serve a dual purpose: they are the primary mechanism for managing angular velocity and the secondary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust intended to arrest momentum often induces significant increases in `angle` and `ang_vel`.

6. **Contact-Induced Torque Spikes**: Applying the main engine (Action 2) while in a single-leg contact state (`[1, 0]` or `[0, 1]`) induces massive angular acceleration, causing `ang_vel` to diverge rapidly.

7. **Post-Contact Flight Re-entry**: High-torque actions during single-leg contact can cause the craft to lose contact entirely (`[0, 0]`), resulting in a "bounce" or a high-energy rotational state that prevents stable dual-leg contact.

8. **Contact State Transition**: The landing process typically follows a sequence: moving from free flight to single-leg contact (`[1, 0]` or `[0, 1]`) before reaching the dual-leg contact state (`[1, 1]`).

9. **Post-Contact Lateral Drift**: Establishing dual-leg contact `[1, 1]` does not automatically arrest lateral momentum; $x\_pos$ and $x\_vel$ can continue to drift significantly post-contact if not actively managed.

10. **Terminal Stability and Failure Penalties**: A SUCCESS outcome is contingent on the stability of the terminal state; high residual `angle`, `ang_vel`, or `velocity` upon reaching dual-leg contact triggers extreme negative terminal rewards (e.g., -100).

---

## 2026-07-02 06:16:56

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **Side-Engine Dual-Purpose Control**: Side engines (Actions 1 or 3) serve a dual purpose: they are the primary mechanism for managing angular velocity and the secondary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust intended to arrest momentum often induces significant increases in `angle` and `ang_vel`.

6. **Contact-Induced Torque Spikes**: Applying the main engine (Action 2) or side engines (Actions 1 or 3) while in a single-leg contact state (`[1, 0]` or `[0, 1]`) induces massive angular acceleration, causing `ang_vel` to diverge rapidly.

7. **Contact State Transition**: The landing process typically follows a sequence: moving from free flight to single-leg contact (`[1, 0]` or `[0, 1]`) before reaching the dual-leg contact state (`[1, 1]`).

8. **Post-Contact Damping**: Once dual-leg contact (`[1, 1]`) is achieved, side engines (Actions 1 or 3) must be used to actively dampen residual `ang_vel` and $x\_vel$ to satisfy terminal stability requirements.

9. **Post-Contact Lateral Drift**: Establishing dual-leg contact `[1, 1]` does not automatically arrest lateral momentum; $x\_pos$ and $x\_vel$ can continue to drift significantly post-contact if not actively managed.

10. **Terminal Stability and Failure Penalties**: A SUCCESS outcome is contingent on the stability of the terminal state; high residual `angle`, `ang_vel`, or `velocity` upon reaching dual-leg contact triggers extreme negative terminal rewards.

---

## 2026-07-02 06:18:21

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **Side-Engine Dual-Purpose Control**: Side engines (Actions 1 or 3) serve a dual purpose: they are the primary mechanism for managing angular velocity and the secondary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust intended to arrest momentum often induces significant increases in `angle` and `ang_vel`.

6. **Contact-Induced Torque and Instability**: Landing on a single leg (`[1, 0]` or `[0, 1]`) can induce sudden, large spikes in `ang_vel`. High angular momentum during or after contact can cause the lander to oscillate between single-leg and dual-leg contact states.

7. **Contact State Transition and Persistence**: The landing process typically follows a sequence from free flight to single-leg contact and then dual-leg contact. However, contact states are not necessarily persistent; high rotation or tilt can cause a leg to lose contact, transitioning the state from `[1, 1]` back to `[1, 0]` or `[0, 1]`.

8. **Post-Contact Damping**: Once dual-leg contact (`[1, 1]`) is achieved, side engines (Actions 1 or 3) must be used to actively dampen residual `ang_vel` and $x\_vel$ to satisfy terminal stability requirements.

9. **Post-Contact Momentum and Angular Divergence**: Establishing dual-leg contact does not automatically arrest movement or rotation; $x\_vel$, `angle`, and `ang_vel` can continue to drift or diverge significantly post-contact if not actively managed.

10. **Terminal Stability and Failure Penalties**: The distinction between PARTIAL and FAILURE outcomes is contingent on the terminal state's stability. High residual `angle`, `ang_vel`, or `velocity` upon reaching contact triggers extreme negative terminal rewards.

---

## 2026-07-02 06:21:31

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **Side-Engine Dual-Purpose Control**: Side engines (Actions 1 or 3) serve a dual purpose: they are the primary mechanism for managing angular velocity and the secondary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust intended to arrest momentum often induces significant increases in `angle` and `ang_vel`.

6. **Contact-Induced Angular Spikes**: Transitioning to a single-leg contact state (`[1, 0]` or `[0, 1]`) induces near-instantaneous, high-magnitude spikes in `ang_vel` (e.g., jumping from $\approx 0$ to $>1.0$), which can rapidly escalate `angle`.

7. **Contact State Transition and Persistence**: The landing process typically follows a sequence from free flight to single-leg contact and then dual-leg contact. However, contact states are not necessarily persistent; high rotation or tilt can cause a leg to lose contact, transitioning the state from `[1, 1]` back to `[1, 0]` or `[0, 1]`.

8. **Side-Engine Induced Instability during Single-Leg Contact**: Applying side-engine thrust (Actions 1 or 3) while the lander is in a single-leg contact state (`[1, 0]` or `[0, 1]`) can exacerbate angular instability, driving rapid increases in the magnitude of `ang_vel` and `angle`.

9. **Post-Contact Momentum and Angular Divergence**: Establishing dual-leg contact (`[1, 1]`) does not automatically arrest movement or rotation; $x\_vel$, `angle`, and `ang_vel` can continue to drift or diverge significantly post-contact if not actively managed.

10. **Terminal Stability and Outcome Determination**: The distinction between PARTIAL and FAILURE outcomes is heavily contingent on terminal stability. Even if dual-leg contact (`[1, 1]`) is achieved, high residual `angle`, `ang_vel`, or `velocity` triggers extreme negative terminal rewards.

---

## 2026-07-02 06:24:15

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **Side-Engine Dual-Purpose Control**: Side engines (Actions 1 or 3) serve a dual purpose: they are the primary mechanism for managing angular velocity and the secondary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust intended to arrest momentum often induces significant increases in `angle` and `ang_vel`.

6. **Contact State Volatility**: Contact states are not necessarily persistent; high rotation, tilt, or lateral velocity can cause the lander to lose contact, transitioning from dual-leg contact (`[1, 1]`) back to free flight (`[0, 0]`).

7. **Post-Contact Momentum and Drift**: Establishing dual-leg contact (`[1, 1]`) does not automatically arrest movement; $x\_vel$, $y\_vel$, and `angle` can continue to drift or diverge significantly post-contact if not actively managed.

8. **Ground Penetration Penalty**: A significant negative terminal reward is triggered when $y\_pos$ reaches or falls below $0.0$, indicating the lander has penetrated the ground plane.

9. **Lateral-Vertical Drift Risk**: High $x\_vel$ or $y\_vel$ during or after contact can lead to uncontrolled lateral or vertical drift, which can subsequently cause ground penetration or loss of contact.

10. **Terminal Stability and Outcome Determination**: The distinction between PARTIAL and FAILURE outcomes is heavily contingent on terminal stability; even if dual-leg contact (`[1, 1]`) is achieved, high residual velocities or ground penetration ($y \le 0$) trigger extreme negative rewards.

---

## 2026-07-02 06:25:52

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **Side-Engine Dual-Purpose Control**: Side engines (Actions 1 or 3) serve a dual purpose: they are the primary mechanism for managing angular velocity and the secondary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust intended to arrest momentum often induces significant increases in `angle` and `ang_vel`.

6. **Contact State Volatility and Staggered Landing**: Contact transitions are often incremental (e.g., transitioning through $[1,0]$ or $[0,1]$) rather than immediate $[0,0] \to [1,1]$. High rotation or tilt can cause a lander to lose contact, transitioning from dual-leg contact back to free flight even at very low altitudes.

7. **Post-Contact Momentum and Drift**: Establishing dual-leg contact (`[1, 1]`) does not automatically arrest movement; $x\_vel$, $y\_vel$, and `angle` can continue to drift, oscillate, or diverge significantly post-contact.

8. **Ground Penetration Penalty**: A significant negative terminal reward is triggered when $y\_pos$ reaches or falls below $0.0$, indicating the lander has penetrated the ground plane.

9. **Low-Altitude Angular Sensitivity**: At low altitudes ($y \approx 0$), side-engine thrusts (Actions 1 or 3) can trigger disproportionately high angular accelerations and velocities, making the final stabilization phase extremely sensitive to torque.

10. **Terminal Stability and Outcome Determination**: The distinction between PARTIAL and FAILURE outcomes is heavily contingent on terminal stability; even if dual-leg contact is achieved, high residual velocities or ground penetration ($y \le 0$) trigger extreme negative rewards.

---

## 2026-07-02 06:27:39

---
1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **Side-Engine Dual-Purpose Control**: Side engines (Actions 1 or 3) serve a dual purpose: they are the primary mechanism for managing angular velocity and the secondary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust intended to arrest momentum often induces significant increases in `angle` and `ang_vel`.

6. **Single-Leg Contact Vulnerability**: Contact states of `[1,0]` or `[0,1]` do not prevent ground penetration ($y \le 0$); the lander can tip over and trigger the terminal penalty even while one leg is in contact with the ground.

7. **Post-Contact Momentum and Drift**: Establishing dual-leg contact (`[1, 1]`) does not automatically arrest movement; $x\_vel$, $y\_vel$, and `angle` can continue to drift, oscillate, or diverge significantly post-contact.

8. **Ground Penetration Penalty**: A significant negative terminal reward is triggered when $y\_pos$ reaches or falls below $0.0$, indicating the lander has penetrated the ground plane (a crash).

9. **Low-Altitude Angular Sensitivity**: At low altitudes ($y \approx 0$), side-engine thrusts (Actions 1 or 3) can trigger disproportionately high angular accelerations and velocities, making the final stabilization phase extremely sensitive to torque.

10. **Angular Velocity/Position Trade-off**: Side-engine thrusts can be utilized to successfully dampen angular velocity (`ang_vel`), though this often results in a simultaneous increase in the absolute `angle` (the degree of tilt).

---

## 2026-07-02 06:32:58

---
1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **Side-Engine Dual-Purpose Control**: Side engines (Actions 1 or 3) serve a dual purpose: they are the primary mechanism for managing angular velocity and the secondary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust intended to arrest momentum often induces significant increases in `angle` and `ang_vel`.

6. **Single-Leg Contact Vulnerability**: Contact states of `[1,0]` or `[0,1]` do not prevent ground penetration ($y \le 0$); the lander can tip over and trigger the terminal penalty even while one leg is in contact with the ground.

7. **Post-Contact Momentum and Drift**: Establishing dual-leg contact (`[1, 1]`) does not automatically arrest movement; $x\_vel$, $y\_vel$, and `angle` can continue to drift, oscillate, or diverge significantly post-contact.

8. **Non-Terminal Ground Penetration**: The $y \le 0$ condition is not an absolute terminal penalty; the lander can survive ground penetration and continue to accrue positive rewards if it maintains stability and establishes contact.

9. **Low-Altitude Angular Sensitivity**: At low altitudes ($y \approx 0$), side-engine thrusts (Actions 1 or 3) can trigger disproportionately high angular accelerations and velocities, making the final stabilization phase extremely sensitive to torque.

10. **Angular Velocity/Position Trade-off**: Side-engine thrusts can be utilized to successfully dampen angular velocity (`ang_vel`), though this often results in a simultaneous increase in the absolute `angle` (the degree of tilt).

---

## 2026-07-02 06:34:49

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **Side-Engine Dual-Purpose Control**: Side engines (Actions 1 or 3) serve a dual purpose: they are the primary mechanism for managing angular velocity and the secondary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust intended to arrest momentum often induces significant increases in `angle` and `ang_vel`.

6. **Post-Contact Angular Instability**: Establishing dual-leg contact (`[1, 1]`) does not act as a damping mechanism for torque; high `ang_vel` can continue to drive `angle` divergence even after the lander is grounded.

7. **Non-Terminal Ground Penetration**: The $y \le 0$ condition is not an absolute terminal penalty; the lander can survive ground penetration and continue to accrue positive rewards if it maintains stability.

8. **Low-Altitude Angular Sensitivity**: At low altitudes ($y \approx 0$), side-engine thrusts (Actions 1 or 3) can trigger disproportionately high angular accelerations and velocities, making the final stabilization phase extremely sensitive to torque.

9. **Angular Velocity/Position Trade-off**: Side-engine thrusts can be utilized to successfully dampen angular velocity (`ang_vel`), though this often results in a simultaneous increase in the absolute `angle` (the degree of tilt).

10. **Landing Stability Requirements**: Achieving a successful landing requires more than dual-leg contact; the lander must simultaneously arrest `ang_vel` and minimize `angle` to prevent post-contact rotation or tipping.

---

## 2026-07-02 06:36:39

---
1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **Side-Engine Dual-Purpose Control**: Side engines (Actions 1 or 3) serve a dual purpose: they are the primary mechanism for managing angular velocity and the secondary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust intended to arrest momentum often induces significant increases in `angle` and `ang_vel`.

6. **Post-Contact Angular Instability**: Establishing dual-leg contact ([1, 1]) does not act as a damping mechanism; side-engine thrusts (Actions 1 or 3) applied while grounded can trigger extreme spikes in `ang_vel`, potentially leading to rapid rotation or tipping despite contact.

7. **Non-Terminal Ground Penetration**: The $y \le 0$ condition is not an absolute terminal penalty; the lander can survive ground penetration and continue to accrue rewards or penalties if it maintains stability.

8. **Low-Altitude/Grounded Sensitivity**: Side-engine thrusts (Actions 1 or 3) trigger disproportionately high angular accelerations and velocities when the lander is at low altitudes ($y \approx 0$) or already in contact with the ground, making the final stabilization phase highly volatile.

9. **Action-Reward Asymmetry**: The reward structure heavily favors Action 2 (main engine) for generating positive rewards through altitude and velocity management, whereas Actions 1 and 3 (side engines) are frequently associated with significant negative rewards (penalties).

10. **Landing Stability Requirements**: Achieving a successful landing requires more than dual-leg contact; the lander must simultaneously arrest `ang_vel` and minimize `angle` to prevent post-contact rotation or instability.

---

## 2026-07-02 06:39:16

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **Side-Engine Dual-Purpose Control**: Side engines (Actions 1 or 3) serve as the primary mechanism for managing angular velocity and the secondary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust intended to arrest momentum often induces significant increases in `angle` and `ang_vel`.

6. **Grounded Contact Disruption**: Side-engine thrusts (Actions 1 or 3) can act as a "kick" mechanism when the lander is grounded; they can induce sufficient angular acceleration to break contact, transitioning the state from $[1, 1]$ to $[1, 0]$ or $[0, 0]$.

7. **Non-Terminal Ground Penetration**: The $y \le 0$ condition is not an absolute terminal penalty; the lander can survive ground penetration and continue to accrue rewards or penalties if it maintains stability.

8. **Extreme Grounded Penalty Volatility**: Side-engine thrusts (Actions 1 or 3) applied at low altitudes or while in contact with the ground trigger disproportionately high angular accelerations and can result in extreme, large-magnitude negative reward penalties.

9. **Action-Reward Asymmetry**: The reward structure heavily favors Action 2 (main engine) for generating positive rewards through altitude and velocity management, whereas Actions 1 and 3 (side engines) are frequently associated with significant negative rewards, especially during post-contact stabilization.

10. **Landing Stability Requirements**: Achieving a successful landing requires more than dual-leg contact; the lander must simultaneously arrest `ang_vel`, minimize `angle`, and manage side-engine usage to prevent contact disruption or rapid rotation.

---

## 2026-07-02 06:43:35

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **Side-Engine Dual-Purpose Control**: Side engines (Actions 1 or 3) serve as the primary mechanism for managing angular velocity and the secondary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust intended to arrest momentum often induces significant increases in `angle` and `ang_vel`.

6. **Grounded Contact Disruption**: Side-engine thrusts (Actions 1 or 3) can act as a "kick" mechanism when the lander is grounded; they can induce sufficient angular acceleration to break contact, transitioning the state from $[1, 1]$ to $[1, 0]$ or $[0, 0]$.

7. **Non-Terminal Ground Penetration**: The $y \le 0$ condition is not an absolute terminal penalty; the lander can survive ground penetration and continue the episode if stability or contact is maintained.

8. **Grounded State Instability**: Applying thrust (Actions 1, 2, or 3) while the lander is in contact with the ground can trigger extreme, large-magnitude negative rewards due to induced angular instability or sudden contact disruption.

9. **Terminal Success Reward**: A large, discrete positive reward (e.g., 100.0) is granted upon the successful completion of a stable landing.

10. **Landing Stability Requirements**: Achieving a successful landing requires the simultaneous arrest of `ang_vel`, minimization of `angle`, and management of $y\_vel$ to achieve and maintain stable dual-leg contact ($[1, 1]$).

---

## 2026-07-02 06:45:21

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **Side-Engine Dual-Purpose Control**: Side engines (Actions 1 or 3) serve as the primary mechanism for managing angular velocity and the secondary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust intended to arrest momentum often induces significant increases in `angle` and `ang_vel`.

6. **Grounded Contact Disruption**: Side-engine thrusts (Actions 1 or 3) can act as a "kick" mechanism when the lander is grounded; they can induce sufficient angular acceleration to break contact, transitioning the state from $[1, 1]$ to $[1, 0]$ or $[0, 0]$.

7. **Non-Terminal Ground Penetration**: The $y \le 0$ condition is not an absolute terminal penalty; the lander can survive ground penetration and continue the episode if stability or contact is maintained.

8. **Fatal Grounded-Thrust Interaction**: Applying side-engine thrust (Actions 1 or 3) while the lander is grounded ($y \le 0$) can trigger immediate terminal failure with a massive negative reward (e.g., -100.0), particularly when the lander is experiencing angular instability.

9. **Terminal Success Reward**: A large, discrete positive reward (e.g., 100.0) is granted upon the successful completion of a stable landing.

10. **Landing Stability Requirements**: Achieving a successful landing requires the simultaneous arrest of `ang_vel`, minimization of `angle`, and management of $y\_vel$ to achieve and maintain stable dual-leg contact ($[1, 1]$).

---

## 2026-07-02 06:47:29

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **Side-Engine Dual-Purpose Control**: Side engines (Actions 1 or 3) serve as the primary mechanism for managing angular velocity and the secondary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust intended to arrest momentum often induces significant increases in `angle` and `ang_vel`.

6. **Sequential Leg Contact**: Ground contact is registered per leg, allowing the lander to transition through intermediate contact states (e.g., $[1, 0]$ or $[0, 1]$) before achieving full dual-leg stability ($[1, 1]$).

7. **Non-Terminal Ground Penetration**: The $y \le 0$ condition is not an absolute terminal penalty; the lander can survive ground penetration and continue the episode if contact is maintained.

8. **Impact-Dependent Termination**: The transition to ground contact can trigger either a stable grounded state or an immediate terminal "crash" (massive negative reward), depending on the impact velocity and angle at the moment of contact.

9. **Grounded Maneuverability**: Once contact is established, the lander can continue to apply thrust (Actions 1, 2, or 3) to manage its orientation or position without immediate termination, provided it does not exceed crash thresholds.

10. **Landing Stability Requirements**: Achieving a successful landing requires the simultaneous arrest of `ang_vel`, minimization of `angle`, and management of $y\_vel$ to achieve and maintain stable dual-leg contact ($[1, 1]$).

---

## 2026-07-02 06:49:43

---
1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **Side-Engine Dual-Purpose Control**: Side engines (Actions 1 or 3) serve as the primary mechanism for managing angular velocity and the secondary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust intended to arrest momentum often induces significant increases in `angle` and `ang_vel`.

6. **Sequential Leg Contact**: Ground contact is registered per leg, allowing the lander to transition through intermediate contact states (e.g., $[1, 0]$ or $[0, 1]$) before achieving full dual-leg stability ($[1, 1]$).

7. **Non-Terminal Ground Penetration**: The $y \le 0$ condition is not an absolute terminal penalty; the lander can survive ground penetration and continue the episode if contact is maintained.

8. **Impact and Contact Rewards**: The transition to ground contact can trigger significant positive reward spikes; however, stability is precarious, as high `ang_vel` or improper orientation during or immediately after contact can trigger massive negative "crash" penalties.

9. **Ground Contact Volatility**: Achieving dual-leg contact $[1, 1]$ does not guarantee a stable grounded state; high angular velocity or aggressive corrective thrusting can cause the lander to lose a leg contact, reverting the state to $[1, 0]$ or $[0, 1]$.

10. **Landing Stability Requirements**: Achieving a successful landing requires the simultaneous arrest of `ang_vel`, minimization of `angle`, and management of $y\_vel$ to achieve and *maintain* stable dual-leg contact ($[1, 1]$).

---

## 2026-07-02 06:53:59

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **Side-Engine Dual-Purpose Control**: Side engines (Actions 1 or 3) serve as the primary mechanism for managing angular velocity and the secondary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust intended to arrest momentum often induces significant increases in `angle` and `ang_vel`.

6. **Sequential Leg Contact**: Ground contact is registered per leg, allowing the lander to transition through intermediate contact states (e.g., $[1, 0]$ or $[0, 1]$) before achieving full dual-leg stability ($[1, 1]$).

7. **Non-Terminal Ground Penetration**: The $y \le 0$ condition is not an absolute terminal penalty; the lander can survive ground penetration (including negative $y$ values) and continue the episode if contact is maintained.

8. **Post-Contact Crash Penalties**: Achieving leg contact does not prevent failure; if `angle` or `ang_vel` is too high during or immediately after the transition to contact, the lander can trigger a massive negative "crash" penalty (e.g., -100).

9. **Ground Contact Volatility**: Achieving dual-leg contact $[1, 1]$ does not guarantee a stable grounded state; aggressive corrective thrusting, particularly from side engines (Actions 1 or 3), can cause the lander to lose a leg contact, reverting the state to $[1, 0]$ or $[0, 1]$.

10. **Landing Stability Requirements**: A successful landing requires the simultaneous arrest of $y\_vel$ and `ang_vel`, the minimization of `angle`, and the maintenance of a stable dual-leg contact state ($[1, 1]$).

---

## 2026-07-02 06:55:06

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **Side-Engine Dual-Purpose Control**: Side engines serve as the primary mechanism for managing angular velocity and the secondary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust intended to arrest momentum often induces significant increases in `angle` and `ang_vel`.

6. **Sequential Leg Contact Transition**: Ground contact is registered per leg ($[1,0]$ or $[0,1]$). The transition to full dual-leg stability ($[1,1]$) is a critical phase where high `ang_vel` can lead to immediate instability.

7. **Post-Contact Rotational Failure**: Achieving $[1, 1]$ contact does not guarantee survival; if the lander fails to arrest `angle` or `ang_vel` shortly after contact, a massive negative "crash" penalty (e.g., -100) is triggered, even if the lander remains on the ground.

8. **Ground Contact Volatility**: Achieving dual-leg contact $[1, 1]$ does not guarantee a stable grounded state; aggressive corrective thrusting, particularly from side engines (Actions 1 or 3), can cause the lander to lose a leg contact, reverting the state to $[1, 0]$ or $[0, 1]$.

9. **Non-Terminal Ground Penetration**: The $y \le 0$ condition is not an absolute terminal penalty; a lander can maintain leg contact and stability while $y$ is negative, effectively "sitting" on the ground.

10. **Post-Landing Micro-Stabilization**: Once dual-leg contact $[1, 1]$ is established, side engines (Actions 1 or 3) can be used to perform micro-adjustments to maintain a near-zero `ang_vel` and a low, stable `angle` to prevent rotational crash penalties.

---

## 2026-07-02 06:56:51

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **Side-Engine Dual-Purpose Control**: Side engines serve as the primary mechanism for managing angular velocity and the secondary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust intended to arrest momentum often induces significant increases in `angle` and `ang_vel`.

6. **Sequential Leg Contact Transition**: The transition to full dual-leg stability ($[1,1]$) is often preceded by a single-leg contact phase ($[1,0]$ or $[0,1]$), where side-engine thrust (Actions 1 or 3) can be used to stabilize the chassis to facilitate the second leg's contact.

7. **Post-Contact Rotational Failure**: Achieving dual-leg contact $[1, 1]$ does not guarantee survival; if the lander fails to arrest `angle` or `ang_vel` shortly after contact, a massive negative "crash" penalty is triggered, even if the lander remains on the ground.

8. **Ground Contact Volatility**: Achieving dual-leg contact $[1, 1]$ is not a permanent state; aggressive corrective thrusting, particularly from side engines (Actions 1 or 3), can cause the lander to lose a leg contact, reverting the state to $[1, 0]$ or $[0, 1]$.

9. **Non-Terminal Ground Penetration**: The $y \le 0$ condition is not an absolute terminal penalty; a lander can maintain stability and receive positive rewards while "sitting" on the ground.

10. **Post-Landing Micro-Stabilization**: Once dual-leg contact $[1, 1]$ is established, the lander must use side engines for extremely fine-grained `angle` and `ang_vel` management; excessive or poorly timed thrust can trigger immediate instability penalties or cause the lander to bounce/revert to a single-leg contact state.

---

## 2026-07-02 06:59:54

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **Side-Engine Dual-Purpose Control**: Side engines serve as the primary mechanism for managing angular velocity and the secondary mechanism for correcting or inducing lateral velocity ($x\_vel$).

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust intended to arrest momentum often induces significant increases in `angle` and `ang_vel`.

6. **Sequential Leg Contact Transition**: The transition to full dual-leg stability ($[1,1]$) is often preceded by a single-leg contact phase ($[1,0]$ or $[0,1]$), where side-engine thrust (Actions 1 or 3) can be used to stabilize the chassis to facilitate the second leg's contact.

7. **Rotational Impact Failure**: Achieving leg contact ($[1,0]$ or $[1,1]$) while possessing significant `ang_vel` or an increasing `angle` triggers a catastrophic crash penalty; rotational energy must be arrested near the moment of contact to prevent immediate episode termination.

8. **Ground Contact Volatility**: Achieving dual-leg contact $[1, 1]$ is not a permanent state; aggressive corrective thrusting, particularly from side engines (Actions 1 or 3), can cause the lander to lose a leg contact, reverting the state to $[1, 0]$ or $[0, 1]$.

9. **Non-Terminal Ground Penetration**: The $y \le 0$ condition is not an absolute terminal penalty; a lander can maintain stability and receive positive rewards while "sitting" on the ground.

10. **Terminal State Differentiation**: A "Partial" outcome can be achieved by maintaining stability or hovering via sustained side-engine thrust (even at a tilted angle), but "Success" requires meeting strict terminal constraints, such as achieving dual-leg contact with near-zero orientation error.

---

## 2026-07-02 07:01:49

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **High-Torque Side Engines**: Side engines (Actions 1 and 3) act as high-gain torque actuators; brief pulses can cause extreme spikes in `ang_vel` (e.g., Episode 1, Step 388 $\to$ 389), making rotational control highly sensitive.

5. **Translational-Rotational Conflict**: High translational momentum ($x\_vel$ or $y\_vel$) creates a conflict where corrective thrust intended to arrest momentum often induces significant increases in `angle` and `ang_vel`.

6. **Leg Contact Volatility**: Leg contact states are highly unstable; the lander can rapidly oscillate between dual-leg contact $[1,1]$, single-leg contact $[1,0]/[0,1]$, and zero-leg contact $[0,0]$ without immediate episode termination.

7. **Rotational Impact Penalty**: Achieving leg contact while possessing significant `angle` or `ang_vel` triggers a massive crash penalty (e.g., -100 reward), even if the lander successfully makes contact with the ground.

8. **Ground-State Persistence**: The lander can maintain a non-terminal state while "sitting" on the ground ($y \approx 0$), even if it loses all leg contact (reverting to $[0,0]$), provided orientation and vertical velocity are managed.

9. **Side-Engine Dual-Purpose Control**: Side engines serve as the primary mechanism for managing angular velocity and the secondary mechanism for correcting or inducing lateral velocity ($x\_vel$).

10. **Outcome Differentiation**: A "Partial" outcome can be achieved by maintaining stability or hovering, but "Success" requires meeting strict terminal constraints, specifically achieving dual-leg contact with near-zero orientation and angular velocity errors.

---

## 2026-07-02 07:03:19

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **High-Gain Side-Engine Torque**: Side engines (Actions 1 and 3) act as high-gain actuators; even brief pulses can cause significant spikes in `ang_vel`, making precise rotational control highly sensitive during both descent and terminal stability phases.

5. **Translational-Rotational Conflict**: Correcting lateral velocity ($x\_vel$) through tilted main thrust or side-engine pulses inherently induces changes in `angle` and `ang_vel`, creating a constant trade-off between translational and rotational stability.

6. **Leg Contact State Transitions**: The lander undergoes transitions between contact states (e.g., $[0,0] \to [1,0] \to [1,1]$) during the landing sequence; achieving and maintaining dual-leg contact $[1,1]$ allows for ground-state persistence but is not the sole criterion for a successful outcome.

7. **Rotational Impact Penalty**: Achieving leg contact while possessing significant `angle` or `ang_vel` triggers a massive crash penalty, even if the lander successfully makes contact with the ground.

8. **Terminal Precision Requirements**: The distinction between "Partial" and "Success" outcomes is determined by error thresholds; a lander may maintain ground contact for an extended duration (as seen in Episode 2) but still fail to meet the strict precision requirements for orientation and velocity.

9. **Ground-State Stability Maintenance**: Once the lander is on the ground ($y \approx 0$), it requires continuous, fine-tuned torque via high-frequency side-engine pulses (Actions 1 or 3) to counteract residual angular momentum and maintain a stable, near-zero `ang_vel`.

10. **Outcome Differentiation**: A "Success" outcome requires the simultaneous satisfaction of all terminal constraints: dual-leg contact, near-zero $x\_vel$ and $y\_vel$, and minimal `angle` and `ang_vel` errors.

---

## 2026-07-02 07:05:07

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **High-Gain Side-Engine Torque**: Side engines (Actions 1 and 3) act as high-gain actuators; even brief pulses can cause significant spikes in `ang_vel`, making precise rotational control highly sensitive during descent and ground-state maintenance.

5. **Translational-Rotational Conflict**: Correcting lateral velocity ($x\_vel$) through tilted main thrust or side-engine pulses inherently induces changes in `angle` and `ang_vel`, creating a constant trade-off between translational and rotational stability.

6. **Contact State Fragility**: Achieving dual-leg contact $[1,1]$ is not a stable terminal state; excessive angular momentum or improper orientation during contact can trigger a "tip-over" event, causing an immediate transition from $[1,1] \to [0,0]$ and a massive negative reward (crash).

7. **Rotational Impact Penalty**: Significant `ang_vel` during the terminal descent/contact transition (the moments leading to $y \approx 0$) triggers heavy penalties, even if the lander successfully makes initial contact.

8. **Ground-State Stability Maintenance**: Once the lander is on the ground ($[1,1]$ contact), it requires continuous, high-frequency torque via side-engine pulses to counteract residual angular momentum and prevent the tip-over transitions observed in failed episodes.

9. **Terminal Reward Structure**: The environment provides a substantial terminal reward (e.g., 100.0) for successfully maintaining ground contact, but this is distinct from the final outcome classification.

10. **Outcome Differentiation**: A "Success" outcome requires the simultaneous satisfaction of all terminal constraints: dual-leg contact, near-zero $x\_vel$ and $y\_vel$, and minimal `angle` and `ang_vel` errors; failure to meet these specific thresholds results in a "Partial" outcome.

---

## 2026-07-02 07:08:59

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **High-Gain Side-Engine Torque**: Side engines (Actions 1 and 3) act as high-gain actuators; even brief pulses can cause significant spikes in `ang_vel`, making precise rotational control highly sensitive during descent and ground-state maintenance.

5. **Translational-Rotational Conflict**: Correcting lateral velocity ($x\_vel$) through tilted main thrust or side-engine pulses inherently induces changes in `angle` and `ang_vel`, creating a constant trade-off between translational and rotational stability.

6. **Sequential Contact Instability**: Leg contact is a multi-stage process ($[1,0] \to [1,1]$ or $[0,1] \to [1,1]$); the transition phase between the first and second leg making contact is a period of extreme angular volatility and heightened tip-over risk.

7. **Rotational Impact Penalty**: Significant `ang_vel` during the terminal descent/contact transition (the moments leading to $y \approx 0$) triggers heavy penalties, even if the lander successfully makes initial contact.

8. **Dynamic Ground-State Maintenance**: Achieving $[1,1]$ contact does not result in a static state; the lander requires continuous, high-frequency micro-adjustments (using side engines or the main engine) to counteract residual translational and angular momentum that could trigger a tip-over.

9. **Terminal Reward Structure**: The environment provides a substantial terminal reward for successfully maintaining ground contact, but this is distinct from the final outcome classification.

10. **Outcome Differentiation**: A "Success" outcome requires the simultaneous satisfaction of extremely narrow thresholds for all terminal constraints: dual-leg contact, minimal $x$ and $y$ position errors, near-zero $x$ and $y$ velocities, and minimal `angle` and `ang_vel` errors.

---

## 2026-07-02 07:10:39

1. **Gravity-Driven Descent**: Constant downward acceleration necessitates sustained vertical thrust (Action 2) to manage $y\_vel$ and prevent uncontrolled descent.

2. **Angular Momentum Coupling**: `angle` and `ang_vel` are inherently coupled; active torque via side engines (Actions 1 or 3) is required to arrest or induce rotation.

3. **Main Engine Vector Decomposition**: Thrust from Action 2 decomposes into vertical and horizontal components; as the absolute `angle` increases, the engine's vertical effectiveness decreases while horizontal drift ($x\_vel$) increases.

4. **High-Gain Side-Engine Torque**: Side engines (Actions 1 and 3) act as high-gain actuators; even brief pulses can cause significant spikes in `ang_vel`, making precise rotational control highly sensitive.

5. **Translational-Rotational Conflict**: Correcting lateral velocity ($x\_vel$) through tilted main thrust or side-engine pulses inherently induces changes in `angle` and `ang_vel`, creating a constant trade-off between translational and rotational stability.

6. **Sequential Contact Instability**: Leg contact is a multi-stage process ($[1,0] \to [1,1]$ or $[0,1] \to [1,1]$); the transition phase between the first and second leg making contact is a period of extreme angular volatility.

7. **Rotational Stability Constraint**: Maintaining a low `angle` is critical for outcome classification; while a lander can achieve the terminal contact reward with high `angle` or `ang_vel`, such states result in a "PARTIAL" outcome rather than "SUCCESS".

8. **Post-Contact Instability and Tip-Over**: Achieving dual-leg contact $[1,1]$ is not a terminal sink; residual translational or angular momentum can trigger a loss of contact (e.g., $[1,1] \to [1,0]$), leading to rapid instability and subsequent penalties.

9. **Reward/Outcome Decoupling**: The environment provides a large terminal reward for successfully establishing ground contact, but this reward is mathematically distinct from the final classification of the attempt (Success vs. Partial).

10. **Multi-Constraint Success Criteria**: A "Success" outcome requires the simultaneous satisfaction of extremely narrow thresholds for all terminal constraints: dual-leg contact, minimal $x$ and $y$ position errors, near-zero $x$ and $y$ velocities, and minimal `angle` and `ang_vel` errors.

---

## 2026-07-02 07:58:53



---

## 2026-07-02 07:59:48

1. **Action 1 (Left Engine)**: Induces angular velocity changes and contributes to both horizontal ($x\_vel$) and vertical ($y\_vel$) velocity shifts.
2. **Action 3 (Right Engine)**: Induces angular velocity changes in the opposite direction of Action 1, serving as the primary mechanism for counteracting rotation.
3. **Action 2 (Main Engine)**: Primarily modulates vertical velocity ($y\_vel$) to manage descent rates, but also generates side effects in horizontal velocity ($x\_vel$) and orientation (angle).
4. **Angular Sensitivity**: The relationship between engine use and angular velocity is highly dynamic; once the `angle` deviates significantly from zero, the `ang_vel` can escalate rapidly, making recovery difficult.
5. **Horizontal Drift**: Cumulative engine usage (Actions 1, 2, and 3) leads to continuous changes in `x_pos` due to the resulting `x_vel`.
6. **Vertical Descent Dynamics**: In the absence of sufficient main engine (Action 2) thrust, `y_pos` decreases and `y_vel` becomes increasingly negative due to gravity.
7. **Landing Contact**: The `left_leg_contact` and `right_leg_contact` states switch to 1.0 upon physical contact with the surface, which often precedes the end of the episode.
8. **Failure Termination**: A terminal reward of -100.000 is applied when the lander undergoes a catastrophic event, such as a high-velocity impact or uncontrolled tipping.
9. **Stabilization Rewards**: Large positive rewards are associated with controlled descent and maintaining a near-vertical orientation as the lander approaches the landing site.
10. **Control Coupling**: Engine actions are heavily coupled; using the main engine (Action 2) to control vertical descent often requires corrective use of side engines (Actions 1 and 3) to mitigate induced angular and horizontal errors.

---

## 2026-07-02 08:09:09

---
1. **Action 1 (Left Engine)**: Induces angular velocity changes and contributes to both horizontal ($x\_vel$) and vertical ($y\_vel$) velocity shifts.
2. **Action 3 (Right Engine)**: Induces angular velocity changes in the opposite direction of Action 1, while also contributing to horizontal ($x\_vel$) and vertical ($y\_vel$) velocity shifts.
3. **Action 2 (Main Engine)**: Primarily modulates vertical velocity ($y\_vel$), but significantly affects horizontal velocity ($x\_vel$), orientation (angle), and angular velocity (ang\_vel).
4. **Angular Sensitivity**: The relationship between engine use and angular velocity is highly dynamic; once the `angle` deviates significantly from zero, the `ang_vel` can escalate rapidly, making recovery difficult.
5. **Multi-Axis Coupling**: All engine actions (1, 2, and 3) are coupled across all degrees of freedom, meaning any thrust applied to manage one parameter (like $y\_vel$) inevitably impacts $x\_vel$ and orientation.
6. **Vertical Descent Dynamics**: In the absence of sufficient main engine (Action 2) thrust, $y\_pos$ decreases and $y\_vel$ becomes increasingly negative due to gravity.
7. **Landing Contact**: The `left_leg_contact` and `right_leg_contact` states switch to 1.0 upon physical contact with the surface.
8. **Landing Stability and Termination**: Physical contact (legs = 1.0) does not automatically terminate the episode; a successful landing requires the lander to achieve both leg contact and a stable, low-velocity state.
9. **Reward Structure**: The environment provides continuous rewards based on descent stability, a high positive terminal reward (e.g., 100.0) for a successful stable landing, and a large negative terminal reward (e.g., -100.0) for catastrophic failure.
10. **Control Coupling**: Using the main engine (Action 2) to manage vertical descent necessitates the compensatory use of side engines (Actions 1 and 3) to mitigate induced horizontal and angular errors.

---

## 2026-07-02 08:10:24

1. **Action 1 (Left Engine)**: Induces angular velocity changes and contributes to both horizontal ($x\_vel$) and vertical ($y\_vel$) velocity shifts, with the direction of the $x\_vel$ shift depending on the current velocity vector.
2. **Action 3 (Right Engine)**: Induces angular velocity changes in the opposite direction of Action 1, while also contributing to horizontal ($x\_vel$) and vertical ($y\_vel$) velocity shifts.
3. **Action 2 (Main Engine)**: Primarily modulates vertical velocity ($y\_vel$), but significantly affects horizontal velocity ($x\_vel$), orientation (angle), and angular velocity (ang\_vel).
4. **Angular Sensitivity**: The relationship between engine use and angular velocity is highly dynamic; as the `angle` deviates from zero, the `ang_vel` can escalate rapidly, making recovery and stabilization difficult.
5. **Multi-Axis Coupling**: All engine actions (1, 2, and 3) are coupled across all degrees of freedom; thrust applied to manage one parameter (such as $y\_vel$) inevitably impacts $x\_vel$ and orientation.
6. **Vertical Descent Dynamics**: In the absence of sufficient main engine (Action 2) thrust, $y\_pos$ decreases and $y\_vel$ becomes increasingly negative due to the effects of gravity.
7. **Landing Contact**: The `left_leg_contact` and `right_leg_contact` states switch to 1.0 upon physical contact with the surface.
8. **Outcome Classification**: Landing contact alone does not guarantee a "SUCCESS" outcome; the final classification (e.g., "SUCCESS" vs "PARTIAL") is heavily dependent on the stability of the `angle` and `ang_vel` at the time of contact and during the post-contact phase.
9. **Post-Contact Instability Penalties**: The reward mechanism continues to apply penalties after leg contact is established; large negative rewards can be triggered if the `angle` or `ang_vel` fails to stabilize or continues to drift significantly post-touchdown.
10. **Control Coupling**: Using the main engine (Action 2) to manage vertical descent necessitates the compensatory use of side engines (Actions 1 and 3) to mitigate induced horizontal and angular errors.

---

## 2026-07-02 08:14:28

1. **Action 1 (Left Engine)**: Induces angular velocity changes and contributes to both horizontal ($x\_vel$) and vertical ($y\_vel$) velocity shifts, with the direction of the $x\_vel$ shift depending on the current velocity vector.
2. **Action 3 (Right Engine)**: Induces angular velocity changes in the opposite direction of Action 1, while also contributing to horizontal ($x\_vel$) and vertical ($y\_vel$) velocity shifts.
3. **Action 2 (Main Engine)**: Primarily modulates vertical velocity ($y\_vel$), but significantly affects horizontal velocity ($x\_vel$), orientation (angle), and angular velocity ($ang\_vel$).
4. **Angular Sensitivity**: The relationship between engine use and angular velocity is highly dynamic; as the `angle` deviates from zero, the `ang_vel` can escalate rapidly, making recovery and stabilization difficult.
5. **Multi-Axis Coupling**: All engine actions (1, 2, and 3) are coupled across all degrees of freedom; thrust applied to manage one parameter (such as $y\_vel$) inevitably impacts $x\_vel$ and orientation.
6. **Vertical Descent Dynamics**: In the absence of sufficient main engine (Action 2) thrust, $y\_pos$ decreases and $y\_vel$ becomes increasingly negative due to the effects of gravity.
7. **Landing Contact Volatility**: The `left_leg_contact` and `right_leg_contact` states switch to 1.0 upon physical contact, but can revert to 0.0 if the lander tips, bounces, or loses stability during the post-touchdown phase.
8. **Outcome Classification**: Landing contact alone does not guarantee a "SUCCESS" outcome; the final classification is heavily dependent on the stabilization of the `angle` and `ang_vel` at the time of contact and during the post-contact phase.
9. **Post-Contact Instability Penalties**: The reward mechanism applies large negative penalties if the lander fails to stabilize, experiences significant post-contact vertical displacement, or exhibits erratic angular/linear motion after contact.
10. **Control Coupling**: Using the main engine (Action 2) to manage vertical descent necessitates the compensatory use of side engines (Actions 1 and 3) to mitigate induced horizontal and angular errors.

---

## 2026-07-02 08:16:13

1. **Side Engine (Action 1 & 3) Dynamics**: These actions induce angular velocity and affect both $x\_vel$ and $y\_vel$; however, post-contact, they can trigger rapid, non-linear increases in $ang\_vel$ that are difficult to arrest.
2. **Main Engine (Action 2) Dynamics**: While primarily modulating $y\_vel$, this action significantly impacts $x\_vel$ and orientation, particularly when the lander's `angle` is non-zero.
3. **Post-Contact Angular Sensitivity**: The environment exhibits heightened angular sensitivity after touchdown; applying side engines to a landed or nearly landed craft can cause $ang\_vel$ to escalate exponentially.
4. **Ground-State Penalty Mechanism**: Applying thrust (especially side engines) while in a contact state (`left_leg_contact` or `right_leg_contact` = 1.0) can result in high-magnitude negative rewards, likely due to induced bouncing or instability on the ground surface.
5. **Multi-Axis Coupling**: All engine actions are coupled across all degrees of freedom; thrust applied to one parameter (such as $y\_vel$) inevitably impacts $x\_vel$ and orientation.
6. **Vertical Descent and Gravity**: In the absence of sufficient main engine thrust, $y\_pos$ decreases and $y\_vel$ becomes increasingly negative due to gravitational acceleration.
7. **Contact State Volatility**: Leg contact states can persist (1.0) throughout the post-landing phase, but the lander may still undergo significant lateral ($x\_vel$) or angular ($ang\_vel$) oscillations while in contact.
8. **Stabilization-Dependent Outcomes**: Final outcome classification (SUCCESS vs. PARTIAL/FAIL) is heavily dependent on the stabilization of `angle`, `ang_vel`, and linear velocities at and after the moment of contact.
9. **Post-Impact Physicality**: Once contact is established, the lander continues to behave as a dynamic body, where engine actions can cause it to slide, bounce, or rotate despite being grounded.
10. **Compensatory Control Requirements**: Managing vertical descent via the main engine necessitates precise, simultaneous compensatory use of side engines to mitigate induced horizontal and angular errors.

---

## 2026-07-02 08:20:41

1. **Side Engine (Action 1 & 3) Dynamics**: These actions induce angular velocity and affect both $x\_vel$ and $y\_vel$; post-contact, they can trigger rapid, non-linear increases in $ang\_vel$ that are difficult to arrest.
2. **Main Engine (Action 2) Dynamics**: While primarily modulating $y\_vel$, this action significantly impacts $x\_vel$ and orientation, particularly when the lander's `angle` is non-zero.
3. **Extreme Side-Engine Contact Penalties**: Applying side engines while in any contact state (`left_leg_contact` or `right_leg_contact` = 1.0) can result in extremely high-magnitude negative rewards (often exceeding -15.0), indicating severe instability or tipping.
4. **Contact-State Volatility**: The lander exhibits bouncing behavior post-touchdown, causing leg contact states to fluctuate between 0.0 and 1.0 as it loses and regains contact with the ground surface.
5. **Multi-Axis Coupling**: All engine actions are coupled across all degrees of freedom; thrust applied to one parameter (such as $y\_vel$) inevitably impacts $x\_vel$ and orientation.
6. **Vertical Descent and Gravity**: In the absence of sufficient main engine thrust, $y\_pos$ decreases and $y\_vel$ becomes increasingly negative due to gravitational acceleration.
7. **Instability via Inaction**: During the landing and post-landing phases, applying "nothing" (Action 0) can result in massive negative rewards if the lack of thrust leads to a loss of stability or an uncontrolled bounce.
8. **Stabilization-Dependent Outcomes**: Final outcome classification is heavily dependent on the stabilization of `angle`, `ang_vel`, and linear velocities at and after the moment of contact.
9. **Post-Impact Physicality**: Once contact is established, the lander continues to behave as a dynamic body, where engine actions can cause it to slide, bounce, or rotate despite being grounded.
10. **Compensatory Control Requirements**: Managing vertical descent via the main engine necessitates precise, simultaneous compensatory use of side engines to mitigate induced horizontal and angular errors.

---

## 2026-07-02 08:22:39

1. **Side Engine (Action 1 & 3) Instability**: Side engines induce angular velocity and affect both $x\_vel$ and $y\_vel$. While necessary for orientation, they are the primary drivers of instability, especially during contact phases.
2. **Main Engine (Action 2) Dynamics**: Primarily modulates $y\_vel$, but significantly impacts $x\_vel$ and `angle` when the lander's orientation is non-zero.
3. **Severe Contact-State Penalties**: Applying side engines (Action 1 or 3) while any leg contact is active (1.0) can trigger extreme negative rewards (e.g., exceeding -13.0), indicating a tipping event or catastrophic loss of stability.
4. **Contact-State Volatility**: Landing is characterized by bouncing behavior, where `left_leg_contact` and `right_leg_contact` fluctuate rapidly between 0.0 and 1.0 upon impact.
5. **Multi-Axis Coupling**: All engine actions are coupled across all degrees of freedom; thrust applied to one parameter (such as $y\_vel$) inevitably impacts $x\_vel$ and orientation.
6. **Gravitational Descent**: In the absence of sufficient main engine thrust, $y\_pos$ decreases and $y\_vel$ becomes increasingly negative due to gravitational acceleration.
7. **Inaction Penalties**: During descent and post-landing, applying "nothing" (Action 0) often results in negative rewards due to the inability to counteract gravity or maintain stability.
8. **Outcome Determination**: Final outcome classification (SUCCESS vs. PARTIAL) is heavily dependent on the stabilization of `angle`, `ang_vel`, and linear velocities at the conclusion of the episode.
9. **Post-Impact Physicality**: Once contact is established, the lander remains a dynamic body; engine actions can cause continued sliding, bouncing, or rotation even while grounded.
10. **Post-Contact Control Conflict**: A high-risk tension exists post-contact: the need to use side engines for orientation stabilization vs. the extreme penalties incurred by using them while the legs are in contact with the ground.

---

## 2026-07-02 08:24:37

1. **Side Engine Instability**: Side engines (Action 1 & 3) induce angular velocity and affect both $x\_vel$ and $y\_vel$; they are necessary for orientation but are the primary drivers of instability.
2. **Main Engine Dynamics**: Action 2 primarily modulates $y\_vel$, but its impact on $x\_vel$ and `angle` is significantly scaled by the lander's current orientation.
3. **Contact-State Reward Dichotomy**: During contact (leg contact = 1.0), engine actions exhibit extreme reward volatility; they can trigger massive penalties (e.g., < -15.0) if they induce instability, but can also yield large positive rewards if they effectively stabilize the lander's orientation and angular velocity.
4. **Contact-State Volatility**: Landing is characterized by rapid fluctuations in `left_leg_contact` and `right_leg_contact` between 0.0 and 1.0 upon impact.
5. **Multi-Axis Coupling**: All engine actions are coupled across all degrees of freedom; thrust applied to one parameter (such as $y\_vel$) inevitably impacts $x\_vel$ and orientation.
6. **Gravitational Descent**: In the absence of sufficient main engine thrust, $y\_pos$ decreases and $y\_vel$ becomes increasingly negative due to gravitational acceleration.
7. **Inaction Penalties**: Applying "nothing" (Action 0) during descent and post-landing often results in negative rewards due to the inability to counteract gravity or maintain stability.
8. **Outcome Determination**: Final outcome classification (SUCCESS vs. PARTIAL) is heavily dependent on the stabilization of `angle`, `ang_vel`, and linear velocities at the conclusion of the episode.
9. **Post-Impact Physicality**: Once contact is established, the lander remains a dynamic body; engine actions can cause continued sliding, bouncing, or rotation even while grounded.
10. **Post-Contact Control Conflict**: A high-risk tension exists post-contact between the necessity of using side engines for orientation stabilization and the extreme penalties incurred if those engines induce instability while the legs are in contact with the ground.

---

## 2026-07-02 08:27:46

---
1. **Side Engine Instability**: Side engines (Action 1 & 3) induce angular velocity and affect both $x\_vel$ and $y\_vel$; they are necessary for orientation but are the primary drivers of instability.
2. **Main Engine Dynamics**: Action 2 primarily modulates $y\_vel$, but its impact on $x\_vel$ and `angle` is significantly scaled by the lander's current orientation.
3. **Extreme Contact-State Reward Dichotomy**: During contact (leg contact = 1.0), engine actions exhibit massive reward volatility; they can trigger extreme penalties (e.g., < -15.0) or yield very large positive rewards (e.g., > 10.0) if they successfully stabilize the lander's orientation and angular velocity.
4. **Contact-State Volatility**: Landing is characterized by rapid fluctuations in `left_leg_contact` and `right_leg_contact` between 0.0 and 1.0 upon impact.
5. **Multi-Axis Coupling**: All engine actions are coupled across all degrees of freedom; thrust applied to one parameter (such as $y\_vel$) inevitably impacts $x\_vel$ and orientation.
6. **Gravitational Descent**: In the absence of sufficient main engine thrust, $y\_pos$ decreases and $y\_vel$ becomes increasingly negative due to gravitational acceleration.
7. **Severe Inaction Penalties**: Applying "nothing" (Action 0) can result in extreme negative rewards (e.g., < -15.0) even after contact is established if the lack of control allows for uncontrolled angular acceleration or instability.
8. **Outcome Determination**: Final outcome classification (SUCCESS vs. PARTIAL) is heavily dependent on the stabilization of `angle`, `ang_vel`, and linear velocities at the conclusion of the episode.
9. **Post-Impact Physicality**: Once contact is established, the lander remains a dynamic body; engine actions can cause continued sliding, bouncing, or rotation even while grounded.
10. **Post-Contact Control Tension**: A high-risk tension exists post-contact between the necessity of using side engines for orientation stabilization and the extreme penalties incurred if those engines induce a tip, bounce, or violent rotation while the legs are in contact with the ground.

---

## 2026-07-02 08:29:31

1. **Side Engine Instability**: Side engines (Action 1 & 3) induce angular velocity and affect both $x\_vel$ and $y\_vel$; they are necessary for orientation but are the primary drivers of instability.
2. **Main Engine Dynamics**: Action 2 primarily modulates $y\_vel$, but its impact on $x\_vel$ and `angle` is significantly scaled by the lander's current orientation.
3. **Extreme Contact-State Reward Dichotomy**: During contact, engine actions exhibit massive reward volatility; they can trigger extreme penalties (e.g., < -10.0) or yield very large positive rewards (e.g., > 10.0) depending on whether the action stabilizes or destabilizes the lander's attitude.
4. **Contact-State Transition**: Landing is characterized by a transition period where `left_leg_contact` and `right_leg_contact` fluctuate rapidly between 0.0 and 1.0 before reaching a potentially stable dual-contact state.
5. **Multi-Axis Coupling**: All engine actions are coupled across all degrees of freedom; thrust applied to one parameter (such as $y\_vel$) inevitably impacts $x\_vel$ and orientation.
6. **Gravitational Descent**: In the absence of sufficient main engine thrust, $y\_pos$ decreases and $y\_vel$ becomes increasingly negative due to gravitational acceleration.
7. **Severe Inaction Penalties**: Applying "nothing" (Action 0) can result in extreme negative rewards (e.g., < -15.0) during descent or post-contact if the lack of control allows for uncontrolled angular acceleration or instability.
8. **Outcome Determination**: Final outcome classification (SUCCESS vs. PARTIAL vs. FAILURE) is heavily dependent on the stabilization of `angle`, `ang_vel`, and linear velocities at the conclusion of the episode.
9. **Grounded Continuous Dynamics**: Once contact is established, the lander does not become a static object; it remains a dynamic body requiring continuous, high-frequency engine corrections (Action 0, 1, 2, or 3) to maintain attitude and prevent drift.
10. **Grounded Attitude Sensitivity**: During the grounded phase, the lander is hypersensitive to angular velocity; even while in contact, engine actions that fail to manage `ang_vel` can trigger immediate and massive penalties, necessitating a delicate balance between orientation control and stability.

---

## 2026-07-02 08:34:37

1. **Side Engine Instability**: Side engines (Action 1 & 3) induce angular velocity and affect both $x\_vel$ and $y\_vel$; they are necessary for orientation but are the primary drivers of instability.
2. **Main Engine Dynamics**: Action 2 primarily modulates $y\_vel$, but its impact on $x\_vel$ and `angle` is significantly scaled by the lander's current orientation.
3. **Terminal Reward Spike**: A massive positive reward (e.g., 100.0) is awarded upon the successful conclusion of an episode, typically when the lander has achieved a stable dual-contact state.
4. **Sequential Contact Transition**: Landing is characterized by a transition period where leg contact occurs sequentially; observations suggest the right leg (`right_leg_contact`) often establishes contact before the left leg.
5. **Multi-Axis Coupling**: All engine actions are coupled across all degrees of freedom; thrust applied to one parameter (such as $y\_vel$) inevitably impacts $x\_vel$ and orientation.
6. **Gravitational Descent**: In the absence of sufficient main engine thrust, $y\_pos$ decreases and $y\_vel$ becomes increasingly negative due to gravitational acceleration.
7. **Severe Inaction Penalties**: Applying "nothing" (Action 0) can result in extreme negative rewards during descent or post-contact if the lack of control allows for uncontrolled drift or angular acceleration.
8. **Grounded Continuous Dynamics**: Once contact is established, the lander remains a dynamic body requiring continuous, high-frequency engine corrections (frequently Action 1) to maintain attitude and prevent drift.
9. **Grounded Velocity Constraints**: To maintain a stable grounded state, the lander must manage its engine output to keep $x\_vel$, $y\_vel$, and `ang_vel` extremely close to zero.
10. **Contact-State Reward Volatility**: During the transition from flight to contact, engine actions exhibit massive reward volatility; they can trigger extreme penalties or large positive rewards depending on whether the action stabilizes or destabilizes the lander's attitude.

---

## 2026-07-02 08:37:50

1. **Side Engine Instability**: Actions 1 and 3 are essential for orientation control but are primary drivers of instability, frequently incurring negative immediate rewards due to the angular velocity and multi-axis drift they induce.
2. **Main Engine Dynamics**: Action 2 is the primary mechanism for countering gravitational descent; it is the most consistent source of positive rewards during the descent phase by modulating $y\_vel$ toward zero.
3. **Terminal Reward Spike**: Successful episodes conclude with a large positive reward spike (e.g., 100.0 in Episode 1), awarded when the lander achieves a stable, low-velocity state with both legs in contact.
4. **Sequential Contact Transition**: The landing process follows a specific sequence where the right leg (`right_leg_contact`) typically establishes contact before the left leg, creating a brief period of asymmetric support.
5. **Multi-Axis Coupling**: All engine actions are coupled across all degrees of freedom; thrust intended to correct one parameter (like $y\_vel$) inevitably affects $x\_vel$ and angular velocity.
6. **Gravitational Descent**: In the absence of sufficient upward thrust from Action 2, $y\_pos$ decreases and $y\_vel$ becomes increasingly negative due to constant gravitational acceleration.
7. **Inaction Penalties**: Applying "nothing" (Action 0) during descent or while grounded often results in negative rewards, as the lander fails to counteract gravity or rotational drift.
8. **Grounded Continuous Dynamics**: Once both legs are in contact, the lander requires high-frequency, continuous engine corrections (often utilizing Actions 1 or 3) to maintain attitude and prevent sliding or tipping.
9. **Grounded Velocity Oscillations**: Even after establishing contact, engine actions can cause small oscillations in $y\_vel$ and $x\_vel$; the agent must manage these pulses to prevent "bouncing" or uncontrolled lateral drift.
10. **Contact-State Reward Volatility**: The transition from flight to contact is marked by extreme reward volatility, where engine actions can trigger massive positive rewards or severe penalties depending on whether they stabilize or destabilize the lander's attitude.

---

## 2026-07-02 08:40:25

1. **Side Engine Instability**: Actions 1 and 3 are essential for orientation control but act as primary drivers of instability, frequently incurring negative immediate rewards due to the induced angular velocity and multi-axis drift.
2. **Main Engine Dynamics**: Action 2 is the primary mechanism for countering gravitational descent, providing the most consistent source of positive rewards by modulating $y\_vel$ toward zero.
3. **Landing Contact Spike**: A significant positive reward spike is awarded upon the initial successful transition to a state where both legs are in contact with low $y\_vel$.
4. **Sequential Leg Contact**: The landing process typically follows a sequence where one leg establishes contact before the other, creating a brief period of asymmetric support.
5. **Multi-Axis Coupling**: All engine actions are coupled across all degrees of freedom; thrust intended to correct one parameter (like $y\_vel$) inevitably affects $x\_vel$ and angular velocity.
6. **Gravitational Descent**: In the absence of sufficient upward thrust from Action 2, $y\_pos$ decreases and $y\_vel$ becomes increasingly negative due to constant gravitational acceleration.
7. **Inaction and Drift Penalties**: Applying "nothing" (Action 0) during descent or while grounded often results in negative rewards, as the lander fails to counteract gravity or rotational drift.
8. **Grounded Tipping and Bouncing**: After landing, engine-induced oscillations can cause a leg to lose contact (`leg_contact` 1.0 $\to$ 0.0), a phenomenon characterized as tipping or bouncing.
9. **Contact-State Reward Volatility**: The most extreme reward fluctuations are tied to leg contact transitions; losing contact while grounded triggers massive penalties, while regaining contact triggers massive rewards.
10. **Grounded Stability Management**: Once both legs are in contact, the lander requires high-frequency, continuous engine corrections to maintain attitude and prevent the tipping/bouncing cycles that trigger contact-state penalties.

---

## 2026-07-02 08:42:56

1. **Side Engine Instability**: Actions 1 and 3 are essential for orientation control but act as primary drivers of instability, frequently inducing angular velocity ($ang\_vel$) that complicates multi-axis drift control.
2. **Main Engine Dynamics**: Action 2 is the primary mechanism for countering gravitational descent, providing the most consistent source of positive rewards by modulating $y\_vel$ toward zero.
3. **Landing Contact Spike**: A significant positive reward spike is awarded upon the initial successful transition to a state where at least one leg establishes contact with low $y\_vel$.
4. **Sequential Leg Contact**: The landing process typically follows a sequence where one leg establishes contact before the other, creating a period of asymmetric support and increased rotational risk.
5. **Multi-Axis Coupling**: All engine actions are coupled across all degrees of freedom; thrust intended to correct one parameter (like $y\_vel$) inevitably affects $x\_vel$ and angular velocity.
6. **Gravitational Descent**: In the absence of sufficient upward thrust from Action 2, $y\_pos$ decreases and $y\_vel$ becomes increasingly negative due to constant gravitational acceleration.
7. **Inaction and Drift Penalties**: Applying "nothing" (Action 0) during descent or while grounded often results in negative rewards, as the lander fails to counteract gravity or rotational drift.
8. **Contact-Induced Angular Spikes**: The transition to contact, particularly during the asymmetric phase of single-leg contact, can trigger high angular velocity spikes that destabilize the lander's attitude and lead to tumbling.
9. **Contact-State Reward Volatility**: Extreme reward fluctuations are tied to leg contact transitions; losing contact while grounded or experiencing a terminal impact with improper orientation triggers massive penalties.
10. **Grounded Stability Management**: Once dual-leg contact is established, the lander requires high-frequency, continuous engine corrections to maintain attitude and prevent the tipping/bouncing cycles that trigger contact loss.

---

## 2026-07-02 08:45:44

1. **Main Engine Descent Control**: Action 2 is the primary mechanism for modulating $y\_vel$ and countering gravitational descent, providing the most consistent source of positive rewards during the approach phase.
2. **Side Engine Angular Coupling**: Actions 1 and 3 are essential for attitude control but inherently induce angular velocity ($ang\_vel$), creating a complex trade-off between orientation correction and rotational stability.
3. **Landing Contact Reward Spike**: A significant positive reward spike is triggered upon the initial transition to a state where at least one leg establishes contact with low $y\_vel$.
4. **Post-Contact Rotational Instability**: The transition to leg contact can induce sudden $ang\_vel$ spikes. If the lander's attitude is not perfectly neutralized during this phase, these spikes can lead to an uncontrollable "tumbling" state where $ang\_vel$ and $angle$ increase exponentially.
5. **Grounded Attitude Maintenance**: Once contact is established, maintaining stability requires precise, high-frequency corrections. Using an engine that exacerbates existing rotation (e.g., firing a side engine that aligns with the direction of a rotational spike) can trigger rapid tipping.
6. **Asymmetric Support Risk**: The period between the first leg establishing contact and both legs being grounded creates a phase of asymmetric support, significantly increasing the risk of rotational instability.
7. **Multi-Axis Coupling**: All engine actions are coupled across all degrees of freedom; thrust intended to correct one parameter (like $y\_vel$) inevitably affects $x\_vel$ and angular velocity.
8. **Gravity and Inaction Penalties**: In the absence of sufficient upward thrust from Action 2, $y\_pos$ and $y\_vel$ degrade due to gravity. Applying "nothing" (Action 0) during critical descent or grounding phases typically results in negative rewards.
9. **Terminal Failure Mechanism**: A terminal failure, such as a tip-over event characterized by high angular velocity while grounded, triggers a massive negative reward penalty.
10. **Contact-State Volatility**: The transition from free-fall to contact is the most mathematically volatile phase of the simulation, characterized by rapid shifts in reward and the potential for immediate state divergence.

---

## 2026-07-02 08:47:38

1. **Main Engine Vertical Control**: Action 2 is the primary mechanism for modulating $y\_vel$ and countering gravitational descent, though its effectiveness is highly dependent on the current $y\_vel$ at the time of application.
2. **Side Engine Angular Coupling**: Actions 1 and 3 are essential for attitude control but inherently induce significant angular velocity ($ang\_vel$) and lateral velocity ($x\_vel$) perturbations, creating a complex multi-variable stabilization problem.
3. **Landing Contact Reward Spikes**: The transition to a contact state ([1,0] or [0,1]) triggers immediate reward spikes, but the magnitude is highly sensitive to the lander's $y\_vel$ at the moment of impact.
4. **Impact-Induced Angular Spikes**: The transition from free-fall to contact, particularly during asymmetric landing phases, induces sudden and potentially massive spikes in $ang\_vel$.
5. **Asymmetric Support Instability**: The phase between the first leg establishing contact and both legs being grounded represents a period of extreme rotational instability where the lander is prone to rapid angular acceleration.
6. **Grounded State Reward Volatility**: Once contact is established, the reward function exhibits high volatility; even minor deviations in $angle$, $y\_vel$, or $x\_vel$ while grounded can result in rapidly oscillating reward values.
7. **Grounded Stability Penalties**: Large negative reward penalties are triggered during the grounded phase if the lander experiences sudden shifts in velocity or orientation, indicating a heavy penalty for "tipping" or "sliding" events.
8. **Multi-Axis Coupling**: Every engine action results in coupled changes across all degrees of freedom; thrust intended for verticality or attitude correction inevitably affects $x\_pos$, $x\_vel$, and $angle$.
9. **Gravity-Induced Descent**: In the absence of sufficient upward thrust from Action 2, gravity consistently degrades $y\_pos$ and $y\_vel$, increasing the kinetic energy at the time of contact.
10. **Terminal Success Reward**: A successful, stabilized landing (characterized by low $y\_vel$, low $ang\_vel$, and both legs grounded) provides a massive, discrete terminal reward spike (e.g., 100.0).

---

## 2026-07-02 08:51:36

1. **Main Engine Vertical/Lateral Coupling**: Action 2 is the primary mechanism for modulating $y\_vel$, but it inherently induces significant lateral ($x\_vel$) and angular perturbations, requiring simultaneous compensation.
2. **Side Engine Angular Coupling**: Actions 1 and 3 are essential for attitude control but induce substantial angular velocity ($ang\_vel$) and lateral velocity ($x\_vel$) changes.
3. **Landing Impact Sensitivity**: The transition to a contact state ([1,0], [0,1], or [1,1]) triggers immediate reward spikes that are highly sensitive to the lander's $y\_vel$ and $ang\_vel$ at the moment of impact.
4. **Asymmetric Support Instability**: The phase between the first leg establishing contact and both legs being grounded represents a period of extreme rotational instability.
5. **Grounded Main Engine Destabilization**: Applying Action 2 (Main Engine) while the lander is in a grounded state ([1,1]) is highly disruptive, frequently triggering large negative reward penalties, likely due to the thrust inducing tipping or bouncing.
6. **Grounded State Reward Optimization**: While the grounded phase is volatile, the reward function can yield significantly high positive values (e.g., >10.0) if the lander maintains extreme stability with minimal angular and lateral velocities.
7. **Grounded Side Engine Utility**: During the grounded phase, Actions 1 and 3 can be used to maintain or achieve high-reward stable states, though they carry the risk of inducing rotational instability if applied excessively.
8. **Multi-Axis Coupling**: Every engine action results in coupled changes across all degrees of freedom; thrust intended for verticality or attitude correction inevitably affects $x\_pos$, $x\_vel$, and $angle$.
9. **Gravity-Induced Descent**: In the absence of sufficient upward thrust from Action 2, gravity consistently degrades $y\_pos$ and $y\_vel$, increasing the kinetic energy at the time of contact.
10. **Terminal Success Reward**: A successful, stabilized landing (characterized by low $y\_vel$, low $ang\_vel$, and both legs grounded) provides a massive, discrete terminal reward spike of 100.0.

---

## 2026-07-02 08:53:08

1. **Main Engine Vertical/Lateral Coupling**: Action 2 is the primary mechanism for modulating $y\_vel$, but it inherently induces significant lateral ($x\_vel$) and angular ($ang\_vel$) perturbations, requiring simultaneous compensation.
2. **Side Engine Angular/Lateral Coupling**: Actions 1 and 3 are essential for attitude control but induce substantial angular velocity ($ang\_vel$) and lateral velocity ($x\_vel$) changes.
3. **Contact-Induced Rotational Volatility**: The transition to a contact state ([1,0] or [0,1]) can trigger sudden, high-magnitude spikes in angular velocity ($ang\_vel$), which, if uncompensated, can cause the lander to lose all leg contact ([0,0]) due to rotational momentum.
4. **Asymmetric Support Instability**: The phase between the first leg establishing contact and both legs being grounded ([1,1]) represents a period of extreme rotational instability and high risk of tipping.
5. **Grounded Main Engine Destabilization**: Applying Action 2 (Main Engine) while the lander is in a grounded state ([1,1]) is highly disruptive, frequently triggering large negative reward penalties, likely due to the thrust inducing bouncing or tipping.
6. **Grounded Side Engine Stabilization**: Once the lander achieves a fully grounded state ([1,1]), side engines (Actions 1 and 3) are the optimal mechanisms for fine-tuning attitude ($angle$) and suppressing $ang\_vel$ to maintain stability.
7. **Multi-Axis Coupling**: Every engine action results in coupled changes across all degrees of freedom ($x\_pos, x\_vel, y\_pos, y\_vel, angle, ang\_vel$).
8. **Gravity-Induced Descent**: In the absence of sufficient upward thrust from Action 2, gravity consistently degrades $y\_pos$ and $y\_vel$, increasing the kinetic energy at the time of contact.
9. **Intermediate Grounding Reward**: Achieving full ground contact ([1,1]) triggers a significant, discrete intermediate reward spike (approximately 19.0), though stability must be maintained immediately following this transition to avoid negative penalties.
10. **Terminal Success Reward**: A successful, stabilized landing (characterized by low $y\_vel$, low $ang\_vel$, and both legs grounded [1,1]) provides a massive, discrete terminal reward spike of 100.0.

---

## 2026-07-02 08:54:41

1. **Main Engine Vertical/Lateral Coupling**: Action 2 is the primary mechanism for modulating $y\_vel$, but it inherently induces significant lateral ($x\_vel$) and angular ($ang\_vel$) perturbations, requiring simultaneous compensation.
2. **Side Engine Angular/Lateral Coupling**: Actions 1 and 3 are essential for attitude control but induce substantial angular velocity ($ang\_vel$) and lateral velocity ($x\_vel$) changes.
3. **Contact-Induced Rotational Volatility**: The transition to a single-leg contact state ([1,0] or [0,1]) can trigger sudden, high-magnitude spikes in angular velocity ($ang\_vel$), which can lead to a total loss of contact if uncompensated.
4. **Asymmetric Support Instability**: The phase between the first leg establishing contact and both legs being grounded ([1,1]) represents a period of extreme rotational instability and high risk of tipping.
5. **Main Engine/Single-Leg Contact Risk**: Applying Action 2 (Main Engine) while the lander is in a single-leg contact state ([1,0] or [0,1]) is highly disruptive and can cause the lander to bounce or tip, resulting in a total loss of leg contact ([0,0]).
6. **Grounded Main Engine Destabilization**: Applying Action 2 while the lander is in a fully grounded state ([1,1]) is highly destabilizing and frequently triggers massive negative reward penalties.
7. **Grounded Side Engine Stabilization**: Once the lander achieves a fully grounded state ([1,1]), side engines (Actions 1 and 3) are the optimal mechanisms for fine-tuning attitude ($angle$) and suppressing $ang\_vel$ to maintain stability.
8. **Post-Contact Attitude Drift**: Achieving full ground contact ([1,1]) does not guarantee stability; if $angle$ and $ang\_vel$ are not actively suppressed during the grounding phase, the lander can still enter a terminal tumble.
9. **Multi-Axis Coupling**: Every engine action results in coupled changes across all degrees of freedom ($x\_pos, x\_vel, y\_pos, y\_vel, angle, ang\_vel$).
10. **Terminal Reward Sensitivity**: Successful landing requires low $y\_vel$, low $ang\_vel$, and stable [1,1] contact; failure to maintain these specific conditions during or after the grounding transition results in a massive terminal penalty of -100.0.

---

## 2026-07-02 08:59:06

1. **Main Engine Vertical/Lateral Coupling**: Action 2 is the primary mechanism for modulating $y\_vel$, but it inherently induces significant lateral ($x\_vel$) and angular ($ang\_vel$) perturbations, requiring simultaneous compensation.
2. **Side Engine Angular/Lateral Coupling**: Actions 1 and 3 are essential for attitude control but induce substantial angular velocity ($ang\_vel$) and lateral velocity ($x\_vel$) changes.
3. **Contact-Induced Rotational Volatility**: The transition to a single-leg contact state ([1,0] or [0,1]) can trigger sudden, high-magnitude spikes in angular velocity ($ang\_vel$), which can lead to a total loss of contact if uncompensated.
4. **Asymmetric Support Instability**: The phase between the first leg establishing contact and both legs being grounded ([1,1]) represents a period of extreme rotational instability and high risk of tipping.
5. **Main Engine/Single-Leg Contact Risk**: Applying Action 2 while the lander is in a single-leg contact state ([1,0] or [0,1]) is highly disruptive and can cause the lander to bounce or tip, resulting in a total loss of leg contact ([0,0]).
6. **Grounded Main Engine Destabilization**: Applying Action 2 while the lander is in a fully grounded state ([1,1]) is highly destabilizing and can trigger high-magnitude spikes in angular velocity ($ang\_vel$), leading to catastrophic failure.
7. **Grounded Side Engine Stabilization**: Once the lander achieves a fully grounded state ([1,1]), side engines (Actions 1 and 3) are the optimal mechanisms for fine-tuning attitude ($angle$) and suppressing $ang\_vel$ to maintain stability.
8. **Post-Contact Attitude/Angle Requirement**: Achieving full ground contact ([1,1]) does not guarantee success; the lander must actively suppress both $ang\_vel$ and the absolute $angle$ during the grounding phase to prevent terminal instability.
9. **Multi-Axis Coupling**: Every engine action results in coupled changes across all degrees of freedom ($x\_pos, x\_vel, y\_pos, y\_vel, angle, ang\_vel$).
10. **Terminal Reward Sensitivity**: Successful landing requires low $y\_vel$, low $ang\_vel$, and low $angle$; failure to maintain these specific conditions during or after the grounding transition results in a massive terminal penalty of -100.0.

---

## 2026-07-02 09:00:35

1. **Main Engine Vertical/Lateral Coupling**: Action 2 is the primary mechanism for modulating $y\_vel$, but it inherently induces significant lateral ($x\_vel$) and angular ($ang\_vel$) perturbations.
2. **Side Engine Attitude/Lateral Control**: Actions 1 and 3 are essential for managing attitude ($angle$ and $ang\_vel$) and can be used to modulate lateral velocity ($x\_vel$).
3. **Contact-Induced Angular Spikes**: The transition to a single-leg contact state ([1,0] or [0,1]) triggers sudden, high-magnitude spikes in angular velocity ($ang\_vel$).
4. **Grounding Phase Instability**: The period between the first leg establishing contact and both legs being grounded ([1,1]) represents a phase of extreme rotational volatility and high risk of tipping.
5. **Single-Leg Contact/Main Engine Risk**: Applying Action 2 while the lander is in a single-leg contact state ([1,0] or [0,1]) is highly disruptive and can cause the lander to bounce or lose all leg contact ([0,0]).
6. **Grounded Main Engine Destabilization**: Applying Action 2 while the lander is in a fully grounded state ([1,1]) is highly destabilizing and triggers high-magnitude spikes in $ang\_vel$, leading to catastrophic failure.
7. **Post-Grounding Stabilization Necessity**: Achieving dual-leg contact ([1,1]) is insufficient for success; the lander must actively use side engines (Actions 1 and 3) to suppress $ang\_vel$ and $angle$ to prevent tip-over.
8. **Terminal Outcome Differentiation**: The distinction between a SUCCESS and a PARTIAL outcome is primarily determined by the lander's ability to maintain minimal $angle$ and $ang\_vel$ during the post-grounding stabilization phase.
9. **Multi-Axis Coupling**: Every engine action results in coupled changes across all degrees of freedom ($x\_pos, x\_vel, y\_pos, y\_vel, angle, ang\_vel$).
10. **Terminal Reward Sensitivity**: Successful landing is contingent on achieving low $y\_vel$, low $ang\_vel$, and low $angle$ during the grounding and stabilization phases; failure to maintain these conditions results in a massive terminal penalty.

---

## 2026-07-02 09:05:40

1. **Main Engine Vertical/Lateral Coupling**: Action 2 is the primary mechanism for modulating $y\_vel$, but it inherently induces significant lateral ($x\_vel$) and angular ($ang\_vel$) perturbations.
2. **Side Engine Attitude/Lateral Control**: Actions 1 and 3 are essential for managing attitude ($angle$ and $ang\_vel$) and can be used to modulate lateral velocity ($x\_vel$).
3. **Contact-Induced Angular Spikes**: The transition to a single-leg contact state ([1,0] or [0,1]) triggers sudden, high-magnitude spikes in angular velocity ($ang\_vel$).
4. **Grounding Phase Instability**: The period between the first leg establishing contact and both legs being grounded ([1,1]) represents a phase of extreme rotational volatility and high risk of tipping.
5. **Grounded-to-Air Bounce Effect**: Applying any engine action (Actions 1, 2, or 3) while the lander is in a fully grounded state ([1,1]) can trigger a sudden loss of all leg contact ([0,0]).
6. **Single-Leg Contact/Main Engine Risk**: Applying Action 2 while the lander is in a single-leg contact state ([1,0] or [0,1]) is highly disruptive and can cause the lander to lose all leg contact ([0,0]).
7. **Post-Grounding Stabilization Necessity**: Achieving dual-leg contact ([1,1]) is insufficient for success; the lander must actively use side engines (Actions 1 and 3) to suppress $ang\_vel$ and $angle$ to prevent tip-over or bouncing.
8. **Terminal Outcome Differentiation**: The distinction between a SUCCESS and a PARTIAL outcome is primarily determined by the lander's ability to maintain minimal $angle$ and $ang\_vel$ during the post-grounding stabilization phase.
9. **Multi-Axis Coupling**: Every engine action results in coupled changes across all degrees of freedom ($x\_pos, x\_vel, y\_pos, y\_vel, angle, ang\_vel$).
10. **Terminal Reward Sensitivity**: Successful landing is contingent on achieving low $y\_vel$, low $ang\_vel$, and low $angle$ during the grounding and stabilization phases; failure to maintain these conditions results in a massive terminal penalty.

---

## 2026-07-02 09:08:21

1. **Main Engine Vertical/Lateral Coupling**: Action 2 is the primary mechanism for modulating $y\_vel$, but it inherently induces significant lateral ($x\_vel$) and angular ($ang\_vel$) perturbations.
2. **Side Engine Attitude/Lateral Control**: Actions 1 and 3 are essential for managing attitude ($angle$ and $ang\_vel$) and can be used to modulate lateral velocity ($x\_vel$).
3. **Single-Leg Lever Effect**: Applying a side engine (Action 1 or 3) while only the opposite leg is in contact ([0,1] for Action 1, [1,0] for Action 3) induces extreme angular velocity spikes, as the engine torque acts upon the lander as a lever pivoted on the grounded leg.
4. **Grounding Phase Volatility**: The transition from a single-leg contact state to a dual-leg contact state ([1,1]) is a period of extreme rotational instability and high risk of tipping.
5. **Grounded-to-Air Bounce Effect**: Applying any engine action (Actions 1, 2, or 3) while the lander is in a fully grounded state ([1,1]) can trigger a sudden loss of all leg contact ([0,0]).
6. **Contact-Loss Feedback Loop**: High angular velocity ($ang\_vel$) during the single-leg contact phase can trigger a feedback loop where increasing tilt leads to total loss of contact ([0,0]) rather than achieving dual-leg grounding.
7. **Post-Grounding Stabilization Necessity**: Achieving dual-leg contact ([1,1]) is insufficient; the lander must actively use side engines (Actions 1 and 3) to suppress $ang\_vel$ and $angle$ to prevent bouncing or tipping.
8. **Terminal Outcome Differentiation**: The distinction between a SUCCESS and a FAILURE is determined by the lander's ability to maintain minimal $angle$, $ang\_vel$, and $y\_vel$ during the post-grounding stabilization phase.
9. **Multi-Axis Coupling**: Every engine action results in coupled changes across all degrees of freedom ($x\_pos, x\_vel, y\_pos, y\_vel, angle, ang\_vel$).
10. **Terminal Reward Sensitivity**: Successful landing is contingent on achieving low $y\_vel$, low $ang\_vel$, and low $angle$ during the grounding and stabilization phases; failure to maintain these conditions results in a massive terminal penalty.

---

## 2026-07-02 10:05:03



---

## 2026-07-02 10:07:39

1. Gravity provides a constant downward acceleration, causing $y\_vel$ to become increasingly negative over time in the absence of upward thrust.
2. The main engine (Action 2) provides significant upward vertical thrust to counteract gravity and manage $y\_vel$.
3. The side engines (Action 1: left, Action 3: right) provide both lateral force (affecting $x\_vel$) and rotational torque (affecting $ang\_vel$).
4. Using side engines to correct the lander's orientation introduces a coupling between $x\_vel$ and $ang\_vel$; excessive use can cause rapid lateral drift.
5. Because the lander's main thrust vector is aligned with its body, the $x\_vel$ is also influenced by the $angle$; a tilted lander will produce lateral acceleration even when using only the main engine.
6. Angular stability is highly sensitive; once $ang\_vel$ reaches a high magnitude, the $angle$ can deviate rapidly, potentially leading to a state where rotational momentum is difficult to arrest.
7. A critical threshold for stability exists; extreme values in $angle$ (e.g., exceeding 0.5 radians) or high $ang\_vel$ during descent are strongly associated with catastrophic failure and negative terminal rewards.
8. The contact sensors ($left\_leg\_contact$ and $right\_leg\_contact$) indicate terrain interaction and are essential for identifying the transition from flight to landing.
9. Successful landing (terminal reward +100) requires the lander to achieve a near-zero $y$ position with minimal $y\_vel$, $x\_vel$, and $ang\_vel$.
10. The environment exhibits momentum persistence; changes in velocity ($x\_vel, y\_vel, ang\_vel$) do not instantly dissipate and require active counter-thrust to stabilize.

---

## 2026-07-02 10:09:24

1. Gravity provides a constant downward acceleration, causing $y\_vel$ to become increasingly negative in the absence of upward thrust.
2. The main engine (Action 2) provides significant upward vertical thrust to manage $y\_vel$ and counteract gravity.
3. The side engines (Action 1: left, Action 3: right) provide both lateral force (affecting $x\_vel$) and rotational torque (affecting $ang\_vel$).
4. The lander's orientation couples thrust to lateral motion; a non-zero $angle$ causes the main engine's thrust to contribute to $x\_vel$ acceleration.
5. Angular stability is highly sensitive; high $ang\_vel$ leads to rapid $angle$ deviations, and rotational momentum requires active counter-torque to arrest.
6. Terrain contact is identified when the $left\_leg\_contact$ and $right\_leg\_contact$ sensors transition to 1.0, typically occurring as $y$ reaches or crosses 0.
7. The impact of landing can trigger sudden, significant spikes in angular velocity ($ang\_vel$), potentially destabilizing the lander immediately upon contact.
8. Post-contact, the lander remains subject to rotational physics; applying side engines while in contact can cause the lander to spin or tumble on the terrain.
9. Successful landing (terminal reward +100) is achieved by establishing terrain contact while maintaining minimal $x\_vel$, $y\_vel$, and $ang\_vel$.
10. The environment exhibits momentum persistence across all velocity components ($x\_vel, y\_vel, ang\_vel$), meaning motion does not dissipate without active counter-thrust.

---

## 2026-07-02 10:12:24

1. Gravity provides a constant downward acceleration, causing $y\_vel$ to become increasingly negative in the absence of upward thrust.
2. The main engine (Action 2) provides significant upward vertical thrust to manage $y\_vel$ and counteract gravity.
3. The side engines (Action 1: left, Action 3: right) provide both lateral force (affecting $x\_vel$) and rotational torque (affecting $ang\_vel$).
4. The lander's orientation couples thrust to lateral motion; a non-zero $angle$ causes the main engine's thrust to contribute to $x\_vel$ acceleration.
5. Angular stability is highly sensitive; high $ang\_vel$ leads to rapid $angle$ deviations, and rotational momentum requires active counter-torque to arrest.
6. Terrain contact is identified when the $left\_leg\_contact$ and $right\_leg\_contact$ sensors transition to 1.0.
7. Terrain contact is not a permanent state; applying thrust (either side or main engines) while in contact can cause the lander to tilt or bounce, causing contact sensors to transition back to 0.0.
8. Post-contact, the lander remains subject to rotational physics; applying engines can trigger sudden, significant spikes in $ang\_vel$, potentially causing the lander to tumble or spin on the terrain.
9. Successful landing (terminal reward +100) is achieved by establishing terrain contact while maintaining minimal $x\_vel$, $y\_vel$, $ang\_vel$, and $angle$.
10. The environment exhibits momentum persistence across all velocity components ($x\_vel, y\_vel, ang\_vel$), meaning motion does not dissipate without active counter-thrust.

---

## 2026-07-02 10:15:17

1. Gravity provides a constant downward acceleration, causing $y\_vel$ to become increasingly negative in the absence of upward thrust.
2. The main engine (Action 2) provides significant upward vertical thrust to manage $y\_vel$ and counteract gravity.
3. Side engines (Action 1: left, Action 3: right) provide both lateral force and rotational torque; Action 1 provides negative $x$ acceleration and positive torque, while Action 3 provides positive $x$ acceleration and negative torque.
4. The lander's orientation couples thrust to lateral motion; a non-zero $angle$ causes the main engine's thrust to contribute to $x\_vel$ acceleration.
5. Angular stability is highly sensitive; high $ang\_vel$ leads to rapid $angle$ deviations, and rotational momentum requires active counter-torque to arrest.
6. Terrain contact is identified when the $left\_leg\_contact$ and $right\_leg\_contact$ sensors transition to 1.0.
7. Terrain contact is not a permanent state; applying thrust (either side or main engines) while in contact can cause the lander to tilt or bounce, causing contact sensors to transition back to 0.0.
8. Applying side engines while in terrain contact can trigger extreme, high-magnitude spikes in $ang\_vel$, leading to rapid, high-velocity tumbling.
9. Successful landing (terminal reward +100) is achieved by establishing terrain contact while maintaining minimal $x\_vel, y\_vel, ang\_vel,$ and $angle$.
10. Terminal failure (reward -100) occurs when the lander's $y\_pos$ falls below the terrain level; momentum persists across all velocity components ($x\_vel, y\_vel, ang\_vel$) until actively counteracted.

---

## 2026-07-02 10:18:50

1. Gravity: Constant downward acceleration causes $y\_vel$ to become increasingly negative in the absence of upward thrust.
2. Main Engine (Action 2): Provides significant upward vertical thrust to manage $y\_vel$ and counteract gravity.
3. Side Engines (Action 1: left, Action 3: right): Action 1 provides negative $x$ acceleration and positive torque; Action 3 provides positive $x$ acceleration and negative torque.
4. Orientation Coupling: The lander's $angle$ causes the main engine's thrust to contribute to lateral $x\_vel$ acceleration.
5. Angular Sensitivity: High $ang\_vel$ leads to rapid $angle$ deviations, and rotational momentum requires active counter-torque to arrest.
6. Contact Detection: Terrain contact is identified when both $left\_leg\_contact$ and $right\_leg\_contact$ sensors transition to 1.0.
7. Contact Dynamics: Applying thrust while in contact can cause the lander to tilt, bounce, or cause the contact sensors to transition back to 0.0.
8. Side Engine Contact Spikes: Applying side engines (Action 1 or 3) while in terrain contact can trigger extreme, high-magnitude spikes in $ang\_vel$, leading to rapid, high-velocity tumbling.
9. Landing Success Criteria: The distinction between success and partial success is determined by the stability of the lander (minimal $x\_vel, y\_vel, ang\_vel,$ and $angle$) at the moment of contact.
10. Failure Conditions: Terminal failure occurs if contact is established while the lander is unstable (high $angle$ or $ang\_vel$) or if momentum in any component is not arrested before $y\_pos$ reaches the terrain level.

---

## 2026-07-02 10:20:15

1. Gravity: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of upward thrust.
2. Main Engine (Action 2): Provides significant upward vertical thrust to counteract gravity and manage $y\_vel$.
3. Side Engines (Action 1: left, Action 3: right): Action 1 provides negative $x$ acceleration and positive torque; Action 3 provides positive $x$ acceleration and negative torque.
4. Orientation Coupling: The lander's $angle$ causes the main engine's thrust to contribute to lateral $x\_vel$ acceleration.
5. Angular Sensitivity: High $ang\_vel$ leads to rapid $angle$ deviations, and rotational momentum requires active counter-torque to arrest.
6. Contact Detection: Terrain contact is confirmed when both $left\_leg\_contact$ and $right\_leg\_contact$ sensors are 1.0.
7. Contact Bouncing: Applying thrust while in contact can cause the lander to tilt or bounce, leading to contact sensors transitioning from 1.0 back to 0.0.
8. Side Engine Grounded Spikes: Applying side engines (Action 1 or 3) while in terrain contact can trigger immediate, high-magnitude spikes in $ang\_vel$ and cause loss of contact on one or both legs.
9. Landing Success Criteria: Success is determined by the stability of the lander (minimal $ang\_vel$ and $angle$) at the moment contact is established and maintained.
10. Termination: Terminal success (a large positive reward) is granted when the lander achieves and maintains stable contact with the terrain.

---

## 2026-07-02 10:22:51

1. Gravity: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of upward thrust.
2. Main Engine (Action 2): Provides significant upward vertical thrust to manage $y\_vel$ and can assist in establishing contact.
3. Side Engines (Action 1: left, Action 3: right): Action 1 provides negative $x$ acceleration and positive torque; Action 3 provides positive $x$ acceleration and negative torque.
4. Orientation Coupling: The lander's $angle$ causes the main engine's thrust to contribute to lateral $x\_vel$ acceleration.
5. Angular Sensitivity: High $ang\_vel$ leads to rapid $angle$ deviations, and rotational momentum requires active counter-torque to arrest.
6. Contact Detection: Terrain contact is confirmed when both $left\_leg\_contact$ and $right\_leg\_contact$ sensors are 1.0.
7. Corresponding Side Engine Penalty: Applying a side engine while its corresponding leg is in contact (Action 1 while $left\_leg\_contact=1.0$ or Action 3 while $right\_leg\_contact=1.0$) triggers severe negative rewards and often results in immediate loss of contact.
8. Opposite Side Engine Stabilization: Applying a side engine while the opposite leg is in contact (Action 1 while $right\_leg\_contact=1.0$ or Action 3 while $left\_leg\_contact=1.0$) can be used to stabilize the lander and restore full contact, potentially yielding high positive rewards.
9. Contact Bouncing: Applying thrust (including the main engine) while in contact can cause the lander to tilt or bounce, leading to the loss of contact on one or both legs.
10. Landing Success: Terminal success is granted when the lander achieves and maintains stable contact (both legs at 1.0) with minimal $angle$ and $ang\_vel$.

---

## 2026-07-02 10:26:36

1. Gravity: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of upward thrust.
2. Main Engine (Action 2): Provides significant upward vertical thrust to manage $y\_vel$ and can be used to assist in establishing or maintaining contact.
3. Side Engines (Action 1: left, Action 3: right): Action 1 provides negative $x$ acceleration and positive torque; Action 3 provides positive $x$ acceleration and negative torque.
4. Orientation Coupling: The lander's $angle$ determines how much the main engine's thrust contributes to lateral $x\_vel$ acceleration.
5. Angular Sensitivity: High $ang\_vel$ causes rapid $angle$ deviations, and rotational momentum requires active counter-torque to arrest.
6. Contact Detection: Terrain contact is confirmed when both $left\_leg\_contact$ and $right\_leg\_contact$ sensors are 1.0.
7. Side Engine/Contact Penalty: Applying a side engine while its corresponding leg is in contact (Action 1 while $left\_leg\_contact=1.0$ or Action 3 while $right\_leg\_contact=1.0$) triggers severe negative rewards, particularly when the lander's $angle$ is non-zero.
8. Opposite Side Engine Stabilization: Applying a side engine while the opposite leg is in contact (Action 1 while $right\_leg\_contact=1.0$ or Action 3 while $left\_leg\_contact=1.0$) can be used to stabilize orientation and often yields high positive rewards.
9. Contact Bouncing: Applying thrust (including the main engine) while in contact can cause the lander to tilt or bounce, potentially leading to the loss of contact on one or both legs.
10. Landing Success: Terminal success is granted via a large positive reward (e.g., 100.0) when the lander achieves and maintains stable contact (both legs at 1.0) with minimal $angle$ and $ang\_vel$.

---

## 2026-07-02 10:28:53

1. Gravity: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of upward thrust.
2. Main Engine (Action 2): Provides significant upward vertical thrust used to manage $y\_vel$ and facilitate landing.
3. Side Engine Mechanics: Action 1 (left) provides negative $x$ acceleration and positive torque; Action 3 (right) provides positive $x$ acceleration and negative torque.
4. Orientation-Thrust Coupling: The lander's $angle$ determines the degree to which the main engine's thrust contributes to lateral $x\_vel$ acceleration.
5. Angular Sensitivity: High $ang\_vel$ leads to rapid $angle$ deviations, and rotational momentum requires active counter-torque to arrest.
6. Contact Detection: Terrain contact is confirmed only when both $left\_leg\_contact$ and $right\_leg\_contact$ sensors are 1.0.
7. Side Engine/Contact Penalty: Applying a side engine while its corresponding leg is in contact (e.g., Action 1 while $left\_leg\_contact=1.0$) generally triggers negative rewards.
8. High-Velocity Stabilization Risks: Using an opposite-side engine to stabilize orientation (e.g., Action 1 while $right\_leg\_contact=1.0$) can result in severe negative rewards if $ang\_vel$ is excessively high.
9. Contact Bouncing: Applying thrust (main or side engines) while in contact can cause the lander to tilt or bounce, potentially leading to the loss of contact on one or both legs.
10. Landing Success/Failure: Terminal success is granted for stable contact (both legs at 1.0) with minimal $angle$ and $ang\_vel$; failure to meet these stability requirements upon contact results in a large negative reward.

---

## 2026-07-02 10:32:31

1. Gravity: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of upward thrust.
2. Main Engine (Action 2): Provides significant upward vertical thrust used to manage $y\_vel$ and facilitate landing.
3. Side Engine Mechanics: Action 1 (left) provides negative $x$ acceleration and positive torque; Action 3 (right) provides positive $x$ acceleration and negative torque.
4. Orientation-Thrust Coupling: The lander's $angle$ determines the degree to which the main engine's thrust contributes to lateral $x\_vel$ acceleration.
5. Angular Sensitivity: High $ang\_vel$ leads to rapid $angle$ deviations, and rotational momentum requires active counter-torque to arrest.
6. Contact States: Terrain contact can be registered on a single leg ($left\_leg\_contact=1.0$ or $right\_leg\_contact=1.0$) or both legs ($1.0, 1.0$).
7. Side Engine/Contact Reward Volatility: Applying side engines while in contact (single or dual leg) can trigger extreme reward magnitudes; rewards are highly positive if torque reduces $ang\_vel$ and highly negative if torque exacerbates rotation.
8. Stabilization via Torque: During contact, side engines are critical for arresting $ang\_vel$ to prevent landing failure, but incorrect application is heavily penalized.
9. Landing Success: Terminal success is granted for stable contact (both legs at 1.0) with minimal $angle$ and $ang\_vel$.
10. Landing Failure: Failure to meet stability requirements or applying improper thrust (such as side engines that exacerbate rotation) upon contact results in large negative rewards.

---

## 2026-07-02 10:37:58

1. Gravity: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of upward thrust.
2. Main Engine: Provides vertical thrust used to manage $y\_vel$ and facilitate landing.
3. Side Engine Mechanics: Action 1 (left) provides negative $x$ acceleration and positive torque; Action 3 (right) provides positive $x$ acceleration and negative torque.
4. Orientation-Thrust Coupling: The lander's $angle$ determines the degree to which the main engine's thrust contributes to lateral $x\_vel$ acceleration.
5. Contact States: Terrain contact is registered on a single leg ($left\_leg\_contact=1.0$ or $right\_leg\_contact=1.0$) or both legs ($1.0, 1.0$).
6. Reward Magnitude Disparity: Absolute reward values are significantly higher during the contact phase than during the free-flight phase.
7. Contact-Induced Reward Volatility: Applying engines while in contact triggers extreme reward swings; side engines can yield massive positive rewards for stabilizing $ang\_vel$ and massive negative rewards for exacerbating it.
8. Post-Contact Instability: Applying thrust (main or side engines) while legs are grounded can cause rapid, unstable shifts in $y\_vel$ or $angle$, potentially leading to large penalties for bouncing or tipping.
9. Angular Sensitivity in Contact: Once legs are grounded, the lander is hyper-sensitive to torque; precise counter-torque is required to arrest $ang\_vel$, as misapplied side engines can cause rapid, violent rotation.
10. Landing Success and Failure: Terminal success requires stable, dual-leg contact with minimal $angle$ and $ang\_vel$; improper thrust application or failure to stabilize upon contact results in large negative rewards.

---

## 2026-07-02 10:46:25

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of upward thrust.
2. **Main Engine Mechanics**: Provides vertical thrust used to manage $y\_vel$. During the contact phase, main engine application can yield significant positive rewards, suggesting a role in maintaining vertical stability or consistent ground pressure.
3. **Side Engine Mechanics**: Action 1 (left) provides negative $x$ acceleration and positive torque; Action 3 (right) provides positive $x$ acceleration and negative torque.
4. **Orientation-Thrust Coupling**: The lander's $angle$ determines the degree to which the main engine's thrust contributes to lateral $x\_vel$ acceleration.
5. **Contact States and Transitions**: Terrain contact can be registered on a single leg, both legs, or transition from one leg to another (e.g., shifting from $right\_leg\_contact$ to $left\_leg\_contact$) during the stabilization phase.
6. **Terminal Reward Magnitude**: Terminal outcomes are characterized by extreme reward values: a value of 100.0 for successful landing and -100.0 for failure.
7. **Contact-Induced Reward Volatility**: Applying engines while in contact triggers extreme reward swings; side engines can yield massive positive rewards for successful angular stabilization or massive negative rewards for exacerbating $ang\_vel$.
8. **Post-Contact Instability**: Applying thrust (main or side engines) while legs are grounded can cause rapid, unstable shifts in $y\_vel$ or $angle$, potentially leading to tipping or bouncing.
9. **Angular Sensitivity in Contact**: Once legs are grounded, the lander is hyper-sensitive to torque; precise counter-torque is required to arrest $ang\_vel$, as misapplied side engines can cause rapid, violent rotation.
10. **Landing Success and Failure**: Terminal success requires stable, dual-leg contact with minimal $angle$ and $ang\_vel$; failure occurs if the lander loses stability or fails to maintain controlled contact, resulting in a large terminal penalty.

---

## 2026-07-02 10:49:46

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of upward thrust.
2. **Main Engine Mechanics**: Provides vertical thrust used to manage $y\_vel$. During the contact phase, main engine application is essential for managing descent rates and maintaining vertical stability.
3. **Side Engine Mechanics**: Action 1 (left) provides negative $x$ acceleration and positive torque; Action 3 (right) provides positive $x$ acceleration and negative torque.
4. **Orientation-Thrust Coupling**: The lander's $angle$ determines the degree to which the main engine's thrust contributes to lateral $x\_vel$ acceleration.
5. **Contact State Transitions**: Ground contact can occur sequentially, where a single leg (e.g., $right\_leg\_contact$) establishes contact before the lander transitions to dual-leg contact ($left\_leg\_contact$ and $right\_leg\_contact$).
6. **Terminal Reward Magnitude**: Terminal outcomes are characterized by extreme reward values: a value of 100.0 for successful landing and -100.0 for failure.
7. **Contact-Induced Reward Volatility**: Applying engines while in contact triggers extreme reward swings; side engines can yield massive positive rewards (e.g., >10.0) during successful contact or stabilization phases.
8. **Grounded Angular Divergence**: Applying side engines while legs are grounded can trigger rapid, runaway increases in $ang\_vel$ and $angle$, causing the lander to tip over and leading to terminal failure.
9. **Angular Sensitivity in Contact**: Once legs are grounded, the lander is hyper-sensitive to torque; precise counter-torque is required to arrest $ang\_vel$, as misapplied side engines can cause rapid, violent rotation.
10. **Landing Success and Failure**: Terminal success requires stable, dual-leg contact with minimal $angle$ and $ang\_vel$; failure occurs if the lander loses stability, tips, or fails to maintain controlled contact.

---

## 2026-07-02 10:52:10

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of upward thrust.
2. **Main Engine Mechanics**: Provides vertical thrust used to manage $y\_vel$. During the contact phase, main engine application is essential for managing descent rates and maintaining vertical stability.
3. **Side Engine Mechanics**: Action 1 (left) provides negative $x$ acceleration and positive torque; Action 3 (right) provides positive $x$ acceleration and negative torque. These engines are used for both orientation control and for managing lateral $x\_vel$ (e.g., counteracting high initial lateral velocities).
4. **Orientation-Thrust Coupling**: The lander's $angle$ determines the degree to which the main engine's thrust contributes to lateral $x\_vel$ acceleration.
5. **Contact State Transitions**: Ground contact can occur sequentially, where a single leg (e.g., $right\_leg\_contact$) establishes contact before the lander transitions to dual-leg contact ($left\_leg\_contact$ and $right\_leg\_contact$).
6. **Terminal Reward Magnitude**: Terminal outcomes are characterized by extreme reward values: a value of 100.0 for successful landing and -100.0 for failure.
7. **Contact-Induced Reward Volatility**: Applying engines while in contact triggers extreme reward swings; effective engine application during contact or stabilization can yield massive positive reward spikes (e.g., >10.0).
8. **Grounded Angular Divergence**: Applying side engines while legs are grounded can trigger rapid, runaway increases in $ang\_vel$ and $angle$, causing the lander to tip over and leading to terminal failure.
9. **Angular Sensitivity in Contact**: Once legs are grounded, the lander is hyper-sensitive to torque; precise counter-torque is required to arrest $ang\_vel$, as misapplied side engines can cause rapid, violent rotation.
10. **Landing Success and Failure**: Terminal success requires stable, dual-leg contact with minimal $angle$ and $ang\_vel$; failure occurs if the lander loses stability, tips, or fails to maintain controlled contact.

---

## 2026-07-02 10:55:32

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of upward thrust.
2. **Main Engine Mechanics**: Provides vertical thrust used to manage $y\_vel$. This engine is the primary tool for controlling descent rates and vertical stability.
3. **Side Engine Mechanics**: Action 1 (left) provides negative $x$ acceleration and positive torque; Action 3 (right) provides positive $x$ acceleration and negative torque. These are used for orientation control and for managing lateral $x\_vel$.
4. **Orientation-Thrust Coupling**: The lander's $angle$ determines the degree to which the main engine's thrust contributes to lateral $x\_vel$ acceleration.
5. **Sequential Contact Transitions**: Ground contact often occurs through a single leg (e.g., $right\_leg\_contact$ becomes 1.0) before transitioning to a dual-leg contact state ($left\_leg\_contact$ and $right\_leg\_contact$ both become 1.0).
6. **Terminal Success Reward**: A successful, stable landing is characterized by a terminal reward of 100.0.
7. **Contact Onset Reward Spikes**: The transition into a contact state (the moment of leg engagement) can trigger significant, immediate positive reward spikes (e.g., >10.0).
8. **Grounded Torque Sensitivity**: Once legs are grounded, the lander becomes hyper-sensitive to torque; applying side engines (Actions 1 or 3) can trigger rapid, runaway increases in $ang\_vel$ and $angle$.
9. **Tipping Risk**: Rapid angular divergence ($angle$ and $ang\_vel$) while the lander is grounded can cause the lander to tip over, leading to terminal failure.
10. **Landing Success Criteria**: Successful outcomes require the lander to achieve and maintain dual-leg contact while minimizing $x\_vel$, $y\_vel$, $angle$, and $ang\_vel$ to near-zero levels.

---

## 2026-07-02 10:57:05

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of upward thrust.
2. **Main Engine Mechanics**: Action 2 provides vertical thrust used to manage $y\_vel$. This engine is the primary tool for controlling descent rates and vertical stability.
3. **Side Engine Mechanics**: Action 1 (left) provides negative $x$ acceleration and positive torque; Action 3 (right) provides positive $x$ acceleration and negative torque.
4. **Orientation-Thrust Coupling**: The lander's $angle$ determines the degree to which the main engine's thrust contributes to lateral $x\_vel$ acceleration.
5. **Sequential Contact Transitions**: Ground contact typically progresses from no contact to single-leg contact (e.g., $right\_leg\_contact = 1.0$) before transitioning to a dual-leg contact state.
6. **Contact Reversibility**: Grounded status is not permanent; high velocities or instability can cause leg contact to revert from 1.0 back to 0.0 (e.g., bouncing or tipping).
7. **Contact Onset Reward Spikes**: The transition into a contact state (the moment of leg engagement) triggers immediate, significant positive reward spikes.
8. **Grounded Torque Sensitivity**: Applying side engines while grounded can trigger rapid changes in $ang\_vel$; extreme angular instability while in contact can lead to severe negative reward penalties.
9. **Terminal Success Reward**: A successful, stable landing is characterized by a terminal reward of 100.0.
10. **Landing Success Criteria**: Successful outcomes require the lander to achieve and maintain dual-leg contact while minimizing $x\_vel$, $y\_vel$, $angle$, and $ang\_vel$ to near-zero levels.

---

## 2026-07-02 11:00:08

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of upward thrust.
2. **Main Engine Mechanics**: Action 2 provides vertical thrust used to manage $y\_vel$. This engine is the primary tool for controlling descent rates and vertical stability.
3. **Side Engine Mechanics**: Action 1 (left) provides negative $x$ acceleration and positive torque; Action 3 (right) provides positive $x$ acceleration and negative torque.
4. **Orientation-Thrust Coupling**: The lander's $angle$ determines the degree to which the main engine's thrust contributes to lateral $x\_vel$ acceleration.
5. **Contact Onset Reward Spikes**: The transition of a leg from 0.0 to 1.0 (either $left\_leg\_contact$ or $right\_leg\_contact$) triggers immediate, significant positive reward spikes.
6. **Sequential Leg Engagement**: Grounded status typically progresses from no contact to single-leg contact before transitioning to a dual-leg contact state.
7. **Contact Reversibility**: Grounded status is not permanent; sudden changes in velocity or orientation can cause leg contact to revert from 1.0 back to 0.0 (e.g., bouncing or tipping).
8. **Grounded Instability Penalties**: While in a contact state, sudden shifts in state (such as rapid changes in $y\_vel$ or $angle$) can trigger severe negative reward penalties, representing a crash or instability event.
9. **Terminal Success Reward**: A successful, stable landing is characterized by a terminal reward of 100.0.
10. **Landing Success Criteria**: Successful outcomes require the lander to achieve and maintain dual-leg contact while minimizing $x\_vel$, $y\_vel$, $angle$, and $ang\_vel$ to near-zero levels.

---

## 2026-07-02 11:07:00

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of upward thrust.
2. **Main Engine Mechanics**: Action 2 provides vertical thrust used to manage $y\_vel$. This engine is the primary tool for controlling descent rates and vertical stability.
3. **Side Engine Mechanics**: Action 1 (left) provides negative $x$ acceleration and positive torque; Action 3 (right) provides positive $x$ acceleration and negative torque.
4. **Orientation-Thrust Coupling**: The lander's $angle$ determines the degree to which the main engine's thrust contributes to lateral $x\_vel$ acceleration.
5. **Contact Onset Reward Spikes**: The transition of a leg from 0.0 to 1.0 (either $left\_leg\_contact$ or $right\_leg\_contact$) triggers immediate, significant positive reward spikes.
6. **Sequential Leg Engagement**: Grounded status typically progresses from no contact to single-leg contact before transitioning to a dual-leg contact state.
7. **Contact Reversibility**: Grounded status is not permanent; sudden changes in velocity or orientation can cause leg contact to revert from 1.0 back to 0.0 (e.g., bouncing or tipping).
8. **Grounded Instability Penalties**: While in a contact state, sudden shifts in state (such as rapid changes in $y\_vel$ or $ang\_vel$) can trigger severe negative reward penalties, representing a crash or instability event.
9. **Terminal Success Reward**: A successful, stable landing is characterized by a terminal reward of 100.0.
10. **Landing Success Criteria**: Successful outcomes require the lander to achieve and maintain dual-leg contact while minimizing $x\_vel$, $y\_vel$, $angle$, and $ang\_vel$ to near-zero levels.

---

## 2026-07-02 11:09:09

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of upward thrust.
2. **Main Engine Mechanics**: Action 2 provides vertical thrust used to manage $y\_vel$. This engine is the primary tool for controlling descent rates and vertical stability.
3. **Side Engine Mechanics**: Action 1 (left) provides negative $x$ acceleration and positive torque; Action 3 (right) provides positive $x$ acceleration and negative torque.
4. **Orientation-Thrust Coupling**: The lander's $angle$ determines the degree to which the main engine's thrust contributes to lateral $x\_vel$ acceleration.
5. **Contact Onset Reward Spikes**: The transition of a leg from 0.0 to 1.0 (either $left\_leg\_contact$ or $right\_leg\_contact$) triggers immediate, significant positive reward spikes.
6. **Sequential Leg Engagement**: Grounded status typically progresses from no contact to single-leg contact before transitioning to a dual-leg contact state.
7. **Contact Reversibility**: Grounded status is not permanent; sudden changes in velocity or orientation can cause leg contact to revert from 1.0 back to 0.0 (e.g., bouncing or tipping).
8. **Grounded Instability Penalties**: While in a contact state, sudden shifts in state (such as rapid changes in $y\_vel$ or $ang\_vel$) can trigger severe negative reward penalties, representing a crash or instability event.
9. **Steady-State Stabilization**: Once grounded, the side engines can be used to maintain a stable equilibrium at a non-zero $angle$ or $x\_vel$ by counteracting the resulting torque and lateral drift.
10. **Terminal Success Criteria**: A successful landing is characterized by a terminal reward of 100.0, achieved by maintaining dual-leg contact while minimizing kinetic energy ($x\_vel$, $y\_vel$) and angular velocity ($ang\_vel$).

---

## 2026-07-02 11:11:15

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of upward thrust.
2. **Main Engine Vertical Control**: Action 2 provides vertical thrust, serving as the primary mechanism for modulating $y\_vel$ and managing descent rates.
3. **Side Engine Lateral/Angular Control**: Action 1 (left) produces negative $x$ acceleration and positive torque; Action 3 (right) produces positive $x$ acceleration and negative torque.
4. **Orientation-Thrust Coupling**: The lander's $angle$ modulates the horizontal component of the main engine's thrust, making $angle$ a critical variable for managing lateral $x\_vel$.
5. **Contact Reward Mechanism**: A transition of either $left\_leg\_contact$ or $right\_leg\_contact$ from 0.0 to 1.0 triggers immediate, high-magnitude positive reward spikes.
6. **Contact Progression**: Landing typically follows a sequential progression from no contact to single-leg contact, followed by dual-leg contact.
7. **Contact Fragility**: Grounded status is not permanent; high kinetic energy or sudden shifts in orientation can cause leg contact to revert from 1.0 to 0.0 (e.g., bouncing or tipping).
8. **High-Velocity Instability Penalties**: Rapid changes in $ang\_vel$ or $y\_vel$ while in a contact state—particularly when $ang\_vel$ reaches high magnitudes—trigger severe negative reward penalties, representing a crash or loss of stability.
9. **Post-Landing Stabilization**: Once dual-leg contact is established, side engines (specifically Action 1 in recent observations) are used to counteract lateral drift and angular velocity to maintain a stable, low-energy equilibrium.
10. **Terminal Success Criteria**: A successful landing is characterized by a terminal reward of 100.0, achieved by maintaining dual-leg contact while minimizing $x\_vel$, $y\_vel$, and $ang\_vel$.

---

## 2026-07-02 11:13:31

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of upward thrust.
2. **Main Engine Vertical/Lateral Control**: Action 2 provides vertical thrust; its horizontal component is modulated by the lander's $angle$, making it a primary mechanism for managing lateral $x\_vel$ during descent.
3. **Side Engine Torque/Lateral Control**: Action 1 (left) produces negative $x$ acceleration and positive torque (counter-clockwise); Action 3 (right) produces positive $x$ acceleration and negative torque (clockwise).
4. **Contact Reward Mechanism**: Transitions of either $left\_leg\_contact$ or $right\_leg\_contact$ from 0.0 to 1.0 trigger immediate, high-magnitude positive reward spikes.
5. **Contact Fragility**: Grounded status is highly sensitive to angular momentum; high magnitudes of $ang\_vel$ can cause leg contact to revert from 1.0 to 0.0, representing a loss of stable footing.
6. **High-Velocity Instability Penalties**: Significant negative reward penalties are triggered by high magnitudes of $ang\_vel$ or $y\_vel$ while in a contact state, representing a loss of control or imminent crash.
7. **Uncorrected Instability Penalties**: In states characterized by high $ang\_vel$ during descent or contact, taking no action (Action 0) can result in rapid accumulation of large negative rewards.
8. **Orientation-Thrust Coupling**: The lander's $angle$ is a critical variable that determines how much of the main engine's thrust is directed horizontally versus vertically.
9. **Contact Progression**: Successful landings typically follow a sequence from no contact to single-leg contact, followed by dual-leg contact.
10. **Terminal Outcomes**: A successful landing is characterized by a terminal reward of 100.0 (maintaining dual-leg contact with low velocities), whereas failure due to instability or crash results in a terminal reward of -100.0.

---

## 2026-07-02 11:15:53

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of upward thrust.
2. **Main Engine Vertical/Lateral Control**: Action 2 provides vertical thrust; its horizontal component is modulated by the lander's $angle$, serving as a primary mechanism for managing $x\_vel$ during descent.
3. **Side Engine Torque/Lateral Control**: Action 1 (left) produces negative $x$ acceleration and positive torque; Action 3 (right) produces positive $x$ acceleration and negative torque.
4. **Contact Reward Mechanism**: Transitions of $left\_leg\_contact$ or $right\_leg\_contact$ from 0.0 to 1.0 trigger immediate, high-magnitude positive reward spikes.
5. **Angular Instability during Contact**: High magnitudes of $ang\_vel$ while in a contact state (even with single-leg contact) are highly destabilizing and can trigger significant negative rewards or a loss of stable footing.
6. **Post-Contact Stabilization**: Once leg contact is established, side engines (Actions 1 and 3) are critical for managing angular momentum to prevent the lander from tipping or losing its grounded status.
7. **Uncorrected Instability Penalties**: In states characterized by high $ang\_vel$ during descent or contact, taking no action (Action 0) leads to the rapid accumulation of large negative rewards.
8. **Orientation-Thrust Coupling**: The lander's $angle$ is a critical variable that determines the distribution of the main engine's thrust between vertical and horizontal axes.
9. **Contact Progression**: Successful landings typically follow a sequence of no contact, single-leg contact, dual-leg contact, and subsequent orientation stabilization.
10. **Terminal Outcomes**: A successful landing (maintaining dual-leg contact with low velocities) results in a terminal reward of 100.0, whereas failure due to instability, high-velocity impact, or unmanaged angular momentum results in a terminal reward of -100.0.

---

## 2026-07-02 11:18:11

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of upward thrust.
2. **Main Engine Vertical/Lateral Control**: Action 2 provides vertical thrust; its horizontal component is modulated by the lander's $angle$, serving as a primary mechanism for managing $x\_vel$ during descent.
3. **Side Engine Torque/Lateral Control**: Action 1 (left engine) produces negative $x$ acceleration and positive torque; Action 3 (right engine) produces positive $x$ acceleration and negative torque.
4. **Contact Reward Mechanism**: Transitions of $left\_leg\_contact$ or $right\_leg\_contact$ from 0.0 to 1.0 trigger immediate, high-magnitude positive reward spikes.
5. **Angular Instability during Contact**: High magnitudes of $ang\_vel$ while in a contact state (even with single-leg contact) are highly destabilizing and can trigger significant negative rewards or a loss of stable footing.
6. **Grounded Status Maintenance**: Once leg contact is established, maintaining the contact state (preventing a transition from 1.0 back to 0.0) is critical; losing contact after it has been established typically indicates tipping and leads to terminal failure.
7. **Uncorrected Instability Penalties**: In states characterized by high $ang\_vel$ during descent or contact, taking no action (Action 0) leads to the rapid accumulation of large negative rewards.
8. **Orientation-Thrust Coupling**: The lander's $angle$ is a critical variable that determines the distribution of the main engine's thrust between vertical and horizontal axes.
9. **Contact Progression**: Successful landings typically follow a sequence of no contact, single-leg contact, dual-leg contact, and subsequent orientation stabilization.
10. **Terminal Outcomes**: A successful landing (maintaining dual-leg contact with low velocities) results in a terminal reward of 100.0, whereas failure due to instability, high-velocity impact, or losing grounded status results in a terminal reward of -100.0.

---

## 2026-07-02 11:22:38

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of upward thrust.
2. **Main Engine Vertical/Lateral Control**: Action 2 provides vertical thrust; its horizontal component is modulated by the lander's $angle$, serving as a primary mechanism for managing $x\_vel$ during descent.
3. **Side Engine Torque/Lateral Control**: Action 1 (left engine) produces negative $x$ acceleration and positive torque; Action 3 (right engine) produces positive $x$ acceleration and negative torque.
4. **Contact Reward Mechanism**: Transitions of $left\_leg\_contact$ or $right\_leg\_contact$ from 0.0 to 1.0 trigger immediate, high-magnitude positive reward spikes.
5. **Single-Leg Contact Instability**: Establishing single-leg contact can induce or coincide with rapid increases in $|ang\_vel|$, which can lead to a catastrophic tumble before dual-leg contact is achieved.
6. **Grounded Status Maintenance**: Once leg contact is established, losing that contact (a transition from 1.0 back to 0.0) is a terminal failure condition indicating the lander has tipped or bounced.
7. **Uncorrected Instability Penalties**: In states characterized by high $|ang\_vel|$, taking no action (Action 0) or failing to apply sufficient corrective torque leads to the rapid accumulation of large negative rewards.
8. **Orientation-Thrust Coupling**: The lander's $angle$ is a critical variable that determines the distribution of the main engine's thrust between the vertical and horizontal axes.
9. **Landing Sequence Requirements**: Successful landings require a controlled progression from no contact to dual-leg contact while simultaneously minimizing $|ang\_vel|$ and $|y\_vel|$ to maintain stability.
10. **Terminal Outcomes**: A successful landing (maintaining dual-leg contact with low velocities) results in a terminal reward of 100.0, whereas failure due to instability, high-velocity impact, or losing grounded status results in a terminal reward of -100.0.

---

## 2026-07-02 11:27:55

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of upward thrust.
2. **Main Engine Control**: Action 2 provides vertical thrust; its horizontal component is modulated by the lander's $angle$, serving as the primary mechanism for managing $x\_vel$ during descent.
3. **Side Engine Lateral and Torque Control**: Action 1 (left engine) produces negative $x$ acceleration and positive torque; Action 3 (right engine) produces positive $x$ acceleration and negative torque.
4. **Contact Reward Spikes**: Transitions of $left\_leg\_contact$ or $right\_leg\_contact$ from 0.0 to 1.0 trigger immediate, high-magnitude positive reward spikes.
5. **Single-Leg Contact Instability**: Establishing single-leg contact can induce or coincide with rapid increases in $|ang\_vel|$, which can lead to a catastrophic tumble before dual-leg contact is achieved.
6. **Grounding and Bouncing**: A transition from 1.0 back to 0.0 in leg contact indicates a loss of grounding (e.g., a bounce or tip). While this can sometimes be recovered from, it triggers negative rewards and requires immediate corrective torque to prevent a terminal failure.
7. **Uncorrected Instability Penalties**: In states characterized by high $|ang\_vel|$, taking no action (Action 0) or failing to apply sufficient corrective torque (Actions 1 or 3) leads to the rapid accumulation of large negative rewards.
8. **Orientation-Thrust Coupling**: The lander's $angle$ is a critical variable that determines the distribution of the main engine's thrust between the vertical and horizontal axes.
9. **Landing Success Requirements**: A "SUCCESS" outcome (terminal 100.0) requires the simultaneous achievement of dual-leg contact and the minimization of $|x\_vel|$, $|y\_vel|$, and $|ang\_vel|$ to near-zero values; failing to reach these velocity thresholds may result in a "PARTIAL" outcome.
10. **Terminal Outcomes**: A successful landing results in a terminal reward of 100.0, whereas failure due to instability, high-velocity impact, or losing grounded status results in a terminal reward of -100.0.

---

## 2026-07-02 11:30:29

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of sufficient upward thrust.
2. **Main Engine Thrust Vectoring**: Action 2 provides vertical thrust; the distribution of this thrust between the vertical and horizontal axes is modulated by the lander's $angle$.
3. **Side Engine Lateral and Torque Control**: Action 1 (left engine) produces negative $x$ acceleration and positive torque; Action 3 (right engine) produces positive $x$ acceleration and negative torque.
4. **Contact Reward Spikes**: A transition of $left\_leg\_contact$ or $right\_leg\_contact$ from 0.0 to 1.0 triggers immediate, high-magnitude positive reward spikes.
5. **Angular Velocity Instability**: Rapid increases in $|ang\_vel|$ immediately following leg contact (particularly single-leg contact) can induce catastrophic instability, preventing the lander from stabilizing even if dual-leg contact is eventually established.
6. **Grounding and Bouncing**: A transition from 1.0 to 0.0 in leg contact indicates a loss of grounding (e.g., a bounce). This state requires immediate corrective torque to prevent a terminal failure.
7. **Angular Momentum Dampening**: High $|ang\_vel|$ requires precise use of side engines (Actions 1 or 3) to dampen rotation; failure to counteract angular momentum while the lander is near the ground leads to rapid accumulation of negative rewards.
8. **Orientation-Thrust Coupling**: The lander's $angle$ is a critical variable that dictates the horizontal component of the main engine's thrust, making orientation control essential for managing $x\_vel$.
9. **Landing Success Requirements**: A "SUCCESS" outcome (terminal 100.0) requires the simultaneous achievement of dual-leg contact and the stabilization of $x\_vel$, $y\_vel$, $angle$, and $ang\_vel$ to near-zero values; dual-leg contact alone is insufficient if angular motion remains high.
10. **Terminal Outcomes**: A successful landing results in a terminal reward of 100.0, whereas failure due to instability, high-velocity impact, or losing grounded status results in a terminal reward of -100.0.

---

## 2026-07-02 11:33:59

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of sufficient upward thrust.
2. **Main Engine Thrust Vectoring**: Action 2 provides vertical thrust; the distribution of this thrust between the vertical and horizontal axes is modulated by the lander's $angle$.
3. **Side Engine Lateral and Torque Control**: Action 1 (left engine) produces negative $x$ acceleration and positive torque; Action 3 (right engine) produces positive $x$ acceleration and negative torque.
4. **Contact Reward Spikes**: A transition of $left\_leg\_contact$ or $right\_leg\_contact$ from 0.0 to 1.0 triggers immediate, high-magnitude positive reward spikes.
5. **Single-Leg Contact Instability**: Achieving single-leg contact can induce a rapid, significant increase in $|ang\_vel|$, which often leads to a "bounce" (loss of grounding) if not immediately mitigated by corrective torque.
6. **Grounding and Bouncing**: A transition from 1.0 to 0.0 in leg contact indicates a loss of grounding (a bounce). Re-establishing contact (0.0 to 1.0) triggers a reward spike but can also be part of a cycle of instability.
7. **Angular Momentum Dampening**: High $|ang\_vel|$ near the ground requires precise use of side engines (Actions 1 or 3) to dampen rotation; failure to counteract angular momentum leads to rapid accumulation of negative rewards and loss of stability.
8. **Orientation-Thrust Coupling**: The lander's $angle$ is a critical variable that dictates the horizontal component of the main engine's thrust, making orientation control essential for managing $x\_vel$.
9. **Landing Success Requirements**: A "SUCCESS" outcome (100.0) requires the simultaneous achievement of dual-leg contact and the stabilization of $x\_vel$, $y\_vel$, $angle$, and $ang\_vel$ to near-zero values.
10. **Outcome Classifications**: "SUCCESS" requires full stabilization; "PARTIAL" outcomes occur when the lander achieves contact but fails to stabilize (e.g., due to bouncing or high angular motion); "FAILURE" (-100.0) results from catastrophic instability or high-velocity impact.

---

## 2026-07-02 11:36:52

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of sufficient upward thrust.
2. **Main Engine Thrust Vectoring**: Action 2 provides vertical thrust; the distribution of this thrust between the vertical and horizontal axes is modulated by the lander's $angle$.
3. **Side Engine Lateral and Torque Control**: Action 1 (left engine) produces negative $x$ acceleration and positive torque; Action 3 (right engine) produces positive $x$ acceleration and negative torque.
4. **Contact Reward Spikes**: A transition of $left\_leg\_contact$ or $right\_leg\_contact$ from 0.0 to 1.0 triggers immediate, high-magnitude positive rewards.
5. **Single-Leg Contact Instability**: Achieving single-leg contact can induce a rapid, significant increase in $|ang\_vel|$ or a "bounce" (loss of grounding), as evidenced by the sudden $ang\_vel$ spike in Episode 1 (Steps 199–200).
6. **Grounding and Bouncing**: A transition from 1.0 to 0.0 in leg contact indicates a loss of grounding (a bounce). Re-establishing contact (0.0 to 1.0) triggers a reward spike but can be part of a cycle of instability.
7. **Angular Momentum Dampening**: High $|ang\_vel|$ near the ground requires precise use of side engines (Actions 1 or 3) to dampen rotation; failure to counteract angular momentum leads to rapid accumulation of negative rewards and loss of stability.
8. **Orientation-Thrust Coupling**: The lander's $angle$ is a critical variable that dictates the horizontal component of the main engine's thrust, making orientation control essential for managing $x\_vel$.
9. **Landing Success Requirements**: A "SUCCESS" outcome requires the simultaneous achievement of dual-leg contact (both legs at 1.0) and the stabilization of $x\_vel$, $y\_vel$, $angle$, and $ang\_vel$ to near-zero or constant values.
10. **Outcome Classifications**: "SUCCESS" requires full stabilization; "PARTIAL" outcomes occur when the lander achieves contact but fails to stabilize (e.g., due to bouncing or high angular motion); "FAILURE" results from catastrophic instability or high-velocity impact.

---

## 2026-07-02 11:39:23

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of sufficient upward thrust.
2. **Main Engine Thrust Vectoring**: Action 2 provides vertical thrust; the distribution of this thrust between the vertical and horizontal axes is modulated by the lander's $angle$.
3. **Side Engine Lateral and Torque Control**: Action 1 (left engine) produces negative $x$ acceleration and positive torque; Action 3 (right engine) produces positive $x$ acceleration and negative torque.
4. **Contact Reward Spikes**: A transition of $left\_leg\_contact$ or $right\_leg\_contact$ from 0.0 to 1.0 triggers immediate, high-magnitude positive rewards.
5. **Single-Leg Contact Instability**: Achieving single-leg contact (one leg at 1.0, the other at 0.0) can induce rapid, significant increases in $|ang\_vel|$ and often precedes a loss of grounding (bounce).
6. **Grounding and Bouncing**: A transition of leg contact from 1.0 to 0.0 indicates a loss of grounding (a bounce). Re-establishing contact (0.0 to 1.0) can trigger massive positive reward spikes but is frequently preceded by large negative rewards due to the impact of the bounce.
7. **Angular Momentum Management**: High $|ang\_vel|$ near the ground requires the application of torque via side engines (Actions 1 or 3) to dampen rotation; failure to counteract angular momentum leads to rapid accumulation of negative rewards.
8. **Orientation-Thrust Coupling**: The lander's $angle$ is a critical variable that dictates the horizontal component of the main engine's thrust, making orientation control essential for managing $x\_vel$.
9. **Landing Success Requirements**: A "SUCCESS" outcome requires the simultaneous achievement of dual-leg contact (both legs at 1.0) and the stabilization of $x\_vel$, $y\_vel$, $angle$, and $ang\_vel$ to near-zero.
10. **Reward and Penalty Scaling**: The reward function utilizes extreme scaling, where high-velocity impacts or catastrophic instability result in large negative penalties (e.g., -17.0), while successful contact or episode stabilization can trigger very high positive rewards (e.g., 100.0).

---

## 2026-07-02 11:45:22

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of sufficient upward thrust.
2. **Main Engine Thrust Vectoring**: Action 2 provides vertical thrust; the distribution of this thrust between the vertical and horizontal axes is modulated by the lander's $angle$.
3. **Side Engine Lateral and Torque Control**: Action 1 (left engine) produces negative $x$ acceleration and positive torque; Action 3 (right engine) produces positive $x$ acceleration and negative torque.
4. **Contact Reward Spikes**: A transition of $left\_leg\_contact$ or $right\_leg\_contact$ from 0.0 to 1.0 (including single-leg contact) triggers significant positive rewards, often in the range of 10.0 to 15.0.
5. **Grounding and Bouncing**: A transition of leg contact from 1.0 to 0.0 indicates a loss of grounding (a bounce), which often follows high angular velocity or high impact velocities.
6. **Catastrophic Crash Penalties**: High-velocity impacts or inappropriate use of the main engine (Action 2) during or immediately after contact can trigger catastrophic crashes, resulting in extreme negative rewards (e.g., -17.0 to -18.0).
7. **Angular Momentum Management**: High $|ang\_vel|$ near the ground requires the application of torque via side engines (Actions 1 or 3) to dampen rotation; failure to counteract angular momentum leads to instability and potential crashes.
8. **Orientation-Thrust Coupling**: The lander's $angle$ is a critical variable that dictates the horizontal component of the main engine's thrust, making orientation control essential for managing $x\_vel$.
9. **Landing Success Requirements**: A "SUCCESS" outcome requires the simultaneous achievement of dual-leg contact (both legs at 1.0) and the stabilization of $x\_vel$, $y\_vel$, $angle$, and $ang\_vel$ to near-zero.
10. **Reward and Penalty Scaling**: The reward function utilizes extreme scaling, where the magnitude of catastrophic crash penalties (e.g., ~ -18.0) is greater than the magnitude of positive rewards for successful leg contact (e.g., ~ 15.0).

---

## 2026-07-02 11:48:33

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of sufficient upward thrust.
2. **Main Engine Thrust Vectoring**: Action 2 provides vertical thrust; the distribution of this thrust between the vertical and horizontal axes is modulated by the lander's $angle$.
3. **Side Engine Lateral and Torque Control**: Action 1 (left engine) produces negative $x$ acceleration and positive torque; Action 3 (right engine) produces positive $x$ acceleration and negative torque.
4. **Contact Reward Spikes**: The action that triggers a transition of $left\_leg\_contact$ or $right\_leg\_contact$ from 0.0 to 1.0 results in a significant positive reward spike (typically between 10.0 and 17.5).
5. **Angular Momentum Instability**: High $|ang\_vel|$ during or immediately after leg contact (leg=1.0) causes rapid, heavy negative rewards, as the lander fails to stabilize its orientation.
6. **Catastrophic Crash Penalties**: High-velocity impacts or specific engine-state mismatches can trigger extreme negative rewards (e.g., ~ -10.0 to -17.0).
7. **Side Engine Grounding Conflict**: Applying side engines (Actions 1 or 3) while in contact with the ground (leg=1.0) or during rapid rotation frequently triggers large negative rewards or crashes.
8. **Orientation-Thrust Coupling**: The lander's $angle$ is a critical variable that dictates the horizontal component of the main engine's thrust, making orientation control essential for managing $x\_vel$.
9. **Terminal Reward**: The simulation concludes with a massive terminal reward of +100.0 at the final step, which is applied regardless of whether the outcome is "SUCCESS" or "PARTIAL."
10. **Reward and Penalty Scaling**: The reward function utilizes extreme scaling, where the terminal bonus (+100.0) and catastrophic crash penalties (~ -17.0) are significantly larger in magnitude than individual contact rewards (~ 15.0).

---

## 2026-07-02 11:54:44

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of sufficient upward thrust.
2. **Main Engine Thrust Vectoring**: Action 2 provides vertical thrust; the distribution of this thrust between the vertical and horizontal axes is modulated by the lander's $angle$.
3. **Side Engine Lateral and Torque Control**: Action 1 (left engine) produces negative $x$ acceleration and positive torque; Action 3 (right engine) produces positive $x$ acceleration and negative torque.
4. **Contact Reward Spikes**: Transitions of $left\_leg\_contact$ or $right\_leg\_contact$ from 0.0 to 1.0, or specific stabilization maneuvers while grounded, can result in significant positive reward spikes (observed ranging from ~13.0 to ~23.5).
5. **Angular Momentum Instability**: High $|ang\_vel|$ during or immediately after leg contact (leg=1.0) causes rapid, heavy negative rewards as the lander fails to stabilize its orientation.
6. **Catastrophic Crash Penalties**: High-velocity impacts or specific state-action mismatches can trigger extreme negative rewards (e.g., ~ -17.0 to -18.8), which can occur both during descent and while the lander is already in contact with the ground.
7. **Side Engine Grounding Conflict**: Applying side engines (Actions 1 or 3) while in contact with the ground (leg=1.0) is highly volatile; it can trigger catastrophic penalties or, in specific stabilization contexts, high positive rewards.
8. **Orientation-Thrust Coupling**: The lander's $angle$ is a critical variable that dictates the horizontal component of the main engine's thrust, making orientation control essential for managing $x\_vel$.
9. **Terminal Reward**: The simulation concludes with a massive terminal reward of +100.0 at the final step, which is applied regardless of whether the outcome is "SUCCESS" or "PARTIAL."
10. **Reward and Penalty Scaling**: The reward function utilizes extreme scaling, where terminal bonuses (+100.0) and catastrophic crash penalties (~ -18.8) are significantly larger in magnitude than individual contact rewards (~ 13.0 to 23.5).

---

## 2026-07-02 11:57:56

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of sufficient upward thrust (Action 2).
2. **Main Engine Thrust Vectoring**: Action 2 provides vertical thrust; the distribution of this thrust between the vertical and horizontal axes is modulated by the lander's $angle$.
3. **Side Engine Lateral and Torque Control**: Action 1 (left engine) produces negative $x$ acceleration and positive torque; Action 3 (right engine) produces positive $x$ acceleration and negative torque.
4. **Contact Reward Spikes**: Transitions of leg contact to 1.0, or successful stabilization maneuvers while grounded, can result in significant positive reward spikes (e.g., ~13.0 to ~23.5).
5. **Angular Momentum Instability**: High $|ang\_vel|$ during or immediately after leg contact (leg=1.0) triggers rapid, heavy negative rewards as the lander fails to stabilize its orientation.
6. **Catastrophic Crash Penalties**: High-velocity impacts or a failure to maintain stability while already grounded can trigger extreme negative rewards (e.g., ~ -17.0 to -18.8).
7. **Side Engine Grounding Volatility**: While grounded (leg=1.0), applying side engines (Actions 1 or 3) is highly volatile; it can trigger either massive positive reward spikes (e.g., ~12.5) or significant negative rewards depending on the orientation.
8. **Orientation-Thrust Coupling**: The lander's $angle$ is a critical variable that dictates the horizontal component of the main engine's thrust, making orientation control essential for managing $x\_vel$.
9. **Terminal Reward Magnitude**: The simulation concludes with a massive terminal reward/penalty (e.g., -100.0) that is significantly larger in magnitude than any other step-wise reward.
10. **Grounded Action Risks**: While grounded, taking no action (Action 0) can result in significant negative rewards (e.g., ~ -9.1), suggesting that active stabilization is often required to maintain a stable state on the ground.

---

## 2026-07-02 11:59:25

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of sufficient upward thrust (Action 2).
2. **Main Engine Thrust Vectoring**: Action 2 provides vertical thrust, but the distribution of this thrust between the vertical and horizontal axes is modulated by the lander's $angle$.
3. **Side Engine Dynamics**: Action 1 (left engine) produces negative $x$ acceleration and positive torque; Action 3 (right engine) produces positive $x$ acceleration and negative torque.
4. **Leg Contact Reward Spikes**: Transitions to a grounded state (leg=1.0) or successful landing maneuvers can trigger significant positive reward spikes.
5. **Angular Momentum Instability**: High $|ang\_vel|$ during or immediately after leg contact (leg=1.0) triggers rapid, heavy negative rewards as the lander fails to maintain orientation.
6. **Catastrophic Crash Penalties**: High-velocity impacts or a failure to stabilize once the lander is already grounded can trigger extreme negative rewards.
7. **Side Engine Grounded Volatility**: While grounded (leg=1.0), applying side engines (Actions 1 or 3) is a high-variance maneuver that can trigger either massive positive reward spikes or significant negative rewards depending on the orientation.
8. **Orientation-Thrust Coupling**: The lander's $angle$ is a critical variable that dictates the horizontal component of the main engine's thrust, making orientation control essential for managing $x\_vel$.
9. **Terminal Reward Polarity**: The simulation concludes with a massive terminal reward or penalty (~100.0 magnitude), where positive values signify successful landing/stabilization and negative values signify failure or a crash.
10. **Grounded Action Risks**: While grounded, taking no action (Action 0) can result in negative rewards, suggesting that continuous active stabilization is often required to maintain a stable state on the ground.

---

## 2026-07-02 12:02:02

1. **Gravity**: A constant downward acceleration increases the magnitude of negative $y\_vel$ in the absence of sufficient upward thrust (Action 2).
2. **Main Engine Reward and Thrust**: Action 2 provides vertical thrust and is the primary mechanism for accumulating positive step-wise rewards during the descent phase.
3. **Side Engine Descent Risk**: During the descent phase, applying side engines (Actions 1 or 3) is highly volatile and frequently induces high $|ang\_vel|$, resulting in immediate negative rewards.
4. **Leg Contact Dynamics**: Transitions to a grounded state (leg=1.0) can trigger significant positive reward spikes, but the state is highly sensitive to subsequent angular momentum.
5. **Post-Contact Angular Instability**: High $|ang\_vel|$ immediately following leg contact (leg=1.0) triggers rapid, heavy negative rewards, even if the vertical velocity is low.
6. **Catastrophic Crash Penalties**: High-velocity impacts or a failure to stabilize the orientation once the lander is grounded triggers extreme negative rewards.
7. **Grounded Stabilization Rewards**: Once the lander is grounded (leg=1.0), active use of engines (Actions 1, 2, or 3) can be used to maintain a stable state and sustain a positive reward stream.
8. **Orientation-Thrust Coupling**: The lander's $angle$ is a critical variable that dictates the horizontal component of the main engine's thrust, making orientation control essential for managing $x\_vel$.
9. **Terminal Reward Polarity**: The simulation concludes with a massive terminal reward of 100.0 for successful landing and stabilization.
10. **Grounded Action Necessity**: While grounded, taking no action (Action 0) is often insufficient to maintain stability or a positive reward stream, as continuous active stabilization is frequently required to prevent angular momentum from causing a crash.

---

## 2026-07-02 12:03:12

---


---

## 2026-07-02 12:06:26

1. Gravity consistently increases the magnitude of negative `y_vel` when no engines are active (Action 0).
2. The main engine (Action 2) is the most effective tool for increasing `y_vel` and counteracting gravitational descent.
3. Side engines (Actions 1 and 3) are primarily used for angular control, as they influence both `angle` and `ang_vel` while also contributing to vertical thrust.
4. Ground contact is indicated by a binary state (0.0 or 1.0) for `left_leg_contact` and `right_leg_contact`.
5. A transition from flight to ground contact can trigger large positive rewards if the descent velocity and angle are within acceptable thresholds.
6. High vertical or angular velocities during or immediately after ground contact trigger significant negative rewards, representing a crash.
7. Once both legs have made contact, the lander can maintain stability through small, frequent bursts of engine thrust (Actions 0, 2, or 3).
8. Angular momentum (`ang_vel`) must be actively managed; high `ang_vel` quickly causes `angle` deviations that are difficult to correct if not addressed early.
9. The simulation concludes with a significant terminal reward (100.0) at the final step.
10. Horizontal movement (`x_pos` and `x_vel`) occurs during descent, indicating that the landing target is a specific coordinate in the 2D plane.

---

## 2026-07-02 12:09:19

1. Gravity increases the magnitude of negative `y_vel` when no engines are active (Action 0).
2. The main engine (Action 2) is the primary tool for increasing `y_vel` and counteracting gravitational descent.
3. Side engines (Actions 1 and 3) provide vertical thrust and are essential for modulating `angle` and `ang_vel`.
4. Ground contact is tracked individually per leg, allowing for asymmetrical contact states where only one leg is in contact (1.0).
5. A transition to ground contact with low descent velocity (`y_vel`) and minimal `angle` can trigger large positive rewards.
6. High vertical velocity (`y_vel`) or high angular velocity (`ang_vel`) during or immediately after ground contact triggers significant negative rewards (crashes).
7. Once one or both legs make contact, the lander can maintain stability through corrective engine bursts.
8. High `ang_vel` is a critical failure risk; even with a low `y_vel`, excessive angular momentum can trigger a terminal crash.
9. The simulation concludes with a significant terminal reward of 100.0 at the final step.
10. The lander must manage horizontal position (`x_pos`) and horizontal velocity (`x_vel`) throughout the descent.

---

## 2026-07-02 12:13:34

1. Gravity increases the magnitude of negative `y_vel` when no engines are active (Action 0).
2. The main engine (Action 2) is the primary tool for increasing `y_vel` and counteracting gravitational descent.
3. Side engines (Actions 1 and 3) are essential for modulating `angle` and `ang_vel`.
4. Ground contact is tracked individually per leg, allowing for asymmetrical contact states where only one leg is in contact.
5. Successful landing requires ground contact with low descent velocity (`y_vel`) and minimal angular velocity (`ang_vel`).
6. High angular velocity (`ang_vel`) during or immediately after ground contact triggers rapid accumulation of significant negative rewards.
7. A crash, often characterized by high `ang_vel` upon contact, results in a terminal penalty of -100.0.
8. A successful landing or completion results in a terminal reward of 100.0.
9. Once ground contact is established, side engines can be used to maintain stability and correct the lander's orientation.
10. The lander must manage horizontal position (`x_pos`) and horizontal velocity (`x_vel`) throughout the descent to ensure stability.

---

## 2026-07-02 12:14:24

1. Gravity increases the magnitude of negative `y_vel` when no engines are active (Action 0).
2. The main engine (Action 2) is the primary tool for increasing `y_vel` and counteracting gravitational descent.
3. Side engines (Action 1 for left, Action 3 for right) are used to modulate `angle` and `ang_vel`.
4. Ground contact is tracked individually per leg, allowing for asymmetrical contact states where only one leg is in contact.
5. Successful landing requires ground contact with low descent velocity (`y_vel`) and minimal angular velocity (`ang_vel`).
6. High angular velocity (`ang_vel`) during or immediately after ground contact triggers a crash and a terminal penalty of -100.0.
7. A successful landing or completion results in a terminal reward of 100.0.
8. Once ground contact is established, side engines and the main engine can be used to maintain orientation and vertical stability.
9. The lander must manage horizontal position (`x_pos`) and horizontal velocity (`x_vel`) throughout the descent to ensure stability.
10. Ground contact does not immediately terminate the episode; the lander must maintain orientation stability in the steps following contact to avoid a crash.

---

## 2026-07-02 12:18:17

1. Gravity increases the magnitude of negative `y_vel` when no engines are active (Action 0).
2. The main engine (Action 2) is the primary tool for increasing `y_vel` and counteracting gravitational descent.
3. Side engines (Action 1 for left, Action 3 for right) are used to modulate `angle` and `ang_vel`.
4. Ground contact is tracked individually per leg, allowing for asymmetrical contact states where only one leg is in contact.
5. Successful landing requires ground contact with low descent velocity (`y_vel`) and minimal angular velocity (`ang_vel`).
6. High angular velocity (`ang_vel`) during or immediately after ground contact triggers a crash and a terminal penalty of -100.0.
7. A successful landing or specific terminal event results in a terminal reward of 100.0.
8. Once ground contact is established, the lander can persist in a state of contact (one or both legs) for an extended duration provided orientation is maintained.
9. The lander can exhibit positive `y_vel` (ascent) and must manage horizontal position (`x_pos`) and horizontal velocity (`x_vel`) to control its trajectory.
10. Ground contact does not immediately terminate the episode; the lander must maintain orientation stability in the steps following contact to avoid a crash.

---

## 2026-07-02 12:20:02

1. Gravity increases the magnitude of negative `y_vel` when no engines are active (Action 0).
2. The main engine (Action 2) is the primary tool for increasing `y_vel` and counteracting gravitational descent.
3. Side engines (Action 1 for left, Action 3 for right) are used to modulate `angle` and `ang_vel` to control orientation.
4. Ground contact is tracked individually per leg, allowing for asymmetrical contact states where only one leg is in contact with the ground.
5. Successful landing requires ground contact with low descent velocity (`y_vel`) and minimal angular velocity (`ang_vel`).
6. High angular velocity (`ang_vel`) during or immediately after ground contact triggers a crash and a terminal penalty of -100.0.
7. A successful landing results in a terminal reward of 100.0.
8. Once ground contact is established (one or both legs), the lander can persist in a state of contact for an extended duration by using engines to maintain stability.
9. The lander must manage horizontal position (`x_pos`) and horizontal velocity (`x_vel`) to control its trajectory.
10. Ground contact does not immediately terminate the episode; the lander must maintain orientation stability in the steps following contact to avoid a crash.

---

## 2026-07-02 12:23:28

---


---

## 2026-07-02 12:25:07

1. Gravity exerts a constant downward acceleration, causing the vertical velocity (`y_vel`) to decrease when no engines are active.
2. The main engine (Action 2) provides significant upward thrust to counteract gravity and control the descent rate (`y_vel`).
3. Side engines (Action 1 for left, Action 3 for right) provide both lateral force and torque, influencing `x_vel`, `angle`, and `ang_vel`.
4. Angular velocity (`ang_vel`) is highly sensitive; small imbalances or improper engine applications can lead to rapid increases in rotation.
5. Successful touchdown requires the simultaneous minimization of vertical velocity (`y_vel`) and angular velocity (`ang_vel`) as the lander approaches `y_pos` near 0.
6. Leg contact (indicated by `left_leg_contact` or `right_leg_contact` being 1.0) changes the landing dynamics and introduces contact-based constraints.
7. High angular velocity or significant tilt angles (`angle`) upon leg contact are primary drivers of landing failure and instability.
8. Once leg contact is established, side engines (Action 1 or 3) can be used to stabilize the craft and counteract residual angular momentum.
9. The lander's horizontal position (`x_pos`) and velocity (`x_vel`) are a result of the combined effects of side engine thrust and the current orientation (`angle`).
10. Maintaining a near-zero `angle` is critical during the descent phase to prevent the side engines from causing excessive horizontal drift or uncontrollable rotation.

---

## 2026-07-02 12:29:13

1. Gravity exerts a constant downward acceleration, necessitating the use of the main engine (Action 2) to manage vertical velocity (`y_vel`) and altitude (`y_pos`).
2. The main engine (Action 2) is the primary tool for vertical descent control and appears to be associated with positive reward components, whereas side engines (Actions 1 and 3) and idling (Action 0) generally incur negative costs.
3. Side engines (Action 1 for left, Action 3 for right) exert lateral force affecting `x_pos` and `x_vel`, as well as torque affecting `angle` and `ang_vel`.
4. Successful touchdown occurs when `y_pos` approaches 0, triggering leg contact (indicated by `left_leg_contact` or `right_leg_contact` becoming 1.0).
5. Leg contact can be asymmetrical, with the left or right leg making contact independently, which can induce sudden changes in orientation and angular velocity.
6. Post-contact, the lander enters a stabilization phase where side engines (Action 1 or 3) are essential to counteract residual angular momentum (`ang_vel`) and tilt (`angle`).
7. Angular velocity (`ang_vel`) is highly sensitive during the transition to contact; improper thrust application can lead to rapid, high-magnitude increases in rotation.
8. The effectiveness of side engines in controlling lateral movement is coupled with the lander's `angle`; the orientation dictates the direction and magnitude of the resulting horizontal force.
9. Maintaining a low `ang_vel` is critical during the final descent to ensure that the lander does not strike the ground with excessive rotational energy.
10. Once contact is established, the main engine (Action 2) can still be used to manage vertical stability, but the focus of control shifts heavily toward using side engines to prevent tipping.

---

## 2026-07-02 12:31:32

---
1. Gravity requires consistent use of the main engine (Action 2) to manage vertical descent (`y_vel`) and altitude (`y_pos`).
2. Action 2 is the primary driver of significant positive rewards, whereas side engines (Actions 1 and 3) and idling (Action 0) are frequently associated with negative costs.
3. Side engines (Action 1: left, Action 3: right) exert lateral force affecting `x_pos` and `x_vel`, as well as torque affecting `angle` and `ang_vel`.
4. Leg contact (indicated by `left_leg_contact` or `right_leg_contact` becoming 1.0) signals the transition to the touchdown phase, but contact alone does not guarantee a successful landing.
5. Contact can be asymmetrical, with one leg making contact independently, which can induce sudden shifts in orientation and angular momentum.
6. High angular velocity (`ang_vel`) is a critical risk factor; excessive rotation during the transition to contact or immediately following contact can trigger a crash.
7. The effectiveness of side engines in providing lateral movement is coupled with the lander's current `angle`, which dictates the direction of the resulting force.
8. A severe crash penalty (reward -100) is triggered by failure conditions, which can include high-velocity impacts or a failure to stabilize angular momentum/orientation after contact.
9. During the landing and post-contact phases, the control objective shifts toward a delicate balance of using the main engine for vertical stability and side engines to mitigate rotational energy.
10. The lander remains susceptible to failure even after leg contact is established if `ang_vel` or `angle` are not immediately managed to prevent tipping.

---

## 2026-07-02 12:33:50

1. Gravity requires consistent use of the main engine (Action 2) to manage vertical descent (`y_vel`) and altitude (`y_pos`).
2. While side engines (Actions 1 and 3) often incur negative costs during the descent phase, they can generate significant positive rewards if used effectively to stabilize the lander during and after the touchdown phase.
3. Side engines exert both lateral force (affecting `x_pos` and `x_vel`) and torque (affecting `angle` and `ang_vel`), with the resulting force vector being highly dependent on the lander's current `angle`.
4. Asymmetrical leg contact (where only one leg reaches a contact value of 1.0) acts as a high-energy mechanical impulse, causing immediate and large spikes in angular velocity (`ang_vel`).
5. The transition period between the first leg making contact and the second leg making contact is a phase of heightened instability characterized by rapid changes in orientation.
6. Excessive angular velocity (`ang_vel`) is a critical risk factor; if not immediately mitigated, it leads to tipping or a crash.
7. Post-contact stabilization requires a delicate balance between using the main engine for vertical stability and side engines to negate the torque induced by the landing impact.
8. The effectiveness of all thrust actions is coupled with the lander's orientation, as `angle` dictates the direction of the resulting force.
9. A severe crash penalty (-100) is triggered by failure conditions, including high-velocity impacts or a failure to stabilize `angle` and `ang_vel` after contact.
10. A successful landing requires the lander to achieve and maintain a state of minimal `ang_vel` and near-zero `angle` once both legs have established contact.

---

## 2026-07-02 12:38:40

1. Gravity requires consistent use of the main engine (Action 2) to manage vertical descent (`y_vel`) and altitude (`y_pos`).
2. Side engines (Actions 1 and 3) incur negative costs during the descent phase but are essential for providing the torque necessary to stabilize the lander post-contact.
3. Side engine thrust is coupled with orientation, exerting both lateral force (affecting `x_pos` and `x_vel`) and torque (affecting `angle` and `ang_vel`) as a function of the lander's current `angle`.
4. Asymmetrical leg contact (where only one leg reaches a contact value of 1.0) generates a sharp mechanical impulse that causes significant and immediate spikes in angular velocity (`ang_vel`).
5. The transition period between the first leg making contact and the second leg establishing contact is a phase of extreme instability characterized by rapid, large-magnitude changes in orientation.
6. Excessive angular velocity (`ang_vel`) is the primary critical risk factor; failure to immediately dampen this velocity leads to tipping or a crash.
7. Post-contact stabilization requires a dual-control strategy: using the main engine to manage vertical momentum and side engines to negate the rotational torque induced by the landing impact.
8. The magnitude and direction of the force vector produced by any thrust action are highly dependent on the lander's current `angle`.
9. Landing outcomes are tiered based on stability: a "SUCCESS" requires achieving and maintaining near-zero `angle` and `ang_vel` once both legs are in contact, whereas failure to stabilize or high-impact velocities result in "PARTIAL" or crash (-100) outcomes.
10. Maintaining a stable post-landing state requires continuous, fine-grained adjustments to prevent residual angular momentum from causing the lander to tip over after the initial contact impulse.

---

## 2026-07-02 12:41:24

1. Gravity requires consistent application of the main engine (Action 2) to manage altitude (`y_pos`) and vertical descent velocity (`y_vel`).
2. Side engines (Actions 1 and 3) provide the torque necessary to manage orientation and the lateral force required to adjust horizontal position (`x_pos`) and velocity (`x_vel`).
3. The effectiveness and direction of thrust from side engines are coupled with the lander's current `angle`, meaning torque and lateral force vary as a function of orientation.
4. Asymmetrical leg contact (where only one leg reaches a contact value of 1.0) triggers a massive mechanical impulse that can cause an immediate, order-of-magnitude spike in angular velocity (`ang_vel`), potentially overriding current rotational control.
5. The period between the first leg making contact and the second leg establishing contact is a critical window of extreme instability characterized by rapid, high-magnitude fluctuations in orientation.
6. Excessive angular velocity (`ang_vel`) remains the primary critical risk factor; failure to immediately dampen this velocity leads to tipping or a crash.
7. Post-contact stabilization requires a dual-control strategy: using the main engine to negate vertical momentum and side engines to negate the rotational torque induced by landing impacts.
8. The magnitude and direction of the force vector produced by any thrust action are highly dependent on the lander's current `angle`.
9. Landing outcomes are strictly tiered based on stability: "SUCCESS" requires near-zero `angle`, `ang_vel`, `x_vel`, and `y_vel` upon contact, whereas high-impact or unstable velocities result in "PARTIAL" or crash (-100) outcomes.
10. Achieving a successful landing requires the simultaneous minimization of all velocity components (`x_vel`, `y_vel`, and `ang_vel`) to prevent post-contact sliding, tipping, or structural failure.

---

## 2026-07-02 12:47:01

1. Gravity requires consistent application of the main engine (Action 2) to manage altitude (`y_pos`) and vertical descent velocity (`y_vel`).
2. Side engines (Actions 1 and 3) provide the torque necessary to manage orientation and the lateral force required to adjust horizontal position (`x_pos`) and velocity (`x_vel`).
3. The effectiveness and direction of thrust from side engines are coupled with the lander's current `angle`, meaning torque and lateral force vary as a function of orientation.
4. Asymmetrical leg contact (where only one leg reaches a contact value of 1.0) triggers a massive mechanical impulse that can cause an immediate, high-magnitude spike in angular velocity (`ang_vel`).
5. The period between the first leg making contact and the second leg establishing contact is a critical window of extreme instability, often characterized by rapid, continuous acceleration of `ang_vel` that can overwhelm current rotational control.
6. Excessive angular velocity (`ang_vel`) remains the primary critical risk factor; failure to immediately dampen this velocity leads to tipping or a crash.
7. Post-contact stabilization requires a dual-control strategy: using the main engine to negate vertical momentum and side engines to negate the rotational torque induced by landing impacts.
8. The magnitude and direction of the force vector produced by any thrust action (1, 2, or 3) are highly dependent on the lander's current `angle`.
9. Landing outcomes are strictly tiered based on stability: "SUCCESS" requires near-zero `angle`, `ang_vel`, `x_vel`, and `y_vel` upon full contact, whereas high-impact or unstable velocities result in "PARTIAL" or crash (-100) outcomes.
10. Achieving a successful landing requires the simultaneous minimization of all velocity components (`x_vel`, `y_vel`, and `ang_vel`) to prevent post-contact sliding, tipping, or structural failure.

---

## 2026-07-02 12:49:47

1. Gravity requires consistent application of the main engine (Action 2) to manage altitude (`y_pos`) and vertical descent velocity (`y_vel`).
2. Side engines (Actions 1 and 3) provide both the lateral force required to adjust horizontal position (`x_pos`) and velocity (`x_vel`) and the torque necessary to manage orientation.
3. The magnitude and direction of the force vector produced by any thrust action (1, 2, or 3) are highly dependent on the lander's current `angle`.
4. Asymmetrical leg contact (where only one leg reaches a value of 1.0) triggers a massive mechanical impulse that causes an immediate, high-magnitude spike in angular velocity (`ang_vel`).
5. The period between the first leg making contact and the second leg establishing contact is a window of extreme instability, characterized by rapid, continuous acceleration of `ang_vel` that can quickly become unmanageable.
6. Excessive angular velocity (`ang_vel`) is the primary critical risk factor; failure to immediately dampen this velocity upon the first leg's contact leads to a crash.
7. Post-contact stabilization requires a dual-control strategy: using the main engine to negate vertical momentum and side engines to negate the rotational torque induced by landing impacts.
8. Achieving a successful landing requires the simultaneous minimization of `angle`, `ang_vel`, `x_vel`, and `y_vel` at the moment of full contact (both legs = 1.0).
9. The magnitude of the rotational impulse during asymmetrical contact is significantly compounded by the lander's `angle` at the moment of impact.
10. Landing at or below the `y_pos = 0` threshold with any significant linear or angular momentum results in an immediate failure.

---

## 2026-07-02 12:53:54

1. Gravity necessitates the consistent application of the main engine (Action 2) to manage altitude (`y_pos`) and vertical descent velocity (`y_vel`).
2. Side engines (Actions 1 and 3) provide both the lateral force required to adjust horizontal position (`x_pos`) and velocity (`x_vel`) and the torque necessary to manage orientation.
3. The direction and magnitude of the force vector produced by any thrust action are highly dependent on the lander's current `angle`.
4. Asymmetrical leg contact (where only one leg reaches 1.0) triggers a mechanical impulse that causes an immediate, high-magnitude spike in angular velocity (`ang_vel`).
5. The period between the first leg making contact and the second leg establishing contact is a window of extreme instability, characterized by rapid, continuous acceleration of `ang_vel`.
6. The magnitude of the rotational impulse during asymmetrical contact is significantly compounded by both the lander's `angle` and its pre-existing `ang_vel` at the moment of impact.
7. Maintaining near-zero `ang_vel` prior to the first leg's contact is the primary requirement for preventing unmanageable rotational acceleration during the landing instability window.
8. Post-contact stabilization requires a dual-control strategy: using the main engine to negate vertical momentum and side engines to counteract the rotational torque induced by landing impacts.
9. Achieving a successful landing requires the simultaneous minimization of `angle`, `ang_vel`, `x_vel`, and `y_vel` at the moment of full contact (both legs = 1.0).
10. Landing at or below the `y_pos = 0` threshold with any significant linear or angular momentum results in an immediate failure.

---

## 2026-07-02 12:55:21

1. Gravity necessitates the consistent application of the main engine (Action 2) to manage altitude (`y_pos`) and vertical descent velocity (`y_vel`).
2. Side engines (Actions 1 and 3) provide both the lateral force required to adjust horizontal position (`x_pos`) and velocity (`x_vel`) and the torque necessary to manage orientation.
3. The direction and magnitude of the force vector produced by any thrust action are highly dependent on the lander's current `angle`.
4. Asymmetrical leg contact (where only one leg reaches 1.0) triggers a mechanical impulse that causes an immediate, high-magnitude spike in angular velocity (`ang_vel`), which can be sufficient to reverse the current direction of rotation.
5. The period between the first leg making contact and the second leg establishing contact is a window of extreme instability, characterized by rapid, continuous acceleration of `ang_vel`.
6. The magnitude of the rotational impulse during asymmetrical contact is significantly compounded by both the lander's `angle` and its pre-existing `ang_vel` at the moment of impact.
7. Maintaining near-zero `ang_vel` prior to the first leg's contact is the primary requirement for preventing unmanageable rotational acceleration during the landing instability window.
8. Post-contact stabilization requires the continuous application of side engines to counteract the rotational torque induced by landing impacts and to maintain low `ang_vel` and `angle`.
9. Achieving a successful landing requires the simultaneous minimization of `angle`, `ang_vel`, `x_vel`, and `y_vel` at the moment of full contact (both legs = 1.0).
10. Landing at or below the `y_pos = 0` threshold with any significant linear or angular momentum results in an immediate failure.

---

## 2026-07-02 12:57:17

1. Gravity necessitates the consistent application of the main engine (Action 2) to manage altitude (`y_pos`) and vertical descent velocity (`y_vel`).
2. Side engines (Actions 1 and 3) provide both the lateral force required to adjust horizontal position/velocity (`x_pos`, `x_vel`) and the torque necessary to manage orientation (`angle`, `ang_vel`).
3. The direction and magnitude of the force vector produced by any thrust action are highly dependent on the lander's current `angle`.
4. Asymmetrical leg contact (where only one leg reaches 1.0) triggers an immediate, high-magnitude spike in angular velocity (`ang_vel`).
5. The period between the first leg making contact and the second leg establishing contact is a window of extreme instability, characterized by rapid, continuous acceleration of `ang_vel`.
6. The magnitude of the rotational impulse during asymmetrical contact is significantly compounded by both the lander's `angle` and its pre-existing `ang_vel` at the moment of impact.
7. Maintaining near-zero `ang_vel` and minimal `angle` prior to the first leg's contact is the primary requirement for preventing unmanageable rotational acceleration during the landing instability window.
8. The main engine (Action 2) can exert rotational torque when the lander is at a non-zero `angle`, which can either dampen or exacerbate existing `ang_vel` depending on the orientation.
9. Post-contact stabilization requires the continuous application of side engines to counteract the rotational torque induced by landing impacts and to maintain low `ang_vel` and `angle`.
10. A successful landing requires the simultaneous minimization of `angle`, `ang_vel`, `x_vel`, and `y_vel` at the moment of full contact; landing at or below `y_pos = 0` with any significant residual linear or angular momentum results in failure.

---

## 2026-07-02 12:58:23

1. Gravity necessitates the consistent application of the main engine (Action 2) to manage altitude (`y_pos`) and vertical descent velocity (`y_vel`).
2. Side engines (Actions 1 and 3) provide both the lateral force required to adjust horizontal position/velocity (`x_pos`, `x_vel`) and the torque necessary to manage orientation (`angle`, `ang_vel`).
3. The direction and magnitude of the force vector produced by any thrust action are highly dependent on the lander's current `angle`.
4. Asymmetrical leg contact (where only one leg reaches 1.0) triggers an immediate, high-magnitude spike in angular velocity (`ang_vel`).
5. The period between the first leg making contact and the second leg establishing contact is a window of extreme instability, characterized by rapid, continuous acceleration of `ang_vel`.
6. The magnitude of the rotational impulse during contact is significantly compounded by both the lander's `angle` and its pre-existing `ang_vel` at the moment of impact.
7. If a non-zero `angle` exists at the moment of full contact (both legs at 1.0), the lander experiences persistent rotational instability that can continue to evolve even after the landing window closes.
8. The main engine (Action 2) exerts significant rotational torque at non-zero `angle`, which can exacerbate `ang_vel` during the critical landing phase, potentially making rotation impossible to arrest.
9. Maintaining near-zero `ang_vel` and minimal `angle` prior to the first leg's contact is the primary requirement for preventing unmanageable rotational acceleration during the landing sequence.
10. A successful landing requires the simultaneous minimization of `angle`, `ang_vel`, `x_vel`, and `y_vel` at the moment of full contact; landing at or below `y_pos = 0` with any significant residual linear or angular momentum results in failure.

---

## 2026-07-02 13:01:34

1. Gravity requires the consistent application of the main engine (Action 2) to manage altitude (`y_pos`) and vertical descent velocity (`y_vel`).
2. Side engines (Actions 1 and 3) provide the lateral force for horizontal movement (`x_pos`, `x_vel`) and the torque required for orientation control (`angle`, `ang_vel`).
3. The magnitude and direction of the force vector produced by any thrust action are highly dependent on the lander's current `angle`.
4. Asymmetrical leg contact (the transition of a single leg from 0.0 to 1.0) triggers an immediate, high-magnitude spike in angular velocity (`ang_vel`).
5. The period between the first leg making contact and the second leg establishing contact is a window of extreme instability, characterized by rapid, continuous acceleration of `ang_vel`.
6. The rotational impulse during contact is significantly compounded by both the lander's `angle` and its pre-existing `ang_vel` at the moment of impact.
7. Even after full contact (both legs at 1.0), the lander remains susceptible to angular velocity spikes if the main engine (Action 2) is applied while a non-zero `angle` exists.
8. The main engine (Action 2) exerts significant rotational torque at non-zero `angle`, which can exacerbate `ang_vel` during the critical landing phase, potentially making rotation impossible to arrest.
9. Maintaining near-zero `ang_vel` and minimal `angle` prior to the first leg's contact is the primary requirement for preventing unmanageable rotational acceleration during the landing sequence.
10. A successful or partial landing requires the simultaneous minimization of `angle`, `ang_vel`, `x_vel`, and `y_vel` at the moment of full contact; landing with significant residual angular momentum results in failure.

---

## 2026-07-02 13:04:59

1. Gravity necessitates the consistent application of the main engine (Action 2) to manage altitude (`y_pos`) and vertical descent velocity (`y_vel`).
2. Side engines (Actions 1 and 3) provide the lateral force for horizontal movement (`x_pos`, `x_vel`) and the torque required for orientation control (`angle`, `ang_vel`).
3. The magnitude and direction of the force vector produced by any thrust action are highly dependent on the lander's current `angle`.
4. Asymmetrical leg contact (the transition of a single leg from 0.0 to 1.0) triggers an immediate, high-magnitude spike in angular velocity (`ang_vel`).
5. The period between the first leg making contact and the second leg establishing contact is a window of extreme instability, characterized by rapid, continuous acceleration of `ang_vel`.
6. Even after both legs have established contact, the lander can experience a loss of contact on one leg (bouncing), which re-introduces asymmetrical instability and rapid angular acceleration.
7. The rotational impulse during contact is significantly compounded by both the lander's `angle` and its pre-existing `ang_vel` at the moment of impact.
8. The main engine (Action 2) exerts significant rotational torque at non-zero `angle`, which can exacerbate `ang_vel` during the critical landing phase, potentially making rotation impossible to arrest even after contact is made.
9. Maintaining near-zero `ang_vel` and minimal `angle` prior to the first leg's contact is the primary requirement for preventing unmanageable rotational acceleration during the landing sequence.
10. A successful landing requires the simultaneous minimization of `angle`, `ang_vel`, `x_vel`, and `y_vel` at the moment of full, stable contact; landing with significant residual angular momentum or during asymmetrical contact results in failure.

---

## 2026-07-02 13:07:31

1. Main engine (Action 2) is required to manage altitude (`y_pos`) and vertical descent velocity (`y_vel`).
2. Side engines (Actions 1 and 3) provide the lateral force for horizontal movement (`x_pos`, `x_vel`) and the torque for orientation control (`angle`, `ang_vel`).
3. The magnitude and direction of the thrust vector produced by any action are highly dependent on the lander's current `angle`.
4. Asymmetrical leg contact (the transition of a single leg from 0.0 to 1.0) triggers an immediate, high-magnitude spike in angular velocity (`ang_vel`), which can involve a sudden reversal of rotational direction.
5. The interval between the first leg making contact and the second leg establishing contact is a period of extreme instability characterized by rapid, continuous acceleration of `ang_vel`.
6. The rotational impulse during contact is significantly compounded by both the lander's `angle` and its pre-existing `ang_vel` at the moment of impact.
7. The main engine (Action 2) exerts significant rotational torque when applied at a non-zero `angle`, which can exacerbate `ang_vel` during the landing phase and make rotation impossible to arrest.
8. Achieving near-zero `ang_vel` and minimal `angle` *prior* to the first leg's contact is the critical requirement for preventing unmanageable rotational acceleration.
9. A successful landing requires the simultaneous minimization of `angle`, `ang_vel`, `x_vel`, and `y_vel` at the moment of stable, dual-leg contact.
10. Once a single leg has made contact, the lander's orientation becomes highly sensitive to thrust; applying engines while the lander is tilted during the asymmetrical contact phase often results in a feedback loop of increasing `ang_vel` and `angle`.

---

## 2026-07-02 13:09:53

1. Main engine (Action 2) is required to manage altitude (`y_pos`) and vertical descent velocity (`y_vel`).
2. Side engines (Actions 1 and 3) provide the lateral force for horizontal movement (`x_pos`, `x_vel`) and the torque for orientation control (`angle`, `ang_vel`).
3. The magnitude and direction of the thrust vector produced by any action are highly dependent on the lander's current `angle`.
4. Asymmetrical leg contact (the transition of a single leg from 0.0 to 1.0) triggers an immediate, high-magnitude spike in angular velocity (`ang_vel`).
5. The interval between the first leg making contact and the second leg establishing contact is a period of extreme instability characterized by rapid, continuous acceleration of `ang_vel`.
6. The rotational impulse during contact is significantly compounded by both the lander's `angle` and its pre-existing `ang_vel` at the moment of impact.
7. The main engine (Action 2) exerts significant rotational torque when applied at a non-zero `angle`, which can exacerbate `ang_vel` during the landing phase and make rotation impossible to arrest.
8. Achieving near-zero `ang_vel` and minimal `angle` *prior* to the first leg's contact is the critical requirement for preventing unmanageable rotational acceleration.
9. Dual-leg contact does not guarantee stability; if `ang_vel` is high at the moment of impact, the resulting rotational impulse can lead to an immediate crash, even if both legs are established.
10. Once a single leg has made contact, the lander's orientation becomes highly sensitive to thrust; applying engines while the lander is tilted during the asymmetrical contact phase often results in a feedback loop of increasing `ang_vel` and `angle`.

---

## 2026-07-02 13:13:35

1. Main engine (Action 2) is required to manage altitude (`y_pos`) and vertical descent velocity (`y_vel`).
2. Side engines (Actions 1 and 3) provide the lateral force for horizontal movement (`x_pos`, `x_vel`) and the torque for orientation control (`angle`, `ang_vel`).
3. The magnitude and direction of the thrust vector produced by any action are highly dependent on the lander's current `angle`.
4. The transition of a single leg from 0.0 to 1.0 (asymmetrical contact) triggers an immediate, high-magnitude spike in angular velocity (`ang_vel`).
5. The interval between the first leg making contact and the second leg establishing contact is a period of extreme instability characterized by rapid, continuous acceleration of `ang_vel`.
6. The rotational impulse during contact is significantly compounded by both the lander's `angle` and its pre-existing `ang_vel` at the moment of impact.
7. The main engine (Action 2) exerts significant rotational torque when applied at a non-zero `angle`, which can exacerbate `ang_vel` and make rotation impossible to arrest during the landing phase.
8. Achieving near-zero `ang_vel` and minimal `angle` *prior* to the first leg's contact is the critical requirement for preventing unmanageable rotational acceleration.
9. Dual-leg contact does not guarantee stability; if `ang_vel` is high at the moment of impact, the resulting rotational impulse can lead to an immediate crash, even if both legs are established.
10. Leg contact is not permanent; if the lander is unstable or highly tilted during the asymmetrical contact phase, the resulting rotational energy can cause the leg to lose contact (transitioning from 1.0 back to 0.0), leading to a bouncing or tipping effect.

---

## 2026-07-02 13:16:17

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
