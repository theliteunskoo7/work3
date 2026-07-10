
---

## 2026-07-08 07:37:16

1. **Gravity and Descent Dynamics:** Gravity causes continuous downward acceleration, evidenced by decreasing $y\_pos$ and negative $y\_vel$ when no thrust is applied.
2. **Main Engine Functionality:** Action 2 (main engine) is essential for managing vertical velocity but incurs heavy reward penalties, likely due to fuel consumption.
3. **Angular Control:** Actions 1 (left engine) and 3 (right engine) are used to modulate the `angle` and `ang_vel`; improper sequencing leads to rapid, unrecoverable tilting.
4. **Failure Mode - Angular Momentum:** Both episodes demonstrate that uncontrolled angular momentum is the primary cause of failure, where `angle` moves far from zero.
5. **The "Death Spiral":** Once `ang_vel` becomes high, the `angle` enters a runaway state (e.g., Episode 1 reaching -4.16), making stabilization impossible regardless of action.
6. **Lateral Drift:** Excessive or poorly timed thrust causes significant $x\_pos$ drift, moving the lander away from the target landing center.
7. **Ineffective Late-Stage Correction:** In Episode 2, attempting to correct tilt with side engines (Actions 1 and 3) very late in the descent (steps 100–127) failed to counter the established angular velocity.
8. **Action Over-reliance:** Frequent, continuous use of the main engine (Action 2) without sufficient lateral stabilization (Actions 1/3) correlates with high negative rewards and instability.
9. **Critical Threshold:** A critical moment occurs when the `angle` exceeds a threshold (roughly $\pm 1.0$); beyond this point, the lander's orientation becomes too extreme to recover.
10. **Terminal State Identification:** Failure is characterized by a high-velocity impact at $y \approx 0$ accompanied by an extreme `angle`, resulting in a massive terminal reward penalty (e.g., -100.0).

---

## 2026-07-08 07:45:12

1. **Gravity and Descent Dynamics:** Gravity causes continuous downward acceleration, evidenced by decreasing $y\_pos$ and increasing negative $y\_vel$ in the absence of upward thrust.
2. **Main Engine Functionality:** Action 2 (main engine) is the primary mechanism for managing vertical velocity and countering gravitational acceleration.
3. **Angular Control:** Actions 1 (left engine) and 3 (right engine) are used to modulate `angle` and `ang_vel`; precise sequencing can maintain a stable, near-vertical orientation for extended periods.
4. **Angular Momentum Runaway:** High `ang_vel` causes the `angle` to enter a runaway state, where the orientation deviates rapidly and non-linearly from zero.
5. **Angular Velocity Spikes:** A sudden surge in the magnitude of `ang_vel` can trigger a rapid orientation collapse, even if the current `angle` has not yet reached extreme values.
6. **Lateral Drift:** Thrust application, particularly when the lander is not perfectly vertical, results in continuous and significant $x\_pos$ displacement.
7. **Stability Maintenance:** The environment allows for periods of relative stability where the `angle` and `ang_vel` can be kept within a narrow range (e.g., $\pm 0.3$ radians) through corrective side-engine pulses.
8. **Reward-State Correlation:** Reward values are directly tied to the state; controlled descent parameters correlate with positive rewards, while extreme angular or vertical velocities correlate with negative rewards.
9. **Dual Critical Thresholds:** System stability is threatened by two distinct metrics: the magnitude of the `angle` (tilt) and the magnitude of the `ang_vel` (rotation speed).
10. **Terminal State Identification:** Failure is characterized by a high-velocity impact at $y \approx 0$, which triggers a large terminal reward penalty and is typically associated with extreme `angle` or `ang_vel` values.

---

## 2026-07-08 07:50:13

1. **Gravity and Descent Dynamics:** Gravity causes continuous downward acceleration, evidenced by decreasing $y\_pos$ and increasing negative $y\_vel$ in the absence of upward thrust.
2. **Main Engine Functionality:** Action 2 (main engine) provides upward thrust to manage vertical velocity, acting to decrease the magnitude of negative $y\_vel$ during descent.
3. **Directional Angular Torque:** Action 1 (left engine) applies positive torque (increasing `ang_vel`), while Action 3 (right engine) applies negative torque (decreasing `ang_vel`).
4. **Angular Momentum Runaway:** High `ang_vel` causes the `angle` to enter a runaway state, where the orientation deviates rapidly and non-linearly from zero.
5. **Angular Velocity Spikes:** Sudden, large-magnitude changes in `ang_vel` can trigger a rapid orientation collapse, even if the current `angle` has not yet reached extreme values.
6. **Thrust-Induced Lateral Drift:** Applying thrust, particularly Action 2, while the lander possesses a non-zero `angle` results in continuous and significant $x\_pos$ and $x\_vel$ displacement.
7. **Stability Maintenance:** System stability can be maintained by using corrective pulses from side engines (Actions 1 and 3) to keep `angle` and `ang_vel` within a narrow range.
8. **Reward-State Correlation:** Reward values are directly tied to the state; controlled descent parameters correlate with positive rewards, while extreme angular or vertical velocities correlate with negative rewards.
9. **Dual Critical Thresholds:** System stability is threatened by two distinct metrics: the magnitude of the `angle` (tilt) and the magnitude of the `ang_vel` (rotation speed).
10. **Terminal State Identification:** Failure is characterized by a high-velocity impact at $y \approx 0$, which triggers a large terminal reward penalty and is typically associated with extreme `angle` or `ang_vel` values.

---

## 2026-07-10 07:02:54

1. **Gravity and Descent Dynamics:** Gravity causes continuous downward acceleration, evidenced by decreasing $y\_pos$ and negative $y\_vel$ when no thrust is applied.
2. **Main Engine Functionality:** Action 2 (main engine) is essential for managing vertical velocity but incurs heavy reward penalties, likely due to fuel consumption.
3. **Angular Control:** Actions 1 (left engine) and 3 (right engine) are used to modulate the `angle` and `ang_vel`; improper sequencing leads to rapid, unrecoverable tilting.
4. **Failure Mode - Angular Momentum:** Both episodes demonstrate that uncontrolled angular momentum is the primary cause of failure, where `angle` moves far from zero.
5. **The "Death Spiral":** Once `ang_vel` becomes high, the `angle` enters a runaway state (e.g., Episode 1 reaching -4.16), making stabilization impossible regardless of action.
6. **Lateral Drift:** Excessive or poorly timed thrust causes significant $x\_pos$ drift, moving the lander away from the target landing center.
7. **Ineffective Late-Stage Correction:** In Episode 2, attempting to correct tilt with side engines (Actions 1 and 3) very late in the descent (steps 100–127) failed to counter the established angular velocity.
8. **Action Over-reliance:** Frequent, continuous use of the main engine (Action 2) without sufficient lateral stabilization (Actions 1/3) correlates with high negative rewards and instability.
9. **Critical Threshold:** A critical moment occurs when the `angle` exceeds a threshold (roughly $\pm 1.0$); beyond this point, the lander's orientation becomes too extreme to recover.
10. **Terminal State Identification:** Failure is characterized by a high-velocity impact at $y \approx 0$ accompanied by an extreme `angle`, resulting in a massive terminal reward penalty (e.g., -100.0).

---

## 2026-07-10 07:10:50

1. **Gravity and Descent Dynamics:** Gravity causes continuous downward acceleration, evidenced by decreasing $y\_pos$ and increasing negative $y\_vel$ in the absence of upward thrust.
2. **Main Engine Functionality:** Action 2 (main engine) is the primary mechanism for managing vertical velocity and countering gravitational acceleration.
3. **Angular Control:** Actions 1 (left engine) and 3 (right engine) are used to modulate `angle` and `ang_vel`; precise sequencing can maintain a stable, near-vertical orientation for extended periods.
4. **Angular Momentum Runaway:** High `ang_vel` causes the `angle` to enter a runaway state, where the orientation deviates rapidly and non-linearly from zero.
5. **Angular Velocity Spikes:** A sudden surge in the magnitude of `ang_vel` can trigger a rapid orientation collapse, even if the current `angle` has not yet reached extreme values.
6. **Lateral Drift:** Thrust application, particularly when the lander is not perfectly vertical, results in continuous and significant $x\_pos$ displacement.
7. **Stability Maintenance:** The environment allows for periods of relative stability where the `angle` and `ang_vel` can be kept within a narrow range (e.g., $\pm 0.3$ radians) through corrective side-engine pulses.
8. **Reward-State Correlation:** Reward values are directly tied to the state; controlled descent parameters correlate with positive rewards, while extreme angular or vertical velocities correlate with negative rewards.
9. **Dual Critical Thresholds:** System stability is threatened by two distinct metrics: the magnitude of the `angle` (tilt) and the magnitude of the `ang_vel` (rotation speed).
10. **Terminal State Identification:** Failure is characterized by a high-velocity impact at $y \approx 0$, which triggers a large terminal reward penalty and is typically associated with extreme `angle` or `ang_vel` values.

---

## 2026-07-10 07:15:50

1. **Gravity and Descent Dynamics:** Gravity causes continuous downward acceleration, evidenced by decreasing $y\_pos$ and increasing negative $y\_vel$ in the absence of upward thrust.
2. **Main Engine Functionality:** Action 2 (main engine) provides upward thrust to manage vertical velocity, acting to decrease the magnitude of negative $y\_vel$ during descent.
3. **Directional Angular Torque:** Action 1 (left engine) applies positive torque (increasing `ang_vel`), while Action 3 (right engine) applies negative torque (decreasing `ang_vel`).
4. **Angular Momentum Runaway:** High `ang_vel` causes the `angle` to enter a runaway state, where the orientation deviates rapidly and non-linearly from zero.
5. **Angular Velocity Spikes:** Sudden, large-magnitude changes in `ang_vel` can trigger a rapid orientation collapse, even if the current `angle` has not yet reached extreme values.
6. **Thrust-Induced Lateral Drift:** Applying thrust, particularly Action 2, while the lander possesses a non-zero `angle` results in continuous and significant $x\_pos$ and $x\_vel$ displacement.
7. **Stability Maintenance:** System stability can be maintained by using corrective pulses from side engines (Actions 1 and 3) to keep `angle` and `ang_vel` within a narrow range.
8. **Reward-State Correlation:** Reward values are directly tied to the state; controlled descent parameters correlate with positive rewards, while extreme angular or vertical velocities correlate with negative rewards.
9. **Dual Critical Thresholds:** System stability is threatened by two distinct metrics: the magnitude of the `angle` (tilt) and the magnitude of the `ang_vel` (rotation speed).
10. **Terminal State Identification:** Failure is characterized by a high-velocity impact at $y \approx 0$, which triggers a large terminal reward penalty and is typically associated with extreme `angle` or `ang_vel` values.

---

## 2026-07-10 09:14:10

1. **Gravity and Descent Dynamics:** Gravity causes continuous downward acceleration, evidenced by decreasing $y\_pos$ and increasing the magnitude of negative $y\_vel$ in the absence of sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides upward thrust to manage $y\_vel$, but its effectiveness in counteracting gravity decreases as the `angle` deviates from zero.
3. **Thrust Vectoring and Tilt:** At high `angle` values, the main engine (Action 2) can inadvertently increase the magnitude of negative $y\_vel$ and cause significant lateral $x\_vel$ displacement due to the tilted thrust vector.
4. **Directional Angular Torque:** Action 1 (left engine) applies positive torque (increasing `ang_vel`), while Action 3 (right engine) applies negative torque (decreasing `ang_vel`).
5. **Angular Momentum Runaway:** High `ang_vel` causes the `angle` to change rapidly, creating a feedback loop where orientation becomes increasingly difficult to correct as the tilt grows.
6. **Thrust-Induced Lateral Drift:** Applying any thrust (Actions 1, 2, or 3) while the lander possesses a non-zero `angle` results in continuous $x\_pos$ and $x\_vel$ displacement.
7. **Stability Maintenance:** System stability requires using corrective pulses from side engines (Actions 1 and 3) to keep both `angle` and `ang_vel` within a narrow range near zero.
8. **Dual Critical Thresholds:** System stability is threatened by two distinct metrics: the magnitude of the `angle` (tilt) and the magnitude of the `ang_vel` (rotation speed).
9. **Terminal State Identification:** Failure is characterized by a high-velocity impact at $y \approx 0$, which triggers a large terminal reward penalty (e.g., -100).
10. **Reward-State Correlation:** Reward values are tied to state parameters; controlled descent (low velocities and minimal tilt) correlates with positive rewards, while extreme angular/vertical velocities or crashes correlate with negative rewards.

---

## 2026-07-10 09:18:32

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, evidenced by decreasing $y\_pos$ and increasing the magnitude of negative $y\_vel$ in the absence of sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides upward thrust to manage $y\_vel$, but its effectiveness in counteracting gravity decreases as the `angle` deviates from zero.
3. **Directional Angular Torque:** Action 1 (left engine) applies positive torque (increasing `ang_vel`), while Action 3 (right engine) applies negative torque (decreasing `ang_vel`).
4. **Angular Momentum Runaway:** High `ang_vel` causes the `angle` to change rapidly, creating a feedback loop where orientation becomes increasingly difficult to correct as the tilt grows.
5. **Thrust-Induced Lateral Drift:** Applying any thrust (Actions 1, 2, or 3) while the lander possesses a non-zero `angle` results in continuous $x\_pos$ and $x\_vel$ displacement due to the tilted thrust vector.
6. **Leg Contact and Landing State:** The `left_leg_contact` and `right_leg_contact` variables indicate touchdown; however, contact does not guarantee stability and can be associated with high angular or vertical velocities.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of three distinct metrics: the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the `y_vel` (descent speed).
8. **Terminal Failure Conditions:** Failure is characterized by a high-velocity impact at $y \approx 0$, which triggers a large terminal reward penalty.
9. **Thrust-Induced Angular Divergence:** At significant `angle` values, the main engine's thrust vector can inadvertently cause both lateral displacement and rapid, uncontrolled increases in `ang_vel`.
10. **Reward-State Correlation:** Reward values are tied to state parameters; controlled descent (low velocities and minimal tilt) correlates with positive rewards, while extreme angular/vertical velocities or crashes correlate with negative rewards.

---

## 2026-07-10 09:23:36

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, evidenced by decreasing $y\_pos$ and increasing the magnitude of negative $y\_vel$ in the absence of sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides upward thrust to manage $y\_vel$, but its vertical effectiveness decreases as the `angle` deviates from zero.
3. **Directional Angular Torque:** Action 1 (left engine) applies positive torque (increasing `ang_vel`), while Action 3 (right engine) applies negative torque (decreasing `ang_vel`).
4. **Angular Momentum Runaway:** High `ang_vel` causes the `angle` to change rapidly, creating a feedback loop where orientation becomes increasingly difficult to correct as the tilt grows.
5. **Thrust-Induced Lateral Acceleration:** Applying any thrust (Actions 1, 2, or 3) while the lander possesses a non-zero `angle` results in lateral acceleration in the direction of the tilt (a positive `angle` induces negative $x\_vel$ acceleration, while a negative `angle` induces positive $x\_vel$ acceleration).
6. **Leg Contact and Landing State:** The `left_leg_contact` and `right_leg_contact` variables indicate touchdown; however, contact does not guarantee a successful landing if the $y\_pos$ crosses below zero or if impact velocities are excessive.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of three distinct metrics: the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the `y_vel` (descent speed).
8. **Terminal Failure Conditions:** Failure is characterized by a high-velocity impact or the lander's position crossing the $y \approx 0$ threshold, which triggers a large terminal reward penalty.
9. **Thrust-Induced Angular Divergence:** At significant `angle` values, the main engine's thrust vector can inadvertently cause both lateral displacement and rapid, uncontrolled increases in `ang_vel`.
10. **Reward-State Correlation:** Reward values are tied to state parameters; controlled descent (low velocities and minimal tilt) correlates with positive rewards, while extreme angular/vertical velocities or crashes correlate with negative rewards.

---

## 2026-07-10 09:31:00

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, evidenced by decreasing $y\_pos$ and increasing the magnitude of negative $y\_vel$ in the absence of sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides upward thrust to manage $y\_vel$, but its vertical effectiveness decreases as the `angle` deviates from zero.
3. **Directional Angular Torque:** Action 1 (left engine) applies positive torque (increasing `ang_vel`), while Action 3 (right engine) applies negative torque (decreasing `ang_vel`).
4. **Angular Momentum Runaway:** High `ang_vel` causes the `angle` to change rapidly, creating a feedback loop where orientation becomes increasingly difficult to correct as the tilt grows.
5. **Thrust-Induced Lateral Acceleration:** Applying any thrust (Actions 1, 2, or 3) while the lander possesses a non-zero `angle` results in lateral acceleration in the direction of the tilt (a positive `angle` induces negative $x\_vel$ acceleration, while a negative `angle` induces positive $x\_vel$ acceleration).
6. **Leg Contact and Landing Success:** The `left_leg_contact` and `right_leg_contact` variables indicate touchdown; however, contact does not guarantee a successful landing if the descent velocity ($y\_vel$), tilt (`angle`), or rotation speed (`ang_vel`) are excessive at the moment of impact.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of three distinct metrics: the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the `y_vel` (descent speed).
8. **Terminal Failure Conditions:** Failure is characterized by a high-velocity impact, the lander's position crossing the $y \approx 0$ threshold, or uncontrolled angular momentum during the touchdown phase.
9. **Thrust-Induced Angular Divergence:** At significant `angle` values, the main engine's thrust vector can inadvertently cause both lateral displacement and rapid, uncontrolled changes in `ang_vel`.
10. **Reward-State Correlation:** Reward values are tied to state parameters; controlled descent (low velocities and minimal tilt) correlates with positive rewards, while extreme angular/vertical velocities or crashes correlate with large negative terminal penalties.

---

## 2026-07-10 09:35:22

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, evidenced by decreasing $y\_pos$ and increasing the magnitude of negative $y\_vel$ in the absence of sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides upward thrust to manage $y\_vel$, but its vertical effectiveness decreases as the `angle` deviates from zero.
3. **Directional Angular Torque:** Action 1 (left engine) applies positive torque (increasing `ang_vel`), while Action 3 (right engine) applies negative torque (decreasing `ang_vel`).
4. **Angular Momentum Runaway:** High `ang_vel` causes the `angle` to change rapidly, creating a feedback loop where orientation becomes increasingly difficult to correct as the tilt grows.
5. **Thrust-Induced Lateral Acceleration:** Applying any thrust while the lander possesses a non-zero `angle` results in lateral acceleration in the direction of the tilt (a positive `angle` induces negative $x\_vel$ acceleration, while a negative `angle` induces positive $x\_vel$ acceleration).
6. **Leg Contact and Landing Success:** While `left_leg_contact` or `right_leg_contact` indicate touchdown, a successful landing requires stability; contact accompanied by excessive descent velocity ($y\_vel$), excessive rotation speed (`ang_vel`), or significant tilt (`angle`) leads to failure.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of three distinct metrics: the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the `y_vel` (descent speed).
8. **Terminal Failure Conditions:** Failure is triggered by high-velocity impact, the $y\_pos$ crossing the zero threshold, or uncontrolled angular momentum during or immediately following the touchdown phase.
9. **Thrust-Induced Angular Divergence:** At significant `angle` values, the main engine's thrust vector can inadvertently cause both lateral displacement and rapid, uncontrolled changes in `ang_vel`.
10. **Reward-State Correlation:** Reward values are tied to state parameters; controlled descent (low velocities and minimal tilt) correlates with positive rewards, while extreme angular/vertical velocities or crashes (including $y\_pos \le 0$) correlate with large negative terminal penalties.

---

## 2026-07-10 09:40:16

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, evidenced by decreasing $y\_pos$ and increasing the magnitude of negative $y\_vel$ in the absence of sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides upward thrust to manage $y\_vel$, but its vertical effectiveness is reduced as the `angle` deviates from zero.
3. **Directional Angular Torque:** Action 1 (left engine) applies positive torque (increasing `ang_vel`), while Action 3 (right engine) applies negative torque (decreasing `ang_vel`).
4. **Angular Momentum Runaway:** High `ang_vel` causes the `angle` to change rapidly, creating a feedback loop where orientation becomes increasingly difficult to correct as the tilt grows.
5. **Thrust-Induced Lateral Acceleration:** Applying any thrust (Actions 1, 2, or 3) results in lateral acceleration ($x\_vel$ change) that is a function of both the specific engine used and the current `angle`.
6. **Leg Contact and Landing Success:** While `left_leg_contact` or `right_leg_contact` indicate touchdown (on one or both legs), a successful landing requires stability; contact accompanied by excessive descent velocity ($y\_vel$), excessive rotation speed (`ang_vel`), or significant tilt (`angle`) leads to failure.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of three distinct metrics: the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the `y_vel` (descent speed).
8. **Terminal Failure Conditions:** Failure is triggered by high-velocity impact, uncontrolled angular momentum, or the $y\_pos$ crossing the zero threshold ($y\_pos \le 0$).
9. **Thrust-Induced Angular Divergence:** At significant `angle` values, the main engine's thrust vector can inadvertently cause rapid, uncontrolled changes in `ang_vel` and lateral displacement.
10. **Reward-State Correlation:** Reward values are tied to state parameters; controlled descent (low velocities and minimal tilt) correlates with positive rewards, while extreme angular/vertical velocities or crashes (including $y\_pos \le 0$) correlate with large negative terminal penalties.

---

## 2026-07-10 09:44:53

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, evidenced by decreasing $y\_pos$ and increasing the magnitude of negative $y\_vel$ in the absence of sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides upward thrust to manage $y\_vel$, but its vertical effectiveness is reduced as the `angle` deviates from zero.
3. **Directional Angular Torque:** Action 1 (left engine) applies positive torque (increasing `ang_vel`), while Action 3 (right engine) applies negative torque (decreasing `ang_vel`).
4. **Angular Momentum Runaway:** High `ang_vel` causes the `angle` to change rapidly, creating a feedback loop where orientation becomes increasingly difficult to correct as the tilt grows.
5. **Thrust-Induced Lateral Acceleration:** Applying any thrust (Actions 1, 2, or 3) results in lateral acceleration ($x\_vel$ change) that is a function of both the specific engine used and the current `angle`.
6. **Contact-Induced Instability:** Once leg contact is established (`left_leg_contact` or `right_leg_contact` = 1.0), the lander undergoes rapid, often uncontrolled changes in `ang_vel` and `angle`, suggesting the contact state significantly disrupts angular stability.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of three distinct metrics: the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the `y_vel` (descent speed).
8. **Terminal Failure Conditions:** Failure is triggered by high-velocity impact, uncontrolled angular momentum, or the $y\_pos$ crossing the zero threshold ($y\_pos \le 0$).
9. **Thrust-Induced Angular Divergence:** At significant `angle` values, the main engine's thrust vector can inadvertently cause rapid, uncontrolled changes in `ang_vel` and lateral displacement.
10. **Reward-Contact-Penalty Dynamics:** While leg contact triggers a significant positive reward spike, this is frequently followed by a large negative terminal penalty due to the resulting angular instability or ground impact.

---

## 2026-07-10 09:49:15

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, evidenced by decreasing $y\_pos$ and increasing the magnitude of negative $y\_vel$ in the absence of sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides upward thrust to manage $y\_vel$, but its vertical effectiveness is reduced as the `angle` deviates from zero.
3. **Directional Angular Torque:** Action 1 (left engine) applies positive torque (increasing `ang_vel`), while Action 3 (right engine) applies negative torque (decreasing `ang_vel`).
4. **Angular Momentum Runaway:** High `ang_vel` causes the `angle` to change rapidly, creating a feedback loop where orientation becomes increasingly difficult to correct as the tilt grows.
5. **Thrust-Induced Lateral Acceleration:** Applying any thrust (Actions 1, 2, or 3) results in lateral acceleration ($x\_vel$ change) that is a function of both the specific engine used and the current `angle`.
6. **Contact-Induced Angular Volatility:** The establishment of leg contact (`left_leg_contact` or `right_leg_contact` = 1.0) triggers rapid, extreme surges in `ang_vel`, which can instantly destabilize the lander's orientation.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of three distinct metrics: the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the `y_vel` (descent speed).
8. **Terminal Failure Conditions:** Failure is triggered by high-velocity impact, uncontrolled angular momentum, or the $y\_pos$ crossing the zero threshold ($y\_pos \le 0$).
9. **Main Engine Torque Coupling:** At significant `angle` values, the main engine (Action 2) generates substantial unintended torque, causing rapid changes in `ang_vel` in addition to its effect on $y\_vel$.
10. **Reward-Contact-Penalty Dynamics:** While leg contact triggers a significant positive reward spike, this is frequently followed by a large negative terminal penalty due to the resulting angular instability or ground impact.

---

## 2026-07-10 09:52:41

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, evidenced by decreasing $y\_pos$ and increasing the magnitude of negative $y\_vel$ in the absence of sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides upward thrust to manage $y\_vel$, but its vertical effectiveness is reduced as the `angle` deviates from zero.
3. **Directional Angular Torque:** Action 1 (left engine) applies positive torque (increasing `ang_vel`), while Action 3 (right engine) applies negative torque (decreasing `ang_vel`).
4. **Angular Momentum Runaway:** High `ang_vel` causes the `angle` to change rapidly, creating a feedback loop where orientation becomes increasingly difficult to correct as the tilt grows.
5. **Thrust-Induced Lateral Acceleration:** Applying any thrust (Actions 1, 2, or 3) results in lateral acceleration ($x\_vel$ change) that is a function of both the specific engine used and the current `angle`.
6. **Contact-Induced Angular Volatility:** Leg contact (`left_leg_contact` or `right_leg_contact` = 1.0) triggers rapid, extreme surges or sign-reversals in `ang_vel`, often causing near-instantaneous destabilization of the lander's orientation.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of three distinct metrics: the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the `y_vel` (descent speed).
8. **Multi-Modal Terminal Failure:** Failure is triggered by the $y\_pos$ crossing the zero threshold ($y\_pos \le 0$) or by excessive angular velocity (`ang_vel`) reaching a threshold that causes immediate termination, even if $y\_pos > 0$.
9. **Main Engine Torque Coupling:** At significant `angle` values, the main engine (Action 2) generates substantial unintended torque, causing rapid changes in `ang_vel` in addition to its effect on $y\_vel$.
10. **Extreme Reward-Penalty Disparity at Contact:** While leg contact can trigger very high positive reward spikes (e.g., >30), these are frequently followed immediately by a large terminal penalty (e.g., -100) due to the resulting angular instability.

---

## 2026-07-10 09:56:40

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, reducing $y\_pos$ and increasing the magnitude of negative $y\_vel$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides upward thrust to manage $y\_vel$, but its vertical effectiveness decreases as the `angle` deviates from zero.
3. **Directional Angular Torque:** Action 1 (left engine) applies positive torque to increase `ang_vel`, while Action 3 (right engine) applies negative torque to decrease `ang_vel`.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid `angle` changes, creating a feedback loop where orientation becomes increasingly difficult to stabilize as tilt grows.
5. **Thrust-Induced Lateral Acceleration:** Applying any engine thrust (Actions 1, 2, or 3) results in lateral acceleration ($x\_vel$ change) that is a function of the specific engine used and the current `angle`.
6. **Contact-Induced Angular Volatility:** The onset of leg contact (`left_leg_contact` or `right_leg_contact` = 1.0) triggers extreme, high-magnitude surges or rapid sign-reversals in `ang_vel`, causing immediate and severe rotational destabilization.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of three distinct metrics: the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the $y\_vel$ (descent speed).
8. **Multi-Modal Terminal Failure:** Failure is triggered either by the $y\_pos$ crossing the zero threshold ($y\_pos \le 0$) or by `ang_vel` reaching a critical threshold that causes immediate termination.
9. **Main Engine Torque Coupling:** At significant `angle` values, the main engine (Action 2) generates substantial unintended torque, causing rapid changes in `ang_vel` in addition to its effect on $y\_vel$.
10. **Contact-Triggered Terminal Penalty:** While leg contact can trigger momentary high positive rewards, it is frequently followed within very few steps by a large terminal penalty (e.g., -100) as the resulting angular instability and descent lead to $y\_pos \le 0$.

---

## 2026-07-10 10:01:01

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides upward thrust to manage $y\_vel$, but its vertical effectiveness is modulated by the current `angle`.
3. **Directional Angular Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque to manipulate `ang_vel`, allowing for orientation control.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid `angle` changes, creating a feedback loop where orientation becomes increasingly difficult to stabilize as tilt grows.
5. **Thrust-Induced Lateral Acceleration:** Applying any engine thrust (Actions 1, 2, or 3) results in lateral acceleration ($x\_vel$ change) that is a function of the specific engine used and the current `angle`.
6. **Contact-Induced Angular Volatility:** The onset of leg contact (`left_leg_contact` or `right_leg_contact` = 1.0) triggers extreme, high-magnitude surges or rapid sign-reversals in `ang_vel`, causing immediate rotational destabilization.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of three distinct metrics: the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the $y\_vel$ (descent speed).
8. **Multi-Modal Terminal Failure:** Failure is triggered either by the $y\_pos$ crossing the zero threshold ($y\_pos \le 0$) or by `ang_vel` reaching a critical threshold that causes immediate termination.
9. **Main Engine Torque Coupling:** At significant `angle` values, the main engine (Action 2) generates substantial unintended torque, causing rapid changes in `ang_vel` in addition to its effect on $y\_vel$.
10. **Contact-Triggered Terminal Penalty:** While leg contact can trigger high momentary rewards, it is frequently followed within very few steps by a large terminal penalty (e.g., -100) as the resulting angular instability and descent lead to $y\_pos \le 0$.

---

## 2026-07-10 10:03:30

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides vertical thrust to manage $y\_vel$, but its vertical effectiveness is modulated by the current `angle`.
3. **Directional Angular Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque to manipulate `ang_vel`, allowing for orientation control.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid `angle` changes, creating a feedback loop where orientation becomes increasingly difficult to stabilize as tilt grows.
5. **Thrust-Induced Lateral Acceleration:** Applying any engine thrust (Actions 1, 2, or 3) results in lateral acceleration ($x\_vel$ change) that is a function of the specific engine used and the current `angle`.
6. **Contact-Induced Angular Volatility:** The onset of leg contact (`left_leg_contact` or `right_leg_contact` = 1.0) triggers extreme, high-magnitude surges or rapid sign-reversals in `ang_vel`, causing immediate rotational destabilization.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of three distinct metrics: the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the $y\_vel$ (descent speed).
8. **Multi-Modal Terminal Failure:** Failure is triggered either by the $y\_pos$ crossing the zero threshold ($y\_pos \le 0$) or by `ang_vel` reaching a critical threshold that causes immediate termination.
9. **Main Engine Torque Coupling:** At significant `angle` values, the main engine (Action 2) generates unintended torque, causing rapid changes in `ang_vel` in addition to its effect on $y\_vel$.
10. **Contact-Preceded Terminal Penalty:** While leg contact can trigger momentary high rewards, it is frequently the precursor to a terminal penalty (e.g., -100) due to contact-induced `ang_vel` spikes that lead to a rapid descent into negative $y\_pos$.

---

## 2026-07-10 10:07:39

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides vertical thrust to manage $y\_vel$, but its vertical effectiveness is modulated by the current `angle`.
3. **Directional Angular Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque to manipulate `ang_vel`, allowing for orientation control.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid `angle` changes, creating a feedback loop where orientation becomes increasingly difficult to stabilize as tilt grows.
5. **Thrust-Induced Lateral Acceleration:** Applying any engine thrust (Actions 1, 2, or 3) results in lateral acceleration ($x\_vel$ change) that is a function of the specific engine used and the current `angle`.
6. **Contact-Induced Angular Volatility:** The onset of leg contact (`left_leg_contact` or `right_leg_contact` = 1.0) triggers immediate, high-magnitude surges or rapid sign-reversals in `ang_vel`.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of three distinct metrics: the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the $y\_vel$ (descent speed).
8. **Multi-Modal Terminal Failure:** Failure is triggered either by the $y\_pos$ crossing the zero threshold ($y\_pos \le 0$) or by `ang_vel` reaching a critical threshold.
9. **Main Engine Torque Coupling:** At significant `angle` values, the main engine (Action 2) generates unintended torque, causing rapid changes in `ang_vel` in addition to its effect on $y\_vel$.
10. **Contact-Terminal Synchronization:** The onset of leg contact is frequently synchronized with the $y\_pos$ crossing the zero threshold, where the resulting `ang_vel` spikes from contact can trigger immediate terminal failure.

---

## 2026-07-10 10:11:35

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides vertical thrust to manage $y\_vel$, but its vertical effectiveness is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`, allowing for orientation control.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid `angle` changes, creating a feedback loop where orientation becomes increasingly difficult to stabilize as tilt grows.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action (1, 2, or 3) is a function of the current `angle`, causing the direction of lateral movement to shift as the lander tilts.
6. **Contact-Induced Angular Volatility:** The onset of leg contact (`left_leg_contact` or `right_leg_contact` = 1.0) triggers immediate, high-magnitude surges or rapid sign-reversals in `ang_vel`.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of three distinct metrics: the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the $y\_vel$ (descent speed).
8. **Multi-Modal Terminal Failure:** Failure is triggered either by the $y\_pos$ crossing the zero threshold ($y\_pos \le 0$) or by `ang_vel` reaching a critical threshold.
9. **Main Engine Torque Coupling:** At significant `angle` values, the main engine (Action 2) generates unintended torque, causing rapid changes in `ang_vel` in addition to its effect on $y\_vel$.
10. **Contact-Driven Terminal Acceleration:** Contact-induced `ang_vel` spikes can cause the system to exceed the critical angular velocity threshold, triggering terminal failure even if $y\_pos$ remains above the ground threshold.

---

## 2026-07-10 10:16:08

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides vertical thrust to manage $y\_vel$, but its vertical effectiveness is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`, allowing for orientation control.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid `angle` changes, creating a feedback loop where orientation becomes increasingly difficult to stabilize as tilt grows.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action (1, 2, or 3) is a function of the current `angle`, causing the direction of lateral movement to shift as the lander tilts.
6. **Contact-Induced Angular Instability:** Leg contact triggers immediate sign-reversals in `ang_vel` or, if the lander's orientation is not corrected, can drive a sustained increase in rotation speed.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of three distinct metrics: the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the $y\_vel$ (descent speed).
8. **Multi-Modal Terminal Failure:** Failure is triggered either by the $y\_pos$ crossing the zero threshold ($y\_pos \le 0$) or by `ang_vel` reaching a critical threshold.
9. **Main Engine Torque Coupling:** At significant `angle` values, the main engine (Action 2) generates unintended torque, causing rapid changes in `ang_vel` in addition to its effect on $y\_vel$.
10. **Post-Contact Descent Risk:** Leg contact does not guarantee altitude stability; if $y\_vel$ is not neutralized, the lander can rapidly transition from contact to a ground collision ($y\_pos \le 0$).

---

## 2026-07-10 10:18:28

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides vertical thrust to manage $y\_vel$, but its vertical effectiveness is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`, allowing for orientation control.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid `angle` changes, creating a feedback loop where orientation becomes increasingly difficult to stabilize as tilt grows.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action (1, 2, or 3) is a function of the current `angle`, causing the direction of lateral movement to shift as the lander tilts.
6. **Contact-Induced Angular Impulse:** Leg contact can trigger massive, sudden spikes or sign-reversals in `ang_vel` (e.g., a jump from -0.05 to +0.30), which can instantly destabilize the lander's orientation.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of three distinct metrics: the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the $y\_vel$ (descent speed).
8. **Multi-Modal Terminal Failure:** Failure is triggered either by the $y\_pos$ crossing the zero threshold ($y\_pos \le 0$) or by `ang_vel` reaching a critical threshold.
9. **Main Engine Torque Coupling:** At significant `angle` values, the main engine (Action 2) generates unintended torque, causing rapid changes in `ang_vel` in addition to its effect on $y\_vel$.
10. **Momentum-Driven Contact Failure:** Leg contact does not negate downward momentum; if $y\_vel$ is not sufficiently neutralized before contact, the lander will rapidly transition from contact to a ground collision ($y\_pos \le 0$).

---

## 2026-07-10 10:21:58

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides vertical thrust to manage $y\_vel$, but its vertical effectiveness is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`, allowing for orientation control.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid `angle` changes, creating a feedback loop where orientation becomes increasingly difficult to stabilize as tilt grows.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action (1, 2, or 3) is a function of the current `angle`, causing the direction of lateral movement to shift as the lander tilts.
6. **Contact-Induced Angular Impulse:** Leg contact can trigger sudden, massive spikes or sign-reversals in `ang_vel` (e.g., a jump from -0.05 to +0.30), which can instantly destabilize the lander's orientation.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the $y\_vel$ (descent speed).
8. **Impact-Velocity-Dependent Terminality:** The outcome of reaching the ground ($y\_pos \le 0$) is determined by the magnitude of $y\_vel$; high-velocity impacts trigger FAILURE, whereas low-velocity impacts allow for a PARTIAL (soft) landing state.
9. **Main Engine Torque Coupling:** At significant `angle` values, the main engine (Action 2) generates unintended torque, causing rapid changes in `ang_vel` in addition to its effect on $y\_vel$.
10. **Non-Terminal Leg Contact:** Leg contact (single or dual) does not automatically terminate the episode or arrest vertical momentum; the lander can exist in a state of contact while $y\_pos > 0$, provided $y\_vel$ is sufficiently low to prevent a rapid transition to a high-velocity ground collision.

---

## 2026-07-10 10:25:23

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides vertical thrust to manage $y\_vel$, but its vertical effectiveness is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`, allowing for orientation control.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid `angle` changes, creating a feedback loop where orientation becomes increasingly difficult to stabilize as tilt grows.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action (1, 2, or 3) is a function of the current `angle`, causing the direction of lateral movement to shift as the lander tilts.
6. **Contact-Induced Angular Impulse:** Leg contact can trigger sudden, massive spikes or sign-reversals in `ang_vel` (e.g., a jump from -0.05 to +0.30), which can instantly destabilize the lander's orientation.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the $y\_vel$ (descent speed).
8. **Terminality and Crash Penalties:** Reaching the ground ($y\_pos \le 0$) with excessive vertical velocity or uncontrolled angular momentum triggers immediate failure and massive negative rewards.
9. **Main Engine Torque Coupling:** At significant `angle` values, the main engine (Action 2) generates unintended torque, causing rapid changes in `ang_vel` in addition to its effect on $y\_vel$.
10. **Post-Contact Kinetic State:** Leg contact does not automatically terminate the episode; the lander can enter a sustained state of "skidding" or "spinning" where it maintains contact while $y\_pos \approx 0$, subject to significant lateral and angular velocities.

---

## 2026-07-10 10:27:05

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides vertical thrust to manage $y\_vel$, but its vertical effectiveness is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`, allowing for orientation control.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid `angle` changes, creating a feedback loop where orientation becomes increasingly difficult to stabilize as tilt grows.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action (1, 2, or 3) is a function of the current `angle`, causing the direction of lateral movement to shift as the lander tilts.
6. **Contact-Induced Angular Impulse:** Leg contact can trigger sudden, massive spikes or sign-reversals in `ang_vel`, which can instantly destabilize the lander's orientation.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** At significant `angle` values, the main engine (Action 2) generates unintended torque, causing rapid changes in `ang_vel` in addition to its effect on $y\_vel$.
9. **Extended Post-Contact Skidding:** Leg contact at or below $y\_pos = 0$ does not immediately terminate the episode; the lander can enter a sustained state of "skidding" or "spinning" where it maintains contact while undergoing high $x\_vel$, $y\_vel$, and $ang\_vel$.
10. **Terminality and Crash Penalties:** Reaching the ground with excessive vertical or lateral velocity, or uncontrolled angular momentum, triggers immediate failure and massive negative rewards.

---

## 2026-07-10 10:29:48

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides vertical thrust to manage $y\_vel$, but its vertical effectiveness is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`, allowing for orientation control.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid `angle` changes, creating a feedback loop where orientation becomes increasingly difficult to stabilize as tilt grows.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action (1, 2, or 3) is a function of the current `angle`, causing the direction of lateral movement to shift as the lander tilts.
6. **Contact-Induced Angular Impulse:** Transitioning to a leg contact state (at or near $y\_pos = 0$) can trigger sudden, massive spikes or sign-reversals in `ang_vel`, potentially causing an immediate loss of orientation control.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** At significant `angle` values, the main engine (Action 2) generates unintended torque, causing rapid changes in `ang_vel` in addition to its effect on $y\_vel$.
9. **Extended Post-Contact Dynamics:** Upon making contact at or below $y\_pos = 0$, the episode does not necessarily terminate instantly; the lander may undergo a period of extreme angular acceleration and skidding before terminal failure is triggered.
10. **Terminality and Crash Penalties:** The episode terminates with a massive negative reward if the lander reaches the ground with excessive velocities or if contact-induced angular momentum becomes unrecoverable.

---

## 2026-07-10 10:32:14

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides vertical thrust to manage $y\_vel$, but its vertical effectiveness is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`, allowing for orientation control.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid `angle` changes, creating a feedback loop where orientation becomes increasingly difficult to stabilize as tilt grows.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action (1, 2, or 3) is a function of the current `angle`, causing the direction of lateral movement to shift as the lander tilts.
6. **Contact-Induced Stability/Reward Dynamics:** Transitioning to a contact state can trigger high positive rewards for successful deceleration, but the state is highly sensitive; subsequent angular or lateral movement while in contact can trigger massive negative penalties.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** At significant `angle` values, the main engine (Action 2) generates unintended torque, causing rapid changes in `ang_vel` in addition to its effect on $y\_vel$.
9. **Extended Post-Contact Skidding Dynamics:** In "PARTIAL" outcomes, the lander can enter an extended skidding phase at near-zero $y\_pos$, where it must minimize all velocity and angular components to avoid frequent, large negative rewards.
10. **Terminality and Outcome Distinction:** "FAILURE" is an immediate terminal state with massive penalties (e.g., -100), often triggered by lateral boundary or velocity violations, whereas "PARTIAL" indicates a successful landing that survives contact through a period of instability.

---

## 2026-07-10 10:35:45

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides vertical thrust to manage $y\_vel$, but its vertical effectiveness is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`, allowing for orientation control.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid `angle` changes, creating a feedback loop where orientation becomes increasingly difficult to stabilize as tilt grows.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action (1, 2, or 3) is a function of the current `angle`, causing the direction of lateral movement to shift as the lander tilts.
6. **Contact-Induced Instability:** Transitioning to a contact state (leg contact = 1.0) creates a high-sensitivity environment where even minor angular velocities (`ang_vel`) can trigger massive negative penalties or immediate terminal failure.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** At significant `angle` values, the main engine (Action 2) generates unintended torque, causing rapid changes in `ang_vel` in addition to its effect on $y\_vel$.
9. **Post-Contact Rotational Escalation:** During the contact phase, engine actions intended for stabilization (such as using side engines to correct tilt or the main engine to manage descent) can cause `ang_vel` to escalate uncontrollably, leading to a "tipping" failure.
10. **Terminality and Outcome Distinction:** "FAILURE" is an immediate terminal state with massive penalties (e.g., -100), often triggered by lateral boundary violations, velocity violations, or excessive angular movement during or immediately after contact.

---

## 2026-07-10 10:36:38

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides vertical thrust to manage $y\_vel$, but its vertical effectiveness is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`, allowing for orientation control.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid `angle` changes, creating a feedback loop where orientation becomes increasingly difficult to stabilize as tilt grows.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action is a function of the current `angle`, causing the direction of lateral movement to shift as the lander tilts.
6. **Contact-Induced Angular Spiking:** The transition of a leg to a contact state (`leg_contact` = 1.0) can trigger an immediate, non-linear spike in `ang_vel`, representing a significant discontinuity in rotational dynamics compared to free-flight.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** At significant `angle` values, the main engine (Action 2) generates unintended torque, causing rapid changes in `ang_vel` in addition to its effect on $y\_vel$.
9. **Post-Contact Control Failure:** During the contact phase, standard stabilization actions (such as side engines or main engine thrust) may be unable to arrest the sudden spike in `ang_vel`, potentially accelerating the tipping sequence.
10. **Terminality and Outcome Distinction:** "FAILURE" is an immediate terminal state with massive penalties, frequently resulting from the uncontrolled tipping or tumbling that occurs immediately upon or after leg contact.

---

## 2026-07-10 10:40:48

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides vertical thrust to manage $y\_vel$, but its vertical effectiveness is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`, allowing for orientation control.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid `angle` changes, creating a feedback loop where orientation becomes increasingly difficult to stabilize as tilt grows.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action is a function of the current `angle`, causing the direction of lateral movement to shift as the lander tilts.
6. **Contact-Induced Angular Discontinuity:** The transition of a leg to a contact state (`leg_contact` = 1.0) triggers immediate, non-linear shifts in `ang_vel`, representing a sudden discontinuity in rotational dynamics compared to free flight.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** At significant `angle` values, the main engine (Action 2) generates unintended torque, causing rapid changes in `ang_vel` in addition to its effect on $y\_vel$.
9. **Single-Leg Pivot Dynamics:** A single-leg contact state (where only one `leg_contact` is 1.0) acts as a rotational pivot, significantly increasing the magnitude of angular acceleration and instability compared to a dual-leg contact state.
10. **Kinetic Energy-Based Terminality:** The transition to a "FAILURE" state is determined by whether the lander's kinetic and rotational energy at the moment of contact exceeds the restorative capacity of the available engine thrust.

---

## 2026-07-10 10:42:56

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides vertical thrust to manage $y\_vel$, but its vertical effectiveness is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`, allowing for orientation control.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid `angle` changes, creating a feedback loop where orientation becomes increasingly difficult to stabilize as tilt grows.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action is a function of the current `angle`, causing the direction of lateral movement to shift as the lander tilts.
6. **Contact-Induced Angular Discontinuity:** The transition of a leg to a contact state (`leg_contact` = 1.0) triggers immediate, non-linear shifts in `ang_vel`, representing a sudden discontinuity in rotational dynamics compared to free flight.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** At significant `angle` values, the main engine (Action 2) generates unintended torque, causing rapid changes in `ang_vel` in addition to its effect on $y\_vel$.
9. **Single-Leg Pivot Instability:** A single-leg contact state acts as a rotational pivot, where engine torques (Actions 1 and 3) generate significantly higher angular acceleration compared to free flight or dual-leg contact.
10. **Kinetic Energy-Based Terminality:** The transition to a "FAILURE" state is determined by whether the lander's kinetic and rotational energy at the moment of contact exceeds the restorative capacity of the available engine thrust.

---

## 2026-07-10 10:46:29

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides vertical thrust to manage $y\_vel$, but its vertical effectiveness is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`, allowing for orientation control.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid `angle` changes, creating a feedback loop where orientation becomes increasingly difficult to stabilize as tilt grows.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action is a function of the current `angle`, causing the direction of lateral movement to shift as the lander tilts.
6. **Contact-Induced Angular Impulse:** The transition of a leg to a contact state (`leg_contact` = 1.0) triggers an immediate, non-linear impulse, causing a sudden shift in `ang_vel` that differs from free-flight rotational dynamics.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** At significant `angle` values, the main engine (Action 2) generates unintended torque, causing rapid changes in `ang_vel` in addition to its effect on $y\_vel$.
9. **Single-Leg Pivot Torque Amplification:** When a single leg is in contact, the main engine (Action 2) produces significantly higher angular acceleration than in free flight, as the contact point acts as a rotational pivot that amplifies engine torque.
10. **Kinetic Energy-Based Terminality:** The transition to a "FAILURE" state is determined by whether the lander's kinetic and rotational energy at the moment of contact exceeds the restorative capacity of the available engine thrust.

---

## 2026-07-10 10:50:56

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides vertical thrust to manage $y\_vel$, but its vertical effectiveness is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`, allowing for orientation control.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid `angle` changes, creating a feedback loop where orientation becomes increasingly difficult to stabilize as tilt grows.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action is a function of the current `angle`, causing the direction of lateral movement to shift as the lander tilts.
6. **Contact-Influenced Rotational Dynamics:** The presence of leg contact (`leg_contact` = 1.0) fundamentally alters `ang_vel` trajectories, often inducing sudden, non-linear shifts in rotational velocity even in the absence of a contact state transition.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** At significant `angle` values, the main engine (Action 2) generates unintended torque, causing rapid changes in `ang_vel` in addition to its effect on $y\_vel$.
9. **Single-Leg Pivot Torque Amplification:** When a single leg is in contact, the main engine (Action 2) produces significantly higher angular acceleration than in free flight, as the contact point acts as a rotational pivot that amplifies engine torque.
10. **Contact-State Volatility and Stabilization:** Single-leg contact creates an unstable pivot prone to bouncing or tipping (rapidly transitioning between contact states), whereas dual-leg contact (`left_leg_contact` and `right_leg_contact` both 1.0) provides a damping effect that tends to stabilize `ang_vel`.

---

## 2026-07-10 10:51:36

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** Action 2 (main engine) provides vertical thrust to manage $y\_vel$, but its vertical effectiveness is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`, allowing for orientation control.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid `angle` changes, creating a feedback loop where orientation becomes increasingly difficult to stabilize as tilt grows.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action is a function of the current `angle`, causing the direction of lateral movement to shift as the lander tilts.
6. **Contact-Induced Rotational Impulse:** The transition from free flight to single-leg contact (`leg_contact` = 1.0) induces a significant, nearly instantaneous impulse in `ang_vel`, causing sudden and large shifts in rotational velocity.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the magnitude of the `angle` (tilt), the magnitude of the `ang_vel` (rotation speed), and the magnitude of the $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** At significant `angle` values, the main engine (Action 2) generates unintended torque, causing rapid changes in `ang_vel` in addition to its effect on $y\_vel$.
9. **Single-Leg Pivot Torque Amplification:** When a single leg is in contact, the main engine (Action 2) produces significantly higher angular acceleration than in free flight, as the contact point acts as a rotational pivot that amplifies engine torque.
10. **Momentum-Contact Instability Trap:** While dual-leg contact provides a damping effect, if the lander enters a contact state while possessing high `ang_vel` or a large `angle`, the combined effects of rotational impulses and pivot-induced torque can render the system unrecoverable.

---

## 2026-07-10 10:53:54

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** The vertical effectiveness of the main engine (Action 2) is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid changes in `angle`, creating a feedback loop that makes orientation increasingly difficult to stabilize.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action is a function of the current `angle`, shifting the direction of lateral movement as the lander tilts.
6. **Contact-Induced Rotational Impulse:** The transition from free flight to single-leg contact induces a sudden, high-magnitude impulse in `ang_vel` that can drastically change the magnitude or even reverse the sign of the rotational velocity.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the `angle` (tilt), `ang_vel` (rotation speed), and $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** At non-zero `angle` values, the main engine (Action 2) generates unintended torque, causing changes in `ang_vel` in addition to its effect on $y\_vel$.
9. **Single-Leg Pivot Torque Amplification:** When a single leg is in contact, the main engine (Action 2) acts upon the contact point as a rotational pivot, generating extreme angular acceleration.
10. **Momentum-Contact Instability Trap:** Entering a contact state while possessing high `ang_vel` or a large `angle` can trigger unrecoverable rotational instability due to the combined effects of contact impulses and pivot-induced torque.

---

## 2026-07-10 10:57:12

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** The vertical effectiveness of the main engine (Action 2) is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid changes in `angle`, creating a feedback loop that makes orientation increasingly difficult to stabilize.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action is a function of the current `angle`, shifting the direction of lateral movement as the lander tilts.
6. **Contact-Induced Rotational Impulse:** The transition from free flight to a contact state (single or dual leg) induces a sudden, high-magnitude impulse in `ang_vel`, which can drastically change the magnitude or reverse the sign of the rotational velocity.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the `angle` (tilt), `ang_vel` (rotation speed), and $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** At non-zero `angle` values, the main engine (Action 2) generates unintended torque, causing changes in `ang_vel` in addition to its effect on $y\_vel$.
9. **Contact-State Torque Amplification:** Once a leg is in contact with the ground, the lander acts as a rotational pivot; any engine action (notably Action 2 and side engines) generates significantly higher angular acceleration than in free flight.
10. **Momentum-Contact Instability Trap:** Entering a contact state while possessing high `ang_vel` or a large `angle` triggers rapid, unrecoverable rotational instability due to the synergistic effects of the contact impulse and the pivot-induced torque.

---

## 2026-07-10 10:59:04

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** The vertical effectiveness of the main engine (Action 2) is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid changes in `angle`, creating a feedback loop that makes orientation increasingly difficult to stabilize.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action is a function of the current `angle`, shifting the direction of lateral movement as the lander tilts.
6. **Contact-Induced Rotational Impulse:** The transition from free flight to a contact state (single or dual leg) induces a sudden, high-magnitude impulse in `ang_vel`, which can drastically change the magnitude or reverse the sign of the rotational velocity.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the `angle` (tilt), `ang_vel` (rotation speed), and $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** At non-zero `angle` values, the main engine (Action 2) generates unintended torque, causing changes in `ang_vel` in addition to its effect on $y\_vel$.
9. **Contact-State Torque Amplification and Ejection:** Once a leg is in contact with the ground, the lander acts as a rotational pivot, significantly amplifying engine torque. High-magnitude actions, especially side engines during single-leg contact, can trigger a "bounce" effect, ejecting the lander from the contact state back into free flight with destabilized angular momentum.
10. **Momentum-Contact Instability Trap:** Entering a contact state while possessing high `ang_vel` or a large `angle` triggers rapid, unrecoverable rotational instability due to the synergistic effects of the contact impulse and the pivot-induced torque, often leading to catastrophic terminal failure.

---

## 2026-07-10 11:00:42

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** The vertical effectiveness of the main engine (Action 2) is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid changes in `angle`, creating a feedback loop that makes orientation increasingly difficult to stabilize.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action is a function of the current `angle`, shifting the direction of lateral movement as the lander tilts.
6. **Contact-Induced Rotational Impulse:** The transition from free flight to a contact state induces a sudden, high-magnitude impulse in `ang_vel`, which can drastically change the magnitude or reverse the sign of the rotational velocity.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the `angle` (tilt), `ang_vel` (rotation speed), and $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** At non-zero `angle` values, the main engine (Action 2) generates unintended torque, causing changes in `ang_vel` in addition to its effect on $y\_vel$.
9. **Contact-State Pivot and Ejection:** Once a leg is in contact with the ground, the lander acts as a rotational pivot, significantly amplifying engine torque. High-magnitude actions can trigger a "bounce" effect, ejecting the lander from the contact state back into free flight.
10. **Impact Velocity and Orientation Criticality:** Catastrophic failure is triggered if ground contact is made while the lander possesses excessive lateral velocity ($x\_vel$) or a significant `angle`, even if the vertical descent speed ($y\_vel$) is controlled.

---

## 2026-07-10 11:04:59

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** The vertical effectiveness of the main engine (Action 2) is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid changes in `angle`, creating a feedback loop that makes orientation increasingly difficult to stabilize.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action is a function of the current `angle`, shifting the direction of lateral movement as the lander tilts.
6. **Contact-Induced Rotational Impulse:** The transition from free flight to a contact state induces a sudden, high-magnitude impulse in `ang_vel`, which can drastically change the magnitude or reverse the sign of the rotational velocity.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the `angle` (tilt), `ang_vel` (rotation speed), and $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** At non-zero `angle` values, the main engine (Action 2) generates unintended torque, causing changes in `ang_vel` in addition to its effect on $y\_vel$.
9. **Contact-State Pivot and Ejection:** Once a leg is in contact with the ground, the lander acts as a rotational pivot, significantly amplifying engine torque. High-magnitude actions can trigger a "bounce" effect, ejecting the lander from the contact state back into free flight.
10. **Lateral Velocity and Impact Criticality:** Catastrophic failure is triggered if ground contact is made while the lander possesses excessive lateral velocity ($x\_vel$) or a significant `angle`. Uncontrolled horizontal drift (high $x\_vel$) is a primary driver of failure, even when vertical descent speed is controlled.

---

## 2026-07-10 11:14:44

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** The vertical effectiveness of the main engine (Action 2) is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid changes in `angle`, creating a feedback loop that makes orientation increasingly difficult to stabilize.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action is a function of the current `angle`, shifting the direction of lateral movement as the lander tilts.
6. **Contact-Induced Rotational Impulse:** The transition from free flight to a contact state induces a sudden, high-magnitude impulse in `ang_vel`, which can drastically change the magnitude or reverse the sign of the rotational velocity.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the `angle` (tilt), `ang_vel` (rotation speed), and $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** At non-zero `angle` values, the main engine (Action 2) generates unintended torque, causing changes in `ang_vel` in addition to its effect on $y\_vel$.
9. **Contact-State Pivot and Ejection:** Once a leg is in contact with the ground, the lander acts as a rotational pivot, significantly amplifying engine torque. High-magnitude actions or improper orientation can trigger an "ejection," where the lander bounces from a contact state back into free flight.
10. **Contact Regime Volatility:** The contact state is highly dynamic, frequently transitioning between three distinct modes: full contact (1,1), partial contact (1,0 or 0,1), and free flight (0,0). These transitions can result in complex sequences of bouncing and re-landing as the lander attempts to achieve stability.

---

## 2026-07-10 11:18:20

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** The vertical effectiveness of the main engine (Action 2) is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid changes in `angle`, creating a feedback loop that makes orientation increasingly difficult to stabilize.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action is a function of the current `angle`, shifting the direction of lateral movement as the lander tilts.
6. **Contact-Induced Rotational Impulse:** The transition from free flight to a contact state induces a sudden, high-magnitude impulse in `ang_vel`, which can drastically change the magnitude or reverse the sign of the rotational velocity.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the `angle` (tilt), `ang_vel` (rotation speed), and $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** At non-zero `angle` values, the main engine (Action 2) generates unintended torque, causing changes in `ang_vel` in addition to its effect on $y\_vel$.
9. **Contact-State Volatility and Ejection:** The lander transitions between free flight (0,0), partial contact (1,0 or 0,1), and full contact (1,1). During contact, the lander acts as a rotational pivot that amplifies torque, which can trigger "ejections" (bounces back into free flight) or rapid, unstable transitions between contact modes.
10. **Contact-Thrust Instability:** Applying high-magnitude thrust (Action 2) while in a full contact state (1,1) can lead to catastrophic instability and extreme negative rewards. Furthermore, even in a zero-action state (Action 0), contact regimes can trigger significant penalties due to uncontrolled vertical/angular oscillations or landing impacts.

---

## 2026-07-10 11:20:23

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** The vertical effectiveness of the main engine (Action 2) is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid changes in `angle`, creating a feedback loop that makes orientation increasingly difficult to stabilize.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action is a function of the current `angle`, shifting the direction of lateral movement as the lander tilts.
6. **Contact-Induced Rotational Impulse:** The transition from free flight to a contact state induces a sudden, high-magnitude impulse in `ang_vel`, which can drastically change the magnitude or reverse the sign of the rotational velocity.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the `angle` (tilt), `ang_vel` (rotation speed), and $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** At non-zero `angle` values, the main engine (Action 2) generates unintended torque, causing changes in `ang_vel` in addition to its effect on $y\_vel$.
9. **Contact-State Volatility and Ground Oscillations:** The lander transitions between free flight (0,0), partial contact (1,0 or 0,1), and full contact (1,1). In the full contact state (1,1), the system exhibits extreme reward volatility; actions (including Action 0) can trigger massive, unpredictable reward swings (both positive and negative) due to unstable ground-interaction physics and oscillations.
10. **Catastrophic Ground Penetration:** A distinct terminal failure mode exists where the lander's $y\_pos$ descends into significant negative values, triggering a massive, immediate penalty (e.g., -100) that distinguishes a ground crash from the incremental instabilities of the contact regime.

---

## 2026-07-10 11:21:22

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** The vertical effectiveness of the main engine (Action 2) is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid changes in `angle`, creating a feedback loop that makes orientation increasingly difficult to stabilize.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action is a function of the current `angle`, shifting the direction of lateral movement as the lander tilts.
6. **Contact-Induced Rotational Impulse:** Transitions between free flight (0,0) and contact states (1,0 or 0,1) induce sudden, high-magnitude impulses in `ang_vel`, which can drastically increase rotational velocity.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the `angle` (tilt), `ang_vel` (rotation speed), and $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** Even at small non-zero `angle` values, the main engine (Action 2) generates significant unintended torque, causing rapid and large changes in `ang_vel`.
9. **Contact-State Reward Volatility:** In the full contact state (1,1), the system exhibits extreme reward volatility; actions can trigger massive, unpredictable reward swings (both high positive and high negative) due to unstable ground-interaction physics.
10. **Catastrophic Ground Penetration:** A terminal failure mode exists where the lander's $y\_pos$ descends into negative values, triggering an immediate, massive penalty (e.g., -100) that terminates the episode.

---

## 2026-07-10 11:24:33

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** The vertical effectiveness of the main engine (Action 2) is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid changes in `angle`, creating a feedback loop that makes orientation increasingly difficult to stabilize.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action is a function of the current `angle`, shifting the direction of lateral movement as the lander tilts.
6. **Contact-Induced Rotational Impulse:** Transitions between free flight (0,0) and contact states (1,0, 0,1, or 1,1) induce sudden, high-magnitude impulses in `ang_vel`, which can drastically increase rotational velocity.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the `angle` (tilt), `ang_vel` (rotation speed), and $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** Even at small non-zero `angle` values, the main engine (Action 2) generates significant unintended torque, causing rapid and large changes in `ang_vel`.
9. **Contact-State Reward Volatility:** Transitions into contact states (1,0, 0,1, or 1,1) result in extreme reward volatility; actions taken during ground contact can trigger massive, unpredictable swings in reward (both highly positive and highly negative) due to ground-interaction physics.
10. **Non-Terminal Ground Interaction:** The $y\_pos \le 0$ threshold defines the ground-interaction regime. Entering this regime does not trigger an immediate terminal failure, but instead allows for continued, high-variance interaction with the ground.

---

## 2026-07-10 11:48:47

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** The vertical effectiveness of the main engine (Action 2) is modulated by the current `angle`.
3. **Opposing Side-Engine Torque:** Action 1 (left engine) and Action 3 (right engine) apply torque in opposite directions to manipulate `ang_vel`.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid changes in `angle`, creating a feedback loop that makes orientation increasingly difficult to stabilize.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action is a function of the current `angle`, shifting the direction of lateral movement as the lander tilts.
6. **Contact-Induced Rotational Impulse:** Transitions between free flight and contact states (when leg contact flags transition from 0 to 1) induce sudden, high-magnitude impulses in `ang_vel`, which can cause rapid, extreme increases in rotational velocity.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the `angle` (tilt), `ang_vel` (rotation speed), and $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** Even at small non-zero `angle` values, the main engine (Action 2) generates significant unintended torque, causing rapid and large changes in `ang_vel`.
9. **Contact-State Reward Volatility:** The reward signal is extremely volatile during ground contact; specific engine actions while in contact can result in massive reward swings (both highly positive and highly negative) due to complex ground-interaction physics.
10. **Non-Terminal Ground Interaction:** The $y\_pos \le 0$ threshold defines a non-terminal ground-interaction regime. The simulation continues post-contact, allowing for continued, high-variance interaction between the lander and the ground.

---

## 2026-07-10 11:50:19

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** The vertical effectiveness of the main engine (Action 2) is modulated by the current `angle`.
3. **Asymmetric Side-Engine Side-Effects:** While Action 1 (left) and Action 3 (right) provide opposing torque to manipulate `ang_vel`, Action 1 is associated with significantly higher-magnitude negative reward penalties during descent compared to Action 3.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid changes in `angle`, creating a feedback loop that makes orientation increasingly difficult to stabilize.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action is a function of the current `angle`, shifting the direction of lateral movement as the lander tilts.
6. **Contact-Induced Rotational Impulse:** Transitions between free flight and contact states (when leg contact flags transition from 0 to 1) induce sudden, high-magnitude impulses in `ang_vel`, which can cause rapid, extreme increases in rotational velocity.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the `angle` (tilt), `ang_vel` (rotation speed), and $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** Even at small non-zero `angle` values, the main engine (Action 2) generates significant unintended torque, causing rapid and large changes in `ang_vel`.
9. **Contact-State Reward Volatility:** The reward signal is extremely volatile during ground contact; engine actions can trigger massive, rapid swings between high positive and highly negative rewards.
10. **Terminal Failure Condition:** A catastrophic reward (-100.0) is triggered at the end of an episode, typically coinciding with the transition to a state where both leg contact flags are active (1.0, 1.0).

---

## 2026-07-10 11:53:19

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** The vertical effectiveness of the main engine (Action 2) is modulated by the current `angle`.
3. **Asymmetric Side-Engine Descent Penalties:** During the descent phase (prior to leg contact), Action 1 (left engine) is associated with consistently higher-magnitude negative reward penalties compared to Action 3 (right engine).
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid changes in `angle`, creating a feedback loop that makes orientation increasingly difficult to stabilize.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action is a function of the current `angle`, shifting the direction of lateral movement as the lander tilts.
6. **Contact-Induced Rotational Impulse:** Transitions between free flight and contact states (when leg contact flags transition from 0 to 1) induce sudden, high-magnitude impulses in `ang_vel`, which can cause rapid, extreme increases in rotational velocity.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the `angle` (tilt), `ang_vel` (rotation speed), and $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** Even at small non-zero `angle` values, the main engine (Action 2) generates significant unintended torque, causing rapid and large changes in `ang_vel`.
9. **Extreme Contact-State Reward Volatility:** Upon ground contact (both legs = 1.0), the reward signal becomes extremely volatile; engine actions can trigger massive, rapid swings between high positive rewards (e.g., >20.0) and high negative rewards (e.g., <-15.0).
10. **Catastrophic Terminal Failure Condition:** A catastrophic reward (-100.0) triggers episode termination, occurring during the contact phase when specific engine actions are taken in unstable states.

---

## 2026-07-10 11:56:31

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** The vertical effectiveness of the main engine (Action 2) is modulated by the current `angle`.
3. **Side-Engine Descent Penalties:** During the descent phase (prior to leg contact), side engine actions (Action 1 and Action 3) are associated with negative rewards, with Action 3 frequently incurring higher-magnitude negative penalties than Action 1.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid changes in `angle`, creating a feedback loop that makes orientation increasingly difficult to stabilize.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action is a function of the current `angle`, shifting the direction of lateral movement as the lander tilts.
6. **Contact-Induced Rotational Impulse:** Transitions between free flight and contact states (when leg contact flags transition from 0 to 1) induce sudden, high-magnitude impulses in `ang_vel`, which can cause rapid, extreme increases in rotational velocity.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the `angle` (tilt), `ang_vel` (rotation speed), and $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** Even at small non-zero `angle` values, the main engine (Action 2) generates unintended torque, causing changes in `ang_vel`.
9. **Extreme Contact-State Reward Volatility:** Upon ground contact (both legs = 1.0), the reward signal becomes extremely volatile; engine actions can trigger rapid swings between high positive rewards (e.g., >10.0) and catastrophic termination.
10. **Catastrophic Terminal Failure Condition:** A catastrophic reward (-100.0) triggers episode termination during the contact phase, often when side engine actions (Action 1 or Action 3) are applied at near-zero `angle` or `ang_vel` values.

---

## 2026-07-10 11:57:46

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** The vertical effectiveness of the main engine (Action 2) is modulated by the current `angle`.
3. **Descent-Phase Side-Engine Penalties:** Side engine actions (Action 1 and Action 3) are associated with negative rewards specifically when the lander is in a descent phase (negative $y\_vel$).
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid changes in `angle`, creating a feedback loop that makes orientation increasingly difficult to stabilize.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action is a function of the current `angle`, shifting the direction of lateral movement as the lander tilts.
6. **Contact-Induced Rotational Impulse:** Transitions from free flight to a contact state (when leg contact flags transition from 0 to 1) induce sudden, high-magnitude impulses in `ang_vel`.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the `angle` (tilt), `ang_vel` (rotation speed), and $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** Even at small non-zero `angle` values, the main engine (Action 2) generates unintended torque, causing changes in `ang_vel`.
9. **Extreme Contact-State Reward Volatility:** Upon ground contact (at least one leg contact flag = 1.0), the reward signal becomes extremely volatile; engine actions can trigger rapid swings between very high positive rewards and catastrophic termination.
10. **Contact-Phase Side-Engine Termination:** A catastrophic reward (-100.0) triggers episode termination when side engine actions (Action 1 or Action 3) are applied during any contact state (where at least one leg contact flag is 1.0).

---

## 2026-07-10 12:00:26

---
1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** The vertical effectiveness of the main engine (Action 2) is modulated by the current `angle`.
3. **Side-Engine Penalty Ubiquity:** Side engine actions (Action 1 and Action 3) are frequently associated with negative rewards, occurring in both ascent and descent phases.
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid changes in `angle`, creating a feedback loop that makes orientation increasingly difficult to stabilize.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action is a function of the current `angle`, shifting the direction of lateral movement as the lander tilts.
6. **Contact-Induced Rotational Impulse:** Transitions from free flight to a contact state (when leg contact flags transition from 0 to 1) induce sudden, high-magnitude impulses in `ang_vel`.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the `angle` (tilt), `ang_vel` (rotation speed), and $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** Even at small non-zero `angle` values, the main engine (Action 2) generates unintended torque, causing changes in `ang_vel`.
9. **Phase-Dependent Main Engine Rewards:** The main engine (Action 2) reward is highly dependent on the flight phase, providing substantial positive rewards during descent while potentially incurring penalties during ascent.
10. **Contact-State Reward Extremes:** Upon ground contact, the reward signal becomes extremely volatile; engine actions can trigger rapid swings between large positive rewards, significant negative penalties, or a terminal -100.0 reward.

---

## 2026-07-10 12:02:19

1. **Gravity-Driven Descent:** Gravity causes continuous downward acceleration, increasing the magnitude of negative $y\_vel$ and decreasing $y\_pos$ unless countered by sufficient upward thrust.
2. **Orientation-Dependent Main Thrust:** The vertical effectiveness of the main engine (Action 2) is modulated by the current `angle`.
3. **Side-Engine Reward Asymmetry:** While both side engines can incur penalties, Action 1 (Left Engine) is more consistently associated with negative rewards across both descent and contact phases than Action 3 (Right Engine).
4. **Angular Momentum Runaway:** High `ang_vel` drives rapid changes in `angle`, creating a feedback loop that makes orientation increasingly difficult to stabilize.
5. **Angle-Dependent Lateral Thrust:** The lateral acceleration ($x\_vel$ change) produced by any engine action is a function of the current `angle`, shifting the direction of lateral movement as the lander tilts.
6. **Contact-Induced Rotational Impulse:** Transitions from free flight to a contact state (when leg contact flags transition from 0 to 1) induce sudden, high-magnitude impulses in `ang_vel`.
7. **Triple-Metric Stability Requirements:** System stability requires the simultaneous management of the `angle` (tilt), `ang_vel` (rotation speed), and $y\_vel$ (descent speed).
8. **Main Engine Torque Coupling:** Even at small non-zero `angle` values, the main engine (Action 2) generates unintended torque, causing changes in `ang_vel`.
9. **Phase-Dependent Main Engine Rewards:** The main engine (Action 2) reward is highly dependent on the flight phase, providing substantial positive rewards during descent or stable contact while potentially incurring heavy penalties during unstable phases.
10. **Contact-State Volatility and Crash Penalties:** Upon ground contact, the reward signal becomes extremely volatile; engine actions can trigger rapid swings between large positive rewards (for stabilization) or catastrophic terminal penalties (up to -100.0) signifying a crash.

---

## 2026-07-10 12:49:11

---


---

## 2026-07-10 12:52:00

1. Main engine (Action 2) provides vertical thrust to counteract downward vertical velocity (`y_vel`).
2. Side engines (Actions 1 and 3) provide torque to control orientation (`angle`) and angular velocity (`ang_vel`).
3. Action 1 increases `ang_vel` whereas Action 3 decreases it, providing the mechanism for rotational correction.
4. Leg contact is a binary state (`left_leg_contact`, `right_leg_contact`) that transitions from 0.0 to 1.0 upon impact.
5. Successful landings with low vertical and angular velocities result in significant positive rewards.
6. High-velocity impacts or high angular momentum during contact trigger severe negative penalties.
7. Horizontal velocity (`x_vel`) causes lateral movement, and the lander can start with significant existing horizontal or vertical momentum.
8. Main engine thrust (Action 2) can induce secondary angular velocity (`ang_vel`) when the lander's `angle` is not zero.
9. Angular velocity (`ang_vel`) must be actively stabilized to prevent it from reaching levels that trigger crash penalties.
10. Engine-applied actions immediately influence the subsequent linear and angular velocities in the next state.

---

## 2026-07-10 12:53:19

1. Main engine (Action 2) provides vertical thrust to counteract downward vertical velocity (`y_vel`).
2. Side engines (Actions 1 and 3) provide torque to control orientation (`angle`) and angular velocity (`ang_vel`).
3. The torque applied by side engines is orientation-dependent, meaning the sign of the resulting change in `ang_vel` depends on the current `angle`.
4. Leg contact is a binary state (`left_leg_contact`, `right_leg_contact`) that transitions from 0.0 to 1.0 upon impact.
5. Successful landings require the simultaneous minimization of `y_vel`, `ang_vel`, and `angle` at the moment of contact.
6. The episode may continue after leg contact is detected, but high angular or vertical velocities during or immediately after contact trigger severe penalties and termination.
7. Horizontal velocity (`x_vel`) drives lateral movement across the landing area.
8. Main engine thrust (Action 2) induces secondary angular velocity (`ang_vel`) whenever the lander's `angle` is non-zero.
9. High angular velocity (`ang_vel`) during the contact phase is a primary driver of high-magnitude failure penalties.
10. Engine-applied actions immediately influence the subsequent linear and angular velocities in the next state.

---

## 2026-07-10 12:55:57

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
