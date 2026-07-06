
---

## 2026-07-05 12:26:26

1. **Gravity and Descent Dynamics**: Gravity continuously pulls the lander downward, evidenced by the increasing negative vertical velocity ($y\_vel$) when thrust is insufficient or absent.
2. **Rotational Sensitivity**: The lander's orientation (angle) is highly sensitive to angular velocity; small deviations rapidly escalate into extreme, unrecoverable tilts.
3. **Main Engine (Action 2) Impact**: While the main engine provides vertical thrust, over-reliance on it without stabilizing rotation causes significant angular instability and tumbling.
4. **Side Engine (Actions 1 & 3) Impact**: Side engines are essential for controlling the angle and lateral movement, but improper sequencing can lead to excessive horizontal drift ($x\_vel$).
5. **Action 0 (Nothing) Risk**: Selecting "nothing" during periods of high angular velocity or high descent speed allows momentum to accelerate the lander toward a crash.
6. **Failure Mode - Terminal Tumble**: Both episodes failed due to a "tumble" where the angle reached extreme values (e.g., -4.5 in Episode 1), making a level landing impossible.
7. **Failure Mode - Lateral Drift**: Episode 2 demonstrates that uncontrolled lateral velocity ($x\_vel$ reaching >2.0) prevents the lander from staying within a safe landing zone.
8. **Failure Mode - Velocity Overshoot**: In both trajectories, the vertical velocity becomes too high to counteract, leading to high-impact failure.
9. **Critical Moment (Episode 1)**: Between steps 40 and 60, the lander fails to stabilize its angle, leading to a progressive and catastrophic rotation.
10. **Critical Moment (Episode 2)**: After step 45, the cumulative effect of side engine usage and main engine thrust fails to correct the increasing tilt and lateral momentum.

---

## 2026-07-05 12:33:31

1. **Gravity and Descent Dynamics**: Gravity continuously decreases vertical velocity ($y\_vel$); without sufficient main engine thrust (Action 2), the lander's descent speed accelerates toward terminal impact.
2. **Rotational Momentum and Rate of Change**: The orientation ($angle$) is the integral of angular velocity ($ang\_vel$); high $|ang\_vel|$ causes the $angle$ to change so rapidly that side engines cannot compensate before the lander reaches extreme tilts.
3. **Main Engine (Action 2) Torque**: While Action 2 primarily increases $y\_vel$ to counter gravity, applying it while the lander has a non-zero $angle$ induces significant rotational torque, exacerbating angular instability.
4. **Right Engine (Action 3) Effects**: Action 3 induces negative angular velocity (clockwise rotation) and increases positive lateral velocity ($x\_vel$).
5. **Left Engine (Action 1) Effects**: Action 1 induces positive angular velocity (counter-clockwise rotation), serving as the primary mechanism to counteract negative $ang\_vel$.
6. **Action 0 (Nothing) Momentum Risk**: Selecting Action 0 during descent or rotation allows gravity, lateral momentum, and angular momentum to accumulate unchecked, making recovery harder in subsequent steps.
7. **Tilt-Thrust Coupling**: There is a critical coupling between $angle$ and thrust efficiency; as the tilt increases, the main engine's ability to provide purely vertical lift decreases, instead contributing to horizontal drift and rotation.
8. **Lateral Velocity Accumulation**: Excessive use of side engines (Actions 1 and 3) to correct tilt can lead to high lateral velocity ($x\_vel$), causing the lander to drift outside of a safe landing zone.
9. **Angular Velocity Runaway**: Once $|ang\_vel|$ exceeds a critical threshold, the rotational acceleration becomes too high for the side engines to arrest, leading to a "terminal tumble" where the $angle$ reaches extreme values.
10. **Impact Instability**: High angular velocity at the moment of leg contact (transition to $left\_leg\_contact$ or $right\_leg\_contact = 1.0$) results in immediate catastrophic failure due to the lander's inability to maintain a level orientation upon landing.

---

## 2026-07-05 12:39:05

1. **Gravity and Descent Dynamics**: Gravity continuously decreases vertical velocity ($y\_vel$); without sufficient main engine thrust (Action 2), the lander's descent speed accelerates toward terminal impact.
2. **Rotational Momentum and Rate of Change**: Orientation ($angle$) is the integral of angular velocity ($ang\_vel$); high $|ang\_vel|$ causes the $angle$ to change rapidly, making orientation control difficult.
3. **Main Engine (Action 2) Torque**: Applying Action 2 while the lander has a non-zero $angle$ induces rotational torque, which can either counteract or exacerbate angular instability depending on the tilt direction.
4. **Right Engine (Action 3) Effects**: Action 3 induces negative angular velocity (clockwise rotation) and increases positive lateral velocity ($x\_vel$).
5. **Left Engine (Action 1) Effects**: Action 1 induces positive angular velocity (counter-clockwise rotation) and increases negative lateral velocity ($x\_vel$).
6. **Action 0 (Nothing) Momentum Risk**: Selecting Action 0 allows gravity, lateral momentum, and angular momentum to accumulate unchecked, reducing the window for successful recovery.
7. **Tilt-Thrust Coupling**: As the $angle$ increases, the main engine's thrust vector becomes less vertical, contributing to horizontal drift ($x\_vel$) and increasing rotational instability.
8. **Lateral Velocity Accumulation**: Frequent use of side engines (Actions 1 and 3) to correct tilt leads to high lateral velocity ($x\_vel$), causing the lander to drift horizontally away from the landing zone.
9. **Rotational Feedback Runaway**: If a side engine is used in a direction that matches the current sign of $ang\_vel$ (e.g., using Action 3 when $ang\_vel < 0$), it creates a positive feedback loop that accelerates the rotation, leading to an unrecoverable "terminal tumble."
10. **Impact Instability**: High $|ang\_vel|$ or extreme $angle$ values at the moment of leg contact (transition to $left\_leg\_contact$ or $right\_leg\_contact = 1.0$) result in immediate catastrophic failure.

---

## 2026-07-05 12:48:24

1. **Gravity and Descent Dynamics**: Gravity continuously accelerates the lander downward (decreases $y\_vel$); the main engine (Action 2) is the primary tool for counteracting this descent and preventing terminal impact.
2. **Rotational Momentum and Rate of Change**: Orientation ($angle$) is the integral of angular velocity ($ang\_vel$); high $|ang\_vel|$ causes rapid changes in orientation, making stabilized descent difficult.
3. **Main Engine (Action 2) Torque**: Applying Action 2 while the lander has a non-zero $angle$ induces rotational torque, which can either correct or exacerbate angular instability depending on the tilt direction.
4. **Right Engine (Action 3) Effects**: Action 3 induces clockwise rotation (negative $ang\_vel$) and modifies lateral velocity ($x\_vel$).
5. **Left Engine (Action 1) Effects**: Action 1 induces counter-clockwise rotation (positive $ang\_vel$) and modifies lateral velocity ($x\_vel$).
6. **Action 0 (Nothing) Momentum Risk**: Selecting Action 0 allows gravity, lateral momentum, and angular momentum to accumulate unchecked, reducing the window for successful recovery.
7. **Side-Engine Vertical Coupling**: When the lander is tilted ($angle \neq 0$), the thrust from side engines (Actions 1 and 3) produces a vertical component; depending on the tilt magnitude and direction, this can either slightly assist or significantly accelerate the descent rate ($y\_vel$).
8. **Lateral Velocity Accumulation**: Frequent use of side engines (Actions 1 and 3) to correct tilt leads to high lateral velocity ($x\_vel$), causing the lander to drift horizontally away from the landing zone.
9. **Rotational Feedback Runaway**: If a side engine is used in a direction that matches the current sign of $ang\_vel$ (e.g., using Action 3 when $ang\_vel < 0$), it creates a positive feedback loop that accelerates rotation into a "terminal tumble."
10. **Impact Instability**: High $|ang\_vel|$ or extreme $angle$ values at the moment of leg contact (transition to $left\_leg\_contact$ or $right\_leg\_contact = 1.0$) result in immediate catastrophic failure.

---

## 2026-07-05 12:52:10

1. **Gravity and Descent Dynamics**: Gravity provides constant downward acceleration; the main engine (Action 2) is the primary tool to counteract $y\_vel$ and prevent high-velocity terminal impact.
2. **Rotational Momentum and Orientation**: Orientation ($angle$) is the integral of angular velocity ($ang\_vel$); high $|ang\_vel|$ causes rapid changes in orientation, making stabilized descent difficult.
3. **Main Engine Rotational Torque**: Applying Action 2 while the lander has a non-zero $angle$ induces rotational torque, which can either correct or exacerbate angular instability depending on the tilt direction.
4. **Side-Engine Rotational Directionality**: Action 1 (Left Engine) induces counter-clockwise rotation (positive $ang\_vel$), while Action 3 (Right Engine) induces clockwise rotation (negative $ang\_vel$).
5. **Side-Engine Vertical Coupling**: When the lander is tilted ($angle \neq 0$), thrust from side engines (Actions 1 and 3) produces a vertical component that can either assist or significantly accelerate the descent rate ($y\_vel$).
6. **Lateral Velocity Accumulation**: Frequent use of side engines (Actions 1 and 3) to correct tilt leads to high lateral velocity ($x\_vel$), causing the lander to drift horizontally away from the landing zone.
7. **Rotational Feedback Runaway**: Using a side engine in a direction that matches the current sign of $ang\_vel$ (e.g., Action 3 when $ang\_vel < 0$) creates a positive feedback loop that accelerates rotation into a "terminal tumble."
8. **Action 0 Momentum Risk**: Selecting Action 0 allows gravity, lateral momentum, and angular momentum to accumulate unchecked, reducing the window for successful recovery.
9. **Critical Descent Velocity**: High magnitude downward velocity ($|y\_vel|$) is a primary failure mode; a crash can occur due to excessive descent speed even if the lander's orientation ($angle$) is successfully stabilized near zero.
10. **Multi-Constraint Impact Stability**: Successful landing requires that $|angle|$, $|ang\_vel|$, and $|y\_vel|$ all remain within safe, low-magnitude thresholds simultaneously at the moment of leg contact.

---

## 2026-07-05 12:56:05

1. **Gravity and Descent Dynamics**: Gravity exerts a constant downward acceleration; the main engine (Action 2) is the primary mechanism to counteract $y\_vel$ and prevent high-velocity terminal impacts.
2. **Rotational Momentum and Orientation**: Orientation ($angle$) is the integral of angular velocity ($ang\_vel$); high $|ang\_vel|$ leads to rapid, difficult-to-correct changes in orientation.
3. **Main Engine Rotational Torque**: Applying the main engine (Action 2) while the lander has a non-zero $angle$ induces rotational torque, which can either assist or exacerbate angular instability depending on the tilt direction.
4. **Side-Engine Rotational Directionality**: Action 1 (Left Engine) induces counter-clockwise rotation (positive $ang\_vel$), while Action 3 (Right Engine) induces clockwise rotation (negative $ang\_vel$).
5. **Side-Engine Velocity Coupling**: When the lander is tilted ($angle \neq 0$), side-engine thrust (Actions 1 and 3) is not purely lateral; it produces a vertical component that can significantly accelerate the descent rate ($y\_vel$).
6. **Lateral Velocity Accumulation**: Frequent or aggressive use of side engines (Actions 1 and 3) to manage rotation causes the accumulation of lateral velocity ($x\_vel$), leading to horizontal drift away from the landing site.
7. **Rotational Feedback Runaway**: Selecting a side engine that matches the current sign of $ang\_vel$ (e.g., Action 3 when $ang\_vel < 0$) creates a positive feedback loop that accelerates the lander into a terminal tumble.
8. **Action 0 Momentum Risk**: Selecting Action 0 (no thrust) allows gravity, lateral momentum, and angular momentum to accumulate unchecked, rapidly narrowing the window for successful recovery.
9. **Critical Descent Velocity**: High magnitude downward velocity ($|y\_vel|$) is a primary failure mode; excessive descent speed at the moment of contact results in a crash regardless of orientation.
10. **Multi-Constraint Impact Stability**: A successful landing requires that $|angle|$, $|ang\_vel|$, and $|y\_vel|$ all remain within low-magnitude thresholds simultaneously at the moment of leg contact.

---

## 2026-07-05 13:00:24

1. **Gravity and Descent Dynamics**: Gravity exerts a constant downward acceleration; the main engine (Action 2) is the primary mechanism to counteract $y\_vel$ and prevent high-velocity terminal impacts.
2. **Rotational Momentum and Orientation**: Orientation ($angle$) is the integral of angular velocity ($ang\_vel$); high $|ang\_vel|$ leads to rapid, difficult-to-correct changes in orientation.
3. **Main Engine Rotational Torque**: Applying the main engine (Action 2) while the lander has a non-zero $angle$ induces rotational torque, which can exacerbate angular instability depending on the tilt direction.
4. **Side-Engine Rotational Directionality**: Action 1 (Left Engine) induces counter-clockwise rotation (positive $ang\_vel$), while Action 3 (Right Engine) induces clockwise rotation (negative $ang\_vel$).
5. **Side-Engine Velocity Coupling**: When the lander is tilted ($angle \neq 0$), side-engine thrust (Actions 1 and 3) produces a vertical component that can significantly influence the descent rate ($y\_vel$), either accelerating or decelerating the fall.
6. **Lateral Velocity Accumulation**: Frequent or aggressive use of side engines (Actions 1 and 3) to manage rotation causes the accumulation of lateral velocity ($x\_vel$), leading to horizontal drift away from the landing site.
7. **Rotational Feedback Runaway**: Selecting a side engine that matches the current sign of $ang\_vel$ (e.g., Action 3 when $ang\_vel < 0$) creates a positive feedback loop that accelerates the lander into a terminal tumble.
8. **Terminal Tumble Dominance**: Once $angle$ or $ang\_vel$ reaches high magnitudes (as seen in Episode 2), the rotational momentum can become so dominant that standard engine actions are insufficient to stabilize the lander's orientation before impact.
9. **Action 0 Momentum Risk**: Selecting Action 0 (no thrust) allows gravity, lateral momentum, and angular momentum to accumulate unchecked, rapidly narrowing the window for successful recovery.
10. **Multi-Constraint Impact Stability**: A successful landing requires that $|angle|$, $|ang\_vel|$, and $|y\_vel|$ all remain within low-magnitude thresholds simultaneously at the moment of leg contact (whether single or dual-leg contact occurs).

---

## 2026-07-05 13:05:42

1. **Gravity and Vertical Velocity**: Gravity exerts a constant downward acceleration; the main engine (Action 2) is the primary mechanism to counteract $y\_vel$ and mitigate high-velocity impacts.
2. **Angular Kinematics**: Orientation ($angle$) is the integral of angular velocity ($ang\_vel$); high $|ang\_vel|$ causes rapid orientation changes that can quickly move the lander into uncontrollable regimes.
3. **Main Engine Induced Torque**: Applying the main engine (Action 2) when the lander is tilted ($angle \neq 0$) induces rotational torque, which can complicate the management of $ang\_vel$ and exacerbate instability.
4. **Side-Engine Rotational Directionality**: Action 1 (Left Engine) induces counter-clockwise rotation (positive $ang\_vel$), while Action 3 (Right Engine) induces clockwise rotation (negative $ang\_vel$).
5. **Asymmetric Thrust Coupling**: When the lander is tilted, side-engine thrust (Actions 1 and 3) produces a vertical component that can significantly influence the descent rate ($y\_vel$), either accelerating or decelerating the fall depending on the tilt direction.
6. **Lateral Velocity Accumulation**: Frequent use of side engines (Actions 1 and 3) to manage rotation causes the accumulation of lateral velocity ($x\_vel$), leading to horizontal drift away from the landing site.
7. **Rotational Feedback Runaway**: Selecting a side engine that matches the current sign of $ang\_vel$ (e.g., Action 3 when $ang\_vel < 0$) creates a positive feedback loop that accelerates the lander into a terminal tumble.
8. **Momentum Dominance**: Once $|angle|$ or $|ang\_vel|$ reaches high magnitudes, the rotational momentum can become so dominant that individual engine actions are insufficient to stabilize the orientation before contact occurs.
9. **Action 0 Momentum Risk**: Selecting Action 0 (no thrust) allows gravity, lateral momentum, and angular momentum to accumulate unchecked, rapidly narrowing the window for successful recovery.
10. **Multi-Constraint Contact Stability**: A successful landing requires that $|angle|$, $|ang\_vel|$, and $|y\_vel|$ all remain within low-magnitude thresholds simultaneously at the moment of leg contact; contact with high $|y\_vel|$ or $|ang\_vel|$ results in failure regardless of leg contact status.

---

## 2026-07-05 13:09:54

1. **Gravity and Vertical Velocity**: Gravity provides a constant downward acceleration; while the main engine (Action 2) is the primary mechanism to counteract $y\_vel$, it must be applied with sufficient frequency and magnitude to prevent high-velocity impacts that exceed stability thresholds.
2. **Angular Kinematics**: The lander's $angle$ is the integral of its $ang\_vel$; high $|ang\_vel|$ causes rapid orientation changes that can quickly move the lander into extreme tilt regimes.
3. **Main Engine Induced Torque**: Applying the main engine (Action 2) when the lander is tilted ($angle \neq 0$) induces rotational torque, which modifies $ang\_vel$ and can exacerbate angular instability.
4. **Side-Engine Rotational Directionality**: Action 1 (Left Engine) induces counter-clockwise rotation (positive $ang\_vel$), while Action 3 (Right Engine) induces clockwise rotation (negative $ang\_vel$).
5. **Asymmetric Thrust Coupling**: When the lander is tilted, side-engine thrust (Actions 1 and 3) produces a vertical component that influences $y\_vel$; depending on the tilt direction, this can either assist in deceleration or inadvertently accelerate the descent rate.
6. **Lateral Velocity Accumulation**: Frequent use of side engines (Actions 1 and 3) to manage rotation causes the accumulation of lateral velocity ($x\_vel$), leading to horizontal drift away from the landing site.
7. **Rotational Feedback Runaway**: Selecting a side engine that matches the current sign of $ang\_vel$ (e.g., Action 3 when $ang\_vel < 0$) creates a positive feedback loop that accelerates the lander into an uncontrollable tumble.
8. **Momentum Dominance**: Once $|angle|$ or $|ang\_vel|$ reaches high magnitudes, the rotational momentum can become so dominant that the available engine thrust is insufficient to stabilize the orientation before ground contact occurs.
9. **Action 0 Momentum Risk**: Selecting Action 0 (no thrust) allows gravity, lateral momentum, and angular momentum to accumulate unchecked, rapidly narrowing the window for successful recovery.
10. **Multi-Constraint Contact Stability**: A successful landing requires that $|angle|$, $|ang\_vel|$, and $|y\_vel|$ all remain within low-magnitude thresholds simultaneously at the moment of leg contact; even a nominally upright lander ($angle \approx 0$) will result in failure if $|y\_vel|$ or $|ang\_vel|$ are too high upon impact.

---

## 2026-07-05 13:15:28

1. **Gravity and Vertical Velocity**: Gravity provides a constant downward acceleration; the main engine (Action 2) is the primary mechanism to counteract $y\_vel$, but it must be applied with sufficient frequency and magnitude to prevent the descent rate from reaching critical impact thresholds.
2. **Angular Kinematics**: The lander's $angle$ is the integral of its $ang\_vel$; high $|ang\_vel|$ causes rapid orientation changes that can quickly move the lander into extreme tilt regimes.
3. **Main Engine Induced Torque**: Applying the main engine (Action 2) when the lander is tilted ($angle \neq 0$) induces rotational torque, which modifies $ang\_vel$ and can exacerbate angular instability.
4. **Side-Engine Rotational Directionality**: Action 1 (Left Engine) induces counter-clockwise rotation (positive $ang\_vel$), while Action 3 (Right Engine) induces clockwise rotation (negative $ang\_vel$).
5. **Asymmetric Thrust Coupling**: When the lander is tilted, side-engine thrust (Actions 1 and 3) produces a vertical component that influences $y\_vel$; depending on the tilt direction, this can either assist in deceleration or inadvertently accelerate the descent rate.
6. **Lateral Velocity Accumulation**: Frequent or excessive use of side engines (Actions 1 and 3) to manage rotation causes the accumulation of lateral velocity ($x\_vel$), leading to significant horizontal drift.
7. **Rotational Feedback Runaway**: Selecting a side engine that matches the current sign of $ang\_vel$ (e.g., Action 3 when $ang\_vel < 0$) creates a positive feedback loop that accelerates the lander into an uncontrollable tumble.
8. **Momentum Dominance**: Once $|angle|$, $|ang\_vel|$, or $|y\_vel|$ reaches high magnitudes, the existing momentum can exceed the maximum corrective capability of the available engine thrust, making stabilization impossible regardless of subsequent actions.
9. **Action 0 Momentum Risk**: Selecting Action 0 (no thrust) allows gravity, lateral momentum, and angular momentum to accumulate unchecked, rapidly narrowing the window for successful recovery.
10. **Multi-Constraint Contact Stability**: A successful landing requires $|angle|$, $|ang\_vel|$, and $|y\_vel|$ to all remain within low-magnitude thresholds simultaneously at the moment of leg contact; trajectory data indicates that high downward velocity ($|y\_vel| \gtrsim 1.5$) is a primary cause of failure even when the lander is relatively upright.

---

## 2026-07-05 13:19:57

1. **Gravity and Vertical Velocity**: Gravity provides a constant downward acceleration; the main engine (Action 2) is the primary mechanism to counteract $y\_vel$, but it must be applied with sufficient frequency and magnitude to prevent the descent rate from reaching critical impact thresholds.
2. **Angular Kinematics**: The lander's $angle$ is the integral of its $ang\_vel$; high $|ang\_vel|$ causes rapid orientation changes that can quickly move the lander into extreme tilt regimes.
3. **Main Engine Induced Torque**: Applying the main engine (Action 2) when the lander is tilted ($angle \neq 0$) induces rotational torque, which modifies $ang\_vel$ and can exacerbate angular instability.
4. **Side-Engine Rotational Directionality**: Action 1 (Left Engine) induces counter-clockwise rotation (positive $ang\_vel$), while Action 3 (Right Engine) induces clockwise rotation (negative $ang\_vel$).
5. **Asymmetric Thrust Coupling**: When the lander is tilted, side-engine thrust (Actions 1 and 3) produces a vertical component that influences $y\_vel$; depending on the tilt direction, this can either assist in deceleration or inadvertently accelerate the descent rate.
6. **Lateral Velocity Accumulation**: Frequent or excessive use of side engines (Actions 1 and 3) to manage rotation causes the accumulation of lateral velocity ($x\_vel$), leading to significant horizontal drift.
7. **Rotational Feedback Runaway**: Selecting a side engine that matches the current sign of $ang\_vel$ (e.g., Action 1 when $ang\_vel > 0$ or Action 3 when $ang\_vel < 0$) creates a positive feedback loop that accelerates the lander into an uncontrollable tumble.
8. **Momentum Dominance**: Once $|angle|$, $|ang\_vel|$, or $|y\_vel|$ reaches high magnitudes, the existing momentum can exceed the maximum corrective capability of the available engine thrust, making stabilization impossible regardless of subsequent actions.
9. **Action 0 Momentum Risk**: Selecting Action 0 (no thrust) allows gravity, lateral momentum, and angular momentum to accumulate unchecked, rapidly narrowing the window for successful recovery.
10. **Multi-Constraint Contact Stability**: A successful landing requires $|angle|$, $|ang\_vel|$, and $|y\_vel|$ to all remain within low-magnitude thresholds simultaneously at the moment of leg contact; failure is highly correlated with descent rates $|y\_vel| \gtrsim 1.2$ or significant tilt $|angle| \gtrsim 0.2$ at the point of impact.

---

## 2026-07-05 13:23:42

1. **Gravity and Vertical Velocity**: Gravity provides a constant downward acceleration; the main engine (Action 2) is the primary mechanism to counteract $y\_vel$, but it must be applied with sufficient frequency and magnitude to prevent the descent rate from reaching critical impact thresholds.
2. **Angular Kinematics**: The lander's $angle$ is the integral of its $ang\_vel$; high $|ang\_vel|$ causes rapid orientation changes that can quickly move the lander into extreme tilt regimes.
3. **Main Engine Induced Torque**: Applying the main engine (Action 2) when the lander is tilted ($angle \neq 0$) induces rotational torque, which modifies $ang\_vel$ and can exacerbate angular instability.
4. **Side-Engine Rotational Directionality**: Action 1 (Left Engine) induces counter-clockwise rotation (positive $ang\_vel$), while Action 3 (Right Engine) induces clockwise rotation (negative $ang\_vel$).
5. **Asymmetric Thrust Coupling**: When the lander is tilted, side-engine thrust (Actions 1 and 3) produces a vertical component that influences $y\_vel$; depending on the tilt direction, this can either assist in deceleration or inadvertently accelerate the descent rate.
6. **Lateral Velocity Accumulation**: Frequent or excessive use of side engines (Actions 1 and 3) to manage rotation causes the accumulation of lateral velocity ($x\_vel$), leading to significant horizontal drift ($x\_pos$ displacement).
7. **Rotational Feedback Runaway**: Selecting a side engine that matches the current sign of $ang\_vel$ (e.g., Action 1 when $ang\_vel > 0$ or Action 3 when $ang\_vel < 0$) creates a positive feedback loop that accelerates the lander into an uncontrollable tumble.
8. **Momentum Dominance**: Once $|angle|$, $|ang\_vel|$, or $|y\_vel|$ reaches high magnitudes, the existing momentum can exceed the maximum corrective capability of the available engine thrust, making stabilization impossible regardless of subsequent actions.
9. **Action 0 Momentum Risk**: Selecting Action 0 (no thrust) allows gravity, lateral momentum, and angular momentum to accumulate unchecked, rapidly narrowing the window for successful recovery.
10. **Landing Stability Thresholds**: Successful landing requires $|angle|$, $|ang\_vel|$, and $|y\_vel|$ to all remain within low-magnitude thresholds simultaneously at the moment of leg contact; recent failures demonstrate that descent rates $|y\_vel| \gtrsim 1.1$ at impact are highly likely to result in failure, even when the lander's orientation ($angle$) is relatively stable.

---

## 2026-07-05 13:28:04

1. **Gravity and Vertical Velocity**: Gravity provides a constant downward acceleration; the main engine (Action 2) is the primary mechanism to counteract $y\_vel$, but it must be applied with sufficient frequency and magnitude to prevent the descent rate from reaching critical impact thresholds.
2. **Angular Kinematics**: The lander's $angle$ is the integral of its $ang\_vel$; high $|ang\_vel|$ causes rapid orientation changes that can quickly move the lander into extreme tilt regimes.
3. **Main Engine Induced Torque**: Applying the main engine (Action 2) when the lander is tilted ($angle \neq 0$) induces rotational torque, which modifies $ang\_vel$ and can exacerbate angular instability.
4. **Side-Engine Rotational Directionality**: Action 1 (Left Engine) induces counter-clockwise rotation (positive $ang\_vel$), while Action 3 (Right Engine) induces clockwise rotation (negative $ang\_vel$).
5. **Asymmetric Thrust Coupling**: When the lander is tilted, side-engine thrust (Actions 1 and 3) produces a vertical component that influences $y\_vel$; depending on the tilt direction, this can either assist in deceleration or inadvertently accelerate the descent rate.
6. **Lateral Velocity Accumulation**: Frequent or excessive use of side engines (Actions 1 and 3) to manage rotation causes the accumulation of lateral velocity ($x\_vel$), leading to significant horizontal drift ($x\_pos$ displacement).
7. **Rotational Feedback Runaway**: Selecting a side engine that matches the current sign of $ang\_vel$ (e.g., Action 1 when $ang\_vel > 0$ or Action 3 when $ang\_vel < 0$) creates a positive feedback loop that accelerates the lander into an uncontrollable tumble.
8. **Momentum Dominance**: Once $|angle|$, $|ang\_vel|$, or $|y\_vel|$ reaches high magnitudes, the existing momentum can exceed the maximum corrective capability of the available engine thrust, making stabilization impossible regardless of subsequent actions.
9. **Action 0 Momentum Risk**: Selecting Action 0 (no thrust) allows gravity, lateral momentum, and angular momentum to accumulate unchecked, rapidly narrowing the window for successful recovery.
10. **Landing Stability and Post-Contact Constraints**: Successful landing requires $|angle|$, $|ang\_vel|$, and $|y\_vel|$ to be minimized at the moment of leg contact; descent rates $|y\_vel| \gtrsim 1.0$ at impact are highly likely to result in failure. Furthermore, applying any engine thrust (Actions 1, 2, or 3) once leg contact has been established ($leg\_contact \ge 1.0$) results in immediate catastrophic failure and massive negative rewards.

---

## 2026-07-05 13:32:48

1. **Gravity and Vertical Velocity**: Gravity provides a constant downward acceleration; the main engine (Action 2) is the primary mechanism to counteract $y\_vel$, but it must be applied with sufficient frequency and magnitude to prevent the descent rate from reaching critical impact thresholds.
2. **Angular Kinematics**: The lander's $angle$ is the integral of its $ang\_vel$; high $|ang\_vel|$ causes rapid orientation changes that can quickly move the lander into extreme tilt regimes.
3. **Main Engine Induced Torque**: Applying the main engine (Action 2) when the lander is tilted ($angle \neq 0$) induces rotational torque, which modifies $ang\_vel$ and can exacerbate angular instability.
4. **Side-Engine Rotational Directionality**: Action 1 (Left Engine) induces counter-clockwise rotation (positive $ang\_vel$), while Action 3 (Right Engine) induces clockwise rotation (negative $ang\_vel$).
5. **Asymmetric Thrust and Torque Amplification**: Side-engine thrust (Actions 1 and 3) produces a vertical component that influences $y\_vel$ and a rotational component that modifies $ang\_vel$; the magnitude of both the vertical lift and the induced torque is significantly amplified as the $|angle|$ increases.
6. **Lateral Velocity Accumulation**: Frequent or excessive use of side engines (Actions 1 and 3) to manage rotation causes the accumulation of lateral velocity ($x\_vel$), leading to significant horizontal drift ($x\_pos$ displacement).
7. **Rotational Feedback Runaway**: Selecting a side engine that matches the current sign of $ang\_vel$ (e.g., Action 1 when $ang\_vel > 0$ or Action 3 when $ang\_vel < 0$) creates a positive feedback loop that accelerates the lander into an uncontrollable tumble.
8. **Momentum Dominance**: Once $|angle|$, $|ang\_vel|$, or $|y\_vel|$ reaches high magnitudes, the existing momentum can exceed the maximum corrective capability of the available engine thrust, making stabilization impossible regardless of subsequent actions.
9. **Action 0 Momentum Risk**: Selecting Action 0 (no thrust) allows gravity, lateral momentum, and angular momentum to accumulate unchecked, rapidly narrowing the window for successful recovery.
10. **Landing Stability and Post-Contact Constraints**: Successful landing requires minimizing $|angle|$, $|ang\_vel|$, and $|y\_vel|$ at impact; catastrophic failure occurs if $y\_pos$ drops below zero or if any engine thrust (Actions 1, 2, or 3) is applied while both legs are in contact ($leg\_contact = [1.0, 1.0]$).

---

## 2026-07-05 13:37:17

1. **Gravity and Vertical Velocity**: Gravity provides a constant downward acceleration; the main engine (Action 2) is the primary mechanism to counteract $y\_vel$, but it must be applied with sufficient frequency and magnitude to prevent the descent rate from reaching critical impact thresholds.
2. **Angular Kinematics**: The lander's $angle$ is the integral of its $ang\_vel$; high $|ang\_vel|$ causes rapid orientation changes that can quickly move the lander into extreme tilt regimes.
3. **Main Engine Induced Torque**: Applying the main engine (Action 2) when the lander is tilted ($angle \neq 0$) induces rotational torque, which modifies $ang\_vel$ and can exacerbate angular instability.
4. **Side-Engine Rotational Directionality**: Action 1 (Left Engine) induces counter-clockwise rotation (positive $ang\_vel$), while Action 3 (Right Engine) induces clockwise rotation (negative $ang\_vel$).
5. **Asymmetric Thrust and Torque Amplification**: Side-engine thrust (Actions 1 and 3) produces a vertical component that influences $y\_vel$ and a rotational component that modifies $ang\_vel$; the magnitude of both the vertical lift and the induced torque is significantly amplified as the $|angle|$ increases.
6. **Lateral Velocity and Angular Coupling**: The use of side engines (Actions 1 and 3) modifies lateral velocity ($x\_vel$), where the direction of the resulting horizontal drift is coupled to the current $angle$.
7. **Rotational Feedback Runaway**: Selecting a side engine that matches the current sign of $ang\_vel$ (e.g., Action 1 when $ang\_vel > 0$ or Action 3 when $ang\_vel < 0$) creates a positive feedback loop that accelerates the lander into an uncontrollable tumble.
8. **Momentum Dominance**: Once $|angle|$, $|ang\_vel|$, or $|y\_vel|$ reaches high magnitudes, the existing momentum can exceed the maximum corrective capability of the available engine thrust, making stabilization impossible regardless of subsequent actions.
9. **Action 0 Momentum Risk**: Selecting Action 0 (no thrust) allows gravity, lateral momentum, and angular momentum to accumulate unchecked, rapidly narrowing the window for successful recovery.
10. **Landing Stability and Post-Contact Constraints**: Successful landing requires minimizing $|angle|$, $|ang\_vel|$, and $|y\_vel|$ at impact; catastrophic failure occurs if $y\_pos$ drops below zero or if any engine thrust (Actions 1, 2, or 3) is applied while both legs are in contact ($leg\_contact = [1.0, 1.0]$).

---

## 2026-07-05 13:40:30

1. **Gravity and Vertical Velocity**: Gravity provides a constant downward acceleration; the main engine (Action 2) is the primary mechanism to counteract $y\_vel$, but it must be applied with sufficient frequency and magnitude to prevent the descent rate from reaching critical impact thresholds.
2. **Angular Kinematics**: The lander's $angle$ is the integral of its $ang\_vel$; high $|ang\_vel|$ causes rapid orientation changes that can quickly move the lander into extreme tilt regimes.
3. **Main Engine Induced Torque**: Applying the main engine (Action 2) when the lander is tilted ($angle \neq 0$) induces rotational torque, which modifies $ang\_vel$ and can exacerbate angular instability.
4. **Side-Engine Rotational Directionality**: Action 1 (Left Engine) induces counter-clockwise rotation (positive $ang\_vel$), while Action 3 (Right Engine) induces clockwise rotation (negative $ang\_vel$).
5. **Asymmetric Thrust and Torque Amplification**: Side-engine thrust (Actions 1 and 3) produces a vertical component that influences $y\_vel$ and a rotational component that modifies $ang\_vel$; the magnitude of both the vertical lift and the induced torque is significantly amplified as the $|angle|$ increases.
6. **Lateral Velocity and Angular Coupling**: The use of side engines (Actions 1 and 3) modifies lateral velocity ($x\_vel$), where the direction of the resulting horizontal drift is coupled to the current $angle$.
7. **Rotational Feedback Runaway**: Selecting a side engine that matches the current sign of $ang\_vel$ (e.g., Action 1 when $ang\_vel > 0$ or Action 3 when $ang\_vel < 0$) creates a positive feedback loop that accelerates the lander into an uncontrollable tumble.
8. **Momentum Dominance**: Once $|angle|$, $|ang\_vel|$, or $|y\_vel|$ reaches high magnitudes, the existing momentum can exceed the maximum corrective capability of the available engine thrust, making stabilization impossible regardless of subsequent actions.
9. **Action 0 Momentum Risk**: Selecting Action 0 (no thrust) allows gravity, lateral momentum, and angular momentum to accumulate unchecked, rapidly narrowing the window for successful recovery.
10. **Landing Constraints and Penalty Triggers**: A catastrophic -100 reward is triggered if the main engine (Action 2) is applied while the altitude $y\_pos$ is below zero or while both legs are in contact ($leg\_contact = [1.0, 1.0]$); side engines (Actions 1 and 3) do not trigger this specific penalty when $y\_pos < 0$.

---

## 2026-07-05 13:46:25

1. **Gravity and Vertical Velocity**: Gravity provides constant downward acceleration; the main engine (Action 2) is the primary mechanism to counteract $y\_vel$, but it must be applied to prevent the altitude $y\_pos$ from dropping below zero.
2. **Angular Kinematics**: The lander's $angle$ is the integral of $ang\_vel$; high $|ang\_vel|$ causes rapid orientation changes that can quickly move the lander into extreme tilt regimes.
3. **Main Engine Induced Torque**: Applying the main engine (Action 2) when the lander is tilted ($angle \neq 0$) induces rotational torque, which modifies $ang\_vel$ and can exacerbate angular instability.
4. **Side-Engine Rotational Directionality**: Action 1 (Left Engine) induces counter-clockwise rotation (positive $ang\_vel$), while Action 3 (Right Engine) induces clockwise rotation (negative $ang\_vel$).
5. **Asymmetric Thrust and Torque Amplification**: Side-engine thrust (Actions 1 and 3) produces a vertical component that influences $y\_vel$ and a rotational component that modifies $ang\_vel$; the magnitude of the induced torque is significantly amplified as $|angle|$ increases.
6. **Lateral Velocity and Angular Coupling**: The use of side engines (Actions 1 and 3) modifies lateral velocity ($x\_vel$), where the direction of the resulting horizontal drift is coupled to the current $angle$.
7. **Rotational Feedback Runaway**: Selecting a side engine that matches the current sign of $ang\_vel$ (e.g., Action 1 when $ang\_vel > 0$ or Action 3 when $ang\_vel < 0$) creates a positive feedback loop that accelerates the lander into an uncontrollable tumble.
8. **Momentum Dominance**: Once $|angle|$, $|ang\_vel|$, or $|y\_vel|$ reaches high magnitudes, the existing momentum can exceed the maximum corrective capability of the available engine thrust, making stabilization impossible.
9. **Contact Persistence and Terminal Penalties**: Leg contact states are irreversible once they reach 1.0; a catastrophic terminal penalty (-100) is triggered when the lander's altitude $y\_pos$ is below zero and both legs are in contact.
10. **Action 0 Momentum Risk**: Selecting Action 0 (no thrust) allows gravity, lateral momentum, and angular momentum to accumulate unchecked, rapidly narrowing the window for successful recovery.

---

## 2026-07-05 13:49:44

1. **Gravity and Vertical Velocity**: Gravity provides constant downward acceleration; the main engine (Action 2) is the primary mechanism to counteract $y\_vel$ and prevent the altitude $y\_pos$ from dropping below zero.
2. **Angular Kinematics**: The lander's $angle$ is the integral of $ang\_vel$; high $|ang\_vel|$ causes rapid orientation changes that can quickly move the lander into extreme tilt regimes.
3. **Main Engine Induced Torque**: Applying the main engine (Action 2) when the lander is tilted ($angle \neq 0$) induces rotational torque, which modifies $ang\_vel$ and can exacerbate angular instability.
4. **Side-Engine Rotational Directionality**: Action 1 (Left Engine) induces counter-clockwise rotation (positive $ang\_vel$), while Action 3 (Right Engine) induces clockwise rotation (negative $ang\_vel$).
5. **Lateral-Angular Coupling**: Side-engine thrust (Actions 1 and 3) modifies lateral velocity ($x\_vel$); the direction of the resulting horizontal drift is coupled to the current $angle$ and the specific engine used.
6. **Torque-Angle Amplification**: The magnitude of the rotational torque produced by side engines is significantly amplified as the tilt $|angle|$ increases.
7. **Rotational Feedback Runaway**: Selecting a side engine that matches the current sign of $ang\_vel$ (e.g., Action 1 when $ang\_vel > 0$ or Action 3 when $ang\_vel < 0$) creates a positive feedback loop that accelerates the lander into an uncontrollable tumble.
8. **Momentum Dominance**: Once $|angle|$, $|ang\_vel|$, or $|y\_vel|$ reaches high magnitudes, the existing momentum can exceed the maximum corrective capability of the available engine thrust, making stabilization impossible.
9. **Conditional Terminal Failure**: A catastrophic terminal penalty (-100) is triggered only when the lander's altitude $y\_pos$ is below zero AND both legs are in contact; single-leg contact while $y\_pos < 0$ does not trigger immediate termination.
10. **Action 0 Momentum Accumulation**: Selecting Action 0 (no thrust) allows gravity, lateral momentum, and angular momentum to accumulate unchecked, rapidly narrowing the window for successful recovery.

---

## 2026-07-05 13:51:57

1. **Gravity and Vertical Velocity**: Gravity provides constant downward acceleration; the main engine (Action 2) is the primary mechanism to counteract $y\_vel$ and prevent the altitude $y\_pos$ from dropping below zero.
2. **Angular Kinematics**: The lander's $angle$ is the integral of $ang\_vel$; high $|ang\_vel|$ causes rapid orientation changes that can quickly move the lander into extreme tilt regimes.
3. **Main Engine Induced Torque**: Applying the main engine (Action 2) when the lander is tilted ($angle \neq 0$) induces rotational torque, which modifies $ang\_vel$ and can exacerbate angular instability.
4. **Angle-Dependent Side-Engine Torque**: While side engines (Actions 1 and 3) induce rotation, the direction of the resulting torque is coupled to the current $angle$; an engine that produces clockwise rotation at a neutral angle may produce counter-clockwise rotation at a significant tilt.
5. **Lateral-Angular Coupling**: Side-engine thrust (Actions 1 and 3) modifies lateral velocity ($x\_vel$); the direction of the resulting horizontal drift is coupled to the current $angle$ and the specific engine used.
6. **Torque-Angle Amplification**: The magnitude of the rotational torque produced by side engines is significantly amplified as the tilt $|angle|$ increases.
7. **Rotational Feedback Runaway**: Selecting a side engine that matches the current sign of $ang\_vel$ (e.g., Action 1 when $ang\_vel > 0$ or Action 3 when $ang\_vel < 0$) creates a positive feedback loop that accelerates the lander into an uncontrollable tumble.
8. **Momentum Dominance**: Once $|angle|$, $|ang\_vel|$, or $|y\_vel|$ reaches high magnitudes, the existing momentum can exceed the maximum corrective capability of the available engine thrust, making stabilization impossible.
9. **Conditional Terminal Failure**: A catastrophic terminal penalty (-100) is triggered only when the lander's altitude $y\_pos$ is below zero AND both legs are in contact; single-leg contact while $y\_pos < 0$ does not trigger immediate termination.
10. **Action 0 Momentum Accumulation**: Selecting Action 0 (no thrust) allows gravity, lateral momentum, and angular momentum to accumulate unchecked, rapidly narrowing the window for successful recovery.

---

## 2026-07-05 13:56:54

1. **Gravity and Vertical Velocity Control**: Gravity provides constant downward acceleration; the main engine (Action 2) is the primary mechanism to counteract $y\_vel$ and prevent $y\_pos$ from dropping below zero.
2. **Angular Kinematics**: The lander's $angle$ is the integral of $ang\_vel$; high $|ang\_vel|$ causes rapid orientation changes that can move the lander into extreme tilt regimes.
3. **Main Engine Induced Torque**: Applying the main engine (Action 2) when the lander is tilted ($angle \neq 0$) induces rotational torque, which modifies $ang\_vel$ and can exacerbate angular instability.
4. **Angle-Dependent Side-Engine Torque**: While side engines (Actions 1 and 3) induce rotation, the direction of the resulting torque is coupled to the current $angle$; an engine that produces clockwise rotation at a neutral angle may produce counter-clockwise rotation at a significant tilt.
5. **Lateral-Angular Coupling**: Side-engine thrust (Actions 1 and 3) modifies lateral velocity ($x\_vel$); the direction of the resulting horizontal drift is coupled to the current $angle$ and the specific engine used.
6. **Torque-Angle Amplification**: The magnitude of the rotational torque produced by side engines is significantly amplified as the tilt $|angle|$ increases.
7. **Rotational Feedback Runaway**: Selecting a side engine that matches the current sign of $ang\_vel$ (e.g., Action 1 when $ang\_vel > 0$ or Action 3 when $ang\_vel < 0$) creates a positive feedback loop that accelerates the lander into an uncontrollable tumble.
8. **Momentum Dominance**: Once $|angle|$, $|ang\_vel|$, or $|y\_vel|$ reaches high magnitudes, the existing momentum can exceed the maximum corrective capability of the available engine thrust, making stabilization impossible.
9. **Conditional Terminal Failure**: A catastrophic terminal penalty (-100) is triggered when $y\_pos < 0$ and both legs are in contact, a condition most likely to result in termination during high-velocity vertical impacts.
10. **Main Engine Recovery Capability**: The main engine (Action 2) is capable of arresting significant negative $y\_vel$ and stabilizing altitude even when the lander is at a non-zero angle or slightly below $y\_pos=0$, provided the angular momentum is not already excessive.

---

## 2026-07-05 13:58:45

1. **Vertical Velocity Control**: Gravity provides constant downward acceleration, and the main engine (Action 2) is the primary mechanism to counteract $y\_vel$ and manage descent rate to prevent high-velocity impacts.
2. **Angular Kinematics**: The lander's $angle$ is the integral of $ang\_vel$; high $|ang\_vel|$ results in rapid orientation changes that can quickly move the lander into extreme tilt regimes.
3. **Main Engine Induced Torque**: Applying the main engine (Action 2) when the lander is at a non-zero $angle$ induces rotational torque, which modifies $ang\_vel$ and can exacerbate angular instability.
4. **Side-Engine Torque-Angle Coupling**: The direction of torque produced by side engines (Actions 1 and 3) is coupled to the sign of the current $angle$; for instance, at a positive $angle$, Action 3 produces positive torque, whereas at a negative $angle$, it produces negative torque.
5. **Lateral-Angular Coupling**: Side-engine thrust (Actions 1 and 3) modifies lateral velocity ($x\_vel$), with the direction of resulting horizontal drift being dependent on both the specific engine used and the current $angle$.
6. **Rotational Feedback Runaway**: Selecting a side engine that produces torque matching the current sign of $ang\_vel$ (e.g., Action 3 when $angle > 0$ and $ang\_vel > 0$, or Action 3 when $angle < 0$ and $ang\_vel < 0$) creates a positive feedback loop that rapidly accelerates the lander into an uncontrollable tumble.
7. **Momentum Dominance and Irreversibility**: Once $|ang\_vel|$, $|y\_vel|$, or $|angle|$ reaches high magnitudes, the existing momentum can exceed the maximum corrective capability of any engine, making stabilization or descent arrest impossible.
8. **Ground Contact Dynamics**: Upon making contact ($left\_leg\_contact$ or $right\_leg\_contact = 1$), the lander can maintain a state near $y\_pos = 0$ through active engine modulation, effectively "hovering" or oscillating near the surface.
9. **Conditional Terminal Failure**: A catastrophic failure is most likely triggered by high-velocity vertical impacts ($y\_vel$ magnitude) or excessive angular momentum at the time of ground contact.
10. **Cumulative Lateral Displacement**: Continuous use of side engines for orientation correction results in significant cumulative $x\_pos$ drift, causing the lander to deviate substantially from its initial lateral position.

---

## 2026-07-05 14:04:14

1. **Vertical Velocity Control**: The main engine (Action 2) is the primary mechanism to counteract $y\_vel$ and manage the descent rate to prevent high-velocity impacts.
2. **Angular Kinematics**: The lander's $angle$ is the integral of $ang\_vel$; high $|ang\_vel|$ results in rapid orientation changes that can quickly move the lander into extreme tilt regimes.
3. **Main Engine Induced Torque**: Applying the main engine (Action 2) induces rotational torque, which modifies $ang\_vel$ and can either stabilize or destabilize the lander's orientation depending on the current angle and angular velocity.
4. **Side-Engine Stabilizing Torque (Action 3)**: The right engine (Action 3) produces a stabilizing torque that opposes the current $angle$; it produces negative torque when $angle > 0$ and positive torque when $angle < 0$.
5. **Side-Engine Destabilizing Torque (Action 1)**: The left engine (Action 1) can act as a destabilizing force; specifically, applying Action 1 when the lander has a positive $angle$ can create a positive feedback loop that increases angular instability.
6. **Lateral-Velocity Coupling**: Side-engine thrust (Actions 1 and 3) modifies lateral velocity ($x\_vel$), with Action 1 generally decreasing $x\_vel$ and Action 3 generally increasing it.
7. **Momentum Dominance and Irreversibility**: Once $|ang\_vel|$, $|y\_vel|$, or $|angle|$ reaches high magnitudes, the existing momentum can exceed the maximum corrective capability of any engine, making stabilization impossible.
8. **Ground Contact Dynamics**: Upon making contact ($left\_leg\_contact$ or $right\_leg\_contact = 1$), the lander can maintain a state near $y\_pos = 0$ through active engine modulation, effectively "hovering."
9. **Conditional Terminal Failure**: A catastrophic failure is most likely triggered by high-velocity vertical impacts or excessive angular momentum at the moment of ground contact.
10. **Cumulative Lateral Displacement**: Continuous use of side engines for orientation correction results in significant cumulative $x\_pos$ drift, causing the lander to deviate from its initial lateral position.

---

## 2026-07-05 14:09:49

1. **Vertical Velocity Management**: The main engine (Action 2) is the primary mechanism for controlling $y\_vel$ to manage the descent rate and ensure a controlled approach to the ground.
2. **Angular Kinematics**: The lander's $angle$ is the integral of its $ang\_vel$; managing angular velocity is essential to prevent large orientation deviations and extreme tilts.
3. **Main Engine Induced Torque**: Applying the main engine (Action 2) induces rotational torque, which modifies $ang\_vel$ and impacts the lander's orientation relative to the vertical axis.
4. **Side-Engine Torque and Angular Control**: The left (Action 1) and right (Action 3) engines provide torque used to adjust $ang\_vel$, allowing for fine-grained orientation management and stabilization.
5. **Lateral Velocity Coupling**: The application of side-engine thrust (Actions 1 and 3) results in direct changes to the lateral velocity ($x\_vel$).
6. **Ground Contact Combinations**: The environment supports four distinct contact states: no legs in contact, only the left leg, only the right leg, or both legs in contact ($left\_leg\_contact$ and $right\_leg\_contact$).
7. **Ground-Contact Hovering and Oscillation**: Once ground contact is established, the lander can maintain a position near $y\_pos = 0$ through active engine modulation, often resulting in continuous small-scale oscillations in $angle$ and $ang\_vel$.
8. **Landing Impact Sensitivity**: Catastrophic failure and significant reward penalties are associated with high vertical velocities ($y\_vel$) or excessive angular momentum ($ang\_vel$) at the moment of ground contact.
9. **Momentum Dominance**: When $|ang\_vel|$, $|y\_vel|$, or $|angle|$ reach critical magnitudes, the existing momentum can exceed the maximum corrective thrust or torque capability of the engines, making stabilization impossible.
10. **Cumulative Lateral Displacement**: Continuous use of side engines to correct orientation leads to significant cumulative $x\_pos$ drift, causing the lander to deviate from its initial lateral position.

---

## 2026-07-05 14:11:46

1. **Vertical Velocity Management**: The main engine (Action 2) is the primary mechanism for controlling $y\_vel$ to manage descent rate and ensure a controlled approach.
2. **Angular Kinematics**: The lander's $angle$ is the integral of its $ang\_vel$; managing angular velocity is essential to prevent extreme orientation deviations.
3. **Main Engine Induced Torque**: Applying the main engine (Action 2) induces rotational torque, which modifies $ang\_vel$ and impacts the lander's orientation.
4. **Side-Engine Dual-Role**: Side engines (Actions 1 and 3) provide torque used to adjust $ang\_vel$ while simultaneously inducing changes in lateral velocity ($x\_vel$).
5. **Lateral Displacement Coupling**: Frequent use of side engines to correct orientation leads to significant cumulative $x\_pos$ drift and increased lateral momentum.
6. **Ground Contact States**: The environment supports four distinct leg contact states: no legs in contact, only the left leg, only the right leg, or both legs in contact.
7. **Post-Landing Stability**: Once ground contact is established, the lander can maintain position near $y\_pos = 0$ through active engine modulation, often resulting in small-scale oscillations in $angle$ and $ang\_vel$.
8. **Landing Impact Sensitivity**: Catastrophic failure and significant reward penalties are associated with high vertical velocities ($y\_vel$) or excessive angular momentum ($ang\_vel$) at the moment of ground contact.
9. **Momentum vs. Control Authority**: When $|ang\_vel|$, $|y\_vel|$, or $|x\_vel|$ reach critical magnitudes, the existing momentum can exceed the maximum corrective thrust or torque capability of the engines, making stabilization impossible.
10. **Angular Momentum Instability**: Rapidly increasing angular velocity ($ang\_vel$) can lead to orientation deviations that are difficult to arrest, as attempts to stabilize the angle via side engines may be insufficient to overcome the existing rotational momentum.

---

## 2026-07-05 14:13:19

1. **Vertical Velocity Control**: The main engine (Action 2) is the primary mechanism for managing descent rate ($y\_vel$) to ensure a controlled approach to the ground.
2. **Angular Kinematics**: The lander's $angle$ is the integral of its $ang\_vel$; managing angular velocity is essential to prevent extreme orientation deviations.
3. **Main Engine Induced Torque**: Applying the main engine (Action 2) induces rotational torque, which modifies $ang\_vel$ and impacts the lander's orientation.
4. **Side-Engine Dual-Role**: Side engines (Actions 1 and 3) provide torque to adjust $ang\_vel$ while simultaneously inducing changes in lateral velocity ($x\_vel$).
5. **Lateral Displacement Coupling**: Frequent use of side engines to correct orientation leads to significant cumulative $x\_pos$ drift and increased lateral momentum.
6. **Ground Contact States**: The environment supports four distinct leg contact states: no legs in contact, only the left leg, only the right leg, or both legs in contact. The lander can settle at or slightly below $y\_pos = 0$.
7. **Catastrophic Rotational Failure**: High angular velocity ($ang\_vel$) at the moment of ground contact is a primary driver of catastrophic failure, potentially resulting in extreme negative rewards (e.g., -100).
8. **Landing Impact Sensitivity**: Significant negative rewards are associated with high vertical velocities ($y\_vel$) or excessive angular momentum ($ang\_vel$) at the moment ground contact is established.
9. **Momentum vs. Control Authority**: When $|ang\_vel|$, $|y\_vel|$, or $|x\_vel|$ reach critical magnitudes, the existing momentum can exceed the maximum corrective thrust or torque capability of the engines, making stabilization impossible.
10. **Post-Landing Oscillations**: Once ground contact is established, the lander can maintain position near $y\_pos \approx 0$ through active engine modulation, which often results in small-scale oscillations in $angle$, $ang\_vel$, and $y\_pos$.

---

## 2026-07-05 14:18:02

1. **Vertical Velocity Control**: The main engine (Action 2) is the primary mechanism for managing descent rate ($y\_vel$) to ensure a controlled approach to the ground.
2. **Angular Kinematics**: The lander's $angle$ is the integral of its $ang\_vel$; managing angular velocity is essential to prevent extreme orientation deviations.
3. **Main Engine Induced Torque**: Applying the main engine (Action 2) induces rotational torque, which modifies $ang\_vel$ and impacts the lander's orientation.
4. **Side-Engine Dual-Role**: Side engines (Actions 1 and 3) provide torque to adjust $ang\_vel$ while simultaneously inducing changes in lateral velocity ($x\_vel$).
5. **Lateral Displacement Coupling**: Frequent use of side engines to correct orientation leads to significant cumulative $x\_pos$ drift and increased lateral momentum.
6. **Ground Contact States**: The environment tracks ground contact via two binary flags (`left_leg_contact` and `right_leg_contact`), allowing for states ranging from no contact to both legs being grounded.
7. **Catastrophic Rotational Failure**: High angular velocity ($ang\_vel$) at the moment of ground contact is a primary driver of catastrophic failure (e.g., -100 reward), even if leg contact has already been established.
8. **Landing Impact Sensitivity**: Significant negative rewards are associated with high vertical velocities ($y\_vel$) or excessive angular momentum ($ang\_vel$) at the moment ground contact is established.
9. **Torque Saturation and Instability**: When $|ang\_vel|$ reaches extreme magnitudes (e.g., $>0.9$), the torque from side engines may become insufficient to arrest rotation or may even exacerbate angular instability, making stabilization impossible.
10. **Post-Landing Oscillations**: Once ground contact is established, the lander can maintain position near $y\_pos \approx 0$ through active engine modulation, which often results in small-scale oscillations in $angle$, $ang\_vel$, and $y\_pos$.

---

## 2026-07-05 14:19:08

1. **Vertical Velocity Control**: The main engine (Action 2) is the primary mechanism for managing descent rate ($y\_vel$) to ensure a controlled approach to the ground.
2. **Angular Kinematics**: The lander's $angle$ is the integral of its $ang\_vel$; managing angular velocity is essential to prevent extreme orientation deviations.
3. **Main Engine Induced Torque**: Applying the main engine (Action 2) induces rotational torque, which modifies $ang\_vel$ and impacts the lander's orientation.
4. **Side-Engine Dual-Role**: Side engines (Actions 1 and 3) provide torque to adjust $ang\_vel$ while simultaneously inducing changes in lateral velocity ($x\_vel$).
5. **Lateral Displacement Coupling**: Frequent use of side engines to correct orientation leads to significant cumulative $x\_pos$ drift and increased lateral momentum.
6. **Ground Contact States**: The environment tracks ground contact via two binary flags (`left_leg_contact` and `right_leg_contact`), allowing for states ranging from no contact to single-leg contact to dual-leg contact.
7. **Catastrophic Landing Transition**: The transition from single-leg contact to dual-leg contact (both flags = 1.0) serves as the critical trigger for the catastrophic failure reward (-100), contingent on the lander's velocity and orientation at that moment.
8. **Single-Leg Ground Dynamics**: After the first leg makes contact, the lander is not immediately stabilized; it can continue to move and undergo significant oscillations in $y\_pos$, $angle$, and $ang\_vel$ before the second leg touches the ground.
9. **Landing Impact Sensitivity**: Significant negative rewards are associated with high vertical velocities ($y\_vel$) or excessive angular momentum ($ang\_vel$) at the moment ground contact is established.
10. **Torque Saturation and Instability**: When $|ang\_vel|$ reaches extreme magnitudes, the torque from side engines may become insufficient to arrest rotation or may even exacerbate angular instability, making stabilization impossible.

---

## 2026-07-05 14:22:10

1. **Main Engine Vertical Control**: The main engine (Action 2) is the primary mechanism for managing the lander's vertical velocity ($y\_vel$), whether the lander is in a descent or ascent phase.
2. **Angular Kinematics**: The lander's $angle$ is the integral of its $ang\_vel$; managing angular velocity is essential to prevent extreme orientation deviations.
3. **Engine-Induced Torque Coupling**: The main engine (Action 2) induces rotational torque, while the side engines (Actions 1 and 3) induce both torque and changes in lateral velocity ($x\_vel$).
4. **Lateral Displacement Drift**: Frequent use of side engines to correct orientation leads to significant cumulative $x\_pos$ drift and increased lateral momentum.
5. **Ground Contact State Tracking**: The environment tracks contact via two binary flags (`left_leg_contact` and `right_leg_contact`), allowing for states ranging from no contact to single-leg contact to dual-leg contact.
6. **Post-Contact Oscillatory Dynamics**: After the first leg makes contact, the lander often experiences bouncing or oscillations, characterized by rapid switching between single-leg and dual-leg contact states.
7. **Contact-State Stability Penalties**: While in any contact state, the lander receives heavy negative rewards if it is not in a perfectly static state (i.e., if velocities are non-zero).
8. **Catastrophic Failure Trigger**: Transitioning to dual-leg contact (both flags = 1.0) while possessing high velocity or extreme orientation triggers a catastrophic failure reward (-100).
9. **Velocity-Sensitive Contact Penalties**: Significant negative rewards (often ranging from -10 to -22) are specifically triggered by non-zero $x\_vel$, $y\_vel$, or $ang\_vel$ during a contact event.
10. **Torque Saturation and Instability**: When $|ang\_vel|$ reaches extreme magnitudes, the torque from side engines may become insufficient to arrest rotation, making stabilization impossible.

---

## 2026-07-05 14:23:57

1. **Main Engine Vertical Control**: The main engine (Action 2) is the primary mechanism for managing the lander's vertical velocity ($y\_vel$), whether in a descent or ascent phase.
2. **Engine-Induced Torque Coupling**: The main engine (Action 2) induces rotational torque, while the side engines (Actions 1 and 3) induce both rotational torque and changes in lateral velocity ($x\_vel$).
3. **Lateral Displacement Drift**: Frequent use of side engines to correct orientation leads to significant cumulative $x\_pos$ drift and increased lateral momentum.
4. **Ground Contact State Tracking**: The environment tracks contact via two binary flags (`left_leg_contact` and `right_leg_contact`), allowing for states ranging from no contact to single-leg contact to dual-leg contact.
5. **Contact-State Stability Penalties**: While in any contact state, the lander receives heavy negative rewards if it is not in a near-static state (i.e., if $x\_vel$, $y\_vel$, or $ang\_vel$ are non-zero).
6. **Catastrophic Failure Trigger**: A catastrophic failure reward (-100) is triggered by extreme velocity or orientation, which can occur during the initial transition to dual-leg contact or while already in a contact state.
7. **Angular-Lateral Coupling**: Using side engines to correct orientation ($angle$) or angular velocity ($ang\_vel$) directly increases lateral velocity ($x\_vel$), creating a direct trade-off between orientation stability and lateral stability.
8. **Single-Leg Contact State**: The lander can enter a transitional state where only one leg has contact (one flag is 1.0), often occurring before the lander achieves dual-leg contact.
9. **Post-Contact Velocity Sensitivity**: Maintaining extremely low $y\_vel$ and $ang\_vel$ is critical once contact is established; high magnitudes in these specific components during contact significantly increase the risk of transitioning from a partial success to a catastrophic failure.
10. **Torque Saturation and Instability**: When $|ang\_vel|$ reaches extreme magnitudes, the torque from side engines may become insufficient to arrest rotation, making orientation stabilization impossible.

---

## 2026-07-05 14:42:54

---
1. **Main Engine Vertical Control**: The main engine (Action 2) is the primary mechanism for managing the lander's vertical velocity ($y\_vel$).
2. **Engine-Induced Torque Coupling**: The main engine (Action 2) induces rotational torque, while the side engines (Actions 1 and 3) induce both rotational torque and changes in lateral velocity ($x\_vel$).
3. **Lateral Displacement Drift**: Frequent use of side engines to correct orientation leads to significant cumulative $x\_pos$ drift and increased lateral momentum.
4. **Contact-State Tracking**: The environment tracks contact via two binary flags (`left_leg_contact` and `right_leg_contact`), enabling states of no contact, single-leg contact, or dual-leg contact.
5. **Contact-State Non-Static Penalties**: While in any contact state, the agent receives massive negative rewards (typically in the -10 to -25 range) if the lander is not in a near-static state ($x\_vel, y\_vel, ang\_vel \approx 0$).
6. **Angular-Lateral Coupling**: Using side engines to correct orientation ($angle$ or $ang\_vel$) directly increases lateral velocity ($x\_vel$), creating a direct trade-off between rotational and lateral stability.
7. **Contact Loss and Bouncing**: Maintaining extremely low $y\_vel$ and $ang\_vel$ is critical upon contact; high velocities can cause the lander to bounce or tip, causing contact flags to toggle back to 0.0 and triggering heavy penalties.
8. **Single-Leg Contact Vulnerability**: Single-leg contact is a highly unstable transitional state; attempting to correct orientation or velocity during this phase frequently results in the lander tipping or losing contact entirely.
9. **Torque Saturation**: When $|ang\_vel|$ reaches extreme magnitudes, the torque from side engines may become insufficient to arrest rotation, making orientation stabilization impossible.
10. **Failure Reward Distinction**: A catastrophic failure reward (-100) is distinct from the high-magnitude instability penalties (-10 to -25) incurred for non-zero velocities while in a contact state.

---

## 2026-07-05 14:47:05

1. **Main Engine Vertical Control**: The main engine (Action 2) is the primary mechanism for managing the lander's vertical velocity ($y\_vel$).
2. **Engine-Induced Torque Coupling**: The main engine (Action 2) induces rotational torque, while the side engines (Actions 1 and 3) induce both rotational torque and changes in lateral velocity ($x\_vel$).
3. **Lateral Displacement Drift**: Frequent use of side engines to correct orientation results in significant cumulative $x\_pos$ drift and increased lateral momentum.
4. **Contact-State Tracking**: The environment tracks contact via two binary flags (`left_leg_contact` and `right_leg_contact`), enabling states of no contact (0,0), single-leg contact (1,0 or 0,1), or dual-leg contact (1,1).
5. **Contact-State Instability Penalties**: While in any contact state, the agent receives massive negative rewards (typically in the -10 to -25 range) if the lander is not in a near-static state ($x\_vel, y\_vel, ang\_vel \approx 0$).
6. **Angular-Lateral Coupling**: Using side engines to correct orientation ($angle$ or $ang\_vel$) directly increases lateral velocity ($x\_vel$), creating a direct trade-off between rotational and lateral stability.
7. **Contact Loss and Bouncing**: Maintaining extremely low $y\_vel$ and $ang\_vel$ is critical upon contact; high velocities or high angular momentum can cause the lander to bounce or tip, causing contact flags to toggle back to (0,0).
8. **Contact Chatter**: During the landing phase, the lander can enter a highly unstable "chatter" state, characterized by rapid oscillations between no contact, single-leg contact, and dual-leg contact.
9. **Angular Velocity Management**: High magnitudes of $|ang\_vel|$ make orientation stabilization significantly more difficult, as the torque from side engines must overcome existing angular momentum to arrest rotation.
10. **Failure Reward Distinction**: A catastrophic failure reward (-100) is distinct from the high-magnitude instability penalties (-10 to -25) incurred for non-zero velocities while in a contact state.

---

## 2026-07-05 14:48:28

1. **Main Engine Vertical Control**: Action 2 is the primary mechanism for managing the lander's vertical velocity ($y\_vel$).
2. **Engine-Induced Torque Coupling**: The main engine (Action 2) induces rotational torque, while the side engines (Actions 1 and 3) induce both rotational torque and changes in lateral velocity ($x\_vel$).
3. **Lateral Displacement Drift**: Frequent use of side engines to correct orientation results in significant cumulative $x\_pos$ drift and increased lateral momentum.
4. **Contact-State Tracking**: The environment tracks contact via two binary flags (`left_leg_contact` and `right_leg_contact`), enabling states of no contact (0,0), single-leg contact (1,0 or 0,1), or dual-leg contact (1,1).
5. **Contact-State Instability Penalties**: While in any contact state (where at least one flag is 1), the agent receives massive negative rewards (typically in the -10 to -25 range) if the lander exhibits non-zero $x\_vel$, $y\_vel$, or $ang\_vel$.
6. **Angular-Lateral Coupling**: Using side engines to correct orientation ($angle$ or $ang\_vel$) directly increases lateral velocity ($x\_vel$), creating a direct trade-off between rotational and lateral stability.
7. **Contact Loss via Momentum**: High magnitudes of lateral velocity ($x\_vel$) or angular velocity ($ang\_vel$) during contact can cause the lander to tip or bounce, causing the contact flags to revert from (1,1) or (1,0) back to (0,0).
8. **Contact Chatter**: During the landing phase, the lander can enter a highly unstable "chatter" state, characterized by rapid oscillations between contact and no-contact states.
9. **Angular Velocity Management**: High magnitudes of $|ang\_vel|$ make orientation stabilization difficult, as the torque from side engines must overcome existing angular momentum to arrest rotation; failure to arrest rotation quickly during contact leads to sustained instability penalties.
10. **Failure Reward Distinction**: A catastrophic failure reward (-100) is distinct from the high-magnitude instability penalties (-10 to -25) incurred for non-zero velocities while in a contact state.

---

## 2026-07-05 14:50:05

1. **Main Engine Vertical Control**: Action 2 is the primary mechanism for managing the lander's vertical velocity ($y\_vel$).
2. **Engine-Induced Torque Coupling**: The main engine (Action 2) induces rotational torque, while the side engines (Actions 1 and 3) induce both rotational torque and changes in lateral velocity ($x\_vel$).
3. **Contact-State Instability Penalties**: While in any contact state (where at least one flag is 1), the agent receives massive negative rewards (typically in the -10 to -25 range) if the lander exhibits non-zero $x\_vel$, $y\_vel$, or $ang\_vel$.
4. **Lateral Displacement Drift**: Frequent use of side engines to correct orientation results in significant cumulative $x\_pos$ drift and increased lateral momentum.
5. **The Landing Stability Requirement**: To avoid massive instability penalties and achieve high rewards, the agent must simultaneously bring $x\_vel$, $y\_vel$, and $ang\_vel$ to near-zero values as contact is established.
6. **Action 0 Inefficacy During Contact**: Choosing Action 0 (nothing) during the contact phase does not mitigate instability penalties if the lander's velocity components have not already been arrested.
7. **Contact Loss via Momentum**: High magnitudes of lateral velocity ($x\_vel$) or angular velocity ($ang\_vel$) during contact can cause the lander to tip or bounce, causing the contact flags to revert from (1,1) or (1,0) back to (0,0).
8. **Failure Reward Distinction**: A catastrophic failure reward (-100) is distinct from the high-magnitude instability penalties (-10 to -25) incurred for non-zero velocities while in a contact state.
9. **Angular-Lateral Trade-off**: Using side engines to correct orientation ($angle$ or $ang\_vel$) directly increases lateral velocity ($x\_vel$), creating a direct conflict between rotational and lateral stability.
10. **Contact State Universality**: Instability penalties are applied consistently across all contact configurations, including single-leg contact (1,0 or 0,1) and dual-leg contact (1,1).

---

## 2026-07-05 14:53:12

1. **Vertical Velocity Regulation**: Action 2 (Main Engine) is the primary mechanism for controlling the lander's vertical velocity ($y\_vel$).
2. **Multi-Axis Engine Coupling**: All engine actions (1, 2, and 3) induce rotational torque ($ang\_vel$); side engines (1 and 3) specifically induce lateral velocity ($x\_vel$), while the main engine also contributes to lateral momentum.
3. **Contact-Velocity Instability Penalty**: If the lander is in any contact state (at least one leg flag is 1) and exhibits non-zero $x\_vel$, $y\_vel$, or $ang\_vel$, it incurs massive negative rewards, typically in the -10 to -25 range.
4. **Contact-Velocity Stability Reward**: If the lander achieves near-zero $x\_vel$, $y\_vel$, and $ang\_vel$ while in a contact state, it receives massive positive rewards, typically in the +10 to +25 range.
5. **Momentum-Induced Contact Loss**: High magnitudes of lateral velocity ($x\_vel$) or angular velocity ($ang\_vel$) during contact can cause the lander to tip or bounce, resulting in a transition from dual-leg (1,1) to single-leg (1,0 or 0,1) or no-leg (0,0) contact states.
6. **Side Engine Lateral Drift**: Frequent use of side engines to correct orientation results in significant cumulative lateral displacement ($x\_pos$) drift and increased lateral momentum ($x\_vel$).
7. **Angular-Lateral Stability Trade-off**: A direct conflict exists between rotational and lateral stability, as using side engines to correct $angle$ or $ang\_vel$ directly increases $x\_vel$.
8. **Action 0 Inefficacy During Contact**: Choosing Action 0 (nothing) during the contact phase does not arrest existing velocities and therefore fails to mitigate instability penalties.
9. **Failure vs. Instability Distinction**: A catastrophic failure reward (-100) is qualitatively and quantitatively distinct from the high-magnitude instability penalties (-10 to -25) or high-magnitude stability rewards (+10 to +25).
10. **Contact State Universality**: Both the instability penalties and the stability rewards are applied consistently across all contact configurations, including single-leg and dual-leg contact states.

---

## 2026-07-05 14:59:42

1. **Vertical Velocity Regulation**: Action 2 (Main Engine) is the primary mechanism for controlling the lander's vertical velocity ($y\_vel$).
2. **Multi-Axis Engine Coupling**: All engine actions (1, 2, and 3) induce rotational torque ($ang\_vel$); side engines (1 and 3) specifically induce lateral velocity ($x\_vel$), while the main engine also contributes to lateral momentum.
3. **Contact-Velocity Instability Penalty**: If the lander is in any contact state (at least one leg flag is 1) and exhibits non-zero $x\_vel$, $y\_vel$, or $ang\_vel$, it incurs massive negative rewards, typically in the -10 to -25 range.
4. **Contact-Velocity Stability Reward**: If the lander achieves near-zero $x\_vel$, $y\_vel$, and $ang\_vel$ while in a contact state, it receives massive positive rewards, typically in the +10 to +25 range.
5. **Momentum-Induced Contact Loss**: High magnitudes of lateral velocity ($x\_vel$) or angular velocity ($ang\_vel$) during contact can cause the lander to tip or bounce, resulting in a transition from dual-leg (1,1) to single-leg (1,0 or 0,1) or no-leg (0,0) contact states.
6. **Side Engine Lateral Drift**: Frequent use of side engines to correct orientation results in significant cumulative lateral displacement ($x\_pos$) drift and increased lateral momentum ($x\_vel$).
7. **Angular-Lateral Stability Trade-off**: A direct conflict exists between rotational and lateral stability, as using side engines to correct $angle$ or $ang\_vel$ directly increases $x\_vel$.
8. **Action 0 Inefficacy During Contact**: Choosing Action 0 (nothing) during the contact phase does not arrest existing velocities and therefore fails to mitigate instability penalties.
9. **Failure vs. Instability Distinction**: A catastrophic failure reward (-100) is qualitatively and quantitatively distinct from the high-magnitude instability penalties (-10 to -25) or high-magnitude stability rewards (+10 to +25).
10. **Landing-Phase Reward Sensitivity**: The reward sign is highly sensitive during the contact transition; high-velocity impacts or sustained movement during contact trigger severe instability penalties, whereas high stability rewards are primarily accumulated once velocities are arrested during a sustained contact state.

---

## 2026-07-05 15:03:04

1. **Vertical Velocity Regulation**: Action 2 (Main Engine) is the primary mechanism for controlling the lander's vertical velocity ($y\_vel$).
2. **Multi-Axis Engine Coupling**: All engine actions (1, 2, and 3) induce rotational torque ($ang\_vel$); side engines (1 and 3) specifically induce lateral velocity ($x\_vel$), while the main engine also contributes to lateral momentum.
3. **Contact-Velocity Instability Penalty**: If the lander is in any contact state (at least one leg flag is 1) and exhibits non-zero $x\_vel$, $y\_vel$, or $ang\_vel$, it incurs massive negative rewards, typically in the -10 to -25 range.
4. **Contact-Velocity Stability Reward**: If the lander achieves near-zero $x\_vel$, $y\_vel$, and $ang\_vel$ while in a contact state, it receives massive positive rewards, typically in the +10 to +25 range.
5. **Momentum-Induced Contact Instability**: High magnitudes of lateral ($x\_vel$) or angular velocity ($ang\_vel$) during or immediately after contact can trigger a "bouncing" effect, causing the lander to rapidly oscillate between contact states (1,1 or 1,0/0,1) and no-contact states (0,0).
6. **Side Engine Lateral Drift**: Frequent use of side engines to correct orientation results in significant cumulative lateral displacement ($x\_pos$) drift and increased lateral momentum ($x\_vel$).
7. **Angular-Lateral Stability Trade-off**: A direct conflict exists between rotational and lateral stability, as using side engines to correct $angle$ or $ang\_vel$ directly increases $x\_vel$.
8. **Action 0 Inefficacy During Contact**: Choosing Action 0 (nothing) during the contact phase does not arrest existing velocities and therefore fails to mitigate instability penalties.
9. **Failure vs. Instability Distinction**: A catastrophic failure reward (-100) is qualitatively and quantitatively distinct from the high-magnitude instability penalties (-10 to -25) or high-magnitude stability rewards (+10 to +25).
10. **Landing-Phase Reward Sensitivity**: The reward sign is highly sensitive during the contact transition; high-velocity impacts or sustained movement during contact trigger severe instability penalties, whereas high stability rewards are primarily accumulated once velocities are arrested during a sustained contact state.

---

## 2026-07-05 15:04:54

1. **Vertical Velocity Regulation**: Action 2 (Main Engine) is the primary mechanism for controlling the lander's vertical velocity ($y\_vel$).
2. **Multi-Axis Engine Coupling**: All engine actions (1, 2, and 3) induce rotational torque ($ang\_vel$); side engines (1 and 3) specifically induce lateral velocity ($x\_vel$), while the main engine also contributes to lateral momentum.
3. **Contact-Velocity Reward/Penalty Coupling**: High-magnitude rewards (+10 to +25) and penalties (-10 to -25) are strictly tied to the intersection of contact status (leg flags) and the magnitude of $x\_vel$, $y\_vel$, and $ang\_vel$.
4. **Momentum-Induced Contact Oscillation**: High magnitudes of lateral ($x\_vel$) or angular velocity ($ang\_vel$) during contact trigger a "bouncing" effect, characterized by rapid oscillations between contact states (1,1 or 1,0/0,1) and no-contact states (0,0).
5. **Side Engine Lateral Drift**: Frequent use of side engines (1 or 3) to correct orientation ($angle$) results in significant cumulative lateral displacement ($x\_pos$) and increased lateral momentum ($x\_vel$).
6. **Angular-Lateral Stability Trade-off**: A direct conflict exists between rotational and lateral stability; using side engines to mitigate $angle$ or $ang\_vel$ directly increases $x\_vel$.
7. **Action 0 Inefficacy**: Choosing Action 0 (nothing) during or immediately after contact fails to arrest existing velocities, which can prevent the transition from instability penalties to stability rewards.
8. **Single-Leg Contact Instability**: States involving only a single leg contact (e.g., [1,0] or [0,1]) are highly unstable and frequently serve as precursors to a transition into a no-contact state (0,0).
9. **Catastrophic Failure Distinction**: A catastrophic failure reward (-100) is distinct from instability penalties and is often triggered by extreme angular velocity ($ang\_vel$) or high-velocity impacts that result in a loss of contact.
10. **Stabilization Requirements**: Accumulating maximum stability rewards requires not just achieving contact, but arresting all velocity components ($x\_vel$, $y\_vel$, $ang\_vel$) while maintaining a sustained, multi-leg contact state.

---

## 2026-07-05 15:07:55

1. **Vertical Velocity Regulation**: Action 2 (Main Engine) is the primary mechanism for controlling the lander's vertical velocity ($y\_vel$).
2. **Multi-Axis Engine Coupling**: All engine actions (1, 2, and 3) induce rotational torque ($ang\_vel$), while side engines (1 and 3) specifically contribute to lateral momentum ($x\_vel$).
3. **Contact-Velocity Reward/Penalty Sensitivity**: During contact, the reward/penalty function is extremely sensitive to the magnitudes of $ang\_vel$ and $x\_vel$; even relatively low angular velocities during contact can trigger significant penalties, whereas specific combinations of low velocities and multi-leg contact yield high rewards.
4. **Momentum-Induced Contact Oscillation**: High magnitudes of lateral ($x\_vel$) or angular velocity ($ang\_vel$) during the approach phase trigger a "bouncing" effect, characterized by rapid oscillations between contact states ([1,1], [1,0], [0,1]) and no-contact states ([0,0]).
5. **Side Engine Lateral Drift**: Frequent use of side engines (1 or 3) to correct orientation ($angle$) results in significant cumulative lateral displacement ($x\_pos$) and increased lateral momentum ($x\_vel$).
6. **Angular-Lateral Stability Trade-off**: A direct conflict exists between rotational and lateral stability; using side engines to mitigate $angle$ or $ang\_vel$ directly increases $x\_vel$.
7. **Action 0 Inefficacy**: Choosing Action 0 (nothing) during or immediately after contact fails to arrest existing velocities, which can prevent the transition from instability penalties to stability rewards.
8. **Sustained Controlled Descent**: The lander can maintain a prolonged, low-velocity vertical descent ($y\_vel$) even when carrying high lateral momentum ($x\_vel$), but such states do not accumulate stability rewards until contact is established.
9. **Contact vs. Stabilization Distinction**: Achieving contact (leg flags = 1) is insufficient for a successful outcome; the lander must also arrest all velocity components ($x\_vel$, $y\_vel$, $ang\_vel$) and maintain a sustained, multi-leg contact state to avoid instability penalties.
10. **Single-Leg Contact Instability**: States involving only a single leg contact (e.g., [1,0] or [0,1]) are highly unstable and frequently serve as precursors to either a transition into a no-contact state (0,0) or extreme angular oscillations.

---

## 2026-07-05 15:10:29

---
1. **Vertical Velocity Regulation**: Action 2 (Main Engine) is the primary mechanism for controlling the lander's vertical velocity ($y\_vel$).
2. **Multi-Axis Engine Coupling**: All engine actions (1, 2, and 3) induce rotational torque ($ang\_vel$), while side engines (1 and 3) specifically contribute to lateral momentum ($x\_vel$).
3. **Catastrophic Angular Penalty during Contact**: Applying torque (via actions 1, 2, or 3) while in a contact state ([1,0] or [1,1]) is extremely high-risk; even minor changes in $ang\_vel$ can trigger massive negative rewards (e.g., $-15$ to $-20$).
4. **Leg-State Transition Volatility**: Transitions between multi-leg contact ([1,1]) and single-leg ([1,0], [0,1]) or no-contact ([0,0]) states are highly volatile; while single-leg contact can occasionally yield high rewards if $ang\_vel$ is near zero, it often serves as the precursor to catastrophic stability loss.
5. **Side Engine Lateral Drift**: Frequent use of side engines (1 or 3) to correct orientation ($angle$) results in significant cumulative lateral displacement ($x\_pos$) and increased lateral momentum ($x\_vel$).
6. **Angular-Lateral Stability Trade-off**: A direct conflict exists between rotational and lateral stability; using side engines to mitigate $angle$ or $ang\_vel$ directly increases $x\_vel$.
7. **Action 0 for Landing Stabilization**: While Action 0 (nothing) fails to arrest existing velocities, it is a critical mechanism for maintaining a stable contact state once the lander has achieved low velocities, preventing additional engine-induced torque.
8. **Momentum-Induced Contact Oscillation**: High magnitudes of lateral ($x\_vel$) or angular velocity ($ang\_vel$) during the approach phase trigger a "bouncing" effect, characterized by rapid oscillations between contact states.
9. **Stability Reward Requirements**: Successful outcomes require not just contact, but the simultaneous arrest of all velocity components ($x\_vel$, $y\_vel$, $ang\_vel$) and the maintenance of a sustained, multi-leg contact state ([1,1]).
10. **Velocity Component Hierarchy in Penalties**: During contact, the reward function is disproportionately sensitive to $ang\_vel$ compared to $x\_vel$ or $y\_vel$; large-scale penalties are predominantly driven by angular instability.

---

## 2026-07-05 15:15:35

1. **Vertical Velocity Regulation**: Action 2 (Main Engine) remains the primary mechanism for controlling the lander's vertical velocity ($y\_vel$).
2. **Multi-Axis Engine Coupling**: All engine actions induce rotational torque ($ang\_vel$), while side engines (1 and 3) specifically contribute to lateral momentum ($x\_vel$).
3. **Contact-Induced Angular Penalties**: Applying torque via any engine action while in a contact state ([1,0], [0,1], or [1,1]) triggers significant negative rewards, with penalties scaling based on the magnitude of $ang\_vel$.
4. **Single-Leg Contact Reward Incentive**: The reward function provides substantial positive reinforcement (often ranging from $+10$ to $+12$) for achieving single-leg contact ([1,0] or [0,1]), incentivizing touchdown even if multi-leg stability is not yet achieved.
5. **Side Engine Lateral Drift**: Frequent use of side engines (1 or 3) to correct orientation ($angle$) results in significant cumulative lateral displacement ($x\_pos$) and increased lateral momentum ($x\_vel$).
6. **Angular-Lateral Stability Trade-off**: A direct conflict exists between rotational and lateral stability; using side engines to mitigate $angle$ or $ang\_vel$ directly increases $x\_vel$.
7. **High-Velocity Terminal Risk**: Excessive angular velocity ($ang\_vel$), particularly when exceeding a threshold of approximately $1.0$, is a primary precursor to catastrophic terminal failure and massive negative penalties (e.g., $-100$).
8. **Momentum-Induced Contact Oscillation**: High magnitudes of lateral ($x\_vel$) or angular velocity ($ang\_vel$) during the approach phase trigger a "bouncing" effect, characterized by rapid oscillations between contact states.
9. **Stability Reward Requirements**: Successful outcomes require not just contact, but the simultaneous arrest of all velocity components and the transition from single-leg contact to a sustained, multi-leg contact state ([1,1]).
10. **Velocity Component Hierarchy in Penalties**: The reward function is disproportionately sensitive to $ang\_vel$ compared to $x\_vel$ or $y\_vel$; large-scale penalties and terminal failures are predominantly driven by angular instability.

---

## 2026-07-05 15:18:25

1. **Vertical Velocity Regulation**: Action 2 (Main Engine) remains the primary mechanism for controlling the lander's vertical velocity ($y\_vel$).
2. **Multi-Axis Engine Coupling**: All engine actions induce rotational torque ($ang\_vel$), while side engines (1 and 3) specifically contribute to lateral momentum ($x\_vel$).
3. **High-Risk Contact Maneuvering**: Applying engine actions (1, 2, or 3) while in any contact state ([1,0], [0,1], or [1,1]) is extremely high-risk and frequently triggers massive negative penalties (e.g., $-10$ to $-20$), often far exceeding descent-phase errors.
4. **Contact-Phase Stabilization Incentives**: Large positive rewards (e.g., $+10$ to $+13$) are awarded for specific engine actions or even inaction (Action 0) during single-leg contact ([1,0] or [0,1]), providing heavy reinforcement for maneuvers that facilitate a stable transition to multi-leg contact ([1,1]).
5. **Side Engine Lateral Drift**: Frequent use of side engines (1 or 3) to correct orientation ($angle$) results in significant cumulative lateral displacement ($x\_pos$) and increased lateral momentum ($x\_vel$).
6. **Angular-Lateral Stability Trade-off**: A direct conflict exists between rotational and lateral stability; using side engines to mitigate $angle$ or $ang\_vel$ directly increases $x\_vel$.
7. **High-Velocity Terminal Risk**: Excessive angular velocity ($ang\_vel$), particularly when exceeding a threshold of approximately $1.0$, is a primary precursor to catastrophic terminal failure and massive negative penalties.
8. **Momentum-Induced Contact Oscillation**: High magnitudes of lateral ($x\_vel$) or angular velocity ($ang\_vel$) during the approach phase trigger a "bouncing" effect, characterized by rapid oscillations between contact states.
9. **Stability Reward Requirements**: Successful outcomes require not just contact, but the simultaneous arrest of all velocity components and the transition from single-leg contact to a sustained, multi-leg contact state ([1,1]).
10. **Penalty Magnitude Hierarchy**: The reward function's penalty hierarchy is dominated by contact-phase stability; penalties incurred due to improper engine use or instability while in contact are significantly more severe than those incurred during the descent phase.

---

## 2026-07-05 15:23:02

1. **Vertical Velocity Regulation**: Action 2 (Main Engine) remains the primary mechanism for controlling the lander's vertical velocity ($y\_vel$).
2. **Multi-Axis Engine Coupling**: Side engines (1 and 3) induce both rotational torque ($ang\_vel$) and lateral momentum ($x\_vel$).
3. **Contact-Phase Penalty Dominance**: Penalties for engine use while in any contact state ([1,0], [0,1], or [1,1]) are significantly more severe than descent-phase errors, often reaching magnitudes of $-10$ to $-21$.
4. **Engine-Induced Bouncing**: Applying engine thrust while in a contact state frequently triggers a "bounce," characterized by an immediate transition from contact ([1,1], [1,0], or [0,1]) back to a no-contact state ([0,0]).
5. **High-Risk Contact Actions**: Action 1 (Left Engine) and Action 2 (Main Engine) are the primary drivers of catastrophic contact-phase instability, frequently triggering the most extreme negative penalties and immediate bounces.
6. **Stabilization via Inaction**: Action 0 (nothing) is heavily reinforced during the contact phase as a critical stabilization mechanism to prevent massive penalties and maintain a sustained multi-leg contact state ([1,1]).
7. **Angular-Lateral Stability Trade-off**: A direct conflict exists between rotational and lateral stability; using side engines to mitigate $angle$ or $ang\_vel$ directly increases lateral displacement ($x\_pos$) and momentum ($x\_vel$).
8. **Momentum-Induced Contact Oscillation**: High magnitudes of lateral ($x\_vel$) or angular velocity ($ang\_vel$) during the approach phase can trigger rapid oscillations between different contact states.
9. **High-Velocity Terminal Risk**: Excessive angular velocity ($ang\_vel$), particularly when exceeding a threshold of approximately $1.0$, is a primary precursor to catastrophic terminal failure.
10. **Successful Landing Criteria**: Successful outcomes require the simultaneous arrest of all velocity components and the maintenance of a sustained, multi-leg contact state ([1,1]).

---

## 2026-07-05 15:26:31

1. **Vertical Velocity Regulation**: Action 2 (Main Engine) remains the primary mechanism for controlling the lander's vertical velocity ($y\_vel$).
2. **Multi-Axis Engine Coupling**: Side engines (1 and 3) induce both rotational torque ($ang\_vel$) and lateral momentum ($x\_vel$).
3. **Contact-State Reward Asymmetry**: There is a stark divide in reward structures based on contact state: using engines (1, 2, or 3) while in a multi-leg contact state ([1,1]) results in extreme penalties, whereas using engines in single-leg ([1,0], [0,1]) or no-contact ([0,0]) states can yield massive positive rewards.
4. **Inaction-Induced Bouncing**: Applying Action 0 (nothing) while in a multi-leg contact state ([1,1]) can paradoxically trigger a "bounce," causing an immediate and sudden transition to a no-contact ([0,0]) or single-leg state.
5. **Catastrophic Contact-Phase Penalties**: Using engines (specifically Action 1 or 2) while in a [1,1] state is the most frequent driver of extreme negative penalties, with magnitudes reaching as low as $-100$.
6. **Single-Leg Engine Utility**: Single-leg contact states ([1,0] or [0,1]) act as high-reward transitional phases where engines can be used effectively to manage momentum, provided they do not trigger an immediate transition to a penalized [1,1] state.
7. **Angular-Lateral Stability Trade-off**: A direct conflict exists between rotational and lateral stability; using side engines to mitigate $angle$ or $ang\_vel$ directly increases lateral displacement ($x\_pos$) and momentum ($x\_vel$).
8. **Momentum-Induced Contact Oscillation**: High magnitudes of lateral ($x\_vel$) or angular velocity ($ang\_vel$) during the approach phase can trigger rapid oscillations between different contact states.
9. **High-Velocity Terminal Risk**: Excessive angular velocity ($ang\_vel$), particularly when exceeding a threshold of approximately $1.0$, is a primary precursor to catastrophic terminal failure.
10. **Successful Landing Criteria**: Successful outcomes require the simultaneous arrest of all velocity components and the maintenance of a sustained, multi-leg contact state ([1,1]).

---

## 2026-07-05 15:31:11

1. **Vertical Velocity Regulation**: Action 2 (Main Engine) remains the primary mechanism for controlling the lander's vertical velocity ($y\_vel$).
2. **Multi-Axis Engine Coupling**: Side engines (Actions 1 and 3) induce both rotational torque ($ang\_vel$) and lateral momentum ($x\_vel$).
3. **Side Engine Descent Disincentive**: Using side engines (1 or 3) during no-contact ([0,0]) or single-leg ([1,0], [0,1]) states frequently incurs negative rewards, unlike the main engine.
4. **Multi-Leg Contact Instability**: In a multi-leg contact state ([1,1]), all actions—including inaction (Action 0)—are susceptible to triggering significant negative penalties.
5. **Inaction-Induced Bouncing**: Applying Action 0 while in a multi-leg contact state ([1,1]) can trigger a "bounce," causing an immediate transition to a no-contact ([0,0]) or single-leg state.
6. **Angular-Lateral Stability Trade-off**: Using side engines to mitigate $angle$ or $ang\_vel$ directly increases lateral displacement ($x\_pos$) and momentum ($x\_vel$).
7. **Momentum-Induced Contact Oscillation**: High magnitudes of lateral ($x\_vel$) or angular velocity ($ang\_vel$) during the approach phase can trigger rapid oscillations between different contact states.
8. **High-Velocity Terminal Crash**: Excessive lateral velocity ($x\_vel$) or extreme angular tilt ($angle$) during the approach or contact phase leads to a catastrophic terminal failure penalty ($-100$).
9. **Single-Leg Engine Utility**: Single-leg contact states ([1,0] or [0,1]) act as high-reward transitional phases where engines can be used effectively to manage momentum.
10. **Successful Landing Criteria**: Successful outcomes require the simultaneous arrest of all velocity components and the maintenance of a sustained, multi-leg contact state ([1,1]).

---

## 2026-07-05 15:37:24

1. **Vertical Velocity Regulation**: Action 2 (Main Engine) remains the primary mechanism for controlling the lander's vertical velocity ($y\_vel$).
2. **Multi-Axis Engine Coupling**: Side engines (Actions 1 and 3) induce both rotational torque ($ang\_vel$) and lateral momentum ($x\_vel$).
3. **Multi-Leg Contact Fragility**: Actions taken while in a multi-leg contact state ([1,1]) that trigger a transition to a single-leg ([1,0], [0,1]) or no-contact ([0,0]) state frequently incur severe negative penalties (often exceeding -15).
4. **Velocity-Driven Reward Scaling**: Large positive rewards (up to ~23) are achievable across all contact states ([1,1], [1,0], [0,1], and [0,0]) when the lander successfully arrests its velocity components.
5. **Contact State Bouncing**: Applying engines or inaction (Action 0) while in a multi-leg contact state ([1,1]) can force a transition to a single-leg or no-contact state.
6. **Angular-Lateral Stability Trade-off**: Using side engines to mitigate $angle$ or $ang\_vel$ directly increases lateral displacement ($x\_pos$) and lateral momentum ($x\_vel$).
7. **Momentum-Induced Instability**: High magnitudes of lateral ($x\_vel$) or angular velocity ($ang\_vel$) during the approach or contact phases can trigger rapid oscillations between different contact states.
8. **High-Velocity Terminal Crash**: Extreme lateral velocity ($x\_vel$) or extreme angular tilt ($angle$) during the approach or contact phase leads to a catastrophic terminal failure penalty.
9. **Successful Landing Criteria**: Successful outcomes require the simultaneous arrest of all velocity components and the maintenance of a sustained, multi-leg contact state ([1,1]).
10. **Single-Leg Momentum Management**: Single-leg contact states ([1,0] and [0,1]) serve as high-reward transitional phases where engines can be used to stabilize momentum and orientation.

---

## 2026-07-05 15:39:12

1. **Vertical Velocity Regulation**: Action 2 (Main Engine) remains the primary mechanism for controlling the lander's vertical velocity ($y\_vel$).
2. **Multi-Axis Engine Coupling**: Side engines (Actions 1 and 3) induce both rotational torque ($ang\_vel$) and lateral momentum ($x\_vel$).
3. **Multi-Leg Contact Fragility**: Any engine action or inaction that triggers a transition from a multi-leg contact state ([1,1]) to a single-leg ([1,0], [0,1]) or no-contact ([0,0]) state incurs severe negative penalties.
4. **Catastrophic Side-Engine Instability**: Applying side engines (Actions 1 or 3) while in a multi-leg contact state ([1,1]) can trigger an immediate transition to a no-contact state ([0,0]), leading to extreme terminal failure penalties as high as -100.
5. **Velocity-Driven Reward Scaling**: Large positive rewards are achievable when the lander successfully arrests all velocity components, regardless of the contact state.
6. **Angular-Lateral Stability Trade-off**: Using side engines to mitigate angular tilt ($angle$) or angular velocity ($ang\_vel$) directly increases lateral displacement ($x\_pos$) and lateral momentum ($x\_vel$).
7. **Momentum-Induced Contact Instability**: High magnitudes of lateral ($x\_vel$) or angular velocity ($ang\_vel$) during the approach or contact phases can trigger rapid oscillations between different contact states.
8. **Terminal Failure Modes**: Catastrophic failure is driven by extreme lateral velocity, extreme angular tilt, or the sudden loss of multi-leg contact (transitioning from [1,1] to [0,0]).
9. **Successful Landing Criteria**: A successful landing requires the simultaneous arrest of all velocity components and the maintenance of a sustained, multi-leg contact state ([1,1]).
10. **Transitional Contact Phases**: Single-leg contact states ([1,0] and [0,1]) serve as high-reward transitional phases where engines are used to stabilize momentum and orientation before reaching the final [1,1] state.

---

## 2026-07-05 15:41:03

1. **Vertical Velocity Regulation**: Action 2 (Main Engine) remains the primary mechanism for controlling the lander's vertical velocity ($y\_vel$).
2. **Multi-Axis Engine Coupling**: Side engines (Actions 1 and 3) induce both rotational torque ($ang\_vel$) and lateral momentum ($x\_vel$).
3. **Contact State Transition Fragility**: Any engine action or inaction that triggers a transition from a multi-leg contact state ([1,1]) to a single-leg ([1,0], [0,1]) or no-contact ([0,0]) state incurs negative penalties.
4. **Catastrophic Side-Engine Instability**: Applying side engines (Actions 1 or 3) while in a multi-leg contact state ([1,1]) can trigger an immediate transition to a no-contact state ([0,0]), leading to extreme terminal failure penalties.
5. **Terminal Failure Magnitude**: A catastrophic terminal penalty (as high as -100) is applied if the lander fails to meet specific stability (angle/angular velocity) or velocity thresholds at the moment of contact.
6. **Angular-Lateral Stability Trade-off**: Using side engines to mitigate angular tilt ($angle$) or angular velocity ($ang\_vel$) directly increases lateral displacement ($x\_pos$) and lateral momentum ($x\_vel$).
7. **Momentum-Induced Contact Instability**: High magnitudes of lateral ($x\_vel$) or angular velocity ($ang\_vel$) during the approach or contact phases can trigger rapid oscillations between different contact states.
8. **Post-Contact Instability Penalties**: Achieving [1,1] contact is insufficient for stability; high $ang\_vel$ or $x\_vel$ while in the [1,1] state incurs severe, continuous negative rewards (often in the -15 to -25 range), simulating tip-overs or ground-sliding.
9. **Successful Landing Criteria**: A successful landing requires the simultaneous arrest of all velocity components and the maintenance of a sustained, multi-leg contact state ([1,1]).
10. **Side-Engine Oscillatory Risk**: Rapidly alternating between side engines (Actions 1 and 3) to correct orientation can induce high-frequency oscillations in $x\_vel$ and $ang\_vel$, making it difficult to stabilize the lander even after contact is established.

---

## 2026-07-05 15:50:40

---
1. **Main Engine Verticality Regulation**: Action 2 (Main Engine) remains the fundamental mechanism for controlling vertical velocity ($y\_vel$) and regulating height ($y\_pos$).
2. **Side Engine Utility and Cost**: Actions 1 and 3 (Side Engines) are the primary tools for managing angular tilt ($angle$) and angular velocity ($ang\_vel$), but they are frequently associated with immediate negative reward increments, likely representing fuel consumption or lateral momentum penalties.
3. **Landing Event Reward Spikes**: A transition into a multi-leg contact state (`[1,1]`) can trigger significant positive reward bonuses (often $>10$), indicating a high-value reward for establishing a successful landing contact.
4. **Catastrophic Contact Loss**: Transitions from any contact state (`[1,1]`, `[1,0]`, or `[0,1]`) to a no-contact state (`[0,0]`) are typically associated with severe negative penalties, simulating crash or tip-over events.
5. **Post-Contact Velocity Sensitivity**: Achieving `[1,1]` contact is not a guarantee of stability; the lander continues to incur significant negative rewards if residual velocities ($x\_vel, y\_vel, ang\_vel$) are not effectively arrested after touchdown.
6. **Angular-Lateral Stability Trade-off**: Using side engines to mitigate angular errors ($angle$ or $ang\_vel$) directly induces lateral displacement ($x\_pos$) and lateral momentum ($x\_vel$).
7. **Landing Phase Contact Oscillations**: The approach and touchdown phase is characterized by high-frequency oscillations between different contact states (e.g., rapid switching between `[1,1]`, `[1,0]`, `[0,1]`, and `[0,0]`).
8. **Continued Main Engine Utility in Contact**: Action 2 is frequently utilized even after multi-leg contact (`[1,1]`) is established, suggesting it is used to zero out residual vertical velocity or maintain altitude.
9. **Stabilization via Inaction**: Once a multi-leg contact state is established, the agent frequently employs Action 0 (Nothing) to attempt to maintain stability and minimize further fuel or lateral movement penalties.
10. **Successful Landing Criteria**: A high-reward landing requires the simultaneous arrest of all velocity components and the maintenance of a sustained, stable, multi-leg contact state (`[1,1]`).

---

## 2026-07-05 15:53:29

1. **Main Engine Verticality Regulation**: Action 2 (Main Engine) is the primary mechanism for controlling vertical velocity ($y\_vel$) and regulating altitude ($y\_pos$).
2. **Side Engine Utility and Cost**: Actions 1 and 3 (Side Engines) are the primary tools for managing angular tilt ($angle$) and angular velocity ($ang\_vel$), but they are associated with fuel consumption penalties.
3. **Contact Establishment Reward Spikes**: Transitions from a no-contact state (`[0,0]`) to *any* contact state (`[1,0]`, `[0,1]`, or `[1,1]`) trigger significant positive reward spikes.
4. **Severe Contact Loss Penalties**: Transitions from any contact state (`[1,1]`, `[1,0]`, or `[0,1]`) back to a no-contact state (`[0,0]`) are associated with extreme negative penalties, often exceeding -10.
5. **Post-Contact Velocity Sensitivity**: Establishing contact is not a guarantee of stability; high residual velocities ($x\_vel, y\_vel, ang\_vel$) can lead to immediate contact loss and subsequent heavy penalties.
6. **Angular-Lateral Stability Trade-off**: Using side engines to mitigate angular errors ($angle$ or $ang\_vel$) directly induces lateral displacement ($x\_pos$) and lateral momentum ($x\_vel$).
7. **Unstable Contact Oscillations**: The landing phase is characterized by high-frequency oscillations where the lander rapidly cycles between contact and no-contact states.
8. **Continued Main Engine Utility in Contact**: Action 2 is frequently utilized even after contact is established, often to arrest residual vertical velocity or maintain altitude.
9. **Stabilization via Inaction**: Once a contact state is established, the agent frequently employs Action 0 (Nothing) to attempt to maintain stability and minimize further fuel or lateral movement penalties.
10. **Successful Landing Criteria**: A high-reward landing requires the simultaneous arrest of all velocity components and the maintenance of a sustained, non-oscillating contact state (`[1,1]`).

---

## 2026-07-05 15:56:19

1. **Main Engine Verticality Regulation**: Action 2 (Main Engine) is the primary mechanism for controlling altitude ($y\_pos$) and regulating vertical velocity ($y\_vel$).
2. **Side Engine Utility and Cost**: Actions 1 and 3 (Side Engines) are the primary tools for managing angular tilt ($angle$) and angular velocity ($ang\_vel$), but they are associated with fuel consumption penalties.
3. **Extreme Contact Establishment Rewards**: Transitions from a no-contact state (`[0,0]`) to any contact state (`[1,0]`, `[0,1]`, or `[1,1]`) trigger massive positive reward spikes, frequently exceeding +10 and often reaching above +20.
4. **Severe Contact Loss Penalties**: Transitions from any contact state back to a no-contact state (`[0,0]`) are associated with extreme negative penalties, frequently exceeding -10 and occasionally reaching -20.
5. **Fragile Contact Stability**: Maintaining contact is extremely difficult; even minimal residual velocities ($x\_vel, y\_vel, ang\_vel$) or slight angular deviations can lead to immediate and repeated contact loss.
6. **Angular-Lateral Stability Trade-off**: Using side engines to mitigate angular errors ($angle$ or $ang\_vel$) directly induces lateral displacement ($x\_pos$) and lateral momentum ($x\_vel$).
7. **Unstable Contact Oscillations**: The landing phase is characterized by high-frequency oscillations where the lander rapidly cycles between contact and no-contact states.
8. **Action-Induced Contact Loss**: In unstable or high-velocity contact states, almost any action—including Action 0 (Nothing) or Action 2 (Main Engine)—can trigger an immediate transition back to a no-contact state.
9. **Continued Main Engine Utility in Contact**: Action 2 is frequently utilized even after contact is established, often to arrest residual vertical velocity or attempt to maintain altitude.
10. **Successful Landing Criteria**: A high-reward landing requires the simultaneous arrest of all velocity components and the maintenance of a sustained, non-oscillating contact state (`[1,1]`).

---

## 2026-07-05 15:58:09

1. **Main Engine Verticality Regulation**: Action 2 (Main Engine) is the primary mechanism for controlling altitude ($y\_pos$) and regulating vertical velocity ($y\_vel$).
2. **Side Engine Angular Management**: Actions 1 and 3 (Side Engines) are the tools for managing angular tilt ($angle$) and angular velocity ($ang\_vel$).
3. **Lateral-Angular Coupling**: Using side engines to mitigate angular errors directly induces lateral displacement ($x\_pos$) and lateral momentum ($x\_vel$). Over long durations, this can lead to significant lateral drift (e.g., drifting from $x \approx 0$ to $x \approx 1$).
4. **Massive Contact Establishment Rewards**: Transitions from a no-contact state (`[0,0]`) to any contact state (`[1,0]`, `[0,1]`, or `[1,1]`) trigger massive positive reward spikes, frequently exceeding +10 and reaching above +20.
5. **Severe Contact Loss and Impact Penalties**: Transitions from a contact state back to a no-contact state are associated with extreme negative penalties (often -10 to -20). Catastrophic terminal events, such as high-velocity impacts, can trigger extreme penalties as large as -100.
6. **Fragile Contact Stability**: Maintaining contact is extremely difficult; minimal residual velocities ($x\_vel, y\_vel, ang\_vel$) or slight angular deviations can lead to immediate and repeated contact loss.
7. **Unstable Contact Oscillations**: The landing phase is characterized by high-frequency oscillations where the lander rapidly cycles between contact and no-contact states.
8. **Action-Induced Contact Loss**: In unstable or high-velocity contact states, almost any action—including Action 0 (Nothing) or Action 2 (Main Engine)—can trigger an immediate transition back to a no-contact state.
9. **Continued Main Engine Utility in Contact**: Action 2 is frequently utilized even after contact is established to arrest residual vertical velocity or attempt to maintain altitude.
10. **Landing Outcome Hierarchy**: A "PARTIAL" outcome can be achieved through intermittent or oscillating contact, whereas a "SUCCESSFUL" landing requires the simultaneous arrest of all velocity components and the maintenance of a sustained, non-oscillating contact state.

---

## 2026-07-05 16:04:54

1. **Main Engine Verticality Regulation**: Action 2 (Main Engine) is the primary mechanism for controlling altitude ($y\_pos$) and regulating vertical velocity ($y\_vel$).
2. **Side Engine Angular Management**: Actions 1 and 3 (Side Engines) are the tools for managing angular tilt ($angle$) and angular velocity ($ang\_vel$).
3. **Lateral-Angular Coupling**: Using side engines to mitigate angular errors directly induces lateral displacement ($x\_pos$) and lateral momentum ($x\_vel$), leading to persistent lateral drift.
4. **Massive Contact Establishment Rewards**: Transitions from a no-contact state (`[0,0]`) to any contact state (`[1,0]`, `[0,1]`, or `[1,1]`) trigger massive positive reward spikes, frequently ranging from +10 to over +25.
5. **Severe Contact Loss and Impact Penalties**: Transitions from a contact state back to a no-contact state are associated with significant negative penalties (often -8 to -20), while catastrophic terminal events, such as high-velocity impacts, can trigger extreme penalties as large as -100.
6. **Fragile Contact Stability**: Maintaining contact is extremely difficult; minimal residual velocities ($x\_vel, y\_vel, ang\_vel$) or slight angular deviations can lead to immediate contact loss.
7. **High-Frequency Reward-Penalty Oscillations**: The landing phase is characterized by intense high-frequency oscillations where the lander rapidly cycles between contact and no-contact states, resulting in a sequence of massive reward spikes and heavy penalties.
8. **Action-Induced Contact Loss**: In unstable or high-velocity contact states, almost any action—including Action 0 (Nothing) or Action 2 (Main Engine)—can trigger an immediate transition back to a no-contact state.
9. **Contact Configuration Volatility**: During landing attempts, the lander frequently transitions between different leg contact configurations (e.g., `[1,1]` to `[1,0]` or `[0,1]`) before eventually losing contact entirely.
10. **Landing Outcome Hierarchy**: A "PARTIAL" outcome is often achieved through sustained but highly oscillating contact, whereas a "SUCCESSFUL" landing requires the simultaneous arrest of all velocity components and the maintenance of a steady, non-oscillating contact state.

---

## 2026-07-05 16:09:37

1. **Main Engine Verticality Regulation**: Action 2 (Main Engine) is the primary mechanism for controlling altitude ($y\_pos$) and regulating vertical velocity ($y\_vel$).
2. **Side Engine Angular Management**: Actions 1 and 3 (Side Engines) are the tools for managing angular tilt ($angle$) and angular velocity ($ang\_vel$).
3. **Lateral-Angular Coupling**: Using side engines to mitigate angular errors directly induces lateral displacement ($x\_pos$) and lateral momentum ($x\_vel$), leading to persistent lateral drift.
4. **Contact Establishment Reward Spikes**: Transitions from a no-contact state (`[0,0]`) to any contact state (`[1,0]`, `[0,1]`, or `[1,1]`) trigger massive positive reward spikes (frequently > +10).
5. **Severe Contact Loss and Impact Penalties**: Transitions from a contact state back to a no-contact state are associated with significant negative penalties (often -8 to -20), while catastrophic terminal events can trigger even larger penalties.
6. **Velocity-Induced Contact Instability**: Maintaining contact is extremely difficult; even minimal residual velocities ($x\_vel, y\_vel, ang\_vel$) or slight angular deviations can lead to immediate contact loss.
7. **High-Frequency Contact Oscillations**: The landing phase is characterized by intense high-frequency oscillations where the lander rapidly cycles between contact and no-contact states, resulting in a sequence of reward spikes and heavy penalties.
8. **Action-Induced Contact Disruption**: In unstable or high-velocity contact states, using side engines (Actions 1 or 3) to correct tilt can immediately trigger a transition back to a no-contact state or a loss of a single leg.
9. **Contact Configuration Volatility**: During landing attempts, the lander frequently transitions between different leg contact configurations (e.g., `[1,1]` to `[1,0]` or `[0,1]`) before eventually losing contact entirely.
10. **Landing Outcome Hierarchy**: A "PARTIAL" outcome is characterized by sustained but highly oscillating contact, whereas a "SUCCESSFUL" landing requires the simultaneous arrest of all velocity components and the maintenance of a steady, non-oscillating contact state.

---

## 2026-07-05 16:12:27

1. **Main Engine Verticality Regulation**: Action 2 (Main Engine) is the primary mechanism for controlling altitude ($y\_pos$) and regulating vertical velocity ($y\_vel$).
2. **Side Engine Angular Management**: Actions 1 and 3 (Side Engines) are the tools for managing angular tilt ($angle$) and angular velocity ($ang\_vel$).
3. **Lateral-Angular Coupling**: Using side engines to mitigate angular errors directly induces lateral displacement ($x\_pos$) and lateral momentum ($x\_vel$), leading to persistent lateral drift.
4. **Contact Establishment Reward Spikes**: Transitions from a no-contact state to any contact state (`[1,0]`, `[0,1]`, or `[1,1]`) trigger massive positive reward spikes.
5. **Severe Contact Loss Penalties**: Transitions from a contact state back to a no-contact state are associated with significant negative penalties (frequently -8 to -20).
6. **Impact-Rebound Dynamics**: High-magnitude contact rewards are frequently followed immediately by high-magnitude contact-loss penalties, indicating that landing impacts often trigger a physical rebound effect.
7. **Velocity-Induced Contact Instability**: Maintaining contact is extremely difficult; even minimal residual velocities ($x\_vel, y\_vel, ang\_vel$) or slight angular deviations can lead to immediate contact loss or a rebound.
8. **Action-Induced Contact Disruption**: In unstable or high-velocity contact states, using side engines (Actions 1 or 3) to correct tilt can immediately trigger a transition back to a no-contact state or a loss of a single leg.
9. **Contact Configuration Volatility**: The landing phase is characterized by rapid transitions between different leg contact configurations (e.g., `[1,1]` to `[1,0]` or `[0,1]`) and intense high-frequency oscillations between contact and no-contact states.
10. **Velocity-Stabilization Requirement**: Sustained, non-oscillating contact requires the simultaneous arrest of all velocity components to prevent kinetic energy from triggering the impact-rebound cycle.

---

## 2026-07-05 16:15:25

---
1. **Main Engine Verticality Regulation**: Action 2 (Main Engine) is the primary mechanism for controlling altitude ($y\_pos$) and regulating vertical velocity ($y\_vel$).
2. **Side Engine Angular Management**: Actions 1 and 3 (Side Engines) are the primary tools for managing angular tilt ($angle$) and angular velocity ($ang\_vel$).
3. **Lateral-Angular Coupling**: Using side engines to mitigate angular errors directly induces lateral displacement ($x\_pos$) and lateral momentum ($x\_vel$), leading to persistent lateral drift.
4. **Contact Establishment Reward Spikes**: Transitions from a no-contact state to any contact state (`[1,0]`, `[0,1]`, or `[1,1]`) trigger massive positive reward spikes.
5. **Severe Contact Loss Penalties**: Transitions from a contact state back to a no-contact state are associated with significant negative penalties (frequently -8 to -20).
6. **Impact-Rebound Dynamics**: High-magnitude contact rewards are frequently followed immediately by high-magnitude contact-loss penalties, indicating that landing impacts often trigger a physical rebound effect.
7. **Velocity-Induced Contact Instability**: Maintaining contact is extremely difficult; even minimal residual velocities ($x\_vel, y\_vel, ang\_vel$) can lead to immediate contact loss or a rebound if corrective thrust is not applied.
8. **Engine-Induced Contact Disruption**: Firing side engines (Actions 1 or 3) or the main engine (Action 2) while in a contact state can immediately trigger a transition back to a no-contact state or a loss of a single leg.
9. **Contact Configuration Volatility**: The landing phase is characterized by rapid transitions between different leg contact configurations (e.g., `[1,1]` to `[1,0]` or `[0,1]`) and intense high-frequency oscillations between contact and no-contact states.
10. **Control-Induced Chatter**: Even when contact is established, the system is prone to high-frequency oscillations caused by rapid, alternating engine commands, which can exacerbate mechanical instability and contact loss.

---

## 2026-07-05 16:17:55

---
1. **Main Engine Verticality Regulation**: Action 2 (Main Engine) is the primary mechanism for controlling altitude ($y\_pos$) and regulating vertical velocity ($y\_vel$).
2. **Side Engine Angular Management**: Actions 1 and 3 (Side Engines) are the primary tools for managing angular tilt ($angle$) and angular velocity ($ang\_vel$).
3. **Lateral-Angular Coupling**: Using side engines to mitigate angular errors directly induces lateral displacement ($x\_pos$) and lateral momentum ($x\_vel$), leading to persistent lateral drift.
4. **Contact Transition Reward Spikes**: Transitions from a no-contact state to any contact state (e.g., `[0,0]` to `[1,1]`) trigger massive positive reward spikes.
5. **Severe Contact Loss Penalties**: Transitions from any contact state back to a no-contact state are associated with significant negative penalties (frequently -8 to -20).
6. **Engine-Induced Contact Disruption**: Firing side engines (Actions 1 or 3) or the main engine (Action 2) while in a contact state can immediately trigger a transition back to a no-contact state or a loss of a single leg.
7. **Momentum-Induced Contact Loss**: High residual velocities ($x\_vel, y\_vel, ang\_vel$) can cause the lander to rebound or drift away from the ground even when no engine is firing (Action 0).
8. **Passive Contact Establishment**: In certain states, Action 0 (nothing) can lead to the establishment of contact if the lander's current trajectory and gravity facilitate the landing transition.
9. **Active Contact Recovery**: Side engines (Actions 1, 3) or the main engine (Action 2) can be used to re-establish contact from a no-contact state, although this often introduces lateral instability.
10. **Contact State Volatility**: The landing phase is characterized by rapid transitions between different leg contact configurations and intense high-frequency oscillations between contact and no-contact states.

---

## 2026-07-05 16:20:55

1. **Main Engine Verticality Regulation**: Action 2 (Main Engine) is the primary mechanism for controlling altitude ($y\_pos$) and regulating vertical velocity ($y\_vel$).
2. **Side Engine Angular Management**: Actions 1 and 3 (Side Engines) are the primary tools for managing angular tilt ($angle$) and angular velocity ($ang\_vel$).
3. **Lateral-Angular Coupling**: Using side engines to mitigate angular errors directly induces lateral displacement ($x\_pos$) and lateral momentum ($x\_vel$), leading to persistent lateral drift.
4. **Contact Transition Reward Spikes**: Transitions from a no-contact state `[0,0]` to any contact state (`[1,1]`, `[1,0]`, or `[0,1]`) trigger massive positive reward spikes.
5. **Severe Contact Loss Penalties**: Transitions from any contact state back to a no-contact state `[0,0]` are associated with significant negative penalties (frequently ranging from -8 to -21).
6. **Engine-Induced Rebound**: Firing the main engine (Action 2) while in a stable full-contact state (`[1,1]`) can trigger an immediate transition back to a no-contact state `[0,0]`.
7. **Passive Contact Loss**: In contact states, taking no action (Action 0) can lead to a loss of contact (`[0,0]`) if the lander's current trajectory, tilt, or velocity is unstable.
8. **Partial Contact Volatility**: States with only a single leg in contact (`[1,0]` or `[0,1]`) are highly unstable; engine actions can either stabilize the lander into `[1,1]` or inadvertently cause a total loss of contact `[0,0]`.
9. **Momentum-Induced Contact Loss**: High residual velocities ($x\_vel, y\_vel, ang\_vel$) can cause the lander to rebound or drift away from the ground even when no engine is firing.
10. **Contact State Volatility**: The landing phase is characterized by rapid transitions between different leg contact configurations and intense high-frequency oscillations between contact and no-contact states.

---

## 2026-07-05 16:30:20

1. **Main Engine (Action 2) Vertical Control**: The primary mechanism for regulating altitude ($y\_pos$) and vertical velocity ($y\_vel$).
2. **Side Engine (Actions 1 & 3) Angular Control**: The primary tools for managing angular tilt ($angle$) and angular velocity ($ang\_vel$).
3. **Lateral Drift Coupling**: Using side engines for angular corrections induces lateral displacement ($x\_pos$) and lateral momentum ($x\_vel$), leading to persistent drift.
4. **Contact Gain Rewards**: Transitions from a no-contact state `[0,0]` to any contact state (`[1,0]`, `[0,1]`, or `[1,1]`) trigger significant positive rewards, with `[1,1]` transitions often providing the highest reward spikes.
5. **Contact and Leg Loss Penalties**: Transitions from any contact state to a no-contact state `[0,0]` or from a full-contact state `[1,1]` to a partial-contact state `[1,0]` or `[0,1]` trigger severe negative penalties (frequently ranging from -8 to -20).
6. **Main Engine Instability**: Firing the main engine (Action 2) while in a partial contact state (`[1,0]` or `[0,1]`) or an unstable full-contact state can inadvertently cause total contact loss (`[0,0]`) or the loss of the remaining leg.
7. **Leg-Swap Dynamics**: Transitions that shift contact from one leg to the other (e.g., `[0,1]` to `[1,0]`) can result in high positive rewards, suggesting a mechanism for stabilizing the lander via weight-shifting.
8. **Passive Contact Loss**: In contact states, taking no action (Action 0) can lead to a loss of contact (`[0,0]`) if the lander's current trajectory, tilt, or velocity is unstable.
9. **Momentum-Induced Rebound**: High residual velocities ($x\_vel, y\_vel, ang\_vel$) can cause the lander to rebound or drift away from the ground even when no engine is firing.
10. **Contact State Volatility**: The landing phase is characterized by high-frequency oscillations between contact and no-contact states and rapid transitions between different leg configurations.

---

## 2026-07-05 16:32:28

1. **Main Engine (Action 2) Vertical Control**: The primary mechanism for regulating altitude ($y\_pos$) and vertical velocity ($y\_vel$).
2. **Side Engine (Actions 1 & 3) Angular Control**: The primary tools for managing angular tilt ($angle$) and angular velocity ($ang\_vel$).
3. **Lateral Drift Coupling**: Using side engines for angular corrections induces lateral displacement ($x\_pos$) and lateral momentum ($x\_vel$), leading to persistent drift.
4. **High-Magnitude Contact Rewards**: Transitions from no-contact (`[0,0]`) to any contact state (`[1,0]`, `[0,1]`, or `[1,1]`) trigger massive positive reward spikes, with full-contact transitions often yielding the highest values (e.g., > 15).
5. **Severe Contact Loss Penalties**: Transitions from any contact state to a no-contact state (`[0,0]`) trigger extreme negative penalties, frequently exceeding -15 to -20.
6. **Main Engine/Contact Interaction**: Firing the main engine (Action 2) while in a contact state or during periods of high angular rotation can inadvertently trigger immediate and total contact loss (`[0,0]`).
7. **Single-Leg and Leg-Swap Rewards**: Transitions that shift contact from one leg to another (e.g., `[0,1]` to `[1,0]`) or establish single-leg contact (`[1,0]` or `[0,1]`) provide significant positive reward spikes.
8. **Angular Velocity Instability Threshold**: High angular velocity ($ang\_vel$) is a primary driver of instability; extreme rotations are highly correlated with catastrophic contact loss and chaotic rebounding.
9. **Momentum-Induced Rebound**: High residual velocities ($x\_vel, y\_vel, ang\_vel$) can cause the lander to bounce or drift away from the ground even when no engine is firing.
10. **Contact State Volatility**: The terminal landing phase is characterized by high-frequency oscillations between contact and no-contact states and rapid transitions between different leg configurations.

---

## 2026-07-05 16:34:47

1. **Main Engine (Action 2) Vertical Control**: The primary mechanism for regulating altitude ($y\_pos$) and vertical velocity ($y\_vel$).
2. **Side Engine (Actions 1 & 3) Angular Control**: The primary tools for managing angular tilt ($angle$) and angular velocity ($ang\_vel$).
3. **Lateral Drift Coupling**: Using side engines for angular corrections induces lateral displacement ($x\_pos$) and lateral momentum ($x\_vel$), leading to persistent drift.
4. **High-Magnitude Contact Rewards**: Transitions from no-contact (`[0,0]`) to any contact state (`[1,0]`, `[0,1]`, or `[1,1]`) trigger massive positive reward spikes, often exceeding +10.
5. **Severe Contact Loss Penalties**: Transitions from any contact state to a no-contact state (`[0,0]`) trigger extreme negative penalties, frequently exceeding -15 to -20.
6. **Engine/Contact Disruption**: Firing any engine (Actions 1, 2, or 3) while in a contact state can trigger immediate and total contact loss (`[0,0]`) or cause chaotic leg-swapping.
7. **Side Engine Operational Cost**: The use of side engines (Actions 1 & 3) during descent frequently incurs continuous negative rewards, especially when they do not immediately result in contact or stabilization.
8. **Angular Velocity Instability Threshold**: High angular velocity ($ang\_vel$) is a primary driver of instability; extreme rotations are highly correlated with catastrophic contact loss and chaotic rebounding.
9. **Momentum-Induced Rebound**: High residual velocities ($x\_vel, y\_vel, ang\_vel$) can cause the lander to bounce or drift away from the ground even when no engine is firing.
10. **Contact State Volatility**: The terminal landing phase is characterized by high-frequency oscillations between contact and no-contact states and rapid transitions between different leg configurations.

---

## 2026-07-05 16:37:56

---
1. **Main Engine (Action 2) Vertical Control**: The primary mechanism for regulating altitude ($y\_pos$) and vertical velocity ($y\_vel$).
2. **Side Engine (Actions 1 & 3) Angular Control**: The primary tools for managing angular tilt ($angle$) and angular velocity ($ang\_vel$).
3. **Lateral Drift Coupling**: Using side engines for angular corrections induces lateral displacement ($x\_pos$) and lateral momentum ($x\_vel$), leading to persistent drift.
4. **High-Magnitude Contact Rewards**: Transitions into any contact state (`[1,0]`, `[0,1]`, or `[1,1]`) frequently trigger massive positive reward spikes.
5. **Extreme Contact Transition Volatility**: Transitions between contact states (e.g., `[1,1]` to `[0,0]` or `[1,1]` to `[1,0]`) are highly unpredictable, triggering extreme reward swings that can range from massive penalties (e.g., $-20$) to massive positive spikes (e.g., $+23$).
6. **Engine/Contact Disruption**: Firing any engine (Actions 1, 2, or 3) while in a contact state frequently triggers immediate contact loss or rapid, chaotic leg-swapping.
7. **Side Engine Operational Cost**: The use of side engines (Actions 1 & 3) during descent frequently incurs continuous negative rewards, even when attempting to stabilize.
8. **Angular Velocity Instability Threshold**: High angular velocity ($ang\_vel$) is a primary driver of instability; extreme rotations are highly correlated with catastrophic contact loss and rebounding.
9. **Momentum-Induced Rebound**: High residual velocities ($x\_vel, y\_vel, ang\_vel$) can cause the lander to bounce or drift away from the ground even when no engine is firing.
10. **Contact State Volatility**: The terminal landing phase is characterized by high-frequency oscillations between contact and no-contact states and rapid transitions between different leg configurations.

---

## 2026-07-05 16:40:59

1. **Main Engine (Action 2) Vertical Control**: The primary mechanism for regulating altitude ($y\_pos$) and vertical velocity ($y\_vel$).
2. **Side Engine (Actions 1 & 3) Angular Control**: The primary tools for managing angular tilt ($angle$) and angular velocity ($ang\_vel$).
3. **Lateral Drift Coupling**: Using side engines for angular corrections induces lateral displacement ($x\_pos$) and lateral momentum ($x\_vel$), leading to persistent drift.
4. **Contact State Reward Extremes**: The presence of contact (`[1,0]`, `[0,1]`, or `[1,1]`) can trigger massive positive spikes or extreme penalties, heavily influenced by the stability of the contact configuration and subsequent actions.
5. **Extreme Transition Volatility**: Transitions between contact states (e.g., `[1,1]` to `[0,0]`) are highly unpredictable and trigger massive, sudden reward swings.
6. **Engine-Induced Contact Instability**: Firing any engine while in a contact state frequently triggers rapid, chaotic leg-swapping (e.g., `[1,1]` $\leftrightarrow$ `[1,0]`) or immediate total contact loss.
7. **Side Engine Operational Cost**: The use of side engines (Actions 1 & 3) during descent frequently incurs continuous negative rewards.
8. **Angular Velocity Instability Threshold**: High angular velocity ($ang\_vel$) is a primary driver of instability; extreme rotations are highly correlated with catastrophic contact loss and rebounding.
9. **Velocity-Induced Contact Oscillation**: Higher residual velocities ($x\_vel, y\_vel$) increase the frequency and chaotic nature of contact-state oscillations during the descent and landing phases.
10. **Terminal Phase Contact Volatility**: The final landing phase is characterized by high-frequency switching between different leg configurations and rapid transitions between contact and no-contact states.

---

## 2026-07-05 16:48:15

1. **Main Engine (Action 2) Vertical Control**: The primary mechanism for regulating altitude ($y\_pos$) and vertical velocity ($y\_vel$).
2. **Side Engine (Actions 1 & 3) Angular Control**: The primary tools for managing angular tilt ($angle$) and angular velocity ($ang\_vel$).
3. **Lateral Drift Coupling**: Using side engines for angular corrections induces lateral displacement ($x\_pos$) and lateral momentum ($x\_vel$), leading to persistent drift.
4. **Contact State Reward Extremes**: Transitions between contact states (e.g., `[0,1] \to [1,1]`) or sudden contact loss trigger massive, sudden reward spikes or penalties.
5. **Side Engine-Contact Conflict**: Firing side engines (Actions 1 or 3) while in a contact state (especially `[1,1]`) is highly correlated with massive negative rewards and immediate contact loss.
6. **Side Engine Operational Cost**: The use of side engines (Actions 1 & 3) during descent frequently incurs continuous negative rewards.
7. **Angular Velocity Instability Threshold**: High angular velocity ($ang\_vel$) is a primary driver of instability, catastrophic contact loss, and rebounding.
8. **Velocity-Induced Contact Oscillation**: Higher residual velocities ($x\_vel, y\_vel$) increase the frequency and chaotic nature of contact-state switching.
9. **Terminal Phase Volatility**: The landing phase is characterized by high-frequency switching between different leg configurations and rapid transitions between contact and no-contact states.
10. **Stabilization Reward**: Reaching a stable, low-velocity `[1,1]` contact state triggers large positive terminal or transition rewards.

---

## 2026-07-05 16:51:48

1. **Main Engine (Action 2) Vertical Control**: The primary mechanism for regulating altitude ($y\_pos$) and vertical velocity ($y\_vel$).
2. **Side Engine (Actions 1 & 3) Angular Control**: The primary tools for managing angular tilt ($angle$) and angular velocity ($ang\_vel$).
3. **Side Engine Operational Cost**: Using side engines (Actions 1 & 3) during descent frequently incurs continuous negative rewards.
4. **Lateral Drift Coupling**: Using side engines for angular corrections induces lateral displacement ($x\_pos$) and lateral momentum ($x\_vel$).
5. **Contact Transition Spikes**: Transitions from non-contact `[0,0]` or partial-contact `[0,1]/[1,0]` states into a full `[1,1]` contact state trigger massive positive reward spikes.
6. **Contact Loss Penalties**: Sudden loss of contact (transitioning from `[1,1]` to `[0,0]`) triggers massive, immediate negative reward penalties.
7. **Side Engine-Contact Conflict**: Firing side engines (Actions 1 or 3) while in a contact state (especially `[1,1]`) is highly correlated with immediate contact loss and massive negative rewards.
8. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) is a primary driver of instability, catastrophic contact loss, and rebounding.
9. **Main Engine-Contact Instability**: Firing the main engine (Action 2) while in a stable `[1,1]` contact state can induce sudden contact loss and significant negative rewards.
10. **Stabilization Reward**: Reaching a stable, low-velocity `[1,1]` contact state is the primary driver of large positive terminal or transition rewards.

---

## 2026-07-05 16:54:54

1. **Main Engine (Action 2) Vertical Control**: The primary mechanism for regulating altitude ($y\_pos$) and vertical velocity ($y\_vel$).
2. **Side Engine (Actions 1 & 3) Angular and Momentum Control**: Used for managing angular tilt ($angle$, $ang\_vel$) and correcting high initial lateral or vertical momentum.
3. **Side Engine Reward Duality**: While side engines often incur continuous negative rewards during descent, they can yield significant positive rewards when used effectively to stabilize high-velocity states.
4. **Lateral Drift Coupling**: Using side engines for angular corrections induces lateral displacement ($x\_pos$) and lateral momentum ($x\_vel$).
5. **Contact Increase Spikes**: Transitions that increase the number of legs in contact (e.g., `[0,0] \to [0,1]`, `[1,0] \to [1,1]`, or `[0,1] \to [1,1]`) trigger substantial positive reward spikes.
6. **Contact Loss Penalties**: Any transition from a full `[1,1]` contact state to a state with fewer contacts (`[1,0]`, `[0,1]`, or `[0,0]`) triggers massive, immediate negative rewards.
7. **Side Engine-Contact Conflict**: Firing side engines (Actions 1 or 3) while in a `[1,1]` contact state is highly correlated with immediate contact loss and massive negative rewards.
8. **Inactivity Risk in Contact**: In a stable `[1,1]` contact state, using Action 0 (nothing) can result in gravity-induced contact loss and massive negative penalties.
9. **Main Engine-Contact Compatibility**: The main engine (Action 2) is significantly more compatible with maintaining a `[1,1]` contact state than side engines, though it may still induce contact loss in partial contact states.
10. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) remains a primary driver of instability, catastrophic contact loss, and rebounding.

---

## 2026-07-05 16:58:07

---
1. **Main Engine (Action 2) Vertical Control**: The primary mechanism for regulating altitude ($y\_pos$) and vertical velocity ($y\_vel$).
2. **Side Engine (Actions 1 & 3) Angular and Lateral Coupling**: Side engines manage angular tilt ($angle$, $ang\_vel$) but inherently induce lateral displacement ($x\_pos$) and momentum ($x\_vel$).
3. **Side Engine Reward Duality and Stabilization**: While side engines often incur continuous negative rewards, they are highly effective at stabilizing high-velocity/high-angle states and re-establishing contact.
4. **Contact Increase and Recovery Spikes**: Substantial positive rewards are triggered by increasing the number of legs in contact, including high-value spikes during contact recovery after a rebound.
5. **Contact Loss Penalties**: Any transition from a full `[1,1]` contact state to a state with fewer contacts (`[1,0]`, `[0,1]`, or `[0,0]`) triggers massive, immediate negative rewards.
6. **Side Engine-Contact Conflict**: Firing side engines (Actions 1 or 3) while in a contact state is highly correlated with immediate contact loss and massive negative rewards.
7. **Inactivity Risk in Contact**: In a stable `[1,1]` contact state, using Action 0 (nothing) can result in gravity-induced contact loss and massive negative penalties.
8. **Main Engine-Contact Compatibility**: The main engine (Action 2) is significantly more compatible with maintaining a `[1,1]` contact state than side engines.
9. **Rebound-Recovery Reward Cycles**: Post-impact, the environment often exhibits high-magnitude reward oscillations, cycling between contact loss penalties and contact recovery spikes.
10. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) remains a primary driver of instability, catastrophic contact loss, and rebounding.

---

## 2026-07-05 17:00:30

1. **Main Engine (Action 2) Vertical Control**: The primary mechanism for regulating altitude ($y\_pos$) and vertical velocity ($y\_vel$).
2. **Side Engine (Actions 1 & 3) Angular and Lateral Coupling**: Side engines manage angular tilt ($angle$, $ang\_vel$) but inherently induce lateral displacement ($x\_pos$) and momentum ($x\_vel$).
3. **Side Engine Flight Penalties**: Side engines (Actions 1 and 3) are strongly correlated with continuous negative rewards during the descent phase (non-contact state).
4. **Contact State Reward Dynamics**: Positive reward spikes are triggered by establishing or increasing contact, whereas any transition from a contact state to a non-contact state triggers massive, immediate negative rewards.
5. **Side Engine-Contact Conflict**: Firing side engines (Actions 1 or 3) while in any contact state ([1,1], [1,0], or [0,1]) is a primary driver of catastrophic contact loss.
6. **Inactivity Risk in Contact**: In a stable contact state, using Action 0 (nothing) is highly likely to result in gravity-induced contact loss and massive negative penalties.
7. **Descent-Phase Action Differentiation**: During descent (non-contact), Action 2 is the only action that consistently yields positive rewards, whereas Action 0 and side engines (1 and 3) are typically penalized.
8. **Main Engine-Contact Vulnerability**: While Action 2 is more compatible with maintaining contact than side engines, it can still trigger contact loss if applied during states of high angular tilt or high vertical velocity.
9. **Rebound-Recovery Reward Cycles**: Post-impact, the environment exhibits high-magnitude reward oscillations, cycling between contact loss penalties and contact recovery spikes.
10. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) serves as the underlying driver for most catastrophic failures, including side-engine-induced contact loss and gravity-induced contact loss.

---

## 2026-07-05 17:05:56

1. **Main Engine (Action 2) Vertical Control**: The primary mechanism for regulating altitude ($y\_pos$) and vertical velocity ($y\_vel$).
2. **Side Engine (Actions 1 & 3) Angular and Lateral Coupling**: Side engines manage angular tilt ($angle$, $ang\_vel$) but inherently induce lateral displacement ($x\_pos$) and momentum ($x\_vel$).
3. **Contact State Reward Dynamics**: The environment exhibits extreme reward oscillations during the landing phase; contact loss or instability triggers massive negative penalties (often in the -10 to -20 range), while establishing or stabilizing contact triggers large positive spikes (often in the +10 to +20 range).
4. **Inactivity Risk in Contact**: Using Action 0 (nothing) while in any contact state ([1,1], [1,0], or [0,1]) is a primary driver of gravity-induced contact loss and massive negative penalties.
5. **Side Engine-Contact Recovery**: While side engines (Actions 1 and 3) are typically penalized during descent, they can be used to successfully transition from a non-contact or partial-contact state to a stable, full-contact [1,1] state.
6. **Main Engine-Contact Vulnerability**: Action 2 can trigger catastrophic contact loss if applied during states of extremely low altitude ($y\_pos \approx 0$), potentially inducing a bounce or tip-over.
7. **Descent-Phase Action Differentiation**: During descent (non-contact), Action 2 is the only action that consistently yields positive rewards, whereas Action 0 and side engines (1 and 3) are typically penalized.
8. **Rebound-Recovery Reward Cycles**: Post-impact, the environment exhibits high-magnitude reward oscillations, cycling between contact loss penalties and contact recovery spikes.
9. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) serves as the underlying driver for most catastrophic failures, including side-engine-induced contact loss and gravity-induced contact loss.
10. **Contact State Transition Priority**: High-magnitude positive reward spikes are specifically associated with the transition from a non-contact state [0,0] to the full-contact [1,1] state.

---

## 2026-07-05 17:08:17

---
1. **Main Engine (Action 2) Verticality**: Action 2 remains the primary mechanism for regulating altitude ($y\_pos$) and vertical velocity ($y\_vel$).
2. **Side Engine (Actions 1 & 3) Coupling**: Side engines manage angular tilt ($angle$, $ang\_vel$) but inherently induce lateral displacement ($x\_pos$) and momentum ($x\_vel$).
3. **Extreme Reward Magnitude**: The environment exhibits massive reward oscillations during contact transitions, with magnitudes now observed in the $\pm 25$ range.
4. **Inactivity Risk in Contact**: Using Action 0 (nothing) while in any contact state is a primary driver of gravity-induced contact loss and massive negative penalties.
5. **Side Engine Stability Risk**: While side engines can facilitate landing, they are highly unstable once contact is established; using Actions 1 or 3 in a $[1,1]$ state frequently induces tip-overs or contact loss ($[1,1] \to [0,0]$ or $[1,0]$).
6. **Side Engine Landing Utility**: Side engines (Actions 1 and 3) can be successfully used to transition from a non-contact state $[0,0]$ to a full-contact $[1,1]$ state during the final descent.
7. **Main Engine Contact Recovery**: Action 2 is a critical tool for recovering from contact loss, often serving as the primary mechanism to transition from $[0,0]$ back to $[1,1]$ following a bounce.
8. **Descent-Phase Reward Differentiation**: During descent (non-contact), Action 2 is the most consistent source of positive rewards, while Action 0 and side engines are typically penalized.
9. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) is the underlying driver for most catastrophic failures, including side-engine-induced contact loss and gravity-induced contact loss.
10. **Contact State Transition Priority**: High-magnitude positive reward spikes are specifically associated with the transition from a non-contact state $[0,0]$ to the full-contact $[1,1]$ state.

---

## 2026-07-05 17:11:26

---
1. **Main Engine (Action 2) Verticality**: Action 2 remains the primary mechanism for regulating altitude ($y\_pos$) and vertical velocity ($y\_vel$).
2. **Side Engine (Actions 1 & 3) Coupling**: Side engines manage angular tilt ($angle$, $ang\_vel$) but inherently induce lateral displacement ($x\_pos$) and momentum ($x\_vel$).
3. **Extreme Reward Magnitude**: The environment exhibits massive reward oscillations during contact transitions, with magnitudes in the $\pm 25$ range.
4. **Inactivity Risk in Contact**: Using Action 0 (nothing) while in a contact state is a primary driver of gravity-induced total contact loss ($[1,1] \to [0,0]$) and massive negative penalties.
5. **Side Engine Contact Instability**: Using Actions 1 or 3 while in a full-contact $[1,1]$ state frequently induces either partial leg loss ($[1,1] \to [1,0]$ or $[0,1]$) or total contact loss ($[1,1] \to [0,0]$), both of which carry heavy negative rewards.
6. **Contact Restoration Utility**: Side engines (Actions 1 and 3) are effective at transitioning from non-contact $[0,0]$ or partial-contact $[1,0]/[0,1]$ states to a full-contact $[1,1]$ state.
7. **Main Engine Contact Recovery**: Action 2 is a critical tool for recovering from total contact loss ($[0,0]$) to return to a full-contact $[1,1]$ state.
8. **Descent-Phase Reward Differentiation**: During descent (non-contact), Action 2 is the most consistent source of positive rewards, while Action 0 and side engines are typically penalized.
9. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) is the underlying driver for most catastrophic failures, including side-engine-induced contact loss and gravity-induced contact loss.
10. **Contact State Volatility**: The landing phase is characterized by rapid, high-magnitude reward oscillations as the agent fluctuates between $[1,1]$, $[1,0]$, $[0,1]$, and $[0,0]$ states.

---

## 2026-07-05 17:14:31

1. **Main Engine (Action 2) Verticality**: Action 2 remains the primary mechanism for regulating altitude ($y\_pos$) and vertical velocity ($y\_vel$).
2. **Side Engine (Actions 1 & 3) Coupling**: Side engines manage angular tilt ($angle$, $ang\_vel$) but inherently induce lateral displacement ($x\_pos$) and momentum ($x\_vel$).
3. **Extreme Transition Rewards**: Contact state transitions (e.g., $[0,0] \to [1,1]$ or $[1,1] \to [0,0]$) trigger massive reward or penalty spikes, often exceeding $\pm 20$.
4. **Inactivity-Induced Contact Loss**: Using Action 0 (nothing) while in a full-contact $[1,1]$ state is a primary driver of gravity-induced contact loss (transitioning to $[0,1]$ or $[0,0]$), resulting in heavy negative rewards.
5. **Side Engine Contact Instability**: Using side engines (Actions 1 or 3) while in a full-contact $[1,1]$ state frequently induces either partial leg loss ($[1,0]$ or $[0,1]$) or total contact loss ($[0,0]$).
6. **Contact Restoration Utility**: Side engines (Actions 1 and 3) are highly effective at transitioning from non-contact $[0,0]$ or partial-contact $[1,0]/[0,1]$ states to a full-contact $[1,1]$ state.
7. **Main Engine Contact Recovery/Risk**: Action 2 is a critical tool for recovering from total contact loss ($[0,0]$) to return to $[1,1]$, but it can also trigger sudden contact loss if used while already in a $[1,1]$ state.
8. **Descent-Phase Reward Differentiation**: During descent (non-contact), Action 2 is the most consistent source of positive rewards, while Action 0 and side engines are typically penalized.
9. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) is the underlying driver for most catastrophic failures, including side-engine-induced contact loss and gravity-induced contact loss.
10. **Contact State Volatility**: The landing phase is characterized by extreme volatility, where single actions can cause rapid, high-magnitude reward oscillations as the agent fluctuates between $[1,1]$, $[1,0]$, $[0,1]$, and $[0,0]$ states.

---

## 2026-07-05 17:17:11

1. **Main Engine (Action 2) Verticality**: Action 2 remains the primary mechanism for regulating altitude ($y\_pos$) and vertical velocity ($y\_vel$) throughout all phases.
2. **Side Engine (Actions 1 & 3) Coupling**: Side engines manage angular tilt ($angle$, $ang\_vel$) but inherently induce lateral displacement ($x\_pos$) and momentum ($x\_vel$).
3. **High-Magnitude Transition Rewards**: Contact state transitions trigger extreme reward or penalty spikes; transitions from non-contact to contact (e.g., $[0,0] \to [1,0]$) yield massive positive rewards ($>10$), while losing contact (e.g., $[1,1] \to [0,0]$) triggers massive penalties (often $<-15$).
4. **Inactivity-Induced Contact Loss**: Using Action 0 (nothing) while in a full-contact $[1,1]$ state is a primary driver of gravity-induced contact loss, often resulting in a transition to $[0,0]$ and heavy negative rewards.
5. **Side Engine Contact Instability**: Using side engines (Actions 1 or 3) while in a full-contact $[1,1]$ state is highly destabilizing and frequently induces either partial leg loss ($[1,0]$ or $[0,1]$) or total contact loss ($[0,0]$).
6. **Side Engine Contact Restoration**: Side engines (Actions 1 and 3) are highly effective at transitioning the lander from a partial-contact state ($[1,0]$ or $[0,1]$) to a full-contact state ($[1,1]$).
7. **Main Engine Recovery Dynamics**: Action 2 is a critical tool for recovering from total contact loss ($[0,0]$) to return to a partial-contact state ($[1,0]$), but it carries the risk of inducing sudden contact loss if used during unstable contact.
8. **Descent-Phase Reward Differentiation**: During descent (non-contact), Action 2 is the most consistent source of positive rewards, while Action 0 and side engines are typically penalized.
9. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) is the underlying driver for most catastrophic failures, including side-engine-induced contact loss and gravity-induced contact loss.
10. **Contact State Volatility**: The landing phase is characterized by extreme volatility, where single actions can cause rapid, high-magnitude reward oscillations as the agent fluctuates between $[1,1]$, $[1,0]$, $[0,1]$, and $[0,0]$ states.

---

## 2026-07-05 17:22:12

1. **Main Engine (Action 2) Verticality**: Action 2 remains the primary mechanism for regulating altitude ($y\_pos$) and vertical velocity ($y\_vel$) throughout all phases.
2. **Side Engine (Actions 1 & 3) Coupling**: Side engines manage angular tilt ($angle$, $ang\_vel$) but induce lateral displacement ($x\_pos$) and momentum ($x\_vel$); Action 1 and Action 3 induce lateral movement in opposite directions.
3. **Non-Contact to Partial Contact Rewards**: Transitioning from a non-contact state $[0,0]$ to a partial-contact state ($[1,0]$ or $[0,1]$) triggers significant positive rewards (typically $>10$).
4. **Partial to Full Contact Restoration Rewards**: Transitioning from partial contact ($[1,0]$ or $[0,1]$) to full contact ($[1,1]$) provides massive reward spikes, often exceeding 10 and reaching as high as $>20$.
5. **Contact Loss Penalty Hierarchy**: Transitioning from full contact to total loss ($[1,1] \to [0,0]$) is more severely penalized (often $<-15$) than transitioning from full contact to partial contact ($[1,1] \to [1,0]$ or $[0,1]$).
6. **Inactivity-Induced Contact Loss**: Using Action 0 (nothing) while in descent or during unstable contact allows gravity to accelerate vertical velocity, frequently causing contact loss.
7. **Side Engine Contact Instability**: Firing side engines (Actions 1 or 3) while in any contact state ($[1,1]$, $[1,0]$, or $[0,1]$) is highly destabilizing and frequently induces further leg loss or total contact loss.
8. **Side Engine Contact Restoration**: Side engines (Actions 1 and 3) are highly effective at transitioning the lander from a partial-contact state ($[1,0]$ or $[0,1]$) to a full-contact state ($[1,1]$).
9. **Main Engine Contact Recovery**: Action 2 is a critical tool for recovering from total contact loss ($[0,0]$) to return to a partial-contact state.
10. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) is the primary driver for most catastrophic failures, including side-engine-induced contact loss and gravity-induced descent instability.

---

## 2026-07-05 17:24:50

1. **Main Engine (Action 2) Verticality**: Action 2 remains the primary mechanism for regulating altitude ($y\_pos$) and vertical velocity ($y\_vel$) throughout all flight phases.
2. **Side Engine (Actions 1 & 3) Coupling**: Side engines manage angular tilt ($angle$, $ang\_vel$) but induce significant lateral displacement ($x\_pos$) and momentum ($x\_vel$).
3. **Non-Contact to Partial Contact Rewards**: Transitioning from a non-contact state $[0,0]$ to a partial-contact state ($[1,0]$ or $[0,1]$) triggers significant positive rewards, typically observed in the range of $10$ to $20$.
4. **Partial to Full Contact Restoration Rewards**: Transitioning from a partial-contact state ($[1,0]$ or $[0,1]$) to a full-contact state ($[1,1]$) provides massive reward spikes.
5. **Contact Loss Penalty Hierarchy**: Transitioning from full contact to total loss ($[1,1] \to [0,0]$), particularly when triggered by side engines, is severely penalized, frequently resulting in rewards $<-15$.
6. **Side Engine Stability Duality**: Actions 1 and 3 serve a dual purpose: they are highly effective at transitioning the lander from partial to full contact, yet they are highly destabilizing and often cause total contact loss if fired while in any contact state.
7. **Inactivity (Action 0) Dynamics**: While using Action 0 allows gravity to accelerate vertical descent (increasing the risk of high-velocity impact), it can also be used to stabilize the lander during the final settling phase once descent is controlled.
8. **Main Engine Contact Recovery**: Action 2 is a critical tool for recovering from total contact loss ($[0,0]$) to return the lander to a partial-contact state.
9. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) is the primary driver for most catastrophic contact loss events, often exacerbated by side-engine-induced corrections.
10. **Lateral Displacement Coupling**: Side engine usage (Actions 1 and 3) creates lateral drift ($x\_pos$) that requires careful compensation to prevent the lander from deviating significantly from its landing coordinate.

---

## 2026-07-05 17:28:00

1. **Main Engine (Action 2) Verticality**: Action 2 is the primary mechanism for regulating altitude ($y\_pos$) and vertical velocity ($y\_vel$) throughout the descent.
2. **Side Engine (Actions 1 & 3) Angular Control**: Actions 1 and 3 are the primary tools for managing angular tilt ($angle$) and angular velocity ($ang\_vel$).
3. **Initial Contact Reward Magnitude**: The transition from a non-contact state ($[0,0]$) to any partial-contact state ($[1,0]$ or $[0,1]$) triggers significant positive rewards, typically observed in the $10$ to $14$ range.
4. **Post-Contact Reward Scaling**: While transitioning from a partial-contact state ($[1,0]$ or $[0,1]$) to a full-contact state ($[1,1]$) provides positive reward, the magnitude is significantly lower than the initial contact spike.
5. **Contact Loss Penalty Hierarchy**: Transitioning from full contact ($[1,1]$) to total loss ($[0,0]$) is severely penalized, with rewards frequently dropping below $-15$.
6. **Engine-Induced Contact Loss**: Once the lander has achieved contact, firing either the main engine (Action 2) or the side engines (Actions 1 and 3) carries a high risk of triggering immediate contact loss.
7. **Inactivity (Action 0) Dynamics**: Action 0 can be utilized to stabilize the lander during the final settling phase once contact is established, though it allows gravity to continue influencing vertical velocity.
8. **Main Engine Contact Recovery**: Action 2 serves as a critical mechanism for recovering from a total contact loss ($[0,0]$) to return the lander to a partial-contact state.
9. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) is the primary driver for most catastrophic contact loss events.
10. **Lateral Displacement Coupling**: Side engine usage (Actions 1 and 3) induces lateral momentum ($x\_vel$) and displacement ($x\_pos$), requiring careful management to avoid deviating from the landing coordinate.

---

## 2026-07-05 17:30:00

1. **Main Engine (Action 2) Verticality**: Action 2 is the primary mechanism for regulating altitude ($y\_pos$) and vertical velocity ($y\_vel$).
2. **Side Engine (Actions 1 & 3) Angular Control**: Actions 1 and 3 are the primary tools for managing angular tilt ($angle$) and angular velocity ($ang\_vel$).
3. **Initial Contact Reward Magnitude**: The transition to a contact state ($[1,0]$, $[0,1]$, or $[1,1]$) triggers significant positive rewards, typically in the $10$ to $14$ range.
4. **Contact Loss Penalty Severity**: Transitioning from a contact state to a non-contact state ($[0,0]$) is heavily penalized, with rewards frequently reaching magnitudes between $-7$ and $-18$.
5. **Contact-State Reward Instability**: Even when contact is maintained ($[1,1]$), the environment can issue large negative rewards if vertical or angular velocities are not sufficiently controlled.
6. **Contact Oscillation Dynamics**: Once contact is established, the lander can enter cycles of losing and regaining contact, with recovery events triggering positive rewards.
7. **Engine-Induced Contact Loss**: Firing any engine (Actions 1, 2, or 3) once contact is established carries a high risk of triggering immediate contact loss.
8. **Terminal Success Reward**: A successful landing, resulting in a stable contact state at the episode's end, provides a massive terminal reward (e.g., $100$).
9. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) is a primary driver for both contact loss events and negative reward spikes during the landing phase.
10. **Lateral Displacement Coupling**: Side engine usage (Actions 1 and 3) induces lateral momentum ($x\_vel$) and displacement ($x\_pos$).

---

## 2026-07-05 17:33:07

1. **Main Engine (Action 2) Verticality**: Action 2 is the primary mechanism for regulating altitude ($y\_pos$) and vertical velocity ($y\_vel$).
2. **Side Engine (Actions 1 & 3) Angular Control**: Actions 1 and 3 are the primary tools for managing angular tilt ($angle$) and angular velocity ($ang\_vel$), but their frequent use during descent often results in consistent negative rewards.
3. **Initial Contact Reward Magnitude**: Transitioning to a contact state ($[1,0]$, $[0,1]$, or $[1,1]$) triggers significant positive rewards, typically in the $10$ to $14$ range.
4. **Contact Loss Penalty Severity**: Transitioning from a contact state to a non-contact state ($[0,0]$) is heavily penalized, with rewards frequently in the $-15$ to $-18$ range.
5. **Contact Recovery Reward**: Re-establishing contact after a loss (transitioning from $[0,0]$ back to a contact state) provides substantial positive rewards, ranging from approximately $9$ to $23$.
6. **Engine-Induced Contact Loss**: Firing any engine (Actions 1, 2, or 3) once contact is established carries a high risk of triggering immediate contact loss.
7. **Lateral Displacement Coupling**: Side engine usage (Actions 1 and 3) induces lateral momentum ($x\_vel$) and displacement ($x\_pos$).
8. **Descent Phase Reward Volatility**: Continuous side-engine corrections during the descent phase often generate a high frequency of negative rewards, even if the angular tilt remains relatively small.
9. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) is a primary driver for both contact loss events and negative reward spikes during the landing phase.
10. **Post-Contact Stability Requirements**: Once contact is established, maintaining the state requires minimizing engine activity, as thrusting frequently interrupts the contact state.

---

## 2026-07-05 17:41:14

---
1. **Main Engine (Action 2) Altitude/Velocity Regulation**: Action 2 is the primary mechanism for regulating altitude ($y\_pos$) and vertical velocity ($y\_vel$) throughout both the descent and post-contact phases.
2. **Side Engine (Actions 1 & 3) Angular/Lateral Control**: Actions 1 and 3 are the tools for managing angular tilt ($angle$), angular velocity ($ang\_vel$), and lateral displacement ($x\_pos$, $x\_vel$).
3. **Contact Reward Magnitude and Variability**: Transitioning to a contact state ($[1,0]$, $[0,1]$, or $[1,1]$) triggers significant positive rewards, typically in the $10$ to $14$ range, though magnitude can vary significantly depending on impact conditions.
4. **Contact Loss Penalty Severity**: Transitioning from a contact state to a non-contact state ($[0,0]$) is heavily penalized, with rewards frequently in the $-8$ to $-15$ range.
5. **Contact Recovery Reward**: Re-establishing contact after a loss (transitioning from $[0,0]$ back to any contact state) provides substantial positive rewards, often ranging from $11$ to $13$.
6. **Engine-Induced Contact Disruption**: Firing any engine (Actions 1, 2, or 3) while a contact state is established carries a high risk of triggering immediate contact loss ($[0,0]$).
7. **Lateral-Angular Momentum Coupling**: The use of side engines (Actions 1 and 3) induces lateral momentum ($x\_vel$) and displacement ($x\_pos$), coupling lateral movement with angular corrections.
8. **Descent Phase Reward Volatility**: Continuous side-engine corrections during the descent phase often generate high-frequency negative rewards, even when angular tilt remains relatively small.
9. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) is a primary driver for both contact loss events and significant negative reward spikes during the landing phase.
10. **Partial Contact State Dynamics**: The environment supports partial contact states (e.g., $[1,0]$ or $[0,1]$); transitioning between these states or into full contact ($[1,1]$) is a key component of maintaining stability.

---

## 2026-07-05 17:43:23

---
1. **Main Engine (Action 2) Altitude/Velocity Regulation**: Action 2 is the primary mechanism for regulating altitude ($y\_pos$) and vertical velocity ($y\_vel$) throughout both the descent and post-contact phases.
2. **Side Engine (Actions 1 & 3) Angular/Lateral Control**: Actions 1 and 3 are the tools for managing angular tilt ($angle$), angular velocity ($ang\_vel$), and lateral displacement ($x\_pos$, $x\_vel$).
3. **Contact Reward Magnitude and Variability**: Transitioning to a contact state ($[1,0]$, $[0,1]$, or $[1,1]$) triggers significant positive rewards, which can range from approximately $8$ to over $21$ depending on the impact conditions.
4. **Contact Loss Penalty Severity**: Transitioning from a contact state to a non-contact state ($[0,0]$) is heavily penalized, with rewards frequently falling in the $-10$ to $-20$ range.
5. **Contact Recovery Reward**: Re-establishing contact after a loss (transitioning from $[0,0]$ back to any contact state) provides substantial positive rewards, often ranging from $8$ to $13$.
6. **Engine-Induced Contact Disruption**: Firing side engines (Actions 1 and 3) while a contact state is established carries a higher risk of triggering immediate contact loss ($[0,0]$) compared to the main engine (Action 2).
7. **Lateral-Angular Momentum Coupling**: The use of side engines (Actions 1 and 3) induces lateral momentum ($x\_vel$) and displacement ($x\_pos$), coupling lateral movement with angular corrections.
8. **Descent Phase Reward Volatility**: Continuous or rapid-fire side-engine corrections during the descent phase often generate high-frequency negative rewards, even when angular tilt remains relatively small.
9. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) is a primary driver for both contact loss events and significant negative reward spikes during the landing phase.
10. **Contact State Transitions**: The environment supports partial contact states (e.g., $[1,0]$ or $[0,1]$); the stability of the lander is highly dependent on managing transitions between these partial states and full contact ($[1,1]$).

---

## 2026-07-05 17:45:27

1. **Main Engine (Action 2) Altitude/Velocity Regulation**: Action 2 is the primary mechanism for regulating altitude ($y\_pos$) and vertical velocity ($y\_vel$) throughout both the descent and post-contact phases.
2. **Side Engine (Actions 1 & 3) Angular/Lateral Control**: Actions 1 and 3 are the tools for managing angular tilt ($angle$), angular velocity ($ang\_vel$), and lateral displacement ($x\_pos$, $x\_vel$).
3. **Contact Reward Magnitude**: Transitioning into a contact state ($[1,0]$, $[0,1]$, or $[1,1]$) triggers significant positive rewards, typically ranging from approximately $8$ to $22$ depending on the impact conditions.
4. **Contact Loss Penalty Severity**: Transitioning from a contact state to a non-contact state ($[0,0]$) is heavily penalized, with rewards frequently falling in the $-15$ to $-20$ range.
5. **Contact Recovery Reward**: Re-establishing contact after a loss (transitioning from $[0,0]$ back to any contact state) provides substantial positive rewards, often ranging from $12$ to $23$.
6. **Engine-Induced Contact Disruption**: Firing any engine (Actions 1, 2, or 3) while a contact state is established carries a high risk of triggering immediate contact loss ($[0,0]$), especially if vertical or angular momentum is not stabilized.
7. **Lateral-Angular Momentum Coupling**: The use of side engines (Actions 1 and 3) induces lateral momentum ($x\_vel$) and displacement ($x\_pos$), coupling lateral movement with angular corrections.
8. **Descent Phase Reward Volatility**: Continuous or rapid-fire side-engine corrections during the descent phase often generate high-frequency negative rewards, even when angular tilt remains relatively small.
9. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) is a primary driver for both contact loss events and significant negative reward spikes during the landing phase.
10. **Contact State Transitions**: The environment supports partial contact states (e.g., $[1,0]$ or $[0,1]$); the stability of the lander is highly dependent on managing transitions between these partial states and full contact ($[1,1]$) without regressing to $[0,0]$.

---

## 2026-07-05 17:48:11

1. **Main Engine (Action 2) Altitude/Velocity Regulation**: Action 2 remains the primary mechanism for managing vertical position ($y\_pos$) and vertical velocity ($y\_vel$) during descent and landing.
2. **Side Engine (Actions 1 & 3) Angular/Lateral Control**: Actions 1 and 3 are the primary tools for controlling angular tilt ($angle$), angular velocity ($ang\_vel$), and lateral displacement/velocity ($x\_pos, x\_vel$).
3. **Contact Reward Magnitude**: Transitioning from a non-contact state to any contact state ($[1,0], [0,1], [1,1]$) triggers significant positive rewards, typically ranging from $8$ to $23$.
4. **Total Contact Loss Penalty**: Transitioning from any contact state to a non-contact state ($[0,0]$) is heavily penalized, with rewards frequently falling in the $-10$ to $-20$ range.
5. **Partial Contact Loss Penalty**: Transitioning from a full contact state ($[1,1]$) to a partial contact state ($[1,0]$ or $[0,1]$) can trigger severe negative rewards, sometimes matching the magnitude of total contact loss.
6. **Contact Recovery Reward**: Re-establishing any form of contact after total loss (transitioning from $[0,0]$ back to any contact state) provides substantial positive rewards.
7. **Engine-Induced Contact Disruption**: Firing any engine (Actions 1, 2, or 3) while a contact state is established carries a high risk of triggering immediate contact loss or a transition to a partial contact state.
8. **Lateral-Angular Momentum Coupling**: The use of side engines (Actions 1 and 3) induces lateral momentum ($x\_vel$) and displacement ($x\_pos$), coupling lateral movement with angular corrections.
9. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) is a primary driver for both contact loss events and significant negative reward spikes during the landing phase.
10. **Contact State Transition Dynamics**: The environment supports complex transitions between partial ($[1,0], [0,1]$) and full ($[1,1]$) contact; stability is highly dependent on managing these transitions without regressing to $[0,0]$.

---

## 2026-07-05 17:50:21

1. **Main Engine (Action 2) Altitude/Velocity Regulation**: Action 2 remains the primary mechanism for managing vertical position ($y\_pos$) and vertical velocity ($y\_vel$) during descent and landing.
2. **Side Engine (Actions 1 & 3) Angular/Lateral Control**: Actions 1 and 3 are the primary tools for controlling angular tilt ($angle$), angular velocity ($ang\_vel$), and lateral displacement/velocity ($x\_pos, x\_vel$).
3. **Side Engine Operational Cost**: Firing side engines (Actions 1 and 3) incurs a consistent negative reward penalty (typically between $-1.5$ and $-2.8$), representing the inherent cost of lateral correction.
4. **Action 0 (Nothing) Penalty**: Taking no action (Action 0) results in regular negative rewards (frequently $-1.5$ to $-2.8$), suggesting a penalty for lack of thrust or failure to maintain stability.
5. **Contact State Transition Rewards/Penalties**: Transitions between contact states ($[1,0], [0,1], [1,1]$) and non-contact states ($[0,0]$) trigger significant reward fluctuations, with losses being heavily penalized and successes being rewarded.
6. **Contact Recovery Reward**: Re-establishing any form of contact after total loss (transitioning from $[0,0]$ back to any contact state) provides substantial positive rewards, often exceeding $+10$.
7. **Engine-Induced Contact Disruption**: Firing any engine (especially side engines) while a contact state is established carries a high risk of triggering immediate contact loss or a transition to a partial contact state.
8. **Lateral-Angular Momentum Coupling**: The use of side engines (Actions 1 and 3) induces lateral momentum ($x\_vel$) and displacement ($x\_pos$), coupling lateral movement with angular corrections.
9. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) is a primary driver for both contact loss events and significant negative reward spikes during the landing phase.
10. **Extreme Instability Penalties**: Contact loss during periods of high instability or high angular velocity can trigger extreme negative rewards (e.g., $<-15$), far exceeding standard contact loss penalties.

---

## 2026-07-05 17:55:53

---
1. **Main Engine (Action 2) Altitude/Velocity Regulation**: Action 2 remains the primary mechanism for managing vertical position ($y\_pos$) and vertical velocity ($y\_vel$) during descent and landing.
2. **Side Engine (Actions 1 & 3) Angular/Lateral Control**: Actions 1 and 3 are the primary tools for controlling angular tilt ($angle$), angular velocity ($ang\_vel$), and lateral displacement/velocity ($x\_pos, x\_vel$).
3. **Contact Re-establishment Rewards**: Transitioning from a non-contact state ($[0,0]$) to any contact state ($[1,0], [0,1], [1,1]$) triggers substantial positive rewards, often exceeding $+10$.
4. **Action 0 (Nothing) Contact Instability**: Taking no action (Action 0) while in a contact state ($[1,0], [0,1], [1,1]$) is highly dangerous and can trigger extreme negative rewards (e.g., $<-15$ or even $<-20$) if the lander loses stability or contact.
5. **Engine-Induced Contact Disruption**: Firing engines (specifically side engines or the main engine) while a contact state is established carries a significant risk of triggering immediate contact loss or a transition back to the non-contact state ($[0,0]$).
6. **Side Engine/No-Action Operational Cost**: Firing side engines (Actions 1 and 3) or taking no action (Action 0) during descent results in regular negative rewards (typically $-1.5$ to $-2.8$).
7. **Lateral-Angular Momentum Coupling**: The use of side engines (Actions 1 and 3) induces lateral momentum ($x\_vel$) and displacement ($x\_pos$), coupling lateral movement with angular corrections.
8. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) is a primary driver for both contact loss events and significant negative reward spikes during the landing and contact phases.
9. **Extreme Instability Penalties**: Contact loss or sudden state transitions occurring during periods of high instability (high $ang\_vel$, $y\_vel$, or erratic angle) trigger extreme negative rewards that far exceed standard penalties.
10. **Contact State Transition Sensitivity**: Transitions between contact states ($[1,0], [0,1], [1,1]$) and non-contact states ($[0,0]$) cause massive reward fluctuations, where successful re-establishment is highly rewarded and sudden loss is heavily penalized.

---

## 2026-07-05 17:57:52

1. **Main Engine (Action 2) Altitude/Velocity Regulation**: Action 2 is the primary mechanism for managing vertical position ($y\_pos$) and vertical velocity ($y\_vel$). It frequently yields positive rewards when effectively counteracting descent or managing velocity during landing.
2. **Side Engine (Actions 1 & 3) Angular/Lateral Control**: Actions 1 and 3 are the primary tools for controlling angular tilt ($angle$), angular velocity ($ang\_vel$), and lateral displacement/velocity ($x\_pos, x\_vel$).
3. **Contact Re-establishment Rewards**: Transitioning from a non-contact state ($[0,0]$) to any contact state ($[1,0], [0,1], [1,1]$) triggers substantial positive rewards, typically in the $+9$ to $+12$ range.
4. **Action 0 (Nothing) for Stability Maintenance**: Once a stable contact state is established, taking no action (Action 0) can be a viable strategy to maintain the state, often resulting in small positive or near-zero rewards.
5. **Engine-Induced Contact Disruption**: Firing engines (specifically the main engine, Action 2) while a contact state is established carries a significant risk of triggering immediate contact loss (e.g., transitioning from $[1,1]$ back to $[1,0]$ or $[0,0]$).
6. **Side Engine Operational Cost**: Firing side engines (Actions 1 and 3) during descent results in regular negative rewards, typically ranging from approximately $-1.5$ to $-3.0$.
7. **Lateral-Angular Momentum Coupling**: The use of side engines (Actions 1 and 3) induces lateral momentum ($x\_vel$) and displacement ($x\_pos$), coupling lateral movement with necessary angular corrections.
8. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) is a primary driver for both contact loss events and significant negative reward spikes during the landing and contact phases.
9. **Extreme Instability Penalties**: Contact loss or sudden state transitions occurring during periods of high instability (high $ang\_vel$, high $y\_vel$, or erratic angle) trigger extreme negative rewards (e.g., $<-15$ or even $<-18$).
10. **Contact State Transition Sensitivity**: Transitions between contact states and non-contact states cause massive reward fluctuations, where successful re-establishment is highly rewarded and sudden loss is heavily penalized.

---

## 2026-07-05 18:00:00

1. **Main Engine (Action 2) Altitude/Velocity Regulation**: Action 2 is the primary mechanism for managing vertical position ($y\_pos$) and vertical velocity ($y\_vel$), essential for controlling descent rates.
2. **Side Engine (Actions 1 & 3) Angular/Lateral Control**: Actions 1 and 3 are used to control angular tilt ($angle$), angular velocity ($ang\_vel$), and lateral displacement ($x\_pos, x\_vel$).
3. **Contact Re-establishment Rewards**: Transitioning from a non-contact state to any contact state ($[1,0], [0,1], [1,1]$) triggers substantial positive rewards, typically in the $+8$ to $+13.5$ range.
4. **Action 0 (Nothing) for Stability Maintenance**: Once a contact state is established, taking no action (Action 0) is a viable strategy to maintain the state and preserve contact.
5. **Engine-Induced Contact Disruption**: Firing engines (including the main engine, Action 2, and side engines, Actions 1 and 3) while a contact state is established carries a significant risk of triggering immediate contact loss.
6. **Side Engine Cost-Benefit Trade-off**: While side engines (Actions 1 and 3) typically incur negative rewards due to fuel/operational costs, their use can result in net positive rewards if they effectively mitigate angular or lateral instability.
7. **Lateral-Angular Momentum Coupling**: The use of side engines (Actions 1 and 3) induces lateral momentum ($x\_vel$) and displacement ($x\_pos$), coupling lateral movement with necessary angular corrections.
8. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) is a primary driver for both contact loss events and significant negative reward spikes during the landing and contact phases.
9. **Contact Loss Penalties**: Sudden transitions from a contact state back to a non-contact state ($[0,0]$ or partial loss) trigger significant negative rewards, typically ranging from approximately $-8$ to $-18$.
10. **Contact State Transition Sensitivity**: Transitions between contact states and non-contact states cause massive reward fluctuations, where successful re-establishment is highly rewarded and sudden loss is heavily penalized.

---

## 2026-07-05 18:02:54

1. **Main Engine (Action 2) Altitude/Velocity Regulation**: Action 2 is the primary mechanism for managing vertical position ($y\_pos$) and vertical velocity ($y\_vel$), essential for controlling descent rates.
2. **Side Engine (Actions 1 & 3) Angular/Lateral Control**: Actions 1 and 3 are used to control angular tilt ($angle$), angular velocity ($ang\_vel$), and lateral displacement ($x\_pos, x\_vel$).
3. **Contact Re-establishment Rewards**: Transitioning from a non-contact state ($[0,0]$) to any contact state ($[1,0], [0,1], [1,1]$) triggers substantial positive rewards, typically in the $+10$ to $+13.8$ range.
4. **Action 0 (Nothing) for Stability Maintenance**: Once a contact state is established, taking no action (Action 0) is a viable strategy to attempt to maintain the state and preserve contact.
5. **Engine-Induced Contact Disruption**: Firing engines (including the main engine, Action 2, and side engines, Actions 1 and 3) while a contact state is established carries a high risk of triggering immediate contact loss.
6. **Contact Loss Penalties**: Sudden transitions from a contact state back to a non-contact or partial contact state trigger significant negative rewards, typically ranging from approximately $-7.9$ to $-16.8$.
7. **Lateral-Angular Momentum Coupling**: The use of side engines (Actions 1 and 3) induces lateral momentum ($x\_vel$) and displacement ($x\_pos$), coupling lateral movement with necessary angular corrections.
8. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) is a primary driver for both contact loss events and significant negative reward spikes during the landing and contact phases.
9. **Contact State Oscillation (Chattering)**: During the final stages of descent/landing, the lander can experience rapid "chattering" or oscillation between different contact states ($[0,0] \leftrightarrow [1,0] \leftrightarrow [0,1] \leftrightarrow [1,1]$).
10. **Contact State Transition Sensitivity**: Transitions between contact states and non-contact states cause massive reward fluctuations, where successful re-establishment is highly rewarded and sudden loss is heavily penalized.

---

## 2026-07-05 18:04:40

1. **Main Engine (Action 2) Altitude/Velocity Regulation**: Action 2 is the primary mechanism for managing vertical position ($y\_pos$) and vertical velocity ($y\_vel$). It is also a critical tool for re-establishing contact during descent.
2. **Side Engine (Actions 1 & 3) Angular/Lateral Control**: Actions 1 and 3 manage angular tilt ($angle$), angular velocity ($ang\_vel$), and lateral displacement ($x\_pos, x\_vel$). These actions can also be used to trigger contact re-establishment.
3. **Contact Re-establishment Rewards**: Transitions from a non-contact state ($[0,0]$) to any contact state ($[1,0], [0,1], [1,1]$) trigger substantial positive rewards, typically ranging from approximately $+10$ to $+16.2$.
4. **Contact Loss Penalties**: Sudden transitions from a contact state back to a non-contact or partial contact state trigger significant negative rewards, often ranging from approximately $-7.5$ to $-17.5$.
5. **Engine-Induced Contact Disruption**: Firing engines (including the main engine, Action 2, and side engines, Actions 1 and 3) while a contact state is established carries a high risk of triggering immediate contact loss.
6. **Action 0 (Nothing) Stability and Risk**: While Action 0 is a strategy for stability maintenance, it can also lead to contact loss if the lander's momentum or orientation is not sufficiently stabilized, resulting in significant penalties.
7. **Lateral-Angular Momentum Coupling**: The use of side engines (Actions 1 and 3) induces lateral momentum ($x\_vel$) and displacement ($x\_pos$), coupling lateral movement with necessary angular corrections.
8. **Angular Velocity Instability**: High angular velocity ($ang\_vel$) is a primary driver for both contact loss events and significant negative reward spikes during the landing and contact phases.
9. **Contact State Oscillation (Chattering)**: During the final stages of descent/landing, the lander can experience rapid "chattering" or oscillation between different contact states ($[0,0] \leftrightarrow [1,0] \leftrightarrow [0,1] \leftrightarrow [1,1]$).
10. **Contact State Transition Sensitivity**: Transitions between contact states and non-contact states cause massive reward fluctuations, where successful re-establishment is highly rewarded and sudden loss is heavily penalized.

---

## 2026-07-05 18:13:52

1. **Main Engine (Action 2) Altitude/Velocity Regulation**: Action 2 is the primary mechanism for managing vertical position ($y\_pos$) and vertical velocity ($y\_vel$). It is used extensively both during descent and to maintain altitude once contact is established.
2. **Side Engine (Actions 1 & 3) Angular/Lateral Control**: Actions 1 and 3 are used to manage angular tilt ($angle$), angular velocity ($ang\_vel$), and lateral displacement ($x\_pos, x\_vel$).
3. **Contact Re-establishment Rewards**: Transitions from a non-contact state ($[0,0]$) or a partial contact state ($[1,0], [0,1]$) to a different contact state (e.g., $[0,1] \to [1,1]$) trigger substantial positive rewards, typically ranging from approximately $+9.0$ to $+23.0$.
4. **Contact Loss Penalties**: Transitions from a contact state ($[1,0], [0,1], [1,1]$) back to a non-contact state ($[0,0]$) or to a different partial contact state trigger significant negative rewards, often ranging from approximately $-7.8$ to $-17.4$.
5. **Post-Contact Maintenance Strategy**: Once contact is established, the lander can maintain stability for long durations by alternating between engine actions (1, 2, 3) and Action 0 (Nothing) to balance altitude, tilt, and lateral movement.
6. **Angular Velocity and Stability**: High angular velocity ($ang\_vel$) is a primary driver of contact loss events; stabilizing $ang\_vel$ is critical during the landing and contact phases to avoid negative reward spikes.
7. **Engine-Induced Contact Loss**: Firing the main engine (Action 2) while in a contact state carries a risk of triggering immediate contact loss if the vertical or angular momentum is not perfectly managed.
8. **Lateral-Angular Momentum Coupling**: The use of side engines (Actions 1 and 3) induces both lateral momentum ($x\_vel$) and angular corrections, coupling lateral displacement with necessary tilt adjustments.
9. **Action 0 Stability and Risk**: While Action 0 (Nothing) is used to maintain a stabilized state, it can also lead to contact loss if the lander's existing momentum or orientation is not sufficiently stabilized.
10. **Contact State Transition Sensitivity**: The environment is highly sensitive to transitions between contact states, where successful re-establishment is highly rewarded and sudden loss of contact is heavily penalized, often occurring in rapid succession (e.g., $[1,1] \to [0,1] \to [1,1]$).

---

## 2026-07-05 18:16:53

1. **Main Engine (Action 2) Verticality Control**: Action 2 is the primary mechanism for regulating vertical position ($y\_pos$) and vertical velocity ($y\_vel$).
2. **Side Engine (Actions 1 & 3) Attitude and Lateral Control**: Actions 1 and 3 are used to manage angular tilt ($angle$), angular velocity ($ang\_vel$), and lateral displacement ($x\_pos, x\_vel$).
3. **Contact Re-establishment Rewards**: Transitions into higher contact states (e.g., from $[0,1]$ to $[1,1]$ or $[0,0]$ to $[1,1]$) trigger substantial positive rewards.
4. **Contact Loss Penalties**: Transitions from any contact state ($[1,0], [0,1], [1,1]$) back to a non-contact state ($[0,0]$) or to a different partial contact state trigger significant negative rewards.
5. **Main Engine Instability during Contact**: Firing the main engine (Action 2) while the lander is in a contact state carries a high risk of triggering immediate contact loss if the resulting vertical or angular momentum is not perfectly managed.
6. **Side Engine Contact State Flipping**: In a partial contact state (e.g., $[1,0]$ or $[0,1]$), using side engines (Actions 1 or 3) can cause the currently engaged leg to lose contact while the other leg gains it (e.g., $[1,0] \to [0,1]$), resulting in a contact loss penalty.
7. **Angular Velocity ($ang\_vel$) as a Stability Driver**: High angular velocity is a primary driver of contact loss; stabilizing $ang\_vel$ is a critical prerequisite for both landing and maintaining stability during the ground phase.
8. **Lateral-Angular Momentum Coupling**: The use of side engines (Actions 1 and 3) induces both lateral momentum ($x\_vel$) and angular corrections, coupling lateral displacement adjustments with necessary tilt management.
9. **Action 0 Stability and Risk**: While Action 0 (Nothing) is used to maintain a stabilized state, it can lead to contact loss if the lander's existing momentum or orientation is not sufficiently stabilized before thrust ceases.
10. **High Contact State Volatility**: The environment is highly sensitive to transitions between contact states, where successful re-establishment and sudden loss of contact can occur in rapid, successive steps.

---

## 2026-07-05 18:18:17

1. **Main Engine (Action 2) Verticality Control**: Action 2 is the primary mechanism for regulating vertical position ($y\_pos$) and vertical velocity ($y\_vel$).
2. **Side Engine (Actions 1 & 3) Attitude and Lateral Control**: Actions 1 and 3 are used to manage angular tilt ($angle$), angular velocity ($ang\_vel$), and lateral displacement ($x\_pos, x\_vel$).
3. **Contact Re-establishment Rewards**: Transitions into higher contact states (e.g., from $[0,0]$ to $[1,0]$ or $[1,1]$) trigger substantial positive rewards, which can be very large (e.g., $>15.0$) during successful touchdown.
4. **Contact Loss Penalties**: Transitions from any contact state back to a non-contact state ($[0,0]$) or to a different partial contact state (e.g., $[1,1] \to [0,1]$) trigger significant negative rewards.
5. **Main Engine Induced Bouncing**: Firing the main engine (Action 2) while in a full contact state ($[1,1]$) can generate enough upward vertical momentum to cause a "bounce," potentially triggering a cascade of contact loss transitions (e.g., $[1,1] \to [0,1] \to [0,0]$).
6. **Side Engine Contact State Flipping**: In a partial contact state (e.g., $[1,0]$ or $[0,1]$), using side engines (Actions 1 or 3) can cause the currently engaged leg to lose contact while the other leg gains it, resulting in a contact loss penalty.
7. **Angular Velocity ($ang\_vel$) as a Primary Instability Driver**: High angular velocity is a primary driver of contact loss; stabilizing $ang\_vel$ is a critical prerequisite for both landing and maintaining stability during the ground phase.
8. **Lateral-Angular Momentum Coupling**: The use of side engines (Actions 1 and 3) induces both lateral momentum ($x\_vel$) and angular corrections, coupling lateral displacement adjustments with necessary tilt management.
9. **Action 0 Stability and Risk**: While Action 0 (Nothing) is used to maintain a stabilized state, it can lead to contact loss if the lander's existing momentum or orientation is not sufficiently stabilized before thrust ceases.
10. **Extreme Reward Volatility during Contact Transitions**: The environment is highly sensitive to contact state transitions, where massive positive and negative reward spikes occur in rapid succession during touchdown, bouncing, or contact loss events.

---

## 2026-07-05 18:54:37

---


---

## 2026-07-05 18:57:06

1. **Main Engine (Action 2)**: Primarily used to adjust vertical velocity (`y_vel`) to manage altitude and counteract gravity.
2. **Lateral Engines (Actions 1 and 3)**: Used to apply torque, directly influencing angular velocity (`ang_vel`) and the lander's angle to maintain orientation.
3. **Gravity**: Exerts a constant downward acceleration, causing `y_vel` to decrease over time when no upward thrust is applied.
4. **Contact Mechanics**: The `left_leg_contact` and `right_leg_contact` flags transition to 1.0 once the lander's altitude (`y_pos`) reaches the ground.
5. **Landing Reward Logic**: High positive rewards are granted when the lander makes ground contact with low vertical (`y_vel`) and angular (`ang_vel`) velocities.
6. **Crash Penalties**: High-velocity impacts (large `y_vel` or `ang_vel` at the moment of contact) result in significant negative rewards.
7. **Horizontal Coupling**: All engine actions (1, 2, and 3) induce changes in horizontal position (`x_pos`) and velocity (`x_vel`), requiring continuous compensation to remain centered.
8. **Angular Momentum**: Controlling `ang_vel` is critical to prevent the angle from diverging, which can lead to uncontrolled rotation and subsequent crashes.
9. **Descent Control**: Achieving a successful landing requires a controlled deceleration phase where `y_vel` is reduced to near-zero as `y_pos` approaches zero.
10. **Post-Landing Stability**: Once contact is established, the lander can maintain a stable state at the ground level if residual velocities are minimized.

---

## 2026-07-05 19:01:41

1. **Main Engine (Action 2)**: Primarily used to regulate vertical velocity (`y_vel`) to control descent rate and manage altitude.
2. **Lateral Engine Dual-Effect**: Actions 1 (left) and 3 (right) provide torque to influence angular velocity (`ang_vel`) and angle, while simultaneously inducing horizontal translation (`x_pos`) and horizontal velocity (`x_vel`).
3. **Gravity**: Exerts a constant downward acceleration, causing `y_vel` to decrease continuously unless counteracted by upward thrust.
4. **Contact Mechanics**: The `left_leg_contact` and `right_leg_contact` flags transition to 1.0 upon ground impact, marking the transition to the landing/terminal phase.
5. **Landing Reward Spikes**: The environment provides massive positive reward spikes (e.g., 9.0–11.0+) immediately upon successful ground contact, especially when velocities are low.
6. **Impact Penalties**: High-magnitude negative rewards are triggered if contact is made with excessive vertical (`y_vel`) or angular (`ang_vel`) velocities.
7. **Horizontal Coupling and Drift**: All engine actions (1, 2, and 3) induce horizontal movement, meaning any attempt to manage altitude or orientation results in lateral drift that requires constant compensation.
8. **Angular Momentum Management**: Precise control of `ang_vel` is essential to prevent the lander's angle from diverging, which can lead to uncontrolled rotation and subsequent crash penalties.
9. **Velocity-Dependent Rewards**: Reward values are highly sensitive to instantaneous state; maintaining low velocities during the approach to the ground is critical for maximizing the landing bonus.
10. **Terminal State Stability**: Once the lander makes contact (`y_pos` near 0 and leg flags at 1.0), the environment allows for a stable terminal state where residual velocities are minimized.

---

## 2026-07-05 19:03:45

1. **Main Engine (Action 2)**: Primarily used to regulate vertical velocity (`y_vel`) to control descent rate and manage altitude.
2. **Lateral Engine Dual-Effect**: Actions 1 (left) and 3 (right) provide torque to influence angular velocity (`ang_vel`) and angle, while simultaneously inducing horizontal translation (`x_pos`) and horizontal velocity (`x_vel`).
3. **Gravity**: Exerts a constant downward acceleration, causing `y_pos` to decrease and `y_vel` to become increasingly negative unless counteracted by upward thrust.
4. **Ground Contact Mechanics**: The `left_leg_contact` and `right_leg_contact` flags transition to 1.0 upon ground impact, marking the landing phase.
5. **Landing Reward Spikes**: The environment provides massive positive reward spikes (e.g., 11.0+) immediately upon successful, stable ground contact.
6. **Impact and Crash Penalties**: High-magnitude negative rewards (e.g., -17.0+) are triggered by high-velocity impacts or unstable orientation during the contact phase.
7. **Horizontal Coupling and Drift**: All engine actions (1, 2, and 3) induce horizontal movement, meaning any attempt to manage altitude or orientation results in lateral drift that requires constant compensation.
8. **Angular Momentum Management**: Precise control of `ang_vel` is essential to prevent the lander's angle from diverging, which leads to uncontrolled rotation and potential crash penalties.
9. **Velocity-Dependent Reward Sensitivity**: Reward values are highly sensitive to the instantaneous state; maintaining low vertical (`y_vel`) and angular (`ang_vel`) velocities during the approach to the ground is critical for maximizing the landing bonus.
10. **Contact Stability and Crash Transitions**: Ground contact is not necessarily a permanent terminal state; an unstable landing or high-velocity impact can cause the lander to lose contact, transitioning the leg flags from 1.0 back to 0.0 and signifying a crash.

---

## 2026-07-05 19:06:35

1. **Main Engine (Action 2) Multidimensionality**: While primarily used to regulate vertical velocity (`y_vel`) and altitude (`y_pos`), the main engine also induces changes in the lander's `angle` and `ang_vel`.
2. **Left Engine (Action 1) Lateral Direction**: This action provides thrust in the negative x direction, evidenced by the decrease in `x_vel` when applied during positive horizontal movement.
3. **Right Engine (Action 3) Lateral Direction**: This action provides thrust in the positive x direction, evidenced by the increase in `x_vel` when applied.
4. **Lateral-Angular Coupling**: Both lateral engines (Actions 1 and 3) provide simultaneous torque to influence `angle` and `ang_vel` alongside their horizontal translation effects.
5. **Gravity and Descent**: Gravity provides a constant downward acceleration that decreases `y_pos` and makes `y_vel` increasingly negative, requiring constant counter-thrust from Action 2.
6. **Horizontal-Vertical Coupling**: All engine actions (1, 2, and 3) induce horizontal movement, meaning altitude management is inextricably linked to horizontal drift compensation.
7. **Dynamic Ground Contact**: Ground contact is not a permanent terminal state; leg contact flags can transition from 1.0 back to 0.0 if the landing is unstable or if velocities are too high.
8. **Velocity-Sensitive Reward Structure**: The environment heavily weights the instantaneous `y_vel` and `ang_vel` during the contact phase, where low velocities are required to avoid massive crash penalties and secure landing bonuses.
9. **Angular Momentum Divergence**: Without precise control of `ang_vel` through lateral engines, the lander's `angle` can diverge rapidly, leading to uncontrolled rotation and contact loss.
10. **Landing Stability and Contact Loss**: As seen in recent trajectories, an unstable landing can lead to a "bouncing" effect where leg contact is lost and then potentially regained, depending on the subsequent actions and resulting velocities.

---

## 2026-07-05 19:09:50

1. **Main Engine (Action 2) Multidimensionality**: While primarily used to regulate vertical velocity (`y_vel`) and altitude (`y_pos`), the main engine also induces changes in the lander's `angle` and `ang_vel`.
2. **Lateral Engine Directionality**: Action 1 (left engine) provides thrust in the negative x direction, while Action 3 (right engine) provides thrust in the positive x direction.
3. **Lateral-Angular Coupling**: Both lateral engines (Actions 1 and 3) provide simultaneous torque to influence `angle` and `ang_vel` alongside their horizontal translation effects.
4. **Gravity and Descent**: Gravity provides a constant downward acceleration that decreases `y_pos`, requiring continuous main engine counter-thrust to manage the descent rate.
5. **Horizontal-Vertical Coupling**: All engine actions induce horizontal movement, meaning vertical altitude management is inextricably linked to horizontal drift compensation.
6. **Asymmetric Leg Contact**: The environment allows for intermediate contact states where only one leg is grounded (e.g., `[1.0, 0.0]` or `[0.0, 1.0]`), which occurs during the transition to full stabilization.
7. **Ground-Engine Interaction (Bouncing)**: Applying engine thrust while in a grounded state can induce a "bounce," causing an immediate loss of leg contact and resulting in significant negative rewards.
8. **Contact Reacquisition Rewards**: The reward structure provides massive positive spikes when the lander transitions from a non-contact state to a contact state (e.g., transitioning from `[0.0, 0.0]` to `[1.0, 0.0]`).
9. **Angular Momentum Divergence**: Without precise control of `ang_vel` through lateral engines, the lander's `angle` can diverge rapidly, leading to uncontrolled rotation and loss of landing stability.
10. **Velocity-Sensitive Landing Dynamics**: High vertical or angular velocities at the moment of impact trigger severe penalties, necessitating low-velocity control to secure landing bonuses and avoid crash penalties.

---

## 2026-07-05 19:15:29

1. **Main Engine (Action 2) Multidimensionality**: While primarily used to regulate vertical velocity (`y_vel`) and altitude (`y_pos`), the main engine also induces changes in the lander's `angle` and `ang_vel`.
2. **Lateral Engine Directionality**: Action 1 (left engine) provides thrust in the negative x direction, reducing `x_vel`, while Action 3 (right engine) provides thrust in the positive x direction, increasing `x_vel`.
3. **Lateral-Angular Coupling**: Both lateral engines (Actions 1 and 3) provide simultaneous torque to influence `angle` and `ang_vel` alongside their horizontal translation effects.
4. **Gravity and Descent**: Gravity provides a constant downward acceleration that decreases `y_pos`, requiring continuous main engine counter-thrust to manage the descent rate.
5. **Cross-Axis Engine Coupling**: Lateral engine actions (1 and 3) also induce changes in vertical velocity (`y_vel`), meaning horizontal drift compensation and vertical altitude management are coupled.
6. **Asymmetric Leg Contact**: The environment allows for intermediate contact states where only one leg is grounded (e.g., `[1.0, 0.0]` or `[0.0, 1.0]`), typically occurring during the transition to full stabilization.
7. **Landing Transition Rewards**: The reward structure provides massive positive spikes when the lander transitions from a non-contact state to a contact state (e.g., transitioning from `[0.0, 0.0]` to `[1.0, 0.0]` or `[0.0, 1.0]`).
8. **High Angular Velocity Penalties**: Executing lateral engine actions (1 or 3) or making contact while `ang_vel` is high triggers significant negative rewards, penalizing uncontrolled rotation or unstable landing attempts.
9. **Angular Momentum Divergence**: Without precise control of `ang_vel` through lateral engines, the lander's `angle` can diverge rapidly, leading to uncontrolled rotation and loss of landing stability.
10. **Velocity-Sensitive Landing Dynamics**: High vertical velocity (`y_vel`) or high angular velocity (`ang_vel`) at the moment of impact/contact triggers severe penalties, necessitating low-velocity control to secure landing bonuses.

---

## 2026-07-05 19:18:05

---
1. **Main Engine (Action 2) Multidimensionality**: While primarily used to regulate altitude (`y_pos`) and vertical velocity (`y_vel`), the main engine also induces changes in the lander's `angle` and `ang_vel`.
2. **Lateral Engine Directionality and Torque**: Action 1 (left engine) provides thrust in the negative x direction, while Action 3 (right engine) provides thrust in the positive x direction; both lateral actions provide simultaneous torque to influence `angle` and `ang_vel`.
3. **Cross-Axis Engine Coupling**: Lateral engine actions (1 and 3) also induce changes in vertical velocity (`y_vel`), meaning horizontal drift compensation and vertical altitude management are coupled.
4. **Gravity and Descent**: Gravity provides a constant downward acceleration that decreases `y_pos`, requiring continuous main engine counter-thrust to manage the descent rate.
5. **Leg Contact Reward Spikes**: The environment provides massive positive reward spikes when the lander transitions from a non-contact state to a contact state (e.g., `[1.0, 0.0]` or `[0.0, 1.0]`).
6. **Sustained Landing Bonuses**: Maintaining stable contact with both legs (`[1.0, 1.0]`) provides significant and continuous positive rewards, incentivizing a successful touchdown.
7. **Critical Impact/Crash Penalties**: Extremely high negative rewards (e.g., -17.34) are triggered when the lander reaches or passes `y_pos = 0` in an unstable manner or suffers a crash upon contact.
8. **Angular Momentum Divergence**: Without precise control of `ang_vel` through lateral engines, the lander's `angle` can diverge rapidly, leading to uncontrolled rotation and loss of landing stability.
9. **High Angular Velocity Penalties**: Executing lateral engine actions or making contact while `ang_vel` is high triggers significant negative rewards, penalizing uncontrolled rotation.
10. **Velocity-Sensitive Landing Dynamics**: High vertical velocity (`y_vel`) or high angular velocity (`ang_vel`) at the moment of impact triggers severe penalties, necessitating low-velocity control to secure landing bonuses.

---

## 2026-07-05 19:27:28

1. **Main Engine (Action 2) Multidimensionality**: While primarily used to regulate altitude (`y_pos`) and vertical velocity (`y_vel`), the main engine also induces changes in the lander's `angle` and `ang_vel`.
2. **Lateral Engine Directionality and Torque**: Action 1 (left engine) provides thrust in the negative x direction, while Action 3 (right engine) provides thrust in the positive x direction; both lateral actions provide simultaneous torque to influence `angle` and `ang_vel`.
3. **Cross-Axis Engine Coupling**: Lateral engine actions (1 and 3) also induce changes in vertical velocity (`y_vel`), meaning horizontal drift compensation and vertical altitude management are coupled.
4. **Gravity and Descent**: Gravity provides a constant downward acceleration that decreases `y_pos`, requiring continuous main engine counter-thrust to manage the descent rate.
5. **Single-Leg Contact Transition Bonus**: The environment provides massive positive reward spikes when the lander transitions from a non-contact state to a single-leg contact state (e.g., transitioning to `[1.0, 0.0]` or `[0.0, 1.0]`).
6. **Dual-Leg Contact Stability Sensitivity**: While dual-leg contact (`[1.0, 1.0]`) is a primary goal, it is highly sensitive to stability; maintaining this state while the lander is unstable or experiencing high impact velocities can trigger massive negative rewards.
7. **Lateral Engine Action Cost**: Executing lateral engine actions (1 and 3) is frequently associated with immediate negative step rewards, suggesting an inherent cost or penalty for using lateral thrust.
8. **Contact State Transition Volatility**: Sudden shifts in contact states (e.g., a single leg losing contact during a dual-leg contact period) are associated with significant reward fluctuations and potential penalties.
9. **Angular Momentum Divergence**: Without precise control of `ang_vel` through lateral engines, the lander's `angle` can diverge rapidly, leading to uncontrolled rotation and loss of landing stability.
10. **Velocity-Sensitive Landing Dynamics**: High vertical velocity (`y_vel`) or high angular velocity (`ang_vel`) at the moment of impact triggers severe penalties, necessitating low-velocity control to secure landing bonuses.

---

## 2026-07-05 19:29:58

---
1. **Main Engine (Action 2) Multidimensionality**: The main engine regulates altitude (`y_pos`) and vertical velocity (`y_vel`) but also induces changes in `angle` and `ang_vel`.
2. **Lateral Engine Directionality and Torque**: Action 1 (left engine) provides negative x-direction thrust, while Action 3 (right engine) provides positive x-direction thrust; both induce torque to influence `angle` and `ang_vel`.
3. **Cross-Axis Engine Coupling**: Lateral engine actions (1 and 3) also affect vertical velocity (`y_vel`), meaning horizontal drift compensation and vertical altitude management are coupled.
4. **Gravity-Driven Descent**: Gravity provides constant downward acceleration, requiring continuous or pulsed main engine counter-thrust to manage the descent rate.
5. **Differential Contact Reward Spikes**: Transitions to single-leg contact states (e.g., `[1.0, 0.0]` or `[0.0, 1.0]`) produce significantly larger reward spikes than transitions to dual-leg contact states (`[1.0, 1.0]`).
6. **Dual-Leg Contact Stability**: Maintaining the dual-leg contact state (`[1.0, 1.0]`) is highly sensitive to stability; uncontrolled rotation or impact velocities can trigger massive negative rewards.
7. **Lateral Engine Action Cost**: Executing lateral engine actions (1 and 3) is frequently associated with immediate negative step rewards, suggesting an inherent cost for using lateral thrust.
8. **Inaction Penalty During Descent**: Using Action 0 (nothing) while the lander is in flight or descending typically results in negative rewards, as it fails to counteract gravity or maintain descent stability.
9. **Angular Momentum Divergence**: Without precise control of `ang_vel` via lateral engines, the lander's `angle` can diverge rapidly, leading to uncontrolled rotation and loss of landing stability.
10. **Velocity-Sensitive Landing Dynamics**: High vertical velocity (`y_vel`) or high angular velocity (`ang_vel`) at the moment of impact triggers severe penalties, necessitating low-velocity control to secure landing bonuses.

---

## 2026-07-05 19:32:25

---
1. **Main Engine (Action 2) Multidimensionality**: The main engine regulates altitude (`y_pos`) and vertical velocity (`y_vel`) but also induces changes in `angle` and `ang_vel`.
2. **Lateral Engine Directionality and Torque**: Action 1 (left engine) provides negative x-direction thrust, while Action 3 (right engine) provides positive x-direction thrust; both induce torque to influence `angle` and `ang_vel`.
3. **Cross-Axis Engine Coupling**: Lateral engine actions (1 and 3) also affect vertical velocity (`y_vel`), meaning horizontal drift compensation and vertical altitude management are coupled.
4. **Gravity-Driven Descent**: Gravity provides constant downward acceleration, requiring continuous or pulsed main engine counter-thrust to manage the descent rate.
5. **Differential Contact Reward Spikes**: Transitions to contact states produce significant reward spikes, with single-leg contact states (`[1.0, 0.0]` or `[0.0, 1.0]`) often yielding larger immediate rewards than transitions to dual-leg contact states (`[1.0, 1.0]`).
6. **Dual-Leg Contact Stability**: Maintaining the dual-leg contact state (`[1.0, 1.0]`) is highly sensitive to stability; uncontrolled rotation or high impact velocities during the transition to dual-leg contact can trigger massive negative rewards.
7. **Lateral Engine Action Cost**: Executing lateral engine actions (1 and 3) is frequently associated with immediate negative step rewards, suggesting an inherent cost for using lateral thrust.
8. **Inaction Penalty During Descent**: Using Action 0 (nothing) while the lander is in flight or descending typically results in negative rewards, as it fails to counteract gravity or maintain descent stability.
9. **Angular Momentum Divergence**: Without precise control of `ang_vel` via lateral engines, the lander's `angle` can diverge rapidly, leading to uncontrolled rotation and loss of landing stability.
10. **Impact-Induced Crash Penalties**: High vertical velocity (`y_vel`) or high angular velocity (`ang_vel`) at the moment of ground contact (`y_pos` $\approx$ 0) triggers severe negative rewards, representing a crash.

---

## 2026-07-05 19:37:23

1. **Main Engine (Action 2) Multidimensionality**: The main engine regulates altitude (`y_pos`) and vertical velocity (`y_vel`) but also induces changes in `angle` and `ang_vel`.
2. **Lateral Engine Directionality and Torque**: Action 1 (left engine) and Action 3 (right engine) provide lateral thrust to manage `x_pos` and `x_vel`, while simultaneously inducing torque that influences `angle` and `ang_vel`.
3. **Cross-Axis Engine Coupling**: Lateral engine actions (1 and 3) also affect vertical velocity (`y_vel`), meaning horizontal drift compensation and vertical altitude management are coupled.
4. **Gravity-Driven Descent**: Gravity provides constant downward acceleration, requiring continuous or pulsed main engine counter-thrust to manage the descent rate and prevent uncontrolled velocity increases.
5. **Differential Contact Reward Spikes**: Transitions to contact states produce significant reward spikes. Specifically, single-leg contact states (`[1.0, 0.0]` or `[0.0, 1.0]`) can yield significantly higher immediate rewards than the immediate transition to a dual-leg contact state (`[1.0, 1.0]`).
6. **Landing Stability and Crash Penalties**: High vertical velocity (`y_vel`), high angular velocity (`ang_vel`), or significant angular instability at the moment of ground contact (`y_pos` $\approx$ 0) triggers severe negative rewards (e.g., -17.0 or lower), representing a crash.
7. **Lateral Engine Action Cost**: Executing lateral engine actions (1 and 3) is associated with negative step rewards; this cost applies both during active flight and even after the lander has established ground contact.
8. **Inaction Penalty During Descent**: Using Action 0 (nothing) while the lander is in flight or descending typically results in negative rewards, as it fails to counteract gravity or maintain descent stability.
9. **Angular Momentum Divergence**: Without precise control of `ang_vel` via lateral engines, the lander's `angle` can diverge rapidly, leading to uncontrolled rotation and loss of landing stability.
10. **Post-Contact Stability and Disruption**: Once dual-leg contact (`[1.0, 1.0]`) is achieved, the lander enters a settling phase where maintaining stability is key; subsequent engine actions (1, 2, or 3) can disrupt this state and lead to reduced or negative rewards.

---

## 2026-07-05 19:39:23

1. **Main Engine (Action 2) Multidimensionality**: The main engine regulates altitude (`y_pos`) and vertical velocity (`y_vel`) but also induces changes in `angle` and `ang_vel`.
2. **Lateral Engine Directionality and Torque**: Action 1 (left engine) and Action 3 (right engine) provide lateral thrust to manage `x_pos` and `x_vel`, while simultaneously inducing torque that influences `angle` and `ang_vel`.
3. **Cross-Axis Engine Coupling**: Lateral engine actions (1 and 3) affect vertical velocity (`y_vel`), meaning horizontal drift compensation and vertical altitude management are coupled.
4. **Gravity-Driven Descent**: Gravity provides constant downward acceleration, requiring continuous or pulsed main engine counter-thrust to manage the descent rate and prevent uncontrolled velocity increases.
5. **Differential Contact Reward Spikes**: Large positive reward spikes occur during the transition from no contact to a single-leg contact state (`[1.0, 0.0]` or `[0.0, 1.0]`). These transition rewards are significantly higher than the reward received for the transition into a dual-leg contact state (`[1.0, 1.0]`).
6. **Landing Stability and Crash Penalties**: Severe negative rewards (e.g., $\approx -18.0$) are triggered if the lander is unstable or possesses residual velocity at the moment of ground contact, even if the legs are already in contact.
7. **Lateral Engine Action Cost**: Executing lateral engine actions (1 and 3) is associated with negative step rewards, which applies both during active flight and after ground contact is established.
8. **Inaction Penalty During Descent**: Using Action 0 (nothing) while the lander is in flight or descending typically results in negative rewards, as it fails to counteract gravity or maintain descent stability.
9. **Angular Momentum Divergence**: Without precise control of `ang_vel` via lateral engines, the lander's `angle` can diverge rapidly, leading to uncontrolled rotation and loss of landing stability.
10. **Post-Contact Instability**: Once dual-leg contact (`[1.0, 1.0]`) is achieved, the lander is not automatically safe; subsequent engine actions or residual $y\_vel$ and $ang\_vel$ can still trigger a crash state.

---

## 2026-07-05 19:44:56

1. **Main Engine (Action 2) Multidimensionality**: The main engine regulates altitude (`y_pos`) and vertical velocity (`y_vel`) but also induces changes in `angle` and `ang_vel`.
2. **Lateral Engine Directionality and Torque**: Action 1 (left engine) and Action 3 (right engine) provide lateral thrust to manage `x_pos` and `x_vel`, while simultaneously inducing torque that influences `angle` and `ang_vel`.
3. **Cross-Axis Engine Coupling**: Lateral engine actions (1 and 3) affect vertical velocity (`y_vel`), meaning horizontal drift compensation and vertical altitude management are coupled.
4. **Gravity-Driven Descent**: Gravity provides constant downward acceleration, requiring continuous or pulsed main engine counter-thrust to manage the descent rate and prevent uncontrolled velocity increases.
5. **Contact State Reward Spikes**: Significant positive reward spikes occur during transitions into contact states, including single-leg contact (`[1.0, 0.0]` or `[0.0, 1.0]`) and dual-leg contact (`[1.0, 1.0]`).
6. **Impact Stability and Severe Penalties**: Extreme negative rewards (e.g., $\approx -17.5$) can be triggered at the moment of contact if the lander is considered unstable due to residual velocity (`x_vel`, `y_vel`) or angular momentum, even if leg contact is established.
7. **Lateral Engine Action Cost**: Executing lateral engine actions (1 and 3) is associated with negative step rewards, which applies both during active flight and after ground contact is established.
8. **Inaction Penalty During Descent**: Using Action 0 (nothing) while the lander is in flight or descending typically results in negative rewards, as it fails to counteract gravity or maintain descent stability.
9. **Angular Momentum Divergence**: Without precise control of `ang_vel` via lateral engines, the lander's `angle` can diverge rapidly, leading to uncontrolled rotation and loss of landing stability.
10. **Post-Contact Instability**: Once dual-leg contact (`[1.0, 1.0]`) is achieved, the lander is not automatically safe; subsequent engine actions or residual $y\_vel$ and $ang\_vel$ can still trigger a crash state.

---

## 2026-07-05 19:47:15

1. **Main Engine (Action 2) Multidimensionality**: The main engine regulates altitude (`y_pos`) and vertical velocity (`y_vel`) but also induces changes in `angle` and `ang_vel`.
2. **Lateral Engine Directionality and Torque**: Action 1 (left engine) and Action 3 (right engine) provide lateral thrust to manage `x_pos` and `x_vel`, while simultaneously inducing torque that influences `angle` and `ang_vel`.
3. **Cross-Axis Engine Coupling**: Lateral engine actions (1 and 3) affect vertical velocity (`y_vel`), meaning horizontal drift compensation and vertical altitude management are coupled.
4. **Gravity-Driven Descent**: Gravity provides constant downward acceleration, requiring continuous or pulsed main engine counter-thrust to manage the descent rate and prevent uncontrolled velocity increases.
5. **Contact State Reward Spikes**: Significant positive reward spikes occur during transitions into contact states, including single-leg contact (`[1.0, 0.0]` or `[0.0, 1.0]`) and dual-leg contact (`[1.0, 1.0]`).
6. **Velocity-Dependent Contact Penalties**: Extreme negative rewards (e.g., $\approx -18.0$) are triggered if contact is established (either single or dual leg) while the lander possesses significant residual vertical (`y_vel`) or horizontal (`x_vel`) velocity.
7. **Lateral Engine Action Cost**: Executing lateral engine actions (1 and 3) is associated with negative step rewards, which applies both during active flight and after ground contact is established.
8. **Inaction Penalty During Descent**: Using Action 0 (nothing) while the lander is in flight or descending typically results in negative rewards, as it fails to counteract gravity or maintain descent stability.
9. **Angular Momentum Divergence**: Without precise control of `ang_vel` via lateral engines, the lander's `angle` can diverge rapidly, leading to uncontrolled rotation and loss of landing stability.
10. **Post-Contact Instability**: Dual-leg contact (`[1.0, 1.0]`) is not a guaranteed safe state; subsequent velocity fluctuations or angular shifts during the contact phase can still trigger severe negative rewards.

---

## 2026-07-05 19:50:41

1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in `angle` and `ang_vel`.
2. **Lateral Engine Directionality and Torque**: Action 1 (left engine) and Action 3 (right engine) provide lateral thrust for `x_pos` and `x_vel` management while simultaneously inducing torque that influences `angle` and `ang_vel`.
3. **Cross-Axis Engine Coupling**: Lateral engine actions (1 and 3) affect vertical velocity (`y_vel`), creating a coupling between horizontal drift compensation and vertical altitude management.
4. **Gravity-Driven Descent**: Constant gravitational acceleration necessitates continuous or pulsed counter-thrust (primarily via Action 2) to manage descent rates and prevent uncontrolled velocity increases.
5. **Contact State Reward Spikes**: Significant positive rewards are triggered by ground contact, with dual-leg contact (`[1.0, 1.0]`) capable of producing substantially higher reward spikes (e.g., $\approx 26.0$) than single-leg contact (e.g., $\approx 15.5$).
6. **Velocity-Dependent Contact Penalties**: High residual vertical (`y_vel`) or horizontal (`x_vel`) velocities at the moment of contact trigger severe negative rewards, penalizing unstable or hard landings.
7. **Lateral Engine Action Cost**: Executing lateral engine actions (1 and 3) is associated with negative step rewards, a cost that persists even after the lander has established contact with the ground.
8. **Inaction Penalty During Descent**: Using Action 0 (nothing) while in flight or during descent typically results in negative rewards as it fails to counteract gravity or maintain descent stability.
9. **Angular Momentum Divergence**: Without precise control of `ang_vel` via lateral engines, the lander's `angle` can diverge rapidly, leading to loss of landing stability.
10. **Post-Contact Reward Dynamics**: After establishing contact, the lander can maintain stability with minimal action, but continued use of engines (especially lateral) primarily accumulates negative step rewards.

---

## 2026-07-05 19:58:35

1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in `angle` and `ang_vel`.
2. **Lateral Engine Directionality and Torque**: Action 1 (left engine) and Action 3 (right engine) provide lateral thrust for `x_pos` and `x_vel` management while simultaneously inducing torque that influences `angle` and `ang_vel`.
3. **Cross-Axis Engine Coupling**: Lateral engine actions (1 and 3) affect vertical velocity (`y_vel`), creating a coupling between horizontal drift compensation and vertical altitude management.
4. **Gravity-Driven Descent**: Constant gravitational acceleration necessitates continuous or pulsed counter-thrust (primarily via Action 2) to manage descent rates and prevent uncontrolled velocity increases.
5. **Contact State Reward Tiers**: Significant positive rewards are triggered by leg contact; however, the magnitude of these rewards is highly sensitive to the stability of the landing and the specific contact state.
6. **Catastrophic Crash Penalties**: Even when ground contact is established ($y\_pos \approx 0$ and legs are in contact), residual horizontal or vertical velocities, or angular instability, can trigger severe negative rewards (e.g., $\approx -20.0$), representing a crash.
7. **Lateral Engine Action Cost**: Executing lateral engine actions (1 and 3) is associated with consistent negative step rewards, a cost that persists even after the lander has established contact with the ground.
8. **Inaction Penalty During Descent**: Using Action 0 (nothing) while in flight or during descent typically results in negative rewards as it fails to counteract gravity or maintain descent stability.
9. **Angular Momentum Divergence**: Without precise control of `ang_vel` via lateral engines, the lander's `angle` can diverge rapidly, leading to a loss of landing stability or a crash upon contact.
10. **Post-Contact Velocity Management**: After establishing contact, the lander must actively minimize all residual velocities (`x_vel`, `y_vel`, and `ang_vel`) to avoid triggering crash penalties and to maintain a stable landing state.

---

## 2026-07-05 20:00:33

1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in `angle` and `ang_vel`.
2. **Lateral Engine Directionality and Torque**: Action 1 (left engine) and Action 3 (right engine) provide lateral thrust for `x_pos` and `x_vel` management while simultaneously inducing torque that influences `angle` and `ang_vel`.
3. **Cross-Axis Engine Coupling**: Lateral engine actions (1 and 3) affect vertical velocity (`y_vel`), creating a coupling between horizontal drift compensation and vertical altitude management.
4. **Gravity-Driven Descent**: Constant gravitational acceleration necessitates continuous or pulsed counter-thrust (primarily via Action 2) to manage descent rates and prevent uncontrolled velocity increases.
5. **High-Magnitude Contact Bonus**: Transitioning the leg contact states from 0.0 to 1.0 triggers a significant positive reward spike (often $\approx +10.0$ to $+12.0$), providing a major incentive for successful touchdown.
6. **Post-Contact Instability Penalties**: Even after legs establish contact, high angular velocities (`ang_vel`) or sudden orientation shifts can trigger severe negative rewards (e.g., $\approx -10.0$), representing a tipping or bouncing event.
7. **Lateral Engine Action Cost**: Executing lateral engine actions (1 and 3) is associated with consistent negative step rewards, a cost that persists even after the lander has established contact with the ground.
8. **Inaction Penalty During Descent**: Using Action 0 (nothing) while in flight or during descent typically results in negative rewards as it fails to counteract gravity or maintain descent stability.
9. **Angular Momentum Divergence**: Without precise control of `ang_vel` via lateral engines, the lander's `angle` can diverge rapidly, leading to a loss of landing stability or a crash upon contact.
10. **Post-Contact Velocity Management**: After establishing contact, the lander must actively minimize all residual velocities—with particular emphasis on `ang_vel`—to avoid triggering large stability penalties and to maintain a stable landing state.

---

## 2026-07-05 20:07:04

1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in `angle` and `ang_vel`.
2. **Lateral Engine Directionality and Torque**: Action 1 (left engine) and Action 3 (right engine) provide lateral thrust for `x_pos` and `x_vel` management while simultaneously inducing torque that influences `angle` and `ang_vel`.
3. **Cross-Axis Engine Coupling**: Lateral engine actions (1 and 3) affect vertical velocity (`y_vel`), creating a coupling between horizontal drift compensation and vertical altitude management.
4. **Gravity-Driven Descent**: Constant gravitational acceleration necessitates continuous or pulsed counter-thrust (primarily via Action 2) to manage descent rates and prevent uncontrolled velocity increases.
5. **Per-Leg Contact Bonuses**: Transitioning the `left_leg_contact` or `right_leg_contact` state from 0.0 to 1.0 independently triggers significant positive reward spikes (ranging from $\approx +10.0$ to $+14.5$).
6. **Ground Penetration Penalties**: Transitioning to a state where `y_pos` becomes negative (indicating the lander has penetrated the ground plane) triggers severe negative rewards (e.g., $\approx -8.9$).
7. **Lateral Engine Action Cost**: Executing lateral engine actions (1 and 3) is associated with consistent negative step rewards, a cost that persists even after the lander has established contact with the ground.
8. **Inaction Penalty During Descent**: Using Action 0 (nothing) while in flight or during descent typically results in negative rewards as it fails to counteract gravity or maintain descent stability.
9. **Angular Momentum Divergence**: Without precise control of `ang_vel` via lateral engines, the lander's `angle` can diverge rapidly, leading to a loss of landing stability or a crash.
10. **Landing Outcome Differentiation**: Establishing leg contact is associated with a "PARTIAL" outcome, suggesting that full success requires additional terminal conditions, such as specific orientation or minimized residual velocities, to be met.

---

## 2026-07-05 20:09:19

1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in `angle` and `ang_vel`.
2. **Lateral Engine Directionality and Torque**: Action 1 (left engine) and Action 3 (right engine) provide lateral thrust for `x_pos` and `x_vel` management while simultaneously inducing torque that influences `angle` and `ang_vel`.
3. **Cross-Axis Engine Coupling**: Lateral engine actions (1 and 3) affect vertical velocity (`y_vel`), creating a coupling between horizontal drift compensation and vertical altitude management.
4. **Gravity-Driven Descent**: Constant gravitational acceleration necessitates continuous or pulsed counter-thrust (primarily via Action 2) to manage descent rates and prevent uncontrolled velocity increases.
5. **Per-Leg Contact Bonuses**: Transitioning the `left_leg_contact` or `right_leg_contact` state from 0.0 to 1.0 independently triggers significant positive reward spikes (observed between $\approx +2.5$ and $+12.8$).
6. **Ground-Plane/Stability Penalties**: Even after establishing leg contact, severe negative rewards (e.g., $\approx -9.8$) can be triggered, likely due to ground penetration or instability in `ang_vel` or `y_vel`.
7. **Lateral Engine Action Cost**: Executing lateral engine actions (1 and 3) is associated with consistent negative step rewards, a cost that persists even after the lander has established contact with the ground.
8. **Inaction Penalty During Descent**: Using Action 0 (nothing) while in flight or during descent typically results in negative rewards as it fails to counteract gravity or maintain descent stability.
9. **Angular Momentum Divergence**: Without precise control of `ang_vel` via lateral engines, the lander's `angle` can diverge rapidly, leading to a loss of landing stability or a crash.
10. **Landing Outcome Differentiation**: Establishing leg contact is associated with a "PARTIAL" outcome, suggesting that full success requires additional terminal conditions, such as specific orientation or minimized residual velocities, to be met.

---

## 2026-07-05 20:12:01

---
1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in both `angle` and `ang_vel`.
2. **Lateral Engine X-Axis Directionality**: Action 1 (left engine) provides thrust in the negative x-direction (decreasing `x_vel`), while Action 3 (right engine) provides thrust in the positive x-direction (increasing `x_vel`).
3. **Lateral Engine Torque and Angular Control**: Action 1 induces negative torque (decreasing `angle` and `ang_vel`), whereas Action 3 induces positive torque (increasing `angle` and `ang_vel`).
4. **Cross-Axis Engine Coupling**: Lateral engine actions (1 and 3) exert a downward force component that affects vertical velocity (`y_vel`), coupling horizontal movement with vertical descent management.
5. **Gravity-Driven Descent**: Constant gravitational acceleration necessitates continuous or pulsed counter-thrust (primarily via Action 2) to manage descent rates and prevent uncontrolled velocity increases.
6. **Per-Leg Contact Bonuses**: Transitioning the `left_leg_contact` or `right_leg_contact` state from 0.0 to 1.0 independently triggers significant positive reward spikes (observed between $\approx +7.9$ and $+12.8$).
7. **Ground-Plane/Stability Penalties**: Even after establishing leg contact, negative rewards can be triggered by instability in `ang_vel`, residual `y_vel`, or orientation.
8. **Lateral Engine Action Cost**: Executing lateral engine actions (1 and 3) is frequently associated with negative step rewards, a cost that persists even after the lander has established contact with the ground.
9. **Angular Momentum Divergence**: Without precise control of `ang_vel` via lateral engines or the main engine, the lander's `angle` can diverge rapidly, leading to a loss of landing stability.
10. **Landing Outcome Differentiation**: Establishing leg contact is associated with a "PARTIAL" outcome, suggesting that full success requires additional terminal conditions, such as minimized residual velocities and stable orientation.

---

## 2026-07-05 20:17:51

1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in both `angle` and `ang_vel`.
2. **Lateral Engine X-Axis Directionality**: Action 1 (left engine) provides thrust in the negative x-direction (decreasing `x_vel`), while Action 3 (right engine) provides thrust in the positive x-direction (increasing `x_vel`).
3. **Lateral Engine Torque and Angular Control**: Actions 1 and 3 induce angular momentum, affecting both `angle` and `ang_vel` through torque.
4. **Cross-Axis Engine Coupling**: Lateral engine actions (1 and 3) exert a vertical force component that affects vertical velocity (`y_vel`), coupling horizontal movement with vertical descent management.
5. **Gravity-Driven Descent**: Constant gravitational acceleration necessitates continuous or pulsed counter-thrust (primarily via Action 2) to manage descent rates and prevent uncontrolled velocity increases.
6. **Per-Leg Contact Bonuses**: Transitioning a leg's contact state from 0.0 to 1.0 triggers significant positive rewards, typically observed in the range of $+10.0$ to $+14.0$, though the magnitude is modulated by the lander's stability and velocity at the moment of contact.
7. **Ground-Plane/Stability Penalties**: Even after establishing leg contact, negative rewards can be triggered by instability in `ang_vel`, high residual `y_vel`, or residual `x_vel`.
8. **Lateral Engine Action Cost**: Executing lateral engine actions (1 and 3) is consistently associated with negative step rewards, representing an operational cost for horizontal maneuvering.
9. **Angular Momentum Divergence**: Without precise control of `ang_vel` via lateral engines or the main engine, the lander's `angle` and `ang_vel` can diverge rapidly, leading to a loss of landing stability.
10. **Landing Outcome Differentiation**: A "PARTIAL" outcome indicates that leg contact has been established, suggesting that full success requires additional terminal conditions, such as minimized residual velocities and a stable orientation.

---

## 2026-07-05 20:20:30

1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in both `angle` and `ang_vel`.
2. **Lateral Engine X-Axis Directionality**: Action 1 (left engine) provides thrust in the negative x-direction (decreasing `x_vel`), while Action 3 (right engine) provides thrust in the positive x-direction (increasing `x_vel`).
3. **Lateral Engine Torque and Angular Control**: Actions 1 and 3 induce angular momentum, affecting both `angle` and `ang_vel` through torque.
4. **Cross-Axis Engine Coupling**: Lateral engine actions (1 and 3) exert a vertical force component that affects vertical velocity (`y_vel`), coupling horizontal movement with vertical descent management.
5. **Gravity-Driven Descent**: Constant gravitational acceleration necessitates continuous or pulsed counter-thrust (primarily via Action 2) to manage descent rates and prevent uncontrolled velocity increases.
6. **Per-Leg Contact Reward Spikes**: Transitioning a leg's contact state from 0.0 to 1.0 triggers significant positive rewards, typically observed in the range of $+8.7$ to $+12.1$.
7. **Post-Contact Stability Penalties**: Even after establishing leg contact, negative rewards can be triggered by instability in `ang_vel`, high residual `y_vel`, or residual `x_vel`.
8. **Action-Specific Step Rewards**: Action 2 is unique in its ability to generate positive step rewards, whereas Actions 0 (nothing), 1 (left), and 3 (right) are associated with consistent negative step rewards representing operational costs.
9. **Angular Momentum Divergence**: Without precise control of `ang_vel` via lateral engines or the main engine, the lander's `angle` and `ang_vel` can diverge rapidly, leading to a loss of landing stability.
10. **Landing Outcome Differentiation**: A "PARTIAL" outcome indicates that leg contact has been established, suggesting that full success requires additional terminal conditions, such as minimized residual velocities and a stable orientation.

---

## 2026-07-05 20:25:49

1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in both `angle` and `ang_vel`.
2. **Lateral Engine X-Axis Directionality**: Action 1 (left engine) provides thrust in the negative x-direction (decreasing `x_vel`), while Action 3 (right engine) provides thrust in the positive x-direction (increasing `x_vel`).
3. **Lateral Engine Torque and Angular Control**: Actions 1 and 3 induce angular momentum, affecting both `angle` and `ang_vel` through torque.
4. **Cross-Axis Engine Coupling**: Lateral engine actions (1 and 3) exert a vertical force component that affects vertical velocity (`y_vel`), coupling horizontal movement with vertical descent management.
5. **Gravity-Driven Descent**: Constant gravitational acceleration necessitates continuous or pulsed counter-thrust (primarily via Action 2) to manage descent rates and prevent uncontrolled velocity increases.
6. **Contact-Induced Reward Phase**: Establishing leg contact (transitioning contact state from 0.0 to 1.0) shifts the reward structure from consistent negative step costs to a phase of significant positive rewards.
7. **Post-Contact Stability Rewards**: Once contact is established, large positive step rewards (e.g., $+8.7$ to $+21.2$) are granted as the lander minimizes residual `x_vel`, `y_vel`, `angle`, and `ang_vel`.
8. **Action-Specific Step Rewards**: Action 2 is the primary driver of positive step rewards, whereas Actions 0 (nothing), 1 (left), and 3 (right) are associated with consistent negative step rewards representing operational costs.
9. **Terminal Stability Reward**: A massive terminal reward of $+100.0$ is triggered when the lander achieves a state of near-zero velocity and near-zero orientation while both legs are in contact with the ground.
10. **Landing Outcome Differentiation**: A "PARTIAL" outcome indicates that leg contact has been established, but the specific terminal stability conditions required for a "FULL" success (or the specific step count threshold) were not met.

---

## 2026-07-05 20:28:43

1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in both `angle` and `ang_vel`.
2. **Lateral Engine X-Axis Directionality**: Action 1 (left engine) provides thrust in the negative x-direction (decreasing `x_vel`), while Action 3 (right engine) provides thrust in the positive x-direction (increasing `x_vel`).
3. **Lateral Engine Torque and Angular Control**: Actions 1 and 3 induce angular momentum, affecting both `angle` and `ang_vel` through torque.
4. **Cross-Axis Engine Coupling**: Lateral engine actions (1 and 3) exert a vertical force component that affects vertical velocity (`y_vel`), coupling horizontal movement with vertical velocity management.
5. **Vertical Velocity and Gravity**: Constant gravitational acceleration necessitates counter-thrust (primarily via Action 2) to manage descent, though a positive `y_vel` allows for ascent maneuvers.
6. **Contact-Induced Reward Phase**: Establishing leg contact (transitioning contact state from 0.0 to 1.0) shifts the reward structure from consistent step costs to a phase of potential positive rewards.
7. **Post-Contact Stability Rewards**: Once contact is established, large positive step rewards are granted as the lander minimizes residual `x_vel`, `y_vel`, `angle`, and `ang_vel`.
8. **Action-Specific Reward Dynamics**: Action 2 is the primary driver of large positive rewards during descent, but lateral engines (Actions 1 and 3) can also generate positive step rewards in the post-contact phase if they contribute to stabilizing the lander.
9. **Terminal Stability Reward**: A massive terminal reward of $+100.0$ is triggered when the lander achieves a state of near-zero velocity and near-zero orientation while both legs are in contact with the ground.
10. **Landing Outcome Differentiation**: A "PARTIAL" outcome indicates that leg contact has been established, but the specific terminal stability conditions required for a "FULL" success were not met.

---

## 2026-07-05 20:31:25

---
1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in both `angle` and `ang_vel`.
2. **Lateral Engine X-Axis Directionality**: Action 1 (left engine) provides thrust in the negative x-direction (decreasing `x_vel`), while Action 3 (right engine) provides thrust in the positive x-direction (increasing `x_vel`).
3. **Lateral Engine Torque and Angular Control**: Actions 1 and 3 induce angular momentum, affecting both `angle` and `ang_vel` through torque.
4. **Cross-Axis Engine Coupling**: Lateral engine actions (1 and 3) exert a vertical force component that affects vertical velocity (`y_vel`), coupling horizontal movement with vertical velocity management.
5. **Vertical Velocity and Gravity**: Constant gravitational acceleration necessitates counter-thrust (primarily via Action 2) to manage descent, though a positive `y_vel` allows for ascent maneuvers.
6. **Contact-Induced Reward Phase Shift**: Establishing leg contact (transitioning contact state from 0.0 to 1.0) shifts the reward structure from consistent step costs to a phase of high-magnitude, highly volatile stability rewards.
7. **Post-Contact Reward Volatility**: In the post-contact phase, individual step rewards exhibit extreme volatility in magnitude, frequently reaching or exceeding $\pm 10.0$.
8. **Stability-Dependent Action Outcomes**: During the post-contact phase, the sign and magnitude of rewards for Actions 1, 2, and 3 are highly sensitive to whether the action maintains or disrupts the lander's instantaneous stability.
9. **Terminal Stability Reward**: A massive terminal reward of $+100.0$ is triggered when the lander achieves a state of near-zero velocity and near-zero orientation while both legs are in contact with the ground.
10. **Landing Outcome Differentiation**: A "PARTIAL" outcome indicates that leg contact has been established, but the specific terminal stability conditions required for a "FULL" success were not met.

---

## 2026-07-05 20:34:46

1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in both `angle` and `ang_vel`.
2. **Lateral Engine X-Axis Directionality**: Action 1 (left engine) provides thrust in the negative x-direction (increasing `x_vel` toward zero or making it more positive), while Action 3 (right engine) provides thrust in the positive x-direction (increasing `x_vel`).
3. **Lateral Engine Torque and Angular Control**: Actions 1 and 3 induce angular momentum, affecting both `angle` and `ang_vel` through torque.
4. **Cross-Axis Engine Coupling**: Lateral engine actions (1 and 3) exert a vertical force component that affects vertical velocity (`y_vel`), coupling horizontal movement with vertical velocity management.
5. **Vertical Velocity and Gravity**: Constant gravitational acceleration necessitates counter-thrust (primarily via Action 2) to manage descent, though a positive `y_vel` allows for ascent maneuvers.
6. **Contact Trigger Condition**: Leg contact (transitioning contact state from 0.0 to 1.0) is triggered when the lander's `y_pos` reaches or crosses the zero threshold.
7. **Contact-Induced Reward Phase Shift**: Establishing leg contact shifts the reward structure from consistent step costs to a phase of high-magnitude, highly volatile stability rewards.
8. **Post-Contact Reward Volatility**: In the post-contact phase, individual step rewards exhibit extreme volatility in magnitude, frequently reaching or exceeding $\pm 10.0$, and are highly sensitive to whether an action maintains or disrupts instantaneous stability.
9. **Terminal Success Criteria**: Terminal success ("FULL" outcome) likely requires strict spatial positioning (e.g., `x_pos` near zero) in addition to near-zero velocity and orientation, as "PARTIAL" outcomes were observed even when the lander achieved stability at non-zero `x_pos`.
10. **Landing Outcome Differentiation**: A "PARTIAL" outcome indicates that leg contact has been established, but the specific terminal stability or spatial conditions required for a "FULL" success were not met.

---

## 2026-07-05 20:41:43

1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in both `angle` and `ang_vel` due to the lander's orientation.
2. **Body-Fixed Thrust Projection**: All engine actions (1, 2, and 3) are body-fixed; their influence on the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Torque and Angular Control**: Actions 1 and 3 induce angular momentum, affecting both `angle` and `ang_vel` through torque.
4. **Cross-Axis Engine Coupling**: The main engine (Action 2) can induce horizontal acceleration (`x_vel`) when the lander is tilted, and lateral engines (Actions 1 and 3) can induce vertical acceleration (`y_vel`), depending on the `angle`.
5. **Vertical Velocity and Gravity**: Constant gravitational acceleration necessitates counter-thrust (primarily via Action 2) to manage descent, though a positive `y_vel` allows for ascent maneuvers.
6. **Contact Trigger Condition**: Leg contact (transitioning contact state from 0.0 to 1.0) is triggered when the lander's `y_pos` reaches or crosses the zero threshold.
7. **Contact-Induced Reward Phase Shift**: Establishing leg contact shifts the reward structure from consistent step costs to a phase of high-magnitude, highly volatile stability rewards.
8. **Post-Contact Reward Volatility**: In the post-contact phase, individual step rewards exhibit extreme volatility in magnitude and sign, reacting sensitively to whether an action maintains or disrupts instantaneous stability.
9. **Terminal Success Criteria**: Terminal success ("FULL") requires strict spatial positioning (e.g., `x_pos` near zero) in addition to near-zero velocity and orientation.
10. **Landing Outcome Differentiation**: A "PARTIAL" outcome indicates that leg contact has been established, but the specific terminal stability or spatial conditions required for a "FULL" success were not met.

---

## 2026-07-05 20:44:31

---
1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in both `angle` and `ang_vel` due to the lander's orientation.
2. **Body-Fixed Thrust Projection**: All engine actions (1, 2, and 3) are body-fixed; their influence on the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Torque and Angular Control**: Actions 1 and 3 induce angular momentum, affecting both `angle` and `ang_vel` through torque.
4. **Cross-Axis Engine Coupling**: The main engine (Action 2) can induce horizontal acceleration (`x_vel`) when the lander is tilted, and lateral engines (Actions 1 and 3) can induce vertical acceleration (`y_vel`), depending on the `angle`.
5. **Vertical Velocity and Gravity**: Constant gravitational acceleration necessitates counter-thrust (primarily via Action 2) to manage descent, though a positive `y_vel` allows for ascent maneuvers.
6. **Contact Trigger Condition**: Leg contact (transitioning contact state from 0.0 to 1.0) is triggered when the lander's `y_pos` reaches or crosses the zero threshold.
7. **Contact-Induced Reward Spikes**: The transition to leg contact triggers an immediate, high-magnitude reward spike that is significantly larger than both descent-phase and post-contact stability rewards.
8. **Post-Contact Stability via Micro-Oscillations**: Following leg contact, the stability of the lander is maintained through high-frequency, low-magnitude engine corrections (primarily using Actions 0, 1, and 3) that counteract gravitational and angular perturbations.
9. **Spatial Success Precision**: The criteria for a "FULL" landing outcome necessitate extremely low values for `x_pos`, as even small lateral deviations (e.g., $|x_{pos}| < 0.01$) may result in a "PARTIAL" outcome.
10. **Landing Outcome Differentiation**: A "PARTIAL" outcome signifies that while leg contact was achieved, the lander failed to meet the precise terminal requirements for position, orientation, or velocity.

---

## 2026-07-05 20:47:17

---
1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in both `angle` and `ang_vel` due to the lander's orientation.
2. **Body-Fixed Thrust Projection**: All engine actions (1, 2, and 3) are body-fixed; their influence on the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Differential Lateral Torque**: Action 1 (left engine) provides a constant positive angular torque (increasing `ang_vel`), whereas Action 3 (right engine) provides a constant negative angular torque (decreasing `ang_vel`), independent of the current sign of `ang_vel`.
4. **Cross-Axis Engine Coupling**: The main engine (Action 2) can induce horizontal acceleration (`x_vel`) when the lander is tilted, and lateral engines (Actions 1 and 3) can induce vertical acceleration (`y_vel`), depending on the `angle`.
5. **Vertical Velocity and Gravity**: Constant gravitational acceleration necessitates counter-thrust (primarily via Action 2) to manage descent, though a positive `y_vel` allows for ascent maneuvers.
6. **Contact Trigger Condition**: Leg contact (transitioning contact state from 0.0 to 1.0) is triggered when the lander's `y_pos` reaches or crosses the zero threshold.
7. **Contact-Induced Reward Spikes**: The transition to leg contact triggers immediate, high-magnitude reward spikes (exceeding 12.0) that are significantly larger than both descent-phase and post-contact stability rewards.
8. **Post-Contact Stability via Micro-Oscillations**: Following leg contact, the stability of the lander is maintained through high-frequency, low-magnitude engine corrections (primarily using Actions 0, 1, and 3) that counteract gravitational and angular perturbations.
9. **Extreme Precision for FULL Outcome**: Both episodes demonstrate that even with $|x_{pos}|$ values significantly below 0.01 (e.g., 0.0033) and near-zero orientation, the outcome remains "PARTIAL", suggesting that "FULL" success requires much more stringent terminal tolerances.
10. **Landing Outcome Differentiation**: A "PARTIAL" outcome signifies that while leg contact was achieved, the lander failed to meet the precise terminal requirements for position, orientation, or velocity.

---

## 2026-07-05 20:49:22

1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in both `angle` and `ang_vel` due to the lander's orientation.
2. **Body-Fixed Thrust Projection**: All engine actions (1, 2, and 3) are body-fixed; their influence on the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Differential Lateral Torque**: Action 1 (left engine) provides a constant positive angular torque, whereas Action 3 (right engine) provides a constant negative angular torque, independent of the current sign of `ang_vel`.
4. **Cross-Axis Engine Coupling**: The main engine (Action 2) can induce horizontal acceleration (`x_vel`) when the lander is tilted, and lateral engines (Actions 1 and 3) can induce vertical acceleration (`y_vel`), depending on the `angle`.
5. **Sequential Leg Contact**: The contact states for the left and right legs can transition to 1.0 independently, allowing for a phase where only one leg is in contact with the ground before both are stabilized.
6. **Contact Trigger Condition**: Leg contact (transitioning contact state from 0.0 to 1.0) is triggered when the lander's `y_pos` reaches or crosses the zero threshold.
7. **Contact-Induced Reward Spikes**: The transition to leg contact triggers immediate, high-magnitude reward spikes (observed between 11.0 and 13.0) that are significantly larger than both descent-phase and post-contact stability rewards.
8. **Post-Contact Stability via Micro-Oscillations**: Following initial leg contact, the stability of the lander is maintained through high-frequency, low-magnitude engine corrections (primarily using Actions 0, 1, and 3) that counteract gravitational and angular perturbations.
9. **Extreme Precision for FULL Outcome**: Both episodes demonstrate that even when $|x_{pos}|$ is extremely low (e.g., 0.0038 in Episode 2), the outcome remains "PARTIAL," suggesting that "FULL" success requires significantly more stringent terminal tolerances for all state variables than previously assumed.
10. **Landing Outcome Differentiation**: A "PARTIAL" outcome signifies that while leg contact was achieved and the lander maintained a level of stability, it failed to meet the precise terminal requirements for position, orientation, or velocity.

---

## 2026-07-05 20:54:25

1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in both `angle` and `ang_vel` due to the lander's orientation.
2. **Body-Fixed Thrust Projection**: All engine actions (1, 2, and 3) are body-fixed; their influence on the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Differential Lateral Torque**: Action 1 (left engine) provides a constant positive angular torque, whereas Action 3 (right engine) provides a constant negative angular torque, independent of the current sign of `ang_vel`.
4. **Sequential Leg Contact**: The contact states for the left and right legs can transition to 1.0 independently, allowing for a phase where only one leg is in contact with the ground (e.g., Step 692 in Episode 1) before both are stabilized.
5. **Cross-Axis Engine Coupling**: The main engine (Action 2) can induce horizontal acceleration (`x_vel`) when the lander is tilted, and lateral engines (Actions 1 and 3) can induce vertical acceleration (`y_vel`), depending on the `angle`.
6. **Contact Trigger and Reward Spikes**: Leg contact (transitioning contact state from 0.0 to 1.0) is triggered when `y_pos` reaches or crosses the zero threshold, which immediately triggers high-magnitude reward spikes (observed between 10.0 and 13.0).
7. **Ascent Capability via Lateral Thrust**: The lander can achieve positive `y_vel` (ascent) by utilizing lateral engines (Actions 1 or 3) while the lander's orientation is tilted to project thrust upward.
8. **Post-Contact Stability via Micro-Oscillations**: Following initial leg contact, the stability of the lander is maintained through high-frequency, low-magnitude engine corrections (primarily using Actions 0, 1, 2, and 3) to counteract gravitational and angular perturbations.
9. **Extreme Precision for FULL Outcome**: Both episodes demonstrate that even when $|x_{pos}|$ and $|y_{pos}|$ are extremely low at the time of contact, the outcome remains "PARTIAL," suggesting that "FULL" success requires significantly more stringent terminal tolerances for all state variables.
10. **Landing Outcome Differentiation**: A "PARTIAL" outcome signifies that while leg contact was achieved and the lander maintained a level of stability, it failed to meet the precise terminal requirements for position, orientation, or velocity.

---

## 2026-07-05 20:57:30

1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in both `angle` and `ang_vel` due to the lander's orientation.
2. **Body-Fixed Thrust Projection**: All engine actions (1, 2, and 3) are body-fixed; their influence on the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Differential Lateral Torque**: Actions 1 (left engine) and 3 (right engine) provide constant angular torques that independently modify `ang_vel` regardless of its current sign.
4. **Sequential Leg Contact**: The contact states for the left and right legs can transition to 1.0 independently, allowing for a period where only one leg is in contact with the ground before both are stabilized.
5. **Cross-Axis Engine Coupling**: The main engine (Action 2) induces horizontal acceleration (`x_vel`) when the lander is tilted, and lateral engines (Actions 1 and 3) can induce vertical acceleration (`y_vel`) depending on the `angle`.
6. **Contact-Triggered Reward Spikes**: The transition of a leg contact state from 0.0 to 1.0 triggers significant positive reward spikes (observed between 10.0 and 13.0).
7. **Post-Contact Ground Penetration**: Following initial leg contact, the lander's `y_pos` can fluctuate slightly below the zero threshold (e.g., entering negative values) while maintaining a contact state of 1.0.
8. **Initial Ascent and Vertical Momentum**: The simulation allows for significant initial positive `y_vel` (ascent), requiring the lander to manage the transition from upward momentum to a controlled descent.
9. **Micro-Oscillatory Stability**: Post-contact stability is maintained through high-frequency, low-magnitude engine corrections (utilizing Actions 0, 1, 2, and 3) to counteract gravitational and angular perturbations.
10. **Terminal Stringency and Impact Penalties**: "PARTIAL" outcomes persist even when $|x_{pos}|$ and $|y_{pos}|$ are extremely low, suggesting that terminal velocity or orientation tolerances are the primary constraints for "FULL" success; additionally, large negative rewards can be triggered by unstable state transitions during the contact phase.

---

## 2026-07-05 20:59:54

1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in both `angle` and `ang_vel` due to the lander's orientation.
2. **Body-Fixed Thrust Projection**: All engine actions (1, 2, and 3) are body-fixed; their influence on the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Differential Lateral Torque**: Actions 1 (left engine) and 3 (right engine) provide constant angular torques that independently modify `ang_vel` regardless of its current sign.
4. **Sequential Leg Contact**: The contact states for the left and right legs can transition to 1.0 independently, allowing for a period where only one leg is in contact with the ground before both are stabilized.
5. **Cross-Axis Engine Coupling**: The main engine (Action 2) induces horizontal acceleration (`x_vel`) when the lander is tilted, and lateral engines (Actions 1 and 3) can induce vertical acceleration (`y_vel`) depending on the `angle`.
6. **Dual-Phase Contact Reward Spikes**: Significant positive reward spikes (~12.0) are triggered by the transition of a leg contact state from 0.0 to 1.0; these spikes occur for both the initial individual leg contact and the subsequent transition to dual-leg contact.
7. **Post-Contact Ground Penetration**: Following initial leg contact, the lander's `y_pos` can fluctuate slightly below the zero threshold (e.g., entering negative values) while maintaining a contact state of 1.0.
8. **Variable Initial State Momentum**: The simulation can initialize with significant momentum in both $x$ and $y$ directions (e.g., negative `x_vel` and positive `y_vel`), requiring immediate corrective action to manage the descent trajectory.
9. **Micro-Oscillatory Stability**: Post-contact stability is maintained through high-frequency, low-magnitude engine corrections (utilizing Actions 0, 1, 2, and 3) to counteract gravitational and angular perturbations.
10. **Terminal Stringency and "PARTIAL" Outcomes**: "PARTIAL" outcomes persist even when $|x_{pos}|$, $|y_{pos}|$, $|x_{vel}|$, and $|y_{vel}|$ are near zero, suggesting that "FULL" success requires meeting extremely high-precision tolerances for orientation and/or sustained stability duration.

---

## 2026-07-05 21:02:08

1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in both `angle` and `ang_vel` due to the lander's orientation.
2. **Body-Fixed Thrust Projection**: All engine actions (1, 2, and 3) are body-fixed; their influence on the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Differential Lateral Torque**: Actions 1 (left engine) and 3 (right engine) provide constant angular torques that modify `ang_vel` and `angle`, with the direction of effect relative to the current orientation determining if the rotation is amplified or attenuated.
4. **Sequential Leg Contact**: The contact states for the left and right legs can transition to 1.0 independently, allowing for a period where only one leg is in contact with the ground before both are stabilized.
5. **Cross-Axis Engine Coupling**: The main engine (Action 2) induces horizontal acceleration (`x_vel`) when the lander is tilted, and lateral engines (Actions 1 and 3) can induce vertical acceleration (`y_vel`) depending on the `angle`.
6. **Dual-Phase Contact Reward Spikes**: Significant positive reward spikes (e.g., ~12.0) are triggered by the transition of a leg contact state from 0.0 to 1.0; these spikes occur for both the initial individual leg contact and the subsequent transition to dual-leg contact.
7. **Post-Contact Ground Penetration**: Following initial leg contact, the lander's `y_pos` can fluctuate slightly below the zero threshold (e.g., entering negative values) while maintaining a contact state of 1.0.
8. **Variable Initial State Momentum**: The simulation can initialize with significantly different momentum profiles, ranging from low-velocity descents to high-velocity horizontal drifts (e.g., $x_{vel} \approx -0.75$), requiring varying strategies for trajectory correction.
9. **Micro-Oscillatory Stability**: Post-contact stability is maintained through high-frequency, low-magnitude engine corrections (utilizing Actions 0, 1, 2, and 3) to counteract gravitational and angular perturbations.
10. **Terminal Stringency and "PARTIAL" Outcomes**: "PARTIAL" outcomes persist even when $|x_{pos}|$, $|y_{pos}|$, $|x_{vel}|$, and $|y_{vel}|$ are extremely close to zero, suggesting that "FULL" success requires meeting much higher precision tolerances for orientation and/or sustained stability duration.

---

## 2026-07-05 21:04:14

1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in both `angle` and `ang_vel` due to the lander's orientation.
2. **Body-Fixed Thrust Projection**: All engine actions (1, 2, and 3) are body-fixed; their influence on the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Differential Lateral Torque**: Actions 1 (left engine) and 3 (right engine) provide constant angular torques that modify `ang_vel` and `angle`, with the direction of effect relative to the current orientation determining if the rotation is amplified or attenuated.
4. **Stochastic Leg Contact Sequence**: The order of leg contact is not fixed; the lander may transition to a single-leg contact state via the left leg first (as seen in Episode 1) or the right leg first (as seen in Episode 2), depending on orientation and descent.
5. **Cross-Axis Engine Coupling**: The main engine (Action 2) induces horizontal acceleration (`x_vel`) when the lander is tilted, and lateral engines (Actions 1 and 3) can induce vertical acceleration (`y_vel`) depending on the `angle`.
6. **Dual-Phase Contact Reward Spikes**: Significant positive reward spikes (ranging from ~10.8 to ~11.7) are triggered by the transition of a leg contact state from 0.0 to 1.0, occurring for both the initial individual leg contact and the subsequent transition to dual-leg contact.
7. **Post-Contact Ground Penetration**: Following initial leg contact, the lander's `y_pos` can fluctuate slightly below the zero threshold (e.g., reaching negative values such as -0.0008) while maintaining a contact state of 1.0.
8. **Variable Initial State Momentum**: The simulation can initialize with significantly different momentum profiles, ranging from negative horizontal drifts (e.g., $x_{vel} \approx -0.65$) to positive horizontal drifts (e.g., $x_{vel} \approx +0.37$).
9. **Micro-Oscillatory Stability and Action 0**: Post-contact stability is maintained through high-frequency engine corrections involving all actions, with Action 0 (nothing) being frequently utilized to allow for minimal drift or to prevent over-correction between active engine pulses.
10. **Terminal Success vs. Step-Limit Partiality**: A "SUCCESS" outcome is a discrete terminal state triggered by meeting stability criteria, characterized by a large end-of-episode reward (e.g., 100.0); "PARTIAL" is the outcome when the simulation reaches the 1000-step maximum limit without triggering this terminal state.

---

## 2026-07-05 21:11:06

---
1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in both `angle` and `ang_vel` due to the lander's orientation.
2. **Body-Fixed Thrust Projection**: All engine actions (1, 2, and 3) are body-fixed; their influence on the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Differential Lateral Torque**: Actions 1 (left engine) and 3 (right engine) provide angular torques that modify `ang_vel` and `angle`, with the direction of effect determining if the rotation is amplified or attenuated.
4. **Stochastic Leg Contact Sequence**: The order of leg contact is not fixed; the lander may transition to a single-leg contact state via the left leg first or the right leg first, depending on descent dynamics.
5. **Cross-Axis Engine Coupling**: The main engine (Action 2) induces horizontal acceleration (`x_vel`) when the lander is tilted, and lateral engines (Actions 1 and 3) can induce vertical acceleration (`y_vel`) depending on the `angle`.
6. **Contact-Triggered Reward Spikes**: Significant positive reward spikes (e.g., ~14.6 in Episode 2) are triggered in close temporal proximity to the transition of a leg contact state from 0.0 to 1.0.
7. **Post-Contact Ground Penetration**: Following initial leg contact, the lander's `y_pos` can fluctuate slightly below the zero threshold (e.g., reaching negative values such as -0.0008) while maintaining a contact state of 1.0.
8. **Variable Initial State Momentum**: The simulation can initialize with significantly different momentum profiles, ranging from positive horizontal drifts to significant negative horizontal drifts.
9. **Micro-Oscillatory Stability and Action 0**: Post-contact stability is maintained through high-frequency engine corrections involving all actions, with Action 0 (nothing) being utilized to manage drift or prevent over-correction between active engine pulses.
10. **Terminal Success vs. Step-Limit Partiality**: A "SUCCESS" outcome is a discrete terminal state triggered by meeting stability criteria (e.g., 100.0 reward); "PARTIAL" is the outcome when the simulation reaches the 1000-step maximum limit, which can occur even if the lander has successfully made contact but failed to stabilize.

---

## 2026-07-05 21:13:21

1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in both `angle` and `ang_vel` due to the lander's current orientation.
2. **Body-Fixed Thrust Projection**: All engine actions (1, 2, and 3) are body-fixed; their influence on the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Differential Lateral Torque**: Actions 1 (left engine) and 3 (right engine) provide angular torques that modify `ang_vel` and `angle`, with the direction of effect determining if the rotation is amplified or attenuated.
4. **Stochastic Leg Contact Sequence**: The order of leg contact is not fixed; the lander may transition to a single-leg contact state via the left leg first or the right leg first (e.g., Episode 2 shows left leg contact at step 622, followed by right leg contact at step 625).
5. **Cross-Axis Engine Coupling**: The main engine (Action 2) induces horizontal acceleration (`x_vel`) when the lander is tilted, and lateral engines (Actions 1 and 3) can induce significant horizontal deceleration or vertical acceleration (`y_vel`) depending on the `angle`.
6. **Contact-Triggered Reward Spikes**: Significant positive reward spikes (e.g., ~13.0 in Episode 2) are triggered specifically during the discrete transition of a leg contact state from 0.0 to 1.0.
7. **Post-Contact Ground Penetration and Velocity Stabilization**: Following initial leg contact, the lander's `y_pos` can fluctuate near or slightly below the zero threshold while the system utilizes high-frequency corrections to stabilize `y_vel` and `ang_vel`.
8. **Variable Initial State Momentum**: The simulation can initialize with significantly different momentum profiles, ranging from varying positive to negative horizontal drifts (`x_vel`) and vertical velocities (`y_vel`).
9. **Micro-Oscillatory Stability and Action 0**: Post-contact stability is maintained through high-frequency engine corrections involving all actions, with Action 0 (nothing) being utilized to manage drift or prevent over-correction between active engine pulses.
10. **Terminal Success vs. Step-Limit Partiality**: A "SUCCESS" outcome is a discrete terminal state triggered by meeting stability criteria; "PARTIAL" is the outcome when the simulation reaches the 1000-step maximum limit, which can occur even if the lander has successfully made contact but has not yet achieved full stability.

---

## 2026-07-05 21:17:53

1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces changes in both `angle` and `ang_vel` due to the lander's current orientation.
2. **Body-Fixed Thrust Projection**: All engine actions (1, 2, and 3) are body-fixed; their influence on the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Differential Lateral Torque**: Actions 1 (left engine) and 3 (right engine) provide angular torques that modify `ang_vel` and `angle`, with the direction of effect determining if the rotation is amplified or attenuated.
4. **Stochastic Leg Contact Sequence**: The order of leg contact is not fixed; the lander can transition to a single-leg contact state via the left leg or the right leg first before reaching full dual-leg contact.
5. **Cross-Axis Engine Coupling**: The main engine (Action 2) induces horizontal acceleration (`x_vel`) when the lander is tilted, and lateral engines (Actions 1 and 3) can induce significant horizontal deceleration or vertical acceleration (`y_vel`) depending on the `angle`.
6. **Contact-Triggered Reward Spikes**: Significant positive reward spikes (e.g., ~12.4 in Episode 1 at step 619, and ~11.0 in Episode 2 at step 680) are triggered specifically during the discrete transition of a leg contact state from 0.0 to 1.0.
7. **Post-Contact Ground Penetration and Velocity Stabilization**: Following initial leg contact, the lander's `y_pos` stabilizes in a narrow band often slightly below the zero threshold (e.g., between -0.001 and 0.000) while the system utilizes high-frequency corrections to maintain near-zero `y_vel` and `ang_vel`.
8. **Variable Initial State Momentum**: The simulation can initialize with significantly different momentum profiles, including varying directions of horizontal drift (`x_vel`) and vertical velocities (`y_vel`).
9. **Micro-Oscillatory Stability and Action 0**: Post-contact stability is maintained through high-frequency engine corrections involving all actions, with Action 0 (nothing) being utilized to manage drift or prevent over-correction between active engine pulses.
10. **Terminal Success vs. Step-Limit Partiality**: A "SUCCESS" outcome is a discrete terminal state triggered by meeting stability criteria; "PARTIAL" is the outcome when the simulation reaches the 1000-step maximum limit, which can occur even if the lander has achieved successful contact and stable orientation.

---

## 2026-07-05 21:19:54

1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces significant changes in both `angle` and `ang_vel` due to the lander's orientation.
2. **Body-Fixed Thrust Projection**: All engine actions (1, 2, and 3) are body-fixed; their influence on the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Differential Lateral Torque**: Actions 1 (left engine) and 3 (right engine) provide angular torques that modify `ang_vel` and `angle`, with the direction of effect determining if the rotation is amplified or attenuated.
4. **Stochastic Leg Contact Sequence**: The order of leg contact is not fixed; the lander can transition to a single-leg contact state (left leg or right leg) before eventually reaching a dual-leg contact state.
5. **Cross-Axis Engine Coupling**: The main engine (Action 2) induces horizontal acceleration (`x_vel`) when the lander is tilted, and lateral engines (Actions 1 and 3) can induce significant horizontal deceleration or vertical acceleration (`y_vel`) depending on the `angle`.
6. **Contact-Triggered Reward Spikes**: Significant positive reward spikes (e.g., ~12.8 in Episode 1 at step 626, and ~12.8 in Episode 2 at step 657) are triggered specifically during the discrete transition of a single leg contact state from 0.0 to 1.0.
7. **Post-Contact Ground Penetration and Velocity Stabilization**: Following initial leg contact, the lander's `y_pos` often stabilizes in a narrow band slightly below the zero threshold (e.g., between -0.003 and 0.000) while the system utilizes high-frequency corrections to maintain near-zero `y_vel` and `ang_vel`.
8. **Variable Initial State Momentum**: The simulation can initialize with significantly different momentum profiles, including varying magnitudes and directions of horizontal drift (`x_vel`) and vertical velocities (`y_vel`).
9. **Micro-Oscillatory Stability and Action 0**: Post-contact stability is maintained through high-frequency engine corrections involving all actions; Action 0 (nothing) is critical for managing drift, damping oscillations, or preventing over-correction between active engine pulses.
10. **Terminal Success vs. Step-Limit Partiality**: A "SUCCESS" outcome is a discrete terminal state; a "PARTIAL" outcome occurs when the simulation reaches the 1000-step maximum limit, which can happen even if the lander has achieved successful contact and established a stable, near-zero velocity state.

---

## 2026-07-05 21:22:58

1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces significant changes in both `angle` and `ang_vel` due to the lander's orientation.
2. **Body-Fixed Thrust Projection**: All engine actions (1, 2, and 3) are body-fixed; their influence on the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Differential Lateral Torque**: Actions 1 (left engine) and 3 (right engine) provide angular torques that modify `ang_vel` and `angle`, with the direction of effect determining if the rotation is amplified or attenuated.
4. **Transient Leg Contact and Rebound Dynamics**: Leg contact is not a permanent state; the lander can experience a "rebound" where contact is lost (transitioning 1.0 to 0.0) due to high vertical or angular velocities, before re-establishing contact.
5. **Cross-Axis Engine Coupling**: The main engine (Action 2) induces horizontal acceleration (`x_vel`) when the lander is tilted, and lateral engines (Actions 1 and 3) can induce significant horizontal deceleration or vertical acceleration (`y_vel`) depending on the `angle`.
6. **Contact-Triggered Reward Volatility**: Transitions between leg contact states (0.0 $\leftrightarrow$ 1.0) are associated with extreme reward volatility, including both massive positive spikes upon contact and significant negative penalties during the loss of contact or rebound phases.
7. **Post-Contact Ground Penetration and Velocity Stabilization**: Following initial leg contact, the lander's `y_pos` often stabilizes in a narrow band slightly below the zero threshold while the system utilizes high-frequency corrections to maintain near-zero `y_vel` and `ang_vel`.
8. **Variable Initial State Momentum**: The simulation can initialize with significantly different momentum profiles, including varying magnitudes and directions of horizontal drift (`x_vel`) and vertical velocities (`y_vel`).
9. **Micro-Oscillatory Stability and Action 0**: Post-contact stability is maintained through high-frequency engine corrections involving all actions; Action 0 (nothing) is critical for managing drift, damping oscillations, or preventing over-correction between active engine pulses.
10. **Terminal Success vs. Step-Limit Partiality**: A "SUCCESS" outcome is a discrete terminal state; a "PARTIAL" outcome occurs when the simulation reaches the 1000-step maximum limit, which can happen even if the lander has achieved successful contact and established a stable, near-zero velocity state.

---

## 2026-07-05 22:01:57

1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces significant changes in both `angle` and `ang_vel` due to the lander's orientation.
2. **Body-Fixed Thrust Projection**: All engine actions (1, 2, and 3) are body-fixed; their influence on the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Differential Lateral Torque**: Actions 1 (left engine) and 3 (right engine) provide angular torques that modify `ang_vel` and `angle`, with the direction of effect determining if the rotation is amplified or attenuated.
4. **Independent and Transient Leg Contact**: Leg contact is not a simultaneous binary state; individual legs can transition independently (1.0 $\leftrightarrow$ 0.0), and the lander can experience "rebound" where contact is lost due to vertical or angular velocity before re-establishing it.
5. **Cross-Axis Engine Coupling**: The main engine (Action 2) induces horizontal acceleration (`x_vel`) when the lander is tilted, and lateral engines (Actions 1 and 3) can induce significant horizontal deceleration or vertical acceleration (`y_vel`) depending on the `angle`.
6. **Contact-Triggered Reward Volatility**: Transitions in leg contact states are associated with extreme reward volatility; while initial contact often triggers massive positive spikes, subsequent rapid oscillations in contact status or high-velocity impacts can trigger significant negative penalties.
7. **Post-Contact Equilibrium and Ground Penetration**: Once contact is established, `y_pos` typically stabilizes in a narrow band around the zero threshold, but the system maintains near-zero `y_vel` and `ang_vel` through high-frequency, micro-oscillatory corrections.
8. **Variable Initial State Momentum**: The simulation can initialize with significantly different momentum profiles, including varying magnitudes and directions of horizontal drift (`x_vel`) and vertical velocities (`y_vel`).
9. **Micro-Oscillatory Stability and Action 0**: Post-contact stability is maintained through high-frequency engine corrections involving all actions; Action 0 (nothing) is critical for managing drift, damping oscillations, or preventing over-correction between active engine pulses.
10. **Terminal Success vs. Step-Limit Partiality**: A "SUCCESS" outcome is a discrete terminal state; a "PARTIAL" outcome occurs when the simulation reaches the 1000-step maximum limit, which can happen even if the lander has achieved successful contact and established a stable, near-zero velocity state.

---

## 2026-07-05 22:04:45

---
1. **Main Engine (Action 2) Multidimensionality**: Action 2 provides vertical thrust to regulate `y_pos` and `y_vel` but also induces significant changes in both `angle` and `ang_vel` due to the lander's orientation.
2. **Body-Fixed Thrust Projection**: All engine actions (1, 2, and 3) are body-fixed; their influence on the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Differential Lateral Torque**: Actions 1 (left engine) and 3 (right engine) provide angular torques that modify `ang_vel` and `angle`, with the direction of effect determining if the rotation is amplified or attenuated.
4. **Independent and Transient Leg Contact**: Leg contact is not a simultaneous binary state; individual legs can transition independently (1.0 $\leftrightarrow$ 0.0), and the lander can experience "rebound" where contact is lost due to vertical or angular velocity before re-establishing it.
5. **Cross-Axis Engine Coupling**: The main engine (Action 2) induces horizontal acceleration (`x_vel`) when the lander is tilted, and lateral engines (Actions 1 and 3) can induce significant horizontal deceleration or vertical acceleration (`y_vel`) depending on the `angle`.
6. **Contact-Transition Reward Spikes**: Massive positive reward spikes are triggered specifically by the discrete transition of `left_leg_contact` or `right_leg_contact` from 0.0 to 1.0.
7. **Post-Contact Vertical Equilibrium**: Once contact is established, `y_pos` typically stabilizes in a narrow band around the zero threshold, while `y_vel` is maintained near zero through continuous engine corrections.
8. **Variable Initial State Momentum**: The simulation can initialize with significantly different momentum profiles, including high-magnitude horizontal drift (`x_vel`) and vertical velocities (`y_vel`) that must be managed prior to touchdown.
9. **Post-Contact Angular Stabilization**: Following contact, maintaining a stable `angle` and near-zero `ang_vel` requires high-frequency, micro-oscillatory pulses from lateral engines (Actions 1 and 3) to counteract residual angular momentum and prevent tipping.
10. **Terminal Success vs. Step-Limit Partiality**: A "SUCCESS" outcome is a discrete terminal state; a "PARTIAL" outcome occurs when the simulation reaches the 1000-step maximum limit, which can happen even if the lander has achieved successful contact and established a stable, near-zero velocity state.

---

## 2026-07-05 22:09:48

---
1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but it is heavily coupled with the lander's rotation, inducing changes in both `angle` and `ang_vel` based on the current orientation.
2. **Body-Fixed Thrust Projection**: All engine actions (1, 2, and 3) are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Translation/Rotation Duality**: Actions 1 (left) and 3 (right) are not purely rotational; depending on the `angle`, they provide significant translational thrust that can be used to counteract both horizontal (`x_vel`) and vertical (`y_vel`) momentum.
4. **Independent and Transient Leg Contact**: The two legs can transition between contact states (0.0 $\leftrightarrow$ 1.0) independently, allowing for single-leg contact or "rebound" scenarios before a stable landing is established.
5. **Main Engine Cross-Axis Coupling**: Due to the lander's tilt, the main engine (Action 2) induces unintended horizontal acceleration (`x_vel`), requiring lateral engine corrections to maintain a vertical descent path.
6. **Contact-Transition Reward Spikes**: Massive positive reward spikes are triggered at the specific time step where a leg's contact state transitions from 0.0 to 1.0.
7. **Post-Contact Vertical and Angular Equilibrium**: Once contact is established, maintaining stability requires continuous, low-magnitude engine corrections to keep `y_pos` near the ground threshold and `angle` near zero.
8. **Variable Initial State Momentum**: The simulation presents diverse initial momentum profiles; for example, high negative `x_vel` paired with high positive `y_vel` requires specific initial lateral engine vectors to stabilize.
9. **Post-Contact Angular Stabilization**: Following successful leg contact, preventing the lander from tipping requires high-frequency, micro-oscillatory pulses from lateral engines (Actions 1 and 3) to dampen residual `ang_vel`.
10. **Terminal Success vs. Step-Limit Partiality**: A "PARTIAL" outcome indicates the simulation reached the 1000-step limit, which can occur even if the lander has achieved successful, stable, and low-velocity contact with the ground.

---

## 2026-07-05 22:11:59

1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but is heavily coupled with the lander's rotation, inducing changes in both `angle` and `ang_vel` based on the current orientation.
2. **Body-Fixed Thrust Projection**: All engine actions (1, 2, and 3) are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Translation/Rotation Duality**: Actions 1 (left) and 3 (right) are not purely rotational; depending on the `angle`, they provide significant translational thrust that can be used to counteract both horizontal (`x_vel`) and vertical (`y_vel`) momentum.
4. **Independent and Transient Leg Contact**: The two legs can transition between contact states (0.0 $\leftrightarrow$ 1.0) independently, allowing for single-leg contact or "rebound" scenarios before a stable landing is established.
5. **Main Engine Cross-Axis Coupling**: Due to the lander's tilt, the main engine (Action 2) induces unintended horizontal acceleration (`x_vel`), requiring lateral engine corrections to maintain a vertical descent path.
6. **Velocity-Dependent Contact-Transition Rewards**: Massive reward spikes are triggered at the specific time step where a leg's contact state transitions from 0.0 to 1.0; the magnitude of these spikes varies (e.g., ~21.8 vs ~13.3), likely influenced by the lander's linear or angular velocity at impact.
7. **Post-Contact Vertical and Angular Equilibrium**: Once contact is established, maintaining stability requires continuous, low-magnitude engine corrections to keep `y_pos` near the ground threshold and `angle` near zero.
8. **High-Magnitude Terminal Success Reward**: A successful landing—achieving stable contact—is marked by a massive terminal reward (e.g., 100.0) and immediate episode termination.
9. **Post-Contact Angular Stabilization**: Following successful leg contact, preventing the lander from tipping requires high-frequency, micro-oscillatory pulses from lateral engines (Actions 1 and 3) to dampen residual `ang_vel`.
10. **Terminal Success vs. Step-Limit Partiality**: A "PARTIAL" outcome indicates the simulation reached the step limit (e.g., 1000 steps) without triggering the terminal success reward, which can occur even if the lander has achieved successful, stable, and low-velocity contact with the ground.

---

## 2026-07-05 22:15:27

---
1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but its effects are heavily coupled with the lander's orientation, inducing changes in both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions (1, 2, and 3) are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Translation/Rotation Duality**: Actions 1 (left) and 3 (right) are not purely rotational; they provide translational thrust that can be used to counteract both horizontal (`x_vel`) and vertical (`y_vel`) momentum depending on the lander's tilt.
4. **Leg Contact Volatility**: The two legs can transition between contact states (0.0 $\leftrightarrow$ 1.0) independently. Contact is not necessarily permanent; landers can lose contact (1.0 $\to$ 0.0) due to instability, rebounds, or tipping.
5. **Main Engine Cross-Axis Coupling**: Due to the lander's tilt, the main engine (Action 2) induces unintended horizontal acceleration (`x_vel`), requiring lateral engine corrections to maintain a vertical descent path.
6. **Contact-Transition Reward Dynamics**: Massive reward spikes are triggered at the specific time step where a leg's contact state transitions (0 $\to$ 1 or 1 $\to$ 0). The sign and magnitude of these spikes are highly sensitive to the lander's state; for example, losing contact (1 $\to$ 0) during instability or a rebound can result in significant negative rewards.
7. **Post-Contact Vertical and Angular Equilibrium**: Once contact is established, maintaining stability requires continuous, low-magnitude engine corrections to keep `y_pos` near the ground threshold and `angle` near zero.
8. **High-Magnitude Terminal Success Reward**: A successful landing—achieving stable contact—is marked by a massive terminal reward and immediate episode termination.
9. **Post-Contact Angular Stabilization**: Following successful leg contact, preventing the lander from tipping or rebounding requires high-frequency, micro-oscillatory pulses from lateral engines (Actions 1 and 3) to dampen residual `ang_vel`.
10. **Terminal Success vs. Step-Limit Partiality**: A "PARTIAL" outcome indicates the simulation reached the step limit without triggering the terminal success reward, which can occur even if the lander has achieved stable, low-velocity contact with the ground.

---

## 2026-07-05 22:21:28

1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but its effects are heavily coupled with the lander's orientation, inducing significant changes in both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions (1, 2, and 3) are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Translation/Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal and vertical momentum, but they also induce rotation, making them double-edged tools for stability.
4. **Contact-Transition Reward Sign-Sensitivity**: Leg contact transitions ($0.0 \leftrightarrow 1.0$) trigger massive reward spikes: transitions from $0 \to 1$ (landing) produce large positive rewards, whereas transitions from $1 \to 0$ (losing contact) produce large negative rewards.
5. **Main Engine Cross-Axis Coupling**: Due to the lander's tilt, the main engine (Action 2) induces unintended horizontal acceleration (`x_vel`), necessitating lateral engine corrections to maintain a vertical descent path.
6. **Inefficacy of Inaction (Action 0)**: Choosing Action 0 (nothing) frequently results in negative rewards during descent and contact phases, suggesting it is unable to counteract gravity or maintain the necessary forces for stability.
7. **Post-Contact Vertical and Angular Equilibrium**: Once contact is established, maintaining stability requires continuous, low-magnitude engine corrections to keep `y_pos` near the ground threshold and `angle` near zero.
8. **High-Magnitude Terminal Success Reward**: A successful landing—achieving stable contact—is marked by a massive terminal reward and immediate episode termination.
9. **Post-Contact Angular Stabilization**: Following successful leg contact, preventing the lander from tipping or rebounding requires high-frequency, micro-oscillatory pulses from lateral engines (Actions 1 and 3) to dampen residual `ang_vel`.
10. **Terminal Success vs. Step-Limit Partiality**: A "PARTIAL" outcome indicates the simulation reached the step limit without triggering the terminal success reward, which can occur even if the lander has achieved stable, low-velocity contact with the ground.

---

## 2026-07-05 22:23:48

1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but its effects are heavily coupled with the lander's orientation, inducing significant changes in both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Translation/Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal and vertical momentum, but they also induce rotation, making them double-edged tools for stability.
4. **Asymmetric Leg Contact States**: The environment tracks `left_leg_contact` and `right_leg_contact` independently; trajectories show the lander can enter partial contact states where one leg is grounded ($1.0$) while the other remains airborne ($0.0$).
5. **Main Engine Cross-Axis Coupling**: Due to the lander's tilt, the main engine (Action 2) induces unintended horizontal acceleration (`x_vel`), necessitating lateral engine corrections to maintain a vertical descent path.
6. **Inefficacy of Inaction (Action 0)**: Choosing Action 0 (nothing) frequently results in negative rewards during descent and contact phases, as it is unable to counteract gravity or maintain necessary forces.
7. **Post-Contact Vertical Equilibrium**: Once contact is established, `y_pos` stabilizes extremely close to the ground threshold (often $\le 0.0$), and maintaining this state requires continuous engine input to prevent rebounding.
8. **Contact-Transition Reward Spikes**: Transitions of leg contact from $0.0 \to 1.0$ trigger massive, immediate positive reward spikes, which are the primary drivers for successful landing behavior.
9. **Post-Contact Damping and Stabilization**: Following leg contact, preventing the lander from tipping or rebounding requires high-frequency, low-magnitude engine pulses (using Actions 1, 2, or 3) to dampen residual `ang_vel` and `y_vel`.
10. **Terminal Success vs. Step-Limit Partiality**: A "PARTIAL" outcome indicates the simulation reached the step limit without triggering the terminal success reward, which can occur even if the lander has achieved stable, low-velocity contact with the ground.

---

## 2026-07-05 22:28:13

1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but its effects are heavily coupled with the lander's orientation, inducing significant changes in both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal and vertical momentum, but they also induce rotation, making them double-edged tools for stability.
4. **Asymmetric Leg Contact States**: The environment tracks `left_leg_contact` and `right_leg_contact` independently; trajectories show the lander can enter partial contact states where one leg is grounded ($1.0$) while the other remains airborne ($0.0$).
5. **Main Engine Cross-Axis Coupling**: Due to the lander's tilt, the main engine (Action 2) induces unintended horizontal acceleration (`x_vel`), necessitating lateral engine corrections to maintain a vertical descent path.
6. **Inefficacy of Inaction (Action 0)**: Choosing Action 0 (nothing) frequently results in negative rewards during descent and contact phases, as it is unable to counteract gravity or maintain necessary forces.
7. **Post-Contact Vertical Equilibrium**: Once contact is established, `y_pos` stabilizes extremely close to the ground threshold (often $\le 0.0$), and maintaining this state requires continuous engine input to prevent rebounding.
8. **Leg-Contact Reward Magnitude**: Transitions of leg contact from $0.0 \to 1.0$ trigger substantial, immediate reward spikes (observed in the range of 11.0 to 12.7), which serve as key signals for landing success.
9. **Post-Contact Damping and Stabilization**: Following leg contact, preventing the lander from tipping or rebounding requires high-frequency, low-magnitude engine pulses (using Actions 1, 2, or 3) to dampen residual `ang_vel` and `y_vel`.
10. **Terminal Success Reward vs. Step-Limit**: A terminal success is identified by a reward of 100.0; a "PARTIAL" outcome indicates the simulation reached the step limit without triggering this specific terminal success reward.

---

## 2026-07-05 22:30:41

---
1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but its effects are heavily coupled with the lander's orientation, inducing significant changes in both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal and vertical momentum, but they also induce rotation, making them double-edged tools for stability.
4. **Asymmetric Leg Contact States**: The environment tracks `left_leg_contact` and `right_leg_contact` independently; trajectories show the lander can enter partial contact states where one leg is grounded ($1.0$) while the other remains airborne ($0.0$).
5. **Main Engine Cross-Axis Coupling**: Due to the lander's tilt, the main engine (Action 2) induces unintended horizontal acceleration (`x_vel`), necessitating lateral engine corrections to maintain a vertical descent path.
6. **Inefficacy of Inaction (Action 0)**: Choosing Action 0 (nothing) frequently results in negative rewards during descent and contact phases, as it is unable to counteract gravity or maintain necessary forces.
7. **Post-Contact Vertical Equilibrium**: Once contact is established, `y_pos` stabilizes extremely close to the ground threshold (often $\le 0.0$), and maintaining this state requires continuous engine input to prevent rebounding.
8. **Leg-Contact Reward Magnitude**: Transitions of leg contact from $0.0 \to 1.0$ trigger substantial, immediate reward spikes (observed in the range of 11.0 to 13.8), which serve as key signals for landing success.
9. **Grounded State Lateral Instability**: Applying lateral thrust (Actions 1 or 3) while in a grounded state ($1.0$) frequently induces torque sufficient to cause the lander to tip or bounce, resulting in severe negative rewards (magnitude $\approx -10.0$) and a subsequent transition of leg contact back to $0.0$.
10. **Terminal Success Reward vs. Step-Limit**: A terminal success is identified by a reward of 100.0; a "PARTIAL" outcome indicates the simulation reached the step limit without triggering this specific terminal success reward.

---

## 2026-07-05 22:33:29

1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but its effects are heavily coupled with the lander's orientation, inducing significant changes in both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal and vertical momentum, but they also induce rotation, making them double-edged tools for stability.
4. **Asymmetric Leg Contact States**: The environment tracks `left_leg_contact` and `right_leg_contact` independently; trajectories show the lander can enter partial contact states where one leg is grounded ($1.0$) while the other remains airborne ($0.0$).
5. **Main Engine Cross-Axis Coupling**: Due to the lander's tilt, the main engine (Action 2) induces unintended horizontal acceleration (`x_vel`), necessitating lateral engine corrections to maintain a vertical descent path.
6. **Inefficacy of Inaction (Action 0)**: Choosing Action 0 (nothing) frequently results in negative rewards during descent and contact phases, as it is unable to counteract gravity or maintain necessary forces.
7. **Post-Contact Vertical Equilibrium**: Once contact is established, `y_pos` stabilizes extremely close to the ground threshold (often $\le 0.0$), and maintaining this state requires continuous engine input to prevent rebounding.
8. **Leg-Contact Reward Magnitude**: Transitions of leg contact from $0.0 \to 1.0$ trigger substantial, immediate reward spikes (observed in the range of 8.3 to 13.0), which serve as key signals for landing success.
9. **Instability and Contact Loss**: Grounded states ($1.0$) are susceptible to torque-induced tipping (often via lateral thrust), where the transition of a leg contact from $1.0$ back to $0.0$ triggers a severe, consistent negative reward of approximately $-10.4$.
10. **Terminal Success Reward vs. Step-Limit**: A terminal success is identified by a reward of 100.0; a "PARTIAL" outcome indicates the simulation reached the step limit without triggering this specific terminal success reward.

---

## 2026-07-05 22:37:51

1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but its effects are heavily coupled with the lander's orientation, inducing significant changes in both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal and vertical momentum, but they also induce rotation, making them double-edged tools for stability.
4. **Asymmetric Leg Contact States**: The environment tracks `left_leg_contact` and `right_leg_contact` independently; trajectories show the lander can enter partial contact states where one leg is grounded ($1.0$) while the other remains airborne ($0.0$).
5. **Main Engine Cross-Axis Coupling**: Due to the lander's tilt, the main engine (Action 2) induces unintended horizontal acceleration (`x_vel`), necessitating lateral engine corrections to maintain a vertical descent path.
6. **Inefficacy of Inaction (Action 0)**: Choosing Action 0 (nothing) frequently results in negative rewards during descent and contact phases, as it is unable to counteract gravity or maintain necessary forces.
7. **Post-Contact Vertical Equilibrium**: Once contact is established, `y_pos` stabilizes extremely close to the ground threshold (often $\le 0.0$), and maintaining this state requires continuous engine input to prevent rebounding or tipping.
8. **Leg-Contact Reward Tiers**: Transitions to leg contact trigger significant reward spikes; single-leg contact transitions ($0 \to 1$) typically yield rewards in the 8.3 to 13.1 range, while transitions resulting in simultaneous dual-leg contact ($0,0 \to 1,1$) can trigger substantially higher spikes (e.g., $\sim 24.7$).
9. **Instability and Contact Loss**: Grounded states ($1.0$) are susceptible to torque-induced tipping (often via lateral thrust), where the transition of a leg contact from $1.0$ back to $0.0$ triggers a severe negative reward (observed in the range of $-10.4$ to $-11.0$).
10. **Terminal Success Reward vs. Step-Limit**: A terminal success is identified by a reward of 100.0; a "PARTIAL" outcome indicates the simulation reached the step limit without triggering this specific terminal success reward, even if the lander has achieved a stable grounded state.

---

## 2026-07-05 22:40:04

1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but its effects are heavily coupled with the lander's orientation, inducing significant changes in both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal and vertical momentum, but they also induce rotation, making them double-edged tools for stability.
4. **Asymmetric Leg Contact States**: The environment tracks `left_leg_contact` and `right_leg_contact` independently; trajectories show the lander can enter partial contact states where one leg is grounded ($1.0$) while the other remains airborne ($0.0$).
5. **Main Engine Cross-Axis Coupling**: Due to the lander's tilt, the main engine (Action 2) induces unintended horizontal acceleration (`x_vel`), necessitating lateral engine corrections to maintain a vertical descent path.
6. **Inefficacy of Inaction (Action 0)**: Choosing Action 0 (nothing) frequently results in negative rewards during descent and contact phases, as it is unable to counteract gravity or maintain necessary forces.
7. **Post-Contact Stabilization**: Once contact is established, the lander can maintain equilibrium near $y\_pos \approx 0.0$ by using continuous engine input, including lateral thrust (Actions 1 and 3), to prevent rebounding or tipping.
8. **Variable Contact Transition Rewards**: Transitions to leg contact trigger reward spikes; single-leg contact transitions typically yield rewards in the 13.0 to 15.0 range, while the subsequent transition to dual-leg contact ($1,0 \to 1,1$) is highly variable, yielding rewards ranging from positive spikes to negative values depending on the lander's stability at the moment of contact.
9. **Instability and Contact Loss**: Grounded states ($1.0$) are susceptible to torque-induced tipping (often via lateral thrust), where the transition of a leg contact from $1.0$ back to $0.0$ triggers a severe negative reward.
10. **Terminal Reward and Outcome Distinction**: A terminal reward of 100.0 is granted upon reaching a stable state, but an episode can be classified as 'PARTIAL' if it terminates due to reaching the step limit, even if the 100.0 reward is triggered in the final step.

---

## 2026-07-05 22:45:09

1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but its effects are heavily coupled with the lander's orientation, inducing significant changes in both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal and vertical momentum, but they also induce rotation, making them double-edged tools for stability.
4. **Asymmetric Leg Contact States**: The environment tracks `left_leg_contact` and `right_leg_contact` independently; trajectories show the lander can enter partial contact states where one leg is grounded ($1.0$) while the other remains airborne ($0.0$).
5. **Contact Transition Rewards**: Transitions to single-leg contact ($0,0 \to 1,0$ or $0,1$) trigger high rewards, typically in the 13.0 to 15.0 range. Subsequent transitions to dual-leg contact ($1,0 \to 1,1$) are also highly variable and can yield significant positive rewards.
6. **Contact Loss Penalty**: Transitioning a leg from a grounded state ($1.0$) back to an airborne state ($0.0$)—often caused by torque-induced tipping—triggers a severe negative reward, observed in the range of -10.0 to -11.0.
7. **Post-Contact Stabilization and Ground Granularity**: Once contact is established, the lander can maintain equilibrium near $y\_pos \approx 0.0$. The ground level is not an absolute barrier at $y=0.0$; the lander can exhibit slightly negative $y\_pos$ values (e.g., $\approx -0.001$) while maintaining leg contact.
8. **Main Engine Cross-Axis Coupling**: Due to the lander's tilt, the main engine (Action 2) induces unintended horizontal acceleration (`x_vel`), necessitating lateral engine corrections to maintain a vertical descent path.
9. **Inefficacy of Inaction (Action 0)**: Choosing Action 0 (nothing) frequently results in negative rewards during descent and contact phases, as it is unable to counteract gravity or maintain necessary forces.
10. **Terminal Reward and Outcome Distinction**: A terminal reward of 100.0 is granted upon reaching a stable state, but an episode can be classified as 'PARTIAL' if it terminates due to reaching the step limit, even if high rewards are achieved in the final steps.

---

## 2026-07-05 22:47:41

---
1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but its effects are heavily coupled with the lander's orientation, inducing significant changes in both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal and vertical momentum, but they also induce rotation, making them double-edged tools for stability.
4. **Asymmetric Leg Contact States**: The environment tracks `left_leg_contact` and `right_leg_contact` independently; trajectories show the lander can enter partial contact states where one leg is grounded ($1.0$) while the other remains airborne ($0.0$).
5. **Contact Transition Rewards**: Transitions to single-leg contact trigger high rewards (13.0 to 15.0), while transitions to dual-leg contact ($1,1$) are also highly rewarding, with observed values in the 10.0 to 12.5 range.
6. **Contact Loss Penalty**: Transitioning a leg from a grounded state ($1.0$) back to an airborne state ($0.0$)—often caused by torque-induced tipping—triggers a severe negative reward, observed in the range of -10.0 to -11.0.
7. **Post-Contact Stabilization and Ground Granularity**: Once dual-leg contact is established, the lander can maintain equilibrium near $y\_pos \approx 0.0$ (or slightly below) using minimal engine input, such as Action 0 or minor lateral corrections.
8. **Main Engine Cross-Axis Coupling**: Due to the lander's tilt, the main engine (Action 2) induces unintended horizontal acceleration (`x_vel`), necessitating lateral engine corrections to maintain a vertical descent path.
9. **Phase-Dependent Utility of Inaction (Action 0)**: While Action 0 is ineffective during descent as it cannot counteract gravity, it is a viable and effective strategy for maintaining stability and high rewards once dual-leg contact is achieved.
10. **Terminal Reward and Outcome Distinction**: A terminal reward of 100.0 is granted upon reaching a stable state, but an episode can be classified as 'PARTIAL' if it terminates due to reaching the step limit, even if high rewards are achieved in the final steps.

---

## 2026-07-05 22:49:45

1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but its effects are heavily coupled with the lander's orientation, inducing significant changes in both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal and vertical momentum, but they also induce rotation, making them double-edged tools for stability.
4. **Asymmetric Leg Contact States**: The environment tracks `left_leg_contact` and `right_leg_contact` independently; trajectories show the lander can enter partial contact states where one leg is grounded ($1.0$) while the other remains airborne ($0.0$).
5. **Contact Transition Rewards**: High rewards are triggered by the *transition* into contact. Moving into a single-leg contact state ($1,0$ or $0,1$) provides significant rewards, observed in the 10.0 to 13.0 range.
6. **Contact Loss Penalty**: Transitioning a leg from a grounded state ($1.0$) back to an airborne state ($0.0$)—often caused by torque-induced tipping—triggers a severe negative reward, observed in the range of -10.0 to -11.0.
7. **Post-Contact Grounded Stability**: Once contact (single or dual leg) is established, the lander can maintain equilibrium near $y\_pos \approx 0.0$ for a significant number of subsequent steps.
8. **Main Engine Cross-Axis Coupling**: Due to the lander's tilt, the main engine (Action 2) induces unintended horizontal acceleration (`x_vel`), necessitating lateral engine corrections to maintain a vertical descent path.
9. **Phase-Dependent Utility of Inaction (Action 0)**: While Action 0 is ineffective during descent as it cannot counteract gravity, it is a viable and effective strategy for maintaining stability and high rewards once dual-leg contact is achieved.
10. **Terminal Reward and Outcome Distinction**: A terminal reward of 100.0 is granted upon reaching a stable state, but an episode is classified as 'PARTIAL' if it terminates due to reaching the step limit, even if high rewards and a stable landing were achieved in the final steps.

---

## 2026-07-05 22:54:58

1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but its effects are heavily coupled with the lander's orientation, inducing significant changes in both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal and vertical momentum, but they also induce rotation, making them double-edged tools for stability.
4. **Asymmetric Leg Contact States**: The environment tracks `left_leg_contact` and `right_leg_contact` independently; trajectories show the lander can enter partial contact states where one leg is grounded ($1.0$) while the other remains airborne ($0.0$).
5. **Contact Transition Rewards**: High rewards are triggered by the transition into contact. Significant positive rewards are granted when moving from an airborne state ($0,0$) into a single-leg contact state ($1,0$ or $0,1$) or a dual-leg contact state ($1,1$).
6. **Contact Loss Penalty**: Transitioning a leg from a grounded state ($1.0$) back to an airborne state ($0.0$)—often caused by torque-induced tipping—triggers a severe negative reward.
7. **Post-Contact Grounded Stability**: Once contact (single or dual leg) is established, the lander can maintain equilibrium near $y\_pos \approx 0.0$ for a significant number of subsequent steps.
8. **Main Engine Cross-Axis Coupling**: Due to the lander's tilt, the main engine (Action 2) induces unintended horizontal acceleration (`x_vel`), necessitating lateral engine corrections to maintain a vertical descent path.
9. **Phase-Dependent Utility of Inaction (Action 0)**: While Action 0 is ineffective during descent as it cannot counteract gravity, it is a viable and effective strategy for maintaining stability and high rewards once dual-leg contact is achieved.
10. **Terminal Reward and Outcome Distinction**: A terminal reward of 100.0 is granted upon reaching a stable state, but an episode is classified as 'PARTIAL' if it terminates due to reaching the step limit, even if high rewards and a stable landing were achieved in the final steps.

---

## 2026-07-05 22:57:54

---
1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but its effects are heavily coupled with the lander's orientation, inducing significant changes in both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal momentum, but they also induce rotation, making them double-edged tools for stability.
4. **Asymmetric Leg Contact States**: The environment tracks `left_leg_contact` and `right_leg_contact` independently; trajectories show the lander can enter and maintain single-leg contact states ($1,0$ or $0,1$) for extended periods.
5. **Contact Transition Rewards**: High rewards are triggered by the transition into contact; significant positive rewards are granted when moving from an airborne state ($0,0$) into either single-leg or dual-leg contact states.
6. **Contact Loss Penalty**: Transitioning a leg from a grounded state ($1.0$) back to an airborne state ($0.0$)—often caused by torque-induced tipping—triggers a severe negative reward.
7. **Engine-Induced Tipping during Ground Contact**: While in a contact state, applying lateral engines (Action 1 or 3) can induce sufficient torque to cause a transition from dual-leg contact ($1,1$) back to a single-leg state ($1,0$ or $0,1$), triggering the Contact Loss Penalty.
8. **Main Engine Cross-Axis Coupling**: Due to the lander's tilt, the main engine (Action 2) induces unintended horizontal acceleration (`x_vel`), necessitating lateral engine corrections to maintain a vertical descent path.
9. **Phase-Dependent Utility of Inaction (Action 0)**: While Action 0 is ineffective during descent as it cannot counteract gravity, it is a viable and effective strategy for maintaining stability and high rewards once dual-leg contact is achieved.
10. **Terminal Reward and Outcome Distinction**: A terminal reward of 100.0 is granted upon reaching a stable state, but an episode is classified as 'PARTIAL' if it terminates due to reaching the step limit, even if high rewards and a stable landing were achieved.

---

## 2026-07-05 23:04:23

1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but its effects are heavily coupled with the lander's orientation, inducing significant changes in both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal momentum, but they also induce rotation, making them double-edged tools for stability.
4. **Asymmetric Leg Contact States**: The environment tracks `left_leg_contact` and `right_leg_contact` independently; trajectories show the lander can enter and maintain single-leg contact states ($1,0$ or $0,1$) for extended periods.
5. **Contact Transition Rewards**: Significant positive rewards are triggered by the transition from an airborne state ($0,0$) into a contact state ($1,0$ or $0,1$), as well as the transition from a single-leg contact state ($1,0$ or $0,1$) to a dual-leg contact state ($1,1$).
6. **Contact Loss Penalty**: Transitioning a leg from a grounded state ($1.0$) back to an airborne state ($0.0$)—resulting in either a single-leg state ($1,0$ or $0,1$) or a total loss of contact ($0,0$)—triggers a severe negative reward.
7. **Engine-Induced Tipping or Lifting**: While in contact, applying lateral engines (Action 1 or 3) can induce sufficient torque to lift a leg, causing a transition from dual-leg to single-leg contact or from single-leg to airborne, triggering the Contact Loss Penalty.
8. **Main Engine Cross-Axis Coupling**: Due to the lander's tilt, the main engine (Action 2) induces unintended horizontal acceleration (`x_vel`), necessitating lateral engine corrections to maintain a vertical descent path.
9. **Phase-Dependent Utility of Inaction (Action 0)**: While Action 0 is ineffective during descent as it cannot counteract gravity, it is a viable and effective strategy for maintaining stability and high rewards once dual-leg contact is achieved.
10. **Terminal Reward and Outcome Distinction**: A terminal reward of 100.0 is granted upon reaching a stable state, but an episode is classified as 'PARTIAL' if it terminates due to reaching the step limit, even if high rewards and a stable landing were achieved.

---

## 2026-07-05 23:06:42

---
1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but its effects are heavily coupled with the lander's orientation, inducing significant changes in both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal momentum, but they also induce rotation, making them double-edged tools for stability.
4. **Asymmetric Leg Contact States**: The environment tracks `left_leg_contact` and `right_leg_contact` independently; trajectories show the lander can enter and maintain single-leg contact states ($1,0$ or $0,1$) for extended periods.
5. **Contact Transition Rewards**: Significant positive rewards are triggered by the transition from an airborne state ($0,0$) into a contact state ($1,0$ or $0,1$), as well as the transition from a single-leg contact state ($1,0$ or $0,1$) to a dual-leg contact state ($1,1$).
6. **Contact Loss Penalty**: Transitioning a leg from a grounded state ($1.0$) back to an airborne state ($0.0$)—resulting in either a single-leg state ($1,0$ or $0,1$) or a total loss of contact ($0,0$)—triggers a severe negative reward.
7. **Engine-Induced Tipping or Lifting**: While in contact, applying lateral engines (Action 1 or 3) can induce sufficient torque to lift a leg, causing a transition from dual-leg to single-leg contact or from single-leg to airborne, triggering the Contact Loss Penalty.
8. **Post-Landing Stabilization Requirements**: Achieving dual-leg contact ($1,1$) does not result in a passive/static state; the lander must perform continuous micro-adjustments using lateral engines (Actions 1 and 3) and inaction (Action 0) to prevent drift in `x_pos`, `angle`, and `ang_vel`.
9. **Grounded Vertical Velocity Management**: Even after touchdown, the main engine (Action 2) is utilized to regulate `y_pos` and `y_vel`, suggesting that vertical stability and pressure management are required to maintain a stable grounded state.
10. **Terminal Reward and Outcome Distinction**: A terminal reward of 100.0 is granted upon reaching a stable state, but an episode is classified as 'PARTIAL' if it terminates due to reaching the step limit, even if high rewards and a stable landing were achieved.

---

## 2026-07-05 23:09:40

1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but its effects are heavily coupled with the lander's orientation, inducing significant changes in both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal momentum, but they also induce rotation, making them double-edged tools for stability.
4. **Asymmetric Leg Contact States**: The environment tracks `left_leg_contact` and `right_leg_contact` independently; trajectories show the lander can enter and maintain single-leg contact states ($1,0$ or $0,1$) for extended periods.
5. **High-Magnitude Contact Transition Rewards**: Significant positive rewards are triggered by the transition from an airborne state ($0,0$) into a single-leg contact state ($1,0$ or $0,1$), as well as the transition from a single-leg contact state into a dual-leg contact state ($1,1$).
6. **Severe Contact Loss Penalty**: Transitioning a leg from a grounded state back to an airborne state—specifically transitioning from a dual-leg contact state ($1,1$) to a single-leg state ($1,0$ or $0,1$) or a total loss of contact ($0,0$)—triggers a massive negative reward.
7. **Engine-Induced Tipping or Lifting**: While in contact, applying lateral engines (Action 1 or 3) can induce sufficient torque to lift a leg, causing a transition from dual-leg to single-leg contact or from single-leg to airborne, triggering the Contact Loss Penalty.
8. **Post-Landing Stabilization Requirements**: Achieving dual-leg contact ($1,1$) does not result in a passive state; the lander requires continuous micro-adjustments using lateral engines (Actions 1 and 3) and inaction (Action 0) to prevent drift in `x_pos`, `angle`, and `ang_vel`.
9. **Grounded Vertical Velocity Management**: Even after touchdown, the main engine (Action 2) is utilized to regulate `y_pos` and `y_vel`, suggesting that vertical stability and pressure management are required to maintain a stable grounded state.
10. **Terminal Reward and Outcome Distinction**: A terminal reward is granted upon reaching a stable state, but an episode is classified as 'PARTIAL' if it terminates due to reaching the step limit, regardless of whether high rewards and a stable landing were achieved.

---

## 2026-07-05 23:14:55

1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but its effects are heavily coupled with the lander's orientation, inducing significant changes in both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal momentum, but they also induce rotation, making them double-edged tools for stability.
4. **Asymmetric Leg Contact States**: The environment tracks `left_leg_contact` and `right_leg_contact` independently; trajectories show the lander can enter and maintain single-leg contact states ($1,0$ or $0,1$) for extended periods.
5. **High-Magnitude Contact Transition Rewards**: Significant positive rewards are triggered by the transition from an airborne state ($0,0$) into a single-leg contact state ($1,0$ or $0,1$), as well as the transition from a single-leg contact state into a dual-leg contact state ($1,1$).
6. **Severe Contact Loss Penalty**: Transitioning from a dual-leg contact state ($1,1$) to either a single-leg state ($1,0$ or $0,1$) or a total loss of contact ($0,0$) triggers a massive negative reward.
7. **Engine-Induced Tipping or Lifting**: While in contact, applying engines (including the main engine, Action 2) can induce sufficient torque or vertical force to lift a leg or the entire body, triggering the Contact Loss Penalty.
8. **Post-Landing Stabilization Requirements**: Achieving dual-leg contact ($1,1$) does not result in a passive state; the lander requires continuous micro-adjustments using lateral engines (Actions 1 and 3) and inaction (Action 0) to prevent drift in `x_pos`, `angle`, and `ang_vel`.
9. **Grounded Vertical Velocity Management**: Even after touchdown, the main engine (Action 2) is utilized to regulate `y_pos` and `y_vel`, suggesting that vertical stability and pressure management are required to maintain a stable grounded state.
10. **Terminal Reward and Outcome Distinction**: A terminal reward is granted upon reaching a stable state, but an episode is classified as 'PARTIAL' if it terminates due to reaching the step limit, regardless of whether high rewards and a stable landing were achieved.

---

## 2026-07-05 23:17:07

1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but its effects are heavily coupled with the lander's orientation, inducing significant changes in both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal momentum, but they also induce rotation, making them double-edged tools for stability.
4. **Asymmetric Leg Contact States**: The environment tracks `left_leg_contact` and `right_leg_contact` independently; trajectories show the lander can enter and maintain single-leg contact states ($1,0$ or $0,1$) for extended periods.
5. **High-Magnitude Contact Transition Rewards**: Significant positive rewards are triggered by the transition from an airborne state ($0,0$) into a single-leg contact state ($1,0$ or $0,1$), as well as the transition from a single-leg contact state into a dual-leg contact state ($1,1$).
6. **Severe Contact Loss Penalty**: Transitioning from a dual-leg contact state ($1,1$) to either a single-leg state ($1,0$ or $0,1$) or a total loss of contact ($0,0$) triggers a massive negative reward.
7. **Lateral Engine Destabilization in Single-Leg Contact**: Applying lateral engines (Actions 1 or 3) while the lander is in a single-leg contact state ($0,1$ or $1,0$) can induce significant instability or tipping, triggering high-magnitude negative rewards.
8. **Post-Landing Stabilization Requirements**: Achieving dual-leg contact ($1,1$) does not result in a passive state; the lander requires continuous micro-adjustments using lateral engines (Actions 1 and 3) and inaction (Action 0) to prevent drift in `x_pos`, `angle`, and `ang_vel`.
9. **Grounded Vertical Velocity Management**: Even after touchdown, the main engine (Action 2) is utilized to regulate `y_pos` and `y_vel`, suggesting that vertical stability and pressure management are required to maintain a stable grounded state.
10. **Terminal Reward and Outcome Distinction**: A terminal reward is granted upon reaching a stable state, but an episode is classified as 'PARTIAL' if it terminates due to reaching the step limit, regardless of whether high rewards and a stable landing were achieved.

---

## 2026-07-05 23:26:54

1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but its effects are heavily coupled with the lander's orientation, inducing significant changes in both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal momentum, but they also induce rotation, making them double-edged tools for stability.
4. **Asymmetric Leg Contact States**: The environment tracks `left_leg_contact` and `right_leg_contact` independently; trajectories show the lander can enter and maintain single-leg contact states ($1,0$ or $0,1$) for extended periods before transitioning to dual-leg contact.
5. **High-Magnitude Contact Transition Rewards**: Significant positive rewards are triggered by the transition from an airborne state ($0,0$) into a single-leg contact state ($1,0$ or $0,1$), and additional high-magnitude rewards are granted upon the transition from a single-leg state into a dual-leg contact state ($1,1$).
6. **Severe Contact Loss Penalty**: Transitioning from a dual-leg contact state ($1,1$) to either a single-leg state ($1,0$ or $0,1$) or a total loss of contact ($0,0$) triggers a massive negative reward.
7. **Lateral Engine Destabilization in Single-Leg Contact**: Applying lateral engines (Actions 1 or 3) while the lander is in a single-leg contact state ($0,1$ or $1,0$) can induce significant instability or tipping, triggering high-magnitude negative rewards.
8. **Post-Landing Stabilization Requirements**: Achieving dual-leg contact ($1,1$) does not result in a passive state; the lander requires continuous and varied micro-adjustments using lateral engines (Actions 1 and 3), the main engine (Action 2), and inaction (Action 0) to maintain stability in `x_pos`, `y_pos`, `angle`, and `ang_vel`.
9. **Grounded Vertical Velocity Management**: Even after touchdown, the main engine (Action 2) is utilized to regulate `y_pos` and `y_vel`, suggesting that maintaining vertical stability and pressure is required to maintain a stable grounded state.
10. **Terminal Reward and Outcome Distinction**: A terminal reward is granted upon reaching a stable state, but an episode is classified as 'PARTIAL' if it terminates due to reaching the step limit, regardless of whether high rewards and a stable landing were achieved.

---

## 2026-07-05 23:29:20

1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but its effects are heavily coupled with the lander's orientation, inducing significant changes in both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal momentum, but they also induce rotation, making them double-edged tools for stability.
4. **Hierarchical Contact State Transitions**: The environment tracks contact through a sequence of states: airborne ($0,0$), single-leg contact ($1,0$ or $0,1$), and dual-leg contact ($1,1$).
5. **Contact-Triggered Reward Structure**: A high-magnitude positive reward is triggered by the transition from an airborne state ($0,0$) into a single-leg contact state ($1,0$ or $0,1$), followed by a secondary reward upon transitioning into a dual-leg contact state ($1,1$).
6. **Severe Contact Loss Penalty**: Transitioning from a dual-leg contact state ($1,1$) to either a single-leg state ($1,0$ or $0,1$) or a total loss of contact ($0,0$) triggers a massive negative reward.
7. **Lateral Engine Destabilization in Single-Leg Contact**: Applying lateral engines (Actions 1 or 3) while the lander is in a single-leg contact state ($0,1$ or $1,0$) can induce significant instability or tipping, triggering high-magnitude negative rewards.
8. **Post-Landing Stabilization Requirements**: Achieving dual-leg contact ($1,1$) does not result in a passive state; the lander requires continuous and varied micro-adjustments using lateral engines (Actions 1 and 3), the main engine (Action 2), and inaction (Action 0) to maintain stability in `x_pos`, `y_pos`, `angle`, and `ang_vel`.
9. **Grounded Vertical and Orientation Management**: Even after touchdown, the main engine (Action 2) and lateral engines are utilized to regulate `y_pos`, `y_vel`, `angle`, and `ang_vel` to maintain a stable grounded state.
10. **Terminal Reward and Outcome Distinction**: A terminal reward is granted upon reaching a stable state, but an episode is classified as 'PARTIAL' if it terminates due to reaching the step limit, regardless of whether high rewards and a stable landing were achieved.

---

## 2026-07-05 23:32:07

1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but its effects are heavily coupled with the lander's orientation, inducing significant changes in both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal momentum, but they also induce rotation, making them double-edged tools for stability.
4. **Hierarchical Contact State Transitions**: The environment tracks contact through a sequence of states: airborne ($0,0$), single-leg contact ($1,0$ or $0,1$), and dual-leg contact ($1,1$).
5. **Contact-Triggered Reward Structure**: A high-magnitude positive reward is triggered by the transition from an airborne state ($0,0$) into a single-leg contact state ($1,0$ or $0,1$), followed by a secondary reward upon transitioning into a dual-leg contact state ($1,1$).
6. **Severe Contact Loss Penalty**: Transitioning from a dual-leg contact state ($1,1$) to either a single-leg state ($1,0$ or $0,1$) or a total loss of contact ($0,0$) triggers a massive negative reward.
7. **Lateral Engine Destabilization in Single-Leg Contact**: Applying lateral engines (Actions 1 or 3) while the lander is in a single-leg contact state ($0,1$ or $1,0$) induces significant instability or tipping, resulting in high-magnitude negative rewards.
8. **Post-Landing Dynamic Drift**: Reaching a dual-leg contact state ($1,1$) does not result in a passive state; the lander experiences continuous drift in `x_pos`, `angle`, and `ang_vel` that persists after touchdown.
9. **Lateral-Primary Grounded Stability**: In the $(1,1)$ state, the lander's horizontal position and orientation are regulated through the use of lateral engines (Actions 1 and 3), while `y_pos` and `y_vel` typically reach a near-zero equilibrium.
10. **Terminal Reward and Outcome Distinction**: A terminal reward is granted upon reaching a stable state, but an episode is classified as 'PARTIAL' if it terminates due to reaching the step limit, regardless of whether a stable landing was achieved.

---

## 2026-07-05 23:40:13

1. **Main Engine (Action 2) Multidimensionality**: Action 2 is the primary regulator of `y_pos` and `y_vel`, but its effects are heavily coupled with the lander's orientation, inducing significant changes in both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal momentum, but they also induce rotation, making them double-edged tools for stability.
4. **Hierarchical Contact State Transitions**: The environment tracks contact through a sequence of states: airborne ($0,0$), single-leg contact ($1,0$ or $0,1$), and dual-leg contact ($1,1$).
5. **Contact-Triggered Reward Structure**: High-magnitude positive rewards are triggered by the transition from an airborne state ($0,0$) into a single-leg contact state ($1,0$ or $0,1$), followed by a secondary reward upon transitioning into a dual-leg contact state ($1,1$).
6. **Severe Contact Loss Penalty**: Transitioning from a dual-leg contact state ($1,1$) back to a single-leg state ($1,0$ or $0,1$) or total loss of contact ($0,0$) triggers a massive negative reward.
7. **Lateral Engine Destabilization in Single-Leg Contact**: Applying lateral engines (Actions 1 or 3) while the lander is in a single-leg contact state ($0,1$ or $1,0$) induces significant instability or tipping.
8. **Post-Landing Dynamic Drift**: Reaching a dual-leg contact state ($1,1$) does not result in a passive state; the lander experiences continuous drift in `x_pos`, `angle`, and `ang_vel` that persists after touchdown.
9. **Grounded Contact Fragility**: In the $(1,1)$ state, the lander is susceptible to losing contact if lateral engines (Actions 1 or 3) are applied in a way that induces sudden vertical or rotational instability (e.g., causing a "bounce").
10. **Terminal Reward and Outcome Distinction**: A terminal reward is granted upon reaching a stable state, but an episode is classified as 'PARTIAL' if it terminates due to reaching the step limit, regardless of whether a stable landing was achieved.

---

## 2026-07-05 23:42:41

1. **Main Engine (Action 2) Multidimensionality**: Action 2 serves as the primary regulator for `y_pos` and `y_vel`, but its application is non-linearly coupled with the lander's orientation, inducing significant torque that alters both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal momentum but simultaneously induce rotation, acting as a double-edged tool for stability.
4. **Hierarchical Contact State Transitions**: The environment tracks contact through a sequence of states: airborne ($0,0$), single-leg contact ($1,0$ or $0,1$), and dual-leg contact ($1,1$).
5. **Transition-Triggered Reward Structure**: High-magnitude positive rewards are specifically tied to state transitions: specifically the transition from airborne ($0,0$) into single-leg contact ($1,0$ or $0,1$), and the subsequent transition into dual-leg contact ($1,1$).
6. **Severe Contact Loss Penalty**: Transitioning from a contact state ($1,1$ or $1,0/0,1$) back to a total loss of contact state ($0,0$) triggers massive negative rewards.
7. **Lateral Engine Destabilization and Bouncing**: Applying lateral engines (Actions 1 or 3) while the lander is in a contact state ($1,0$, $0,1$, or $1,1$) frequently induces rotational instability or vertical "bounces," often resulting in immediate contact loss.
8. **Post-Landing Dynamic Drift**: Reaching a dual-leg contact state ($1,1$) does not result in a passive state; the lander experiences continuous drift in `x_pos`, `angle`, and `ang_vel` that persists after touchdown.
9. **Contact Recovery Reward Potential**: Re-establishing dual-leg contact ($1,1$) after a period of being airborne ($0,0$) is highly rewarded, suggesting the reward structure prioritizes the achievement of the stable state even after instability occurs.
10. **Terminal Reward and Outcome Distinction**: A terminal reward is granted upon reaching a stable state, but an episode is classified as 'PARTIAL' if it terminates due to reaching the step limit, regardless of whether a stable landing was achieved.

---

## 2026-07-05 23:47:35

1. **Main Engine (Action 2) Multidimensionality**: Action 2 serves as the primary regulator for `y_pos` and `y_vel`, but its application is non-linearly coupled with the lander's orientation, inducing significant torque that alters both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal momentum but simultaneously induce rotation, acting as a double-edged tool for stability.
4. **Hierarchical Contact State Transitions**: The environment tracks contact through a sequence of states: airborne ($0,0$), single-leg contact ($1,0$ or $0,1$), and dual-leg contact ($1,1$).
5. **Transition-Triggered Reward Structure**: High-magnitude positive rewards are tied to specific contact state transitions: moving from airborne ($0,0$) into single-leg contact ($1,0$ or $0,1$), and the subsequent transition into dual-leg contact ($1,1$).
6. **Severe Contact Loss Penalty**: Transitioning from a higher contact state (such as dual-leg $1,1$) to a lesser contact state (such as single-leg $1,0$ or $0,1$) triggers massive negative rewards.
7. **Lateral Engine Destabilization and Bouncing**: Applying lateral engines (Actions 1 or 3) while the lander is in a contact state frequently induces rotational instability or vertical "bounces," which can trigger contact loss.
8. **Persistent Post-Landing Dynamics**: Reaching a dual-leg contact state ($1,1$) does not result in a static equilibrium; the lander experiences continuous drift and oscillation in `x_pos`, `y_pos`, `angle`, and `ang_vel` that persists after touchdown.
9. **Contact Recovery Reward Potential**: Re-establishing dual-leg contact ($1,1$) after a period of instability or contact loss is highly rewarded, suggesting the reward structure prioritizes the achievement of the stable state regardless of prior state changes.
10. **Terminal Reward and Outcome Distinction**: A terminal reward is granted upon reaching a stable state, but an episode is classified as 'PARTIAL' if it terminates due to reaching the step limit, regardless of whether a stable landing was achieved.

---

## 2026-07-05 23:50:27

1. **Main Engine (Action 2) Multidimensionality**: Action 2 serves as the primary regulator for `y_pos` and `y_vel`, but its application is non-linearly coupled with the lander's orientation, inducing significant torque that alters both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal momentum but simultaneously induce rotation, acting as a double-edged tool for stability.
4. **Hierarchical Contact State Transitions**: The environment tracks contact through a sequence of states: airborne ($0,0$), single-leg contact ($1,0$ or $0,1$), and dual-leg contact ($1,1$).
5. **Transition-Triggered Reward Structure**: High-magnitude positive rewards are tied to specific contact state transitions (e.g., airborne to single-leg, or single-leg to dual-leg), including high rewards for re-establishing dual-leg contact ($1,1$) after a period of instability.
6. **Severe Contact Loss Penalty**: Transitioning from a higher contact state (such as dual-leg $1,1$) to a lesser contact state (such as single-leg $1,0$ or $0,1$) triggers massive negative rewards.
7. **Lateral Engine Destabilization and Bouncing**: Applying lateral engines (Actions 1 or 3) while the lander is in a contact state frequently induces rotational instability or vertical "bounces," which can trigger contact loss.
8. **Persistent Post-Landing Kinetic Oscillations**: Reaching a dual-leg contact state ($1,1$) does not result in a static equilibrium; the lander experiences continuous, non-dampened oscillations in `x_pos`, `y_pos`, `angle`, and `ang_vel` that persist for the remainder of the episode.
9. **Landing Impact Momentum**: The transition from airborne to contact states can impart sudden and significant angular momentum, causing abrupt spikes in `ang_vel` (e.g., `ang_vel` can jump from near-zero to magnitudes exceeding 0.3 during the transition into contact).
10. **Terminal Reward and Outcome Distinction**: A terminal reward is granted upon reaching a stable state, but an episode is classified as 'PARTIAL' if it terminates due to reaching the step limit, regardless of whether a stable landing was achieved.

---

## 2026-07-06 14:21:41

1. **Main Engine (Action 2) Multidimensionality**: Action 2 serves as the primary regulator for `y_pos` and `y_vel`, but its application is non-linearly coupled with the lander's orientation, inducing significant torque that alters both `angle` and `ang_vel`.
2. **Body-Fixed Thrust Projection**: All engine actions are body-fixed; the resulting acceleration in the world-frame `x_vel` and `y_vel` is a trigonometric function of the lander's current `angle`.
3. **Lateral Engine Rotation Duality**: Actions 1 (left) and 3 (right) provide translational thrust to counteract horizontal momentum but simultaneously induce rotation, acting as a double-edged tool for stability.
4. **Hierarchical Contact State Transitions**: The environment tracks contact through a sequence of states: airborne ($0,0$), single-leg contact ($1,0$ or $0,1$), and dual-leg contact ($1,1$).
5. **Transition-Triggered Reward Structure**: High-magnitude positive rewards are tied to specific contact state transitions (e.g., airborne to single-leg, or single-leg to dual-leg), including high rewards for re-establishing dual-leg contact ($1,1$) after a period of instability.
6. **Severe Contact Loss Penalty**: Transitioning from a higher contact state (such as dual-leg $1,1$) to a lesser contact state (such as single-leg $1,0$ or $0,1$) triggers massive negative rewards.
7. **Lateral Engine Destabilization and Bouncing**: Applying lateral engines (Actions 1 or 3) while the lander is in a contact state frequently induces rotational instability or vertical "bounces," which can trigger contact loss.
8. **Persistent Post-Landing Kinetic Oscillations**: Reaching a dual-leg contact state ($1,1$) does not result in a static equilibrium; the lander experiences continuous, non-dampened oscillations in `x_pos`, `y_pos`, `angle`, and `ang_vel` that persist for the remainder of the episode.
9. **Descent Velocity-Induced Instability**: High-magnitude downward `y_vel` during the approach to or during contact states (e.g., $|y\_vel| > 1.0$ while in a contact state) is a significant precursor to catastrophic failure.
10. **Terminal Crash Mechanics and Penalties**: A massive terminal penalty (-100) is triggered by a crash event, which is characterized by the lander's `y_pos` falling below zero (ground collision) or the `angle` reaching extreme deviations that preclude an upright landing.

---

## 2026-07-06 14:22:16

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
