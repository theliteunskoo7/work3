
---

## 2026-07-08 02:39:57

1. **Gravity and Descent:** Gravity continuously increases the downward vertical velocity ($\dot{y}$); failure to apply the main engine (2) leads to uncontrolled descent.
2. **Main Engine Dynamics:** Action 2 is essential for altitude control but contributes to horizontal displacement ($x\_vel$) and can influence angular stability.
3. **Orientation Control:** Side engines (1 and 3) are used to manipulate the angle ($\theta$) and angular velocity ($\dot{\theta}$), with action 3 specifically driving the craft toward negative angles.
4. **Angular Momentum Sensitivity:** The system is highly sensitive to angular velocity; once $\dot{\theta}$ reaches high magnitudes, the craft enters a "death spiral" that is difficult to arrest.
5. **Failure via Inaction:** Prolonged periods of action 0 (nothing) cause both vertical velocity and angular instability to accumulate, leading to terminal states.
6. **Failure via Uncoordinated Oscillation:** Rapidly switching between the main engine (2) and a side engine (3) without stabilization often exacerbates rotation rather than correcting it.
7. **Failure via Overcorrection:** Excessive use of side engines (as seen in Episode 2) drives the angle $\theta$ to extreme values, making the lander impossible to level.
8. **Critical Threshold (Angle):** A critical failure point occurs when the angle $\theta$ exceeds a stability threshold, at which point engine thrust can no longer counteract the rotational momentum.
9. **Critical Threshold (Velocity):** High vertical descent velocities ($\dot{y}$) combined with high angular velocities ($\dot{\theta}$) signify a point of no return regardless of subsequent actions.
10. **Trajectory Pattern:** Both episodes demonstrate a transition from attempted control to "panic" behavior—characterized by high-frequency, high-magnitude engine bursts that fail to mitigate the increasing entropy of the state.

---

## 2026-07-08 02:47:38

1. **Gravity and Vertical Descent:** Gravity continuously increases the downward vertical velocity ($\dot{y}$); failure to apply the main engine (2) leads to uncontrolled descent and the rapid accumulation of negative vertical velocity.
2. **Main Engine Dynamics:** Action 2 is essential for altitude control but is not a purely vertical force; it contributes to horizontal displacement ($x\_vel$) and influences angular stability.
3. **State-Dependent Orientation Control:** Side engines (1 and 3) are used to manipulate the angle ($\theta$) and angular velocity ($\dot{\theta}$), with action 3 driving the craft toward negative angles; however, the directional impact of side engines is highly dependent on the current orientation.
4. **Angular Momentum Sensitivity:** The system is extremely sensitive to angular velocity ($\dot{\theta}$); once $\dot{\theta}$ reaches high magnitudes, the resulting angular momentum makes the orientation difficult to arrest.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability to accumulate, rapidly narrowing the window for effective recovery.
6. **Main Engine-Induced Rotational Drift:** In non-upright orientations, continuous application of the main engine (2) can exacerbate angular drift rather than correcting it, as the engine's thrust vector induces additional rotational momentum.
7. **Failure via Uncoordinated Oscillation:** Rapidly switching between the main engine (2) and side engines (1 or 3) without first stabilizing the angular velocity ($\dot{\theta}$) often results in uncoordinated oscillations that increase the entropy of the state.
8. **Critical Orientation Threshold:** A critical failure point occurs when the angle $\theta$ exceeds a stability threshold (approximately -1.0 to -1.5 radians), at which point engine thrust becomes insufficient to counteract the accumulated rotational momentum.
9. **Kinetic Convergence of Failure:** High vertical descent velocities ($\dot{y}$) combined with high angular velocities ($\dot{\theta}$) signify a point of no return, where the energy required for simultaneous altitude and orientation correction exceeds the available thrust.
10. **Maneuverability Erosion:** As the magnitudes of $\theta$, $\dot{\theta}$, and $\dot{y}$ increase, the craft enters a state of decreasing maneuverability where high-frequency engine bursts fail to mitigate the increasing instability.

---

## 2026-07-08 02:52:27

1. **Gravity and Vertical Descent:** Gravity continuously increases the downward vertical velocity ($\dot{y}$); failure to apply the main engine (2) leads to uncontrolled descent and the rapid accumulation of negative vertical velocity.
2. **Main Engine Multi-Axis Dynamics:** Action 2 is essential for altitude control but is not a purely vertical force; it contributes significantly to horizontal displacement ($x\_vel$) and introduces torque that influences angular stability.
3. **Directional Side Engine Influence:** Side engines (1 and 3) manipulate the angle ($\theta$) and angular velocity ($\dot{\theta}$); specifically, action 3 drives the craft toward increasingly negative angles and negative angular velocities.
4. **Angular Momentum Sensitivity:** The system is extremely sensitive to angular velocity ($\dot{\theta}$); once $\dot{\theta}$ reaches high magnitudes, the resulting angular momentum becomes difficult to arrest with standard engine bursts.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability to accumulate, rapidly narrowing the window for effective recovery.
6. **Rotational Reinforcement via Main Engine:** In non-upright orientations, the main engine (2) can act as a rotational driver; rather than correcting orientation, its thrust vector can exacerbate angular displacement by increasing the absolute magnitude of $\theta$.
7. **Failure via Uncoordinated Oscillation:** Rapidly switching between the main engine (2) and side engines (1 or 3) fails to stabilize the craft if the angular momentum is already high, often resulting in a continuous divergence of the angle.
8. **Critical Orientation Threshold:** A critical failure point occurs when the angle $\theta$ exceeds a stability threshold (approximately -1.0 radians), at which point the main engine's thrust becomes primarily rotational, making simultaneous altitude and orientation correction nearly impossible.
9. **Kinetic Convergence of Failure:** The simultaneous accumulation of high vertical descent velocities ($\dot{y}$) and high angular velocities ($\dot{\theta}$) signifies a point of no return, where the energy required to correct both vectors exceeds the available thrust.
10. **Maneuverability Erosion:** As the magnitudes of $\theta$, $\dot{\theta}$, and $\dot{y}$ increase, the craft enters a state of decreasing control authority where engine inputs have diminishing returns on stabilizing the state.

---

## 2026-07-08 03:03:34

1. **Gravity and Vertical Descent:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); failure to apply the main engine (2) results in rapid, uncontrolled descent.
2. **Main Engine Multi-Axis Dynamics:** Action 2 is essential for altitude control but is not a purely vertical force; it introduces significant horizontal displacement ($x\_vel$) and contributes to angular instability.
3. **Orientation-Dependent Side Engine Torque:** Side engines (1 and 3) manipulate angular velocity ($\dot{\theta}$), but the effective direction of the torque is coupled to the craft's orientation ($\theta$); an engine's ability to stabilize or destabilize the rotation is contingent upon the current angle.
4. **Angular Momentum Sensitivity:** The system is extremely sensitive to angular velocity ($\dot{\theta}$); once $\dot{\theta}$ reaches high magnitudes, the resulting angular momentum becomes difficult to arrest with standard engine bursts.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability to accumulate, rapidly narrowing the window for effective recovery.
6. **Rotational Reinforcement via Main Engine:** In non-upright orientations, the main engine (2) can act as a rotational driver; its thrust vector can exacerbate angular displacement by increasing the magnitude of $\theta$.
7. **Failure via Uncoordinated Oscillation:** Rapidly switching between the main engine (2) and side engines (1 or 3) fails to stabilize the craft if the angular momentum is already high, often resulting in a continuous divergence of the angle.
8. **Kinetic Convergence of Failure:** The simultaneous accumulation of high vertical descent velocities ($\dot{y}$) and high angular velocities ($\dot{\theta}$) signifies a point of no return, where the energy required to correct both vectors exceeds the available thrust.
9. **Thrust-Induced Reward Penalties:** The application of the main engine (2) is associated with significant instantaneous negative rewards, representing the energetic cost of thrust or the penalty for the instability and horizontal displacement it introduces.
10. **Maneuverability Erosion:** As the magnitudes of $\theta$, $\dot{\theta}$, and $\dot{y}$ increase, the craft enters a state of decreasing control authority where engine inputs have diminishing returns on stabilizing the state.

---

## 2026-07-08 03:07:50

1. **Gravity and Vertical Descent:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); failure to apply the main engine (2) results in rapid, uncontrolled descent.
2. **Main Engine Multi-Axis Dynamics:** Action 2 is not a purely vertical force; it introduces significant horizontal displacement ($x\_vel$) and contributes to angular instability through induced torque.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$); an engine's ability to stabilize or destabilize rotation is contingent upon whether the resulting torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Momentum Sensitivity:** The system is extremely sensitive to angular velocity ($\dot{\theta}$); once $\dot{\theta}$ reaches high magnitudes, the resulting angular momentum becomes difficult to arrest with standard engine bursts.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Rotational Reinforcement via Main Engine:** In non-upright orientations ($\theta \neq 0$), the main engine (2) acts as a rotational driver; its thrust vector can exacerbate angular displacement by increasing the magnitude of $\theta$ and $\dot{\theta}$.
7. **Failure via Uncoordinated Oscillation:** Rapidly switching between the main engine (2) and side engines (1 or 3) fails to stabilize the craft if the angular momentum is already high, often resulting in a continuous divergence of the angle.
8. **Kinetic Convergence of Failure:** Failure is characterized by the simultaneous accumulation of high vertical descent velocities ($\dot{y}$), high angular velocities ($\dot{\theta}$), and high angular displacement ($\theta$); at this point, the energy required to correct these vectors exceeds the available thrust.
9. **Thrust-Induced Reward Penalties:** The application of the main engine (2) is associated with significant instantaneous negative rewards, representing the energetic cost of thrust and the penalties for the instability and horizontal displacement it introduces.
10. **Maneuverability Erosion:** As the magnitudes of $\theta$, $\dot{\theta}$, and $\dot{y}$ increase, the craft enters a state of decreasing control authority where engine inputs have diminishing returns on stabilizing the state.

---

## 2026-07-08 03:10:53

1. **Gravity and Vertical Descent:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); failure to apply the main engine (2) results in rapid, uncontrolled descent.
2. **Main Engine Multi-Axis Dynamics:** Action 2 is not a purely vertical force; it introduces significant horizontal displacement ($x\_vel$) and contributes to angular instability through induced torque.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$); an engine's ability to stabilize or destabilize rotation is contingent upon whether the resulting torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Momentum Sensitivity:** The system is extremely sensitive to angular velocity ($\dot{\theta}$); once $\dot{\theta}$ reaches high magnitudes, the resulting angular momentum becomes difficult to arrest with standard engine bursts.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Rotational Reinforcement via Main Engine:** In non-upright orientations ($\theta \neq 0$), the main engine (2) acts as a rotational driver; its thrust vector can exacerbate angular displacement by increasing the magnitude of $\theta$ and $\dot{\theta}$.
7. **Failure via Uncoordinated Oscillation:** Rapidly switching between the main engine (2) and side engines (1 or 3) fails to stabilize the craft if the angular momentum is already high, often resulting in a continuous divergence of the angle.
8. **Kinetic Convergence of Failure:** Failure is characterized by the simultaneous accumulation of high vertical descent velocities ($\dot{y}$), high angular velocities ($\dot{\theta}$), and high angular displacement ($\theta$); at this point, the energy required to correct these vectors exceeds the available thrust.
9. **Reward-Thrust Dynamics:** The reward signal is heavily weighted toward vertical velocity ($\dot{y}$) stabilization; consequently, applying the main engine (2) to arrest high-velocity descent can result in significant instantaneous positive rewards, potentially offsetting the energetic cost of thrust.
10. **Non-Linear Control Erosion:** As the magnitudes of $\theta$, $\dot{\theta}$, and $\dot{y}$ increase, the craft enters a regime of decreasing control authority where engine inputs—particularly the main engine (2)—can trigger disproportionately large and destabilizing spikes in angular velocity ($\dot{\theta}$).

---

## 2026-07-08 03:15:04

1. **Gravity and Vertical Descent:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); failure to apply the main engine (2) results in rapid, uncontrolled descent.
2. **Main Engine Multi-Axis Dynamics:** Action 2 introduces significant horizontal displacement ($x\_vel$) and angular instability; high horizontal velocity magnitudes can persist throughout the descent even during active vertical thrust application.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$); an engine's ability to stabilize or destabilize rotation is contingent upon whether the resulting torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Momentum Dominance:** High angular velocity ($\dot{\theta}$) is a critical failure driver; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively small or near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Rotational Reinforcement via Main Engine:** In non-upright orientations ($\theta \neq 0$), the main engine (2) acts as a rotational driver; its thrust vector can exacerbate angular displacement by increasing the magnitude of $\theta$ and $\dot{\theta}$.
7. **Failure via Uncoordinated Oscillation:** Rapidly switching between the main engine (2) and side engines (1 or 3) fails to stabilize the craft if the angular momentum is already high, often resulting in a continuous divergence of the angle.
8. **Kinetic Convergence of Failure:** Failure is characterized by the simultaneous accumulation of high vertical descent velocities ($\dot{y}$), high angular velocities ($\dot{\theta}$), and high angular displacement ($\theta$); at this point, the energy required to correct these vectors exceeds the available thrust.
9. **Reward-Instability Conflict:** The reward signal's heavy weighting toward $\dot{y}$ stabilization can create a deceptive feedback loop, where applying the main engine (2) to arrest descent yields high instantaneous rewards while simultaneously driving the craft toward terminal angular velocity ($\dot{\theta}$).
10. **Non-Linear Control Erosion:** As the magnitudes of $\theta$, $\dot{\theta}$, and $\dot{y}$ increase, the craft enters a regime of decreasing control authority where engine inputs—particularly the main engine (2)—can trigger disproportionately large and destabilizing spikes in angular velocity ($\dot{\theta}$).

---

## 2026-07-08 03:20:27

1. **Gravity and Terminal Vertical Descent:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$). If $\dot{y}$ exceeds a critical threshold, the main engine (2) may fail to arrest the descent, causing $\dot{y}$ to continue increasing in magnitude despite sustained thrust.
2. **Main Engine Horizontal Inertia:** Action 2 introduces horizontal displacement ($x\_vel$), but the engine has limited capacity to attenuate existing high horizontal velocities; high $x\_vel$ tends to persist throughout the descent regardless of vertical thrust application.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$); an engine's ability to stabilize or destabilize rotation is contingent upon whether the resulting torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Momentum Dominance:** High angular velocity ($\dot{\theta}$) is a critical failure driver; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively small or near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Rotational Reinforcement via Main Engine:** In non-upright orientations ($\theta \neq 0$), the main engine (2) acts as a rotational driver; its thrust vector can exacerbate angular displacement by increasing the magnitude of both $\theta$ and $\dot{\theta}$.
7. **Failure via Uncoordinated Oscillation:** Rapidly switching between the main engine (2) and side engines (1 or 3) fails to stabilize the craft if the angular momentum is already high, often resulting in a continuous divergence of the angle.
8. **Kinetic Convergence of Failure:** Failure is characterized by the simultaneous accumulation of high vertical descent velocities ($\dot{y}$), high angular velocities ($\dot{\theta}$), and high angular displacement ($\theta$); at this point, the kinetic energy of the system exceeds the available thrust's ability to restore stability.
9. **Reward-Instability Conflict:** The reward signal's weighting toward $\dot{y}$ stabilization can create a deceptive feedback loop, where applying the main engine (2) to arrest descent yields high instantaneous rewards while simultaneously driving the craft toward terminal angular velocity ($\dot{\theta}$).
10. **Non-Linear Control Erosion:** As the magnitudes of $\theta$, $\dot{\theta}$, and $\dot{y}$ increase, the craft enters a regime of decreasing control authority where engine inputs—particularly the main engine (2)—can trigger disproportionately large and destabilizing spikes in angular velocity ($\dot{\theta}$) while failing to meaningfully arrest $\dot{y}$.

---

## 2026-07-08 03:24:02

1. **Gravity and Terminal Vertical Descent:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$). If $\dot{y}$ exceeds a critical threshold, the main engine (2) may struggle to arrest the descent, leading to a terminal velocity that makes recovery impossible.
2. **Main Engine Horizontal Inertia:** Action 2 introduces horizontal displacement ($x\_vel$), but the engine has limited capacity to attenuate existing high horizontal velocities; high $x\_vel$ tends to persist throughout the descent regardless of vertical thrust application.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$); an engine's ability to stabilize or destabilize rotation is contingent upon whether the resulting torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Momentum Dominance:** High angular velocity ($\dot{\theta}$) is a critical failure driver; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively small or near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Main Engine-Induced Angular Spikes:** The main engine (2) acts as a primary driver of angular momentum; applying action 2 can trigger disproportionately large, sudden spikes in angular velocity ($\dot{\theta}$), particularly when the craft is not perfectly upright ($\theta \neq 0$).
7. **Side Engine Divergence Threshold:** Once angular velocity ($\dot{\theta}$) or displacement ($\theta$) exceeds a specific threshold, side engines (1 and 3) frequently cease to act as corrective forces and instead act as accelerators of angular momentum, causing rapid and uncontrolled divergence.
8. **Kinetic Convergence of Failure:** Failure is characterized by the simultaneous accumulation of high vertical descent velocities ($\dot{y}$), high angular velocities ($\dot{\theta}$), and high angular displacement ($\theta$); at this point, the kinetic energy of the system exceeds the available thrust's ability to restore stability.
9. **The Main Engine Reward Trap:** The reward signal's heavy weighting toward $\dot{y}$ stabilization creates a deceptive feedback loop; the main engine (2) can produce massive instantaneous rewards by successfully arresting descent, even while simultaneously injecting the catastrophic $\dot{\theta}$ spikes that lead to terminal instability.
10. **Non-Linear Control Erosion:** As the magnitudes of $\theta$, $\dot{\theta}$, and $\dot{y}$ increase, the craft enters a regime of decreasing control authority where engine inputs—particularly the main engine (2)—can trigger disproportionately large and destabilizing spikes in angular velocity ($\dot{\theta}$) while failing to meaningfully arrest $\dot{y}$.

---

## 2026-07-08 03:28:08

1. **Gravity and Terminal Vertical Descent:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $\dot{y}$ exceeds a critical threshold, the main engine (2) may fail to arrest the descent, leading to a terminal velocity that makes recovery impossible.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent; the main engine has limited capacity to attenuate existing high horizontal velocities regardless of vertical thrust application.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$); their ability to stabilize or destabilize rotation is contingent upon whether the resulting torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Momentum Dominance:** High angular velocity ($\dot{\theta}$) is a critical failure driver; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively small or near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Main Engine-Induced Angular Spikes:** The main engine (2) acts as a primary driver of angular momentum; applying action 2 can trigger disproportionately large, sudden spikes in angular velocity ($\dot{\theta}$), particularly when the craft is not perfectly upright ($\theta \neq 0$).
7. **Side Engine Divergence Threshold:** Once angular velocity ($\dot{\theta}$) or displacement ($\theta$) exceeds a specific threshold, side engines (1 and 3) frequently cease to act as corrective forces and instead act as accelerators of angular momentum, causing rapid divergence.
8. **The Main Engine Reward Trap:** The reward signal's heavy weighting toward $\dot{y}$ stabilization creates a deceptive feedback loop; the main engine (2) can produce massive instantaneous rewards by successfully arresting descent, even while simultaneously injecting the catastrophic $\dot{\theta}$ spikes that lead to terminal instability.
9. **Critical Angular Landing Constraint:** Achieving leg contact (leg_contact=1) does not guarantee a successful landing; if the angular displacement ($\theta$) or angular velocity ($\dot{\theta}$) is outside a narrow stability window at the moment of contact, the system transitions immediately to a failure state.
10. **Kinetic Convergence of Failure:** Failure is characterized by the simultaneous accumulation of high vertical descent velocities ($\dot{y}$), high angular velocities ($\dot{\theta}$), and high angular displacement ($\theta$); at this point, the kinetic energy of the system exceeds the available thrust's ability to restore stability.

---

## 2026-07-08 03:32:16

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) is near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Main Engine-Induced Angular Spikes:** The main engine (2) acts as a primary driver of angular momentum; applying action 2 can trigger disproportionately large spikes in $\dot{\theta}$, particularly when $\theta \neq 0$.
7. **Side Engine Destabilization:** Side engines (1 and 3) can act as accelerators of angular momentum; in certain states, applying a side engine can induce massive, sudden spikes in $\dot{\theta}$ that exacerbate rotation rather than correcting it.
8. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; the main engine (2) can produce high instantaneous rewards by arresting descent while simultaneously injecting catastrophic $\dot{\theta}$ spikes.
9. **Triple-Constraint Landing Window:** A successful landing (leg_contact=1) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$). Failure to meet any one of these windows at the moment of contact results in a failure state.
10. **Kinetic Convergence of Failure:** Failure is characterized by the simultaneous accumulation of high vertical descent velocities ($\dot{y}$), high angular velocities ($\dot{\theta}$), and high angular displacement ($\theta$); at this point, the system's total kinetic energy exceeds the available thrust's ability to restore stability.

---

## 2026-07-08 03:34:57

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) is near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** Both the main engine (2) and side engines (1 and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often exacerbating existing rotation rather than correcting it.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce high instantaneous rewards by arresting descent while simultaneously injecting catastrophic $\dot{\theta}$ spikes.
8. **Deceptive Terminal Rewards:** The reward function can produce exceptionally high positive values (e.g., $>15$) during the final steps of a descent by successfully minimizing $\dot{y}$, even if the craft's orientation or contact state is insufficient for a stable landing.
9. **Triple-Constraint Landing Window:** A successful landing (leg_contact=1) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Contact-Induced Angular Instability:** The transition to a leg contact state (`leg_contact=1`) can trigger massive, sudden spikes in angular velocity ($\dot{\theta}$), potentially inducing a failure state even if the pre-contact state appeared relatively stable.

---

## 2026-07-08 03:39:12

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) is near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often exacerbating existing rotation rather than correcting it.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce high instantaneous rewards by arresting descent while simultaneously injecting catastrophic $\dot{\theta}$ spikes.
8. **Deceptive Terminal Rewards:** The reward function can produce exceptionally high positive values (e.g., $>10$) during the final steps of a descent by successfully minimizing $\dot{y}$, even if the craft's orientation or contact state is insufficient for a stable landing.
9. **Triple-Constraint Landing Window:** A successful landing (leg_contact=1) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Contact-Phase Torque Volatility:** The transition to a leg contact state (`leg_contact=1`) renders the craft hyper-sensitive to torque; side-engine actions (1 or 3) taken during the contact phase can trigger immediate, massive spikes in angular velocity ($\dot{\theta}$), even when attempting corrective maneuvers.

---

## 2026-07-08 03:42:56

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) is near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often exacerbating existing rotation rather than correcting it.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce massive instantaneous rewards (e.g., $>20$) by attempting to arrest descent, even when it injects catastrophic $\dot{\theta}$ spikes.
8. **Deceptive Terminal Rewards:** The reward function can produce exceptionally high positive values during the final steps of a descent by successfully minimizing $\dot{y}$, even if the craft's angular velocity ($\dot{\theta}$) is high or the contact state is insufficient (e.g., only one leg making contact).
9. **Triple-Constraint Landing Window:** A successful landing (leg_contact=1) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Contact-Phase Torque Volatility:** The transition to a leg contact state (`leg_contact=1`) renders the craft hyper-sensitive to torque; side-engine actions (1 or 3) taken during the contact phase can trigger immediate, massive spikes in angular velocity ($\dot{\theta}$), often leading to immediate failure.

---

## 2026-07-08 03:45:29

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) is near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce massive instantaneous rewards (e.g., $>15$) by attempting to arrest descent, even when it injects catastrophic $\dot{\theta}$ spikes.
8. **Deceptive Terminal Rewards:** The reward function can produce exceptionally high positive values during the final steps of a descent by successfully minimizing $\dot{y}$, even if the craft's angular velocity ($\dot{\theta}$) is high or the contact state is insufficient.
9. **Triple-Constraint Landing Window:** A successful landing (leg_contact=1) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Contact-Phase Torque Volatility:** The transition to a leg contact state (`leg_contact=1`) renders the craft hyper-sensitive to torque; while the main engine (2) may be used for vertical stabilization, side-engine actions (1 or 3) during contact trigger immediate, massive spikes in $\dot{\theta}$ that lead to rapid terminal failure.

---

## 2026-07-08 03:49:55

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) is near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce massive instantaneous rewards by attempting to arrest descent, even when it injects catastrophic $\dot{\theta}$ spikes.
8. **Deceptive Terminal Rewards:** The reward function can produce exceptionally high positive values during the final steps of a descent by successfully minimizing $\dot{y}$, even if the craft's angular velocity ($\dot{\theta}$) is high or the contact state is insufficient.
9. **Triple-Constraint Landing Window:** A successful landing (leg_contact=1) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Contact-Phase Rotational Instability:** The transition to a leg contact state (`leg_contact=1`) initiates a regime of extreme angular volatility; during this phase, inaction (action 0) fails to arrest $\dot{\theta}$ growth, and side-engine actions (1 or 3) often trigger massive, unrecoverable angular velocity spikes that lead to rapid terminal failure.

---

## 2026-07-08 03:52:26

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) is near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce massive instantaneous rewards by attempting to arrest descent, even when it injects catastrophic $\dot{\theta}$ spikes.
8. **Deceptive Terminal Rewards:** The reward function can produce exceptionally high positive values (e.g., >7.0) during the final steps of a descent by successfully minimizing $\dot{y}$ or managing $\theta$, immediately preceding a catastrophic terminal penalty (-100).
9. **Triple-Constraint Landing Window:** A successful landing (`leg_contact=1`) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Contact-Phase Stability Threshold:** The onset of leg contact (`leg_contact=1`) initiates a high-sensitivity regime where the terminal penalty (-100) is triggered by excessive $\dot{\theta}$ or $\theta$. During this phase, inaction (action 0) can lead to rapid $\dot{\theta}$ divergence, and side-engine actions (1 or 3) are highly likely to induce unrecoverable angular velocity spikes.

---

## 2026-07-08 03:55:01

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) is near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce massive instantaneous rewards by attempting to arrest descent, even when it injects catastrophic $\dot{\theta}$ spikes.
8. **Deceptive Terminal Rewards:** The reward function can produce exceptionally high positive values (e.g., >7.0) during the final steps of a descent by successfully minimizing $\dot{y}$ or managing $\theta$, immediately preceding a catastrophic terminal penalty (-100).
9. **Triple-Constraint Landing Window:** A successful landing (`leg_contact=1`) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Contact-Phase Reward Volatility:** The transition to $y \le 0$ and leg contact (`leg_contact=1`) initiates a high-sensitivity regime characterized by extreme reward volatility. The reward can oscillate violently between high positive values and heavy penalties as it responds to minute changes in $\theta$ and $\dot{\theta}$. During this phase, side-engine actions (1 or 3) are highly likely to trigger unrecoverable angular velocity spikes.

---

## 2026-07-08 03:58:52

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) is near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce massive instantaneous rewards by attempting to arrest descent, even when it injects catastrophic $\dot{\theta}$ spikes.
8. **Extreme Deceptive Terminal Rewards:** The reward function can produce exceptionally high positive values (exceeding 10.0) during the final steps of a descent or immediately upon leg contact, masking the imminent catastrophic terminal penalty (-100) caused by a subsequent loss of angular stability.
9. **Triple-Constraint Landing Window:** A successful landing (`leg_contact=1`) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Contact-Phase Side-Engine Instability:** Once `leg_contact=1` is achieved, the application of side engines (1 or 3) acts as a high-magnitude catalyst for unrecoverable angular velocity ($\dot{\theta}$) spikes. These actions can trigger rapid, terminal rotation even if the reward signal remains temporarily positive due to vertical velocity management.

---

## 2026-07-08 04:02:07

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively low.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce massive instantaneous rewards by attempting to arrest descent, even when such actions are taken during or after leg contact.
8. **Extreme Deceptive Terminal Rewards:** The reward function can produce exceptionally high positive values (exceeding 10.0) during the final steps of a descent or immediately upon leg contact, masking the imminent catastrophic terminal penalty (-100) caused by a subsequent loss of stability.
9. **Triple-Constraint Landing Window:** A successful landing (`leg_contact=1`) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Post-Contact Side-Engine Instability:** Once `leg_contact=1` is achieved, the application of side engines (1 or 3) acts as a high-magnitude catalyst for unrecoverable angular velocity ($\dot{\theta}$) spikes, which can trigger rapid, terminal rotation even if the reward signal remains temporarily positive.

---

## 2026-07-08 04:04:49

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively low.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce massive instantaneous rewards by attempting to arrest descent, even when such actions are taken during or after leg contact.
8. **Extreme Deceptive Terminal Rewards:** The reward function can produce exceptionally high positive values (exceeding 10.0) during the final steps of a descent or immediately upon leg contact, masking the imminent catastrophic terminal penalty (-100) caused by a subsequent loss of stability.
9. **Triple-Constraint Landing Window:** A successful landing (`leg_contact=1`) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Post-Contact Stability Fragility:** Once `leg_contact=1` is achieved, the craft enters a critical state where angular velocity ($\dot{\theta}$) becomes hyper-sensitive; the application of side engines (1 or 3) or even the persistence of existing angular momentum acts as a catalyst for unrecoverable $\dot{\theta}$ spikes, triggering rapid terminal rotation.

---

## 2026-07-08 04:07:29

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively low.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce massive instantaneous rewards by attempting to arrest descent, even when such actions are taken during or after leg contact.
8. **Extreme Post-Contact Reward Deception:** The reward function can produce exceptionally high positive values (exceeding 10.0) immediately after leg contact is achieved, masking an imminent catastrophic terminal penalty (-100) caused by unrecoverable rotational instability.
9. **Triple-Constraint Landing Window:** A successful landing (`leg_contact=1`) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Post-Contact Rotational Volatility:** Once `leg_contact=1` is achieved, the craft enters a hyper-sensitive state where existing angular momentum or side-engine corrections (1 or 3) act as catalysts for unrecoverable $\dot{\theta}$ spikes, triggering rapid terminal rotation.

---

## 2026-07-08 04:08:29

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively low.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce massive instantaneous rewards by attempting to arrest descent, even when such actions are taken during or after leg contact.
8. **Extreme Post-Contact Reward Deception:** The reward function can produce exceptionally high positive values (exceeding 13.0) during or immediately after leg contact, which can mask an imminent catastrophic terminal penalty (-100) caused by unrecoverable rotational instability.
9. **Triple-Constraint Landing Window:** A successful landing (`leg_contact=1`) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Post-Contact Rotational Volatility:** Once `leg_contact=1` is achieved, side-engine actions (1 and 3) are highly volatile and frequently act as the direct catalyst for unrecoverable $\dot{\theta}$ spikes, leading to rapid terminal rotation even when the craft appears stabilized.

---

## 2026-07-08 04:11:11

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively low.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce massive instantaneous rewards (often exceeding 13.0) by attempting to arrest descent, even when such actions fail to stabilize the craft's rotation.
8. **Extreme Post-Contact Reward Deception:** The reward function can produce exceptionally high positive values during or immediately after leg contact, which can mask an imminent catastrophic terminal penalty (-100) caused by unrecoverable rotational instability.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact (`leg_contact=1`) can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action (action 0) is taken.
10. **Post-Contact Rotational Volatility:** Once `leg_contact=1` is achieved, side-engine actions (1 and 3) are highly volatile and frequently act as the direct catalyst for escalating unrecoverable $\dot{\theta}$ spikes, leading to rapid terminal rotation.

---

## 2026-07-08 04:13:06

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively low.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce very high instantaneous rewards (e.g., >15.0) by attempting to arrest descent, even when such actions fail to stabilize the craft's rotation.
8. **Post-Contact Reward-Outcome Disparity:** Achieving leg contact (`leg_contact=1`) can trigger exceptionally high positive rewards, but these may only signify a "PARTIAL" outcome rather than a "SUCCESS," indicating that contact alone is insufficient for a successful mission.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Immediate Terminality of Unstable Contact:** If leg contact is achieved while angular velocity ($\dot{\theta}$) is high, the system can transition from high positive rewards to an immediate terminal penalty (-100) almost instantaneously, leaving no window for corrective action.

---

## 2026-07-08 04:14:41

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively low.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce high instantaneous rewards by attempting to arrest descent, even when such actions fail to stabilize the craft's rotation.
8. **Contact Maintenance Requirement:** While achieving leg contact (`leg_contact=1`) triggers high positive rewards, contact is not a permanent state; losing contact (e.g., via a "bounce") incurs significant negative penalties, even if angular stability is maintained.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Immediate Terminality of Unstable Contact:** If leg contact is achieved while angular velocity ($\dot{\theta}$) is high, the system can transition from high positive rewards to an immediate terminal penalty (-100) almost instantaneously, leaving no window for corrective action.

---

## 2026-07-08 04:22:24

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively low.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce high instantaneous rewards by attempting to arrest descent, even when such actions fail to stabilize the craft's rotation or exacerbate $\dot{\theta}$.
8. **Contact Maintenance Requirement:** While achieving leg contact (`leg_contact=1`) triggers high positive rewards, contact is not a permanent state; losing contact (e.g., via a "bounce") incurs significant negative penalties.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Contact-Phase Velocity Sensitivity:** Even after achieving stable contact, high vertical velocity ($\dot{y}$) or angular velocity ($\dot{\theta}$) can trigger severe negative rewards and induce "bouncing" (loss of leg contact), disrupting the continuous accumulation of positive contact rewards.

---

## 2026-07-08 04:23:28

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is the primary driver of failure; extreme $\dot{\theta}$ can induce an immediate terminal crash (massive negative reward) even when the craft is already in a contact state.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Side-Engine Instability Post-Contact:** Once contact is achieved (`leg_contact=1`), the use of side engines (1 and 3) becomes extremely high-risk, as they can trigger massive, uncontrolled spikes in $|\dot{\theta}|$ that lead to immediate bouncing or crashing.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce high instantaneous rewards by attempting to arrest descent, even when such actions fail to stabilize the craft's rotation or exacerbate $\dot{\theta}$.
8. **Contact Fragility and Bouncing:** Contact is a fragile state; excessive angular velocity or sudden engine-induced torque can cause the craft to "bounce" (transition from `leg_contact=1` back to `leg_contact=0`), disrupting reward accumulation.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Terminal State Thresholds:** The simulation enforces strict stability limits; exceeding critical thresholds for $|\dot{y}|$ or $|\dot{\theta}|$ triggers an immediate terminal failure, often overriding any positive rewards accumulated during the descent or contact phase.

---

## 2026-07-08 04:25:21

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is the primary driver of failure; extreme $\dot{\theta}$ can induce an immediate terminal crash (massive negative reward, e.g., -100) even when the craft is already in a contact state.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Side-Engine Instability Post-Contact:** Once contact is achieved (`leg_contact=1`), the use of side engines (1 and 3) is extremely high-risk; while used for orientation control, they can trigger massive, rapid spikes in $|\dot{\theta}|$ that threaten to induce immediate bouncing or crashes.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce high instantaneous rewards by attempting to arrest descent, even when such actions fail to stabilize the craft's rotation or exacerbate $\dot{\theta}$.
8. **Contact Fragility and Bouncing:** Contact is a fragile state; excessive angular velocity or sudden engine-induced torque can cause the craft to "bounce" (transition from `leg_contact=1` to `leg_contact=0`), a transition often marked by a sudden reversal of vertical velocity ($\dot{y}$) from negative to positive.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Terminal State Thresholds:** The simulation enforces strict stability limits; exceeding critical thresholds for $|\dot{y}|$ or $|\dot{\theta}|$ triggers an immediate terminal failure, often overriding any positive rewards accumulated during the descent or contact phase.

---

## 2026-07-08 04:27:03

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance and Terminal Failure:** High angular velocity ($\dot{\theta}$) is the primary driver of failure; extreme $\dot{\theta}$ can induce an immediate terminal crash (massive negative reward, e.g., -100) even when the craft is already in a contact state.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Post-Contact Engine Volatility:** Once contact is achieved (`leg_contact=1`), applying any engine thrust (1, 2, or 3) is extremely high-risk; even if the craft is grounded, engine use can trigger massive, sudden negative rewards (e.g., -10 to -20), likely due to rapid angular oscillations or ground-rebound effects.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce high instantaneous rewards by attempting to arrest descent, even when such actions fail to stabilize the craft's rotation or exacerbate $\dot{\theta}$.
8. **Contact Fragility and Bouncing:** Contact is a fragile state; excessive angular velocity or sudden engine-induced torque can cause the craft to "bounce" (transition from `leg_contact=1` to `leg_contact=0`), a transition often marked by a sudden reversal of vertical velocity ($\dot{y}$) from negative to positive.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Terminal State Thresholds:** The simulation enforces strict stability limits; exceeding critical thresholds for $|\dot{y}|$ or $|\dot{\theta}|$ triggers an immediate terminal failure, often overriding any positive rewards accumulated during the descent or contact phase.

---

## 2026-07-08 04:32:20

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance and Terminal Failure:** High angular velocity ($\dot{\theta}$) is the primary driver of failure; extreme $\dot{\theta}$ can induce an immediate terminal crash (massive negative reward) even when the craft is in a contact state (`leg_contact=1`).
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Post-Contact Engine Volatility:** Once contact is achieved (`leg_contact=1`), applying side engine thrust (1 or 3) is highly penalized and frequently triggers negative rewards, even if the craft is otherwise stable on the ground.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce high instantaneous rewards by attempting to arrest descent, even when such actions induce high $\dot{\theta}$ that leads to terminal instability.
8. **Grounded Stability via Inaction:** Once the craft achieves a landed state with low angular velocity ($\dot{\theta} \approx 0$), it can maintain a stable, high-reward state indefinitely by utilizing action 0.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Contact Configuration Transitions:** The simulation allows for transitions in contact states, such as moving from single-leg contact to dual-leg contact (`leg_contact` transitioning from `[1, 0]` or `[0, 1]` to `[1, 1]`), which is necessary for a stable landing.

---

## 2026-07-08 04:34:40

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance and Terminal Failure:** High angular velocity ($\dot{\theta}$) is the primary driver of failure; extreme $\dot{\theta}$ can induce immediate, massive terminal penalties even when the craft is in a contact state (`leg_contact=1`).
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Post-Contact Engine Volatility:** Once contact is achieved (`leg_contact=1`), applying side engine thrust (1 or 3) is highly penalized and frequently triggers large negative rewards, even if the craft appears otherwise stable.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce high instantaneous rewards by attempting to arrest descent, even when such actions induce the high $\dot{\theta}$ that leads to terminal instability.
8. **Grounded Stability via Inaction:** Once the craft achieves a landed state with low angular velocity ($\dot{\theta} \approx 0$), it can maintain a stable, high-reward state by utilizing action 0.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Contact-State Penalty Magnification:** Applying any engine thrust (1, 2, or 3) while in a contact state (`leg_contact=1`) triggers disproportionately large negative rewards (e.g., values exceeding -10.0), indicating that thrust-induced tipping or bouncing is a critical failure mode.

---

## 2026-07-08 04:37:31

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance and Terminal Failure:** High angular velocity ($\dot{\theta}$) is the primary driver of failure; extreme $\dot{\theta}$ can induce immediate, massive terminal penalties even when the craft is in a contact state (`leg_contact=1`).
5. **Inaction-Induced State Decay:** During descent, prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Post-Contact Side Engine Volatility:** Once contact is achieved (`leg_contact=1`), side engine thrust (1 or 3) is extremely volatile; it can either provide critical orientation stabilization or trigger massive negative rewards (often $<-10.0$) by inducing tipping or bouncing.
7. **Post-Contact Main Engine Volatility:** In a contact state, the main engine (2) is a high-risk action that can either facilitate stabilization through upward thrust or cause catastrophic bouncing and tipping with extreme negative rewards.
8. **The Inaction Stability Paradox:** While action 0 is the optimal way to maintain a stable, landed state, it becomes a failure mode if the lander enters the contact state with a significant tilt, as gravity and impact torque will cause the craft to tip over without active correction.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Contact-State Reward Sensitivity:** The reward signal in the contact state is hypersensitive to state variables; minute variations in orientation ($\theta$) and angular velocity ($\dot{\theta}$) at the moment of thrust determine whether an action results in extreme positive stabilization rewards or massive negative penalties.

---

## 2026-07-08 04:38:59

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Catastrophic Terminal Failure:** Extreme angular velocity ($\dot{\theta}$) or orientation ($\theta$) during the contact state (`leg_contact=1`) can trigger a massive terminal penalty (e.g., $-100.0$), signifying a complete crash or tip-over.
5. **Inaction-Induced State Decay:** During descent, prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Side-Engine Volatility in Contact:** Once contact is achieved, side engine thrust (1 or 3) is extremely volatile; it can provide critical orientation stabilization or trigger massive negative rewards (e.g., $<-20.0$) by inducing tipping.
7. **Main Engine Utility in Contact:** In the contact state, the main engine (2) is a high-risk/high-reward action that can facilitate significant stabilization rewards (e.g., $>10.0$) or cause catastrophic bouncing and tipping.
8. **The Inaction Stability Paradox:** While action 0 is the optimal way to maintain a stable, landed state, it becomes a failure mode if the lander enters the contact state with a significant tilt, as gravity and impact torque will cause the craft to tip over without active correction.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Contact-State Reward Bimodality:** The reward signal in the contact state is highly sensitive to state variables; minute variations in orientation ($\theta$) and angular velocity ($\dot{\theta}$) at the moment of thrust determine whether an action results in high positive stabilization rewards or massive terminal penalties.

---

## 2026-07-08 04:40:45

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Catastrophic Terminal Failure:** Extreme angular velocity ($\dot{\theta}$) or orientation ($\theta$) during the contact state (`leg_contact=1`) triggers a massive terminal penalty (e.g., $-100.0$), signifying a complete crash or tip-over.
5. **Inaction-Induced State Decay:** During descent, prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Side-Engine Volatility in Contact:** Once contact is achieved, side engine thrust (1 or 3) is extremely volatile; it can provide critical orientation stabilization (e.g., rewards $>20.0$) or trigger massive negative rewards (e.g., $<-10.0$) by inducing tipping.
7. **Main Engine Risk in Contact:** In the contact state, the main engine (2) is a high-risk/high-reward action that can facilitate significant stabilization rewards or cause catastrophic bouncing and tipping if not precisely timed with the craft's angular momentum.
8. **The Inaction Stability Paradox:** While action 0 is the optimal way to maintain a stable, landed state once equilibrium is reached, it becomes a failure mode if the lander enters the contact state with insufficient damping, as gravity and impact torque will cause the craft to tip over without active correction.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Contact-State Reward Bimodality:** The reward signal in the contact state is extremely sensitive to the precise state variables; minute variations in orientation ($\theta$) and angular velocity ($\dot{\theta}$) at the moment of thrust determine whether an action results in high positive stabilization rewards or massive terminal penalties.

---

## 2026-07-08 04:45:51

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust capacity.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Contact-State Volatility and Bouncing:** The transition to the contact state (`leg_contact=1`) is not necessarily a terminal equilibrium; incorrect thrusting can induce significant bouncing, causing the lander to lose contact (`leg_contact=0`) and enter a highly unstable, high-velocity state.
5. **High-Stakes Bimodality in Contact:** During contact, the reward signal is extremely sensitive to the precise state variables; precise thrusting can facilitate significant stabilization rewards ($>10.0$), while miscalculated actions can trigger massive negative penalties ($<-10.0$) through tipping or bouncing.
6. **Main Engine Risk in Contact:** In the contact state, the main engine (2) is a high-risk/high-reward action that can either facilitate rapid stabilization or cause catastrophic bouncing and loss of contact if not perfectly timed with the craft's angular momentum.
7. **Catastrophic Tip-Over Penalties:** Extreme angular velocity ($\dot{\theta}$) or orientation ($\theta$) during or immediately following a contact event triggers massive terminal penalties, signifying a complete crash, tip-over, or loss of control.
8. **Inaction-Induced State Decay:** During both descent and contact, prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Micro-State Sensitivity of Rewards:** The reward signal is hypersensitive to minute variations in $\theta$ and $\dot{\theta}$ at the moment of thrust; small deviations in these variables determine whether an action results in high stabilization rewards or massive terminal penalties.

---

## 2026-07-08 04:47:38

1. **Gravity-Driven Vertical Acceleration:** Continuous increase in the magnitude of negative vertical velocity ($\dot{y}$) is the primary driver of unrecoverable descent; exceeding a critical threshold makes landing impossible regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) is highly persistent throughout the descent, and the main engine provides minimal capacity to attenuate existing horizontal momentum.
3. **Orientation-Coupled Side Engine Torque:** The corrective capacity of side engines (1 and 3) is contingent upon whether the applied torque opposes or reinforces the current angular velocity ($\dot{\theta}$); misapplication leads to rapid angular divergence.
4. **Contact-State Volatility:** Achieving leg contact is not a terminal equilibrium; incorrect thrusting or impact can induce significant bouncing or high-velocity instability, even after contact is established.
5. **Asymmetric Contact Reward Potential:** The reward signal can be highly positive even during asymmetric contact (one leg), provided the craft's orientation ($\theta$) and angular velocity ($\dot{\theta}$) are successfully stabilized.
6. **Main Engine Risk in Contact:** The main engine (2) is a critical tool for managing vertical velocity during contact but carries a high risk of triggering catastrophic bounces or tip-overs if not perfectly synchronized with the craft's rotation.
7. **Extreme Terminal Tip-Over Penalties:** Catastrophic loss of orientation control (tip-over) results in massive terminal penalties (up to -100.0), which can occur even when both legs are in a contact state.
8. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) during both descent and contact allow both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for recovery.
9. **Impact-Induced Angular Spikes:** The physical transition to a contact state induces sudden, significant spikes in angular velocity ($\dot{\theta}$) due to impact-related torque, requiring immediate corrective action.
10. **Micro-State Reward Sensitivity:** The reward signal is hypersensitive to the interplay between the contact state and the craft's rotational state ($\theta, \dot{\theta}$); minute deviations determine whether an action results in high stabilization rewards or massive terminal penalties.

---

## 2026-07-08 04:49:18

1. **Gravity-Driven Vertical Acceleration:** Continuous increase in the magnitude of negative vertical velocity ($\dot{y}$) is the primary driver of unrecoverable descent; exceeding a critical threshold makes landing impossible regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) is highly persistent throughout the descent; side engines provide minimal capacity to attenuate existing horizontal momentum, often requiring the craft to manage descent while drifting.
3. **Orientation-Coupled Side Engine Torque:** The corrective capacity of side engines (1 and 3) is highly sensitive to the current angular velocity ($\dot{\theta}$); misapplication of side engines during a descent or contact phase leads to rapid angular divergence and immediate negative reward accumulation.
4. **Contact-State Volatility:** Achieving leg contact is not a terminal equilibrium; the transition to contact can induce significant bouncing (returning to 0.0 contact states) or high-velocity angular instability that persists after the initial impact.
5. **Asymmetric Contact Reward Potential:** The reward signal can experience massive positive spikes (e.g., Step 314, Episode 1) during the initial transition to contact, even if the craft's orientation or angular velocity is not yet fully stabilized.
6. **Main Engine Risk in Contact:** The main engine (2) is essential for managing vertical velocity during the contact phase but carries a high risk of triggering catastrophic tip-overs or bounces if applied while the craft's rotational state ($\theta, \dot{\theta}$) is uncontrolled.
7. **Extreme Terminal Tip-Over Penalties:** Catastrophic loss of orientation control (tip-over) results in massive terminal penalties (up to -100.0), which can occur even after successful leg contact has been established.
8. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) during both descent and contact allow both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for recovery.
9. **Impact-Induced Angular Spikes:** The physical transition to a contact state induces sudden, significant spikes in angular velocity ($\dot{\theta}$) due to impact-related torque, necessitating immediate and precise corrective thrust to prevent a tip-over.
10. **Post-Contact Rotational Dominance:** Upon leg contact, the reward landscape undergoes a fundamental phase shift; the primary driver of reward (and failure) shifts from managing vertical velocity ($\dot{y}$) to the immediate suppression of impact-induced angular velocity ($\dot{\theta}$).

---

## 2026-07-08 04:52:22

---
1. **Gravity-Driven Vertical Acceleration:** Continuous increase in the magnitude of negative vertical velocity ($\dot{y}$) is the primary driver of unrecoverable descent; exceeding a critical threshold makes landing impossible regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) is highly persistent throughout the descent; side engines provide minimal capacity to attenuate existing horizontal momentum, often requiring the craft to manage descent while drifting.
3. **Orientation-Coupled Side Engine Torque:** The corrective capacity of side engines (1 and 3) is highly sensitive to the current angular velocity ($\dot{\theta}$); misapplication of side engines during a descent or contact phase leads to rapid angular divergence and immediate negative reward accumulation.
4. **Contact-State Volatility:** Achieving leg contact is not a terminal equilibrium; the transition to contact can induce significant bouncing (returning to 0.0 contact states) or high-velocity angular instability that persists after the initial impact.
5. **Asymmetric Contact Reward Potential:** The reward signal can experience massive positive spikes during the initial transition to a contact state, even if the craft's orientation or angular velocity is not yet fully stabilized.
6. **Impact-Induced Angular Spikes:** The physical transition to a contact state induces sudden, significant spikes in angular velocity ($\dot{\theta}$) due to impact-related torque, necessitating immediate and precise corrective thrust to prevent a tip-over.
7. **Extreme Post-Contact Stability Penalties:** Once leg contact is established, the magnitude of negative rewards for engine application is significantly higher than during the descent phase, heavily penalizing thrust that fails to perfectly stabilize the craft's current state.
8. **Angle-Magnitude Scaling of Penalties:** During the contact phase, the severity of negative rewards incurred from engine actions (1, 2, or 3) scales with the absolute magnitude of the current angle ($\theta$).
9. **Main Engine Risk in Contact:** The main engine (2) is essential for managing vertical velocity during the contact phase but carries a high risk of triggering catastrophic penalties if applied while the craft's orientation ($\theta, \dot{\theta}$) is not near zero.
10. **Post-Contact Rotational Dominance:** Upon leg contact, the reward landscape undergoes a fundamental phase shift; the primary driver of reward (and failure) shifts from managing vertical velocity ($\dot{y}$) to the immediate suppression of both angular velocity ($\dot{\theta}$) and angular deviation ($\theta$).

---

## 2026-07-08 04:57:00

1. **Gravity-Driven Vertical Acceleration:** Continuous increase in the magnitude of negative vertical velocity ($\dot{y}$) is the primary driver of unrecoverable descent; exceeding a critical threshold makes landing impossible regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) is highly persistent throughout the descent; side engines provide minimal capacity to attenuate existing horizontal momentum, often requiring the craft to manage descent while drifting.
3. **Orientation-Coupled Side Engine Torque:** The corrective capacity of side engines (1 and 3) is highly sensitive to the current angular velocity ($\dot{\theta}$); misapplication of side engines during descent or contact leads to rapid angular divergence.
4. **Impact-Induced Angular Spikes:** The physical transition to a contact state induces sudden, significant spikes in angular velocity ($\dot{\theta}$) due to impact-related torque, which can immediately trigger unrecoverable rotational instability.
5. **Asymmetric Contact Reward Spikes:** The reward signal experiences massive positive spikes during the initial transition to a contact state, which can temporarily mask the immediate onset of post-impact angular divergence.
6. **Post-Contact Rotational Dominance:** Upon leg contact, the reward landscape undergoes a fundamental phase shift; the primary driver of reward (and failure) shifts from managing vertical velocity ($\dot{y}$) to the immediate suppression of both angular velocity ($\dot{\theta}$) and angular deviation ($\theta$).
7. **Extreme Post-Contact Penalty Scaling:** During the contact phase, the severity of negative rewards incurred from any engine action (1, 2, or 3) scales aggressively with the absolute magnitude of the current angle ($\theta$).
8. **Main Engine Instability Risk:** The main engine (2) carries extreme risk during the contact phase; its application can trigger massive negative rewards even when vertical velocity is near zero, likely due to torque-induced instability or orientation mismatch.
9. **Angular Divergence as Failure Driver:** In the contact phase, the primary mechanism of failure is a rapid increase in $\theta$ driven by $\dot{\theta}$ spikes; once $\theta$ deviates significantly, the resulting penalties become catastrophic and often unrecoverable.
10. **Contact-State Equilibrium Volatility:** Achieving leg contact is not a terminal equilibrium; maintaining a stable landing requires high-precision suppression of all rotational components ($\theta, \dot{\theta}$) to prevent the craft from entering a high-penalty divergent state.

---

## 2026-07-08 04:59:06

---
1. **Gravity-Driven Vertical Acceleration:** Continuous increase in the magnitude of negative vertical velocity ($\dot{y}$) is the primary driver of unrecoverable descent; exceeding a critical threshold makes landing impossible regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) is highly persistent throughout the descent; side engines provide minimal capacity to attenuate existing horizontal momentum, often requiring the craft to manage descent while drifting.
3. **Side-Engine Torque Sensitivity:** The corrective capacity of side engines (1 and 3) is highly sensitive to the current angular velocity ($\dot{\theta}$); applying side engines while the craft possesses significant angular momentum or angular deviation frequently results in immediate, substantial negative rewards.
4. **Post-Contact Reward Volatility:** Upon transitioning to a contact state, the reward landscape becomes extremely volatile; the environment produces massive positive spikes for successful contact but can immediately pivot to catastrophic negative rewards if stability is not maintained.
5. **High-Variance Main Engine Utility:** The main engine (2) serves as a high-stakes stabilization tool during the contact phase; it can provide the highest positive rewards for managing descent/orientation (e.g., Step 325, Ep 2) but also carries an extreme risk of triggering massive negative rewards if it induces torque-related instability.
6. **Penalty of Inaction during Contact:** During the contact phase, taking no action (Action 0) is often a high-penalty behavior; if the craft is not in a perfect state of rotational equilibrium, inaction leads to rapid divergence and significant negative rewards.
7. **Post-Contact Rotational Dominance:** Once leg contact is established, the primary driver of reward (and failure) shifts from managing vertical velocity ($\dot{y}$) to the immediate and continuous suppression of both angular velocity ($\dot{\theta}$) and angular deviation ($\theta$).
8. **Angular Divergence as Failure Driver:** In the contact phase, the primary mechanism of failure is a rapid increase in $\theta$ driven by $\dot{\theta}$ spikes; once $\theta$ deviates significantly, the resulting penalties become catastrophic and often unrecoverable.
9. **Orientation-Dependent Penalty Scaling:** The severity of negative rewards incurred from any engine action (1, 2, or 3) during the contact phase scales aggressively with the absolute magnitude of the current angle ($\theta$) and angular velocity ($\dot{\theta}$).
10. **Contact-State Equilibrium Fragility:** Achieving leg contact is not a terminal state but a high-entropy equilibrium; maintaining a stable landing requires constant, high-precision corrective thrust to prevent the craft from entering a high-penalty divergent state.

---

## 2026-07-08 05:01:37

---
1. **Gravity-Driven Vertical Acceleration:** Continuous increase in the magnitude of negative vertical velocity ($\dot{y}$) is the primary driver of unrecoverable descent; exceeding a critical threshold makes landing impossible regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) is highly persistent throughout the descent; side engines provide minimal capacity to attenuate existing horizontal momentum, often requiring the craft to manage descent while drifting.
3. **Side-Engine Torque Sensitivity during Descent:** The corrective capacity of side engines (1 and 3) is highly sensitive to the current angular velocity ($\dot{\theta}$); applying side engines while the craft possesses significant angular momentum or angular deviation frequently results in immediate, substantial negative rewards.
4. **Extreme Post-Contact Reward Volatility:** Upon transitioning to a contact state, the reward landscape becomes extremely volatile; the environment produces massive positive spikes (e.g., +12.0) for successful stabilization but can immediately pivot to catastrophic negative rewards (e.g., -17.0) if contact is lost or stability is breached.
5. **Main Engine Utility in Contact Stabilization:** The main engine (2) serves as the primary high-stakes tool for managing vertical velocity ($\dot{y}$) during the contact phase; it is the most frequent driver of the highest positive rewards but carries extreme risk if it induces torque-related instability.
6. **Massive Inaction Penalty during Contact:** During the contact phase, taking no action (Action 0) is a high-penalty behavior; if the craft is not in a perfect state of rotational or vertical equilibrium, inaction leads to rapid divergence and massive negative rewards (e.g., -16.5).
7. **Contact-State Variable Dominance:** Once leg contact is established, the primary driver of reward shifts from managing altitude to the immediate and continuous suppression of both angular velocity ($\dot{\theta}$) and angular deviation ($\theta$), alongside the management of vertical velocity ($\dot{y}$).
8. **Angular Divergence as a Rapid Failure Mechanism:** In the contact phase, the primary mechanism of failure is a rapid increase in $\theta$ driven by $\dot{\theta}$ spikes; once $\theta$ deviates significantly, the resulting penalties become catastrophic and often unrecoverable.
9. **Action-State Non-Linearity in Contact:** The sign and magnitude of rewards for engine actions (1, 2, or 3) during contact are non-linearly coupled to the instantaneous state; an engine action that provides massive positive rewards in one step can trigger a massive negative reward in the next if it causes a slight angular or vertical drift.
10. **Active Equilibrium Maintenance:** Achieving leg contact is not a terminal state but a high-entropy equilibrium; maintaining a stable landing requires constant, high-frequency, and high-precision corrective thrust to prevent the craft from entering a high-penalty divergent state.

---

## 2026-07-08 05:03:18

1. **Gravity-Driven Vertical Acceleration:** Continuous increase in the magnitude of negative vertical velocity ($\dot{y}$) is the primary driver of unrecoverable descent; exceeding a critical threshold makes landing impossible regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) is highly persistent throughout the descent; side engines provide minimal capacity to attenuate existing horizontal momentum, often requiring the craft to manage descent while drifting.
3. **Side-Engine Torque Sensitivity during Descent:** The corrective capacity of side engines (1 and 3) is highly sensitive to the current angular velocity ($\dot{\theta}$); applying side engines while the craft possesses significant angular momentum or angular deviation frequently results in immediate, substantial negative rewards.
4. **Extreme Post-Contact Reward Volatility:** Upon transitioning to a contact state, the reward landscape becomes extremely volatile; the environment produces massive positive spikes for successful stabilization but can immediately pivot to catastrophic negative rewards if stability is breached.
5. **Main Engine Utility in Vertical Management:** The main engine (2) serves as the primary tool for managing vertical velocity ($\dot{y}$); it is the most frequent driver of the highest positive rewards during both the final descent and the initial contact phase.
6. **Catastrophic Inaction Penalty during Contact:** During the contact phase, taking no action (Action 0) is a terminal failure mechanism; if the craft is not in a state of perfect rotational or vertical equilibrium, inaction can trigger a massive, terminal -100 penalty.
7. **Contact-State Variable Dominance:** Once leg contact is established, the primary driver of reward shifts from managing altitude to the immediate and continuous suppression of both angular velocity ($\dot{\theta}$) and angular deviation ($\theta$), alongside the management of vertical velocity ($\dot{y}$).
8. **Angular Divergence as a Rapid Failure Mechanism:** In the contact phase, the primary mechanism of failure is a rapid increase in $\theta$ driven by $\dot{\theta}$ spikes; once $\theta$ deviates significantly, the resulting penalties become catastrophic and often unrecoverable.
9. **Action-State Non-Linearity in Contact:** The sign and magnitude of rewards for engine actions (1, 2, or 3) during contact are non-linearly coupled to the instantaneous state; an engine action that provides massive positive rewards in one step can trigger a massive negative reward in the next if it causes a slight angular or vertical drift.
10. **Dual-Path Terminal Failure:** Terminal failure is achieved through two distinct modes: a high-energy impact (crash) at the moment of contact, or a failure of active equilibrium maintenance during the post-contact stabilization phase.

---

## 2026-07-10 04:16:06

1. **Gravity and Descent:** Gravity continuously increases the downward vertical velocity ($\dot{y}$); failure to apply the main engine (2) leads to uncontrolled descent.
2. **Main Engine Dynamics:** Action 2 is essential for altitude control but contributes to horizontal displacement ($x\_vel$) and can influence angular stability.
3. **Orientation Control:** Side engines (1 and 3) are used to manipulate the angle ($\theta$) and angular velocity ($\dot{\theta}$), with action 3 specifically driving the craft toward negative angles.
4. **Angular Momentum Sensitivity:** The system is highly sensitive to angular velocity; once $\dot{\theta}$ reaches high magnitudes, the craft enters a "death spiral" that is difficult to arrest.
5. **Failure via Inaction:** Prolonged periods of action 0 (nothing) cause both vertical velocity and angular instability to accumulate, leading to terminal states.
6. **Failure via Uncoordinated Oscillation:** Rapidly switching between the main engine (2) and a side engine (3) without stabilization often exacerbates rotation rather than correcting it.
7. **Failure via Overcorrection:** Excessive use of side engines (as seen in Episode 2) drives the angle $\theta$ to extreme values, making the lander impossible to level.
8. **Critical Threshold (Angle):** A critical failure point occurs when the angle $\theta$ exceeds a stability threshold, at which point engine thrust can no longer counteract the rotational momentum.
9. **Critical Threshold (Velocity):** High vertical descent velocities ($\dot{y}$) combined with high angular velocities ($\dot{\theta}$) signify a point of no return regardless of subsequent actions.
10. **Trajectory Pattern:** Both episodes demonstrate a transition from attempted control to "panic" behavior—characterized by high-frequency, high-magnitude engine bursts that fail to mitigate the increasing entropy of the state.

---

## 2026-07-10 04:23:48

1. **Gravity and Vertical Descent:** Gravity continuously increases the downward vertical velocity ($\dot{y}$); failure to apply the main engine (2) leads to uncontrolled descent and the rapid accumulation of negative vertical velocity.
2. **Main Engine Dynamics:** Action 2 is essential for altitude control but is not a purely vertical force; it contributes to horizontal displacement ($x\_vel$) and influences angular stability.
3. **State-Dependent Orientation Control:** Side engines (1 and 3) are used to manipulate the angle ($\theta$) and angular velocity ($\dot{\theta}$), with action 3 driving the craft toward negative angles; however, the directional impact of side engines is highly dependent on the current orientation.
4. **Angular Momentum Sensitivity:** The system is extremely sensitive to angular velocity ($\dot{\theta}$); once $\dot{\theta}$ reaches high magnitudes, the resulting angular momentum makes the orientation difficult to arrest.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability to accumulate, rapidly narrowing the window for effective recovery.
6. **Main Engine-Induced Rotational Drift:** In non-upright orientations, continuous application of the main engine (2) can exacerbate angular drift rather than correcting it, as the engine's thrust vector induces additional rotational momentum.
7. **Failure via Uncoordinated Oscillation:** Rapidly switching between the main engine (2) and side engines (1 or 3) without first stabilizing the angular velocity ($\dot{\theta}$) often results in uncoordinated oscillations that increase the entropy of the state.
8. **Critical Orientation Threshold:** A critical failure point occurs when the angle $\theta$ exceeds a stability threshold (approximately -1.0 to -1.5 radians), at which point engine thrust becomes insufficient to counteract the accumulated rotational momentum.
9. **Kinetic Convergence of Failure:** High vertical descent velocities ($\dot{y}$) combined with high angular velocities ($\dot{\theta}$) signify a point of no return, where the energy required for simultaneous altitude and orientation correction exceeds the available thrust.
10. **Maneuverability Erosion:** As the magnitudes of $\theta$, $\dot{\theta}$, and $\dot{y}$ increase, the craft enters a state of decreasing maneuverability where high-frequency engine bursts fail to mitigate the increasing instability.

---

## 2026-07-10 04:28:37

1. **Gravity and Vertical Descent:** Gravity continuously increases the downward vertical velocity ($\dot{y}$); failure to apply the main engine (2) leads to uncontrolled descent and the rapid accumulation of negative vertical velocity.
2. **Main Engine Multi-Axis Dynamics:** Action 2 is essential for altitude control but is not a purely vertical force; it contributes significantly to horizontal displacement ($x\_vel$) and introduces torque that influences angular stability.
3. **Directional Side Engine Influence:** Side engines (1 and 3) manipulate the angle ($\theta$) and angular velocity ($\dot{\theta}$); specifically, action 3 drives the craft toward increasingly negative angles and negative angular velocities.
4. **Angular Momentum Sensitivity:** The system is extremely sensitive to angular velocity ($\dot{\theta}$); once $\dot{\theta}$ reaches high magnitudes, the resulting angular momentum becomes difficult to arrest with standard engine bursts.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability to accumulate, rapidly narrowing the window for effective recovery.
6. **Rotational Reinforcement via Main Engine:** In non-upright orientations, the main engine (2) can act as a rotational driver; rather than correcting orientation, its thrust vector can exacerbate angular displacement by increasing the absolute magnitude of $\theta$.
7. **Failure via Uncoordinated Oscillation:** Rapidly switching between the main engine (2) and side engines (1 or 3) fails to stabilize the craft if the angular momentum is already high, often resulting in a continuous divergence of the angle.
8. **Critical Orientation Threshold:** A critical failure point occurs when the angle $\theta$ exceeds a stability threshold (approximately -1.0 radians), at which point the main engine's thrust becomes primarily rotational, making simultaneous altitude and orientation correction nearly impossible.
9. **Kinetic Convergence of Failure:** The simultaneous accumulation of high vertical descent velocities ($\dot{y}$) and high angular velocities ($\dot{\theta}$) signifies a point of no return, where the energy required to correct both vectors exceeds the available thrust.
10. **Maneuverability Erosion:** As the magnitudes of $\theta$, $\dot{\theta}$, and $\dot{y}$ increase, the craft enters a state of decreasing control authority where engine inputs have diminishing returns on stabilizing the state.

---

## 2026-07-10 04:42:57

1. **Gravity and Vertical Descent:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); failure to apply the main engine (2) results in rapid, uncontrolled descent.
2. **Main Engine Multi-Axis Dynamics:** Action 2 is essential for altitude control but is not a purely vertical force; it introduces significant horizontal displacement ($x\_vel$) and contributes to angular instability.
3. **Orientation-Dependent Side Engine Torque:** Side engines (1 and 3) manipulate angular velocity ($\dot{\theta}$), but the effective direction of the torque is coupled to the craft's orientation ($\theta$); an engine's ability to stabilize or destabilize the rotation is contingent upon the current angle.
4. **Angular Momentum Sensitivity:** The system is extremely sensitive to angular velocity ($\dot{\theta}$); once $\dot{\theta}$ reaches high magnitudes, the resulting angular momentum becomes difficult to arrest with standard engine bursts.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability to accumulate, rapidly narrowing the window for effective recovery.
6. **Rotational Reinforcement via Main Engine:** In non-upright orientations, the main engine (2) can act as a rotational driver; its thrust vector can exacerbate angular displacement by increasing the magnitude of $\theta$.
7. **Failure via Uncoordinated Oscillation:** Rapidly switching between the main engine (2) and side engines (1 or 3) fails to stabilize the craft if the angular momentum is already high, often resulting in a continuous divergence of the angle.
8. **Kinetic Convergence of Failure:** The simultaneous accumulation of high vertical descent velocities ($\dot{y}$) and high angular velocities ($\dot{\theta}$) signifies a point of no return, where the energy required to correct both vectors exceeds the available thrust.
9. **Thrust-Induced Reward Penalties:** The application of the main engine (2) is associated with significant instantaneous negative rewards, representing the energetic cost of thrust or the penalty for the instability and horizontal displacement it introduces.
10. **Maneuverability Erosion:** As the magnitudes of $\theta$, $\dot{\theta}$, and $\dot{y}$ increase, the craft enters a state of decreasing control authority where engine inputs have diminishing returns on stabilizing the state.

---

## 2026-07-10 04:47:13

1. **Gravity and Vertical Descent:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); failure to apply the main engine (2) results in rapid, uncontrolled descent.
2. **Main Engine Multi-Axis Dynamics:** Action 2 is not a purely vertical force; it introduces significant horizontal displacement ($x\_vel$) and contributes to angular instability through induced torque.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$); an engine's ability to stabilize or destabilize rotation is contingent upon whether the resulting torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Momentum Sensitivity:** The system is extremely sensitive to angular velocity ($\dot{\theta}$); once $\dot{\theta}$ reaches high magnitudes, the resulting angular momentum becomes difficult to arrest with standard engine bursts.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Rotational Reinforcement via Main Engine:** In non-upright orientations ($\theta \neq 0$), the main engine (2) acts as a rotational driver; its thrust vector can exacerbate angular displacement by increasing the magnitude of $\theta$ and $\dot{\theta}$.
7. **Failure via Uncoordinated Oscillation:** Rapidly switching between the main engine (2) and side engines (1 or 3) fails to stabilize the craft if the angular momentum is already high, often resulting in a continuous divergence of the angle.
8. **Kinetic Convergence of Failure:** Failure is characterized by the simultaneous accumulation of high vertical descent velocities ($\dot{y}$), high angular velocities ($\dot{\theta}$), and high angular displacement ($\theta$); at this point, the energy required to correct these vectors exceeds the available thrust.
9. **Thrust-Induced Reward Penalties:** The application of the main engine (2) is associated with significant instantaneous negative rewards, representing the energetic cost of thrust and the penalties for the instability and horizontal displacement it introduces.
10. **Maneuverability Erosion:** As the magnitudes of $\theta$, $\dot{\theta}$, and $\dot{y}$ increase, the craft enters a state of decreasing control authority where engine inputs have diminishing returns on stabilizing the state.

---

## 2026-07-10 04:50:17

1. **Gravity and Vertical Descent:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); failure to apply the main engine (2) results in rapid, uncontrolled descent.
2. **Main Engine Multi-Axis Dynamics:** Action 2 is not a purely vertical force; it introduces significant horizontal displacement ($x\_vel$) and contributes to angular instability through induced torque.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$); an engine's ability to stabilize or destabilize rotation is contingent upon whether the resulting torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Momentum Sensitivity:** The system is extremely sensitive to angular velocity ($\dot{\theta}$); once $\dot{\theta}$ reaches high magnitudes, the resulting angular momentum becomes difficult to arrest with standard engine bursts.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Rotational Reinforcement via Main Engine:** In non-upright orientations ($\theta \neq 0$), the main engine (2) acts as a rotational driver; its thrust vector can exacerbate angular displacement by increasing the magnitude of $\theta$ and $\dot{\theta}$.
7. **Failure via Uncoordinated Oscillation:** Rapidly switching between the main engine (2) and side engines (1 or 3) fails to stabilize the craft if the angular momentum is already high, often resulting in a continuous divergence of the angle.
8. **Kinetic Convergence of Failure:** Failure is characterized by the simultaneous accumulation of high vertical descent velocities ($\dot{y}$), high angular velocities ($\dot{\theta}$), and high angular displacement ($\theta$); at this point, the energy required to correct these vectors exceeds the available thrust.
9. **Reward-Thrust Dynamics:** The reward signal is heavily weighted toward vertical velocity ($\dot{y}$) stabilization; consequently, applying the main engine (2) to arrest high-velocity descent can result in significant instantaneous positive rewards, potentially offsetting the energetic cost of thrust.
10. **Non-Linear Control Erosion:** As the magnitudes of $\theta$, $\dot{\theta}$, and $\dot{y}$ increase, the craft enters a regime of decreasing control authority where engine inputs—particularly the main engine (2)—can trigger disproportionately large and destabilizing spikes in angular velocity ($\dot{\theta}$).

---

## 2026-07-10 04:54:27

1. **Gravity and Vertical Descent:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); failure to apply the main engine (2) results in rapid, uncontrolled descent.
2. **Main Engine Multi-Axis Dynamics:** Action 2 introduces significant horizontal displacement ($x\_vel$) and angular instability; high horizontal velocity magnitudes can persist throughout the descent even during active vertical thrust application.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$); an engine's ability to stabilize or destabilize rotation is contingent upon whether the resulting torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Momentum Dominance:** High angular velocity ($\dot{\theta}$) is a critical failure driver; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively small or near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Rotational Reinforcement via Main Engine:** In non-upright orientations ($\theta \neq 0$), the main engine (2) acts as a rotational driver; its thrust vector can exacerbate angular displacement by increasing the magnitude of $\theta$ and $\dot{\theta}$.
7. **Failure via Uncoordinated Oscillation:** Rapidly switching between the main engine (2) and side engines (1 or 3) fails to stabilize the craft if the angular momentum is already high, often resulting in a continuous divergence of the angle.
8. **Kinetic Convergence of Failure:** Failure is characterized by the simultaneous accumulation of high vertical descent velocities ($\dot{y}$), high angular velocities ($\dot{\theta}$), and high angular displacement ($\theta$); at this point, the energy required to correct these vectors exceeds the available thrust.
9. **Reward-Instability Conflict:** The reward signal's heavy weighting toward $\dot{y}$ stabilization can create a deceptive feedback loop, where applying the main engine (2) to arrest descent yields high instantaneous rewards while simultaneously driving the craft toward terminal angular velocity ($\dot{\theta}$).
10. **Non-Linear Control Erosion:** As the magnitudes of $\theta$, $\dot{\theta}$, and $\dot{y}$ increase, the craft enters a regime of decreasing control authority where engine inputs—particularly the main engine (2)—can trigger disproportionately large and destabilizing spikes in angular velocity ($\dot{\theta}$).

---

## 2026-07-10 04:59:50

1. **Gravity and Terminal Vertical Descent:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$). If $\dot{y}$ exceeds a critical threshold, the main engine (2) may fail to arrest the descent, causing $\dot{y}$ to continue increasing in magnitude despite sustained thrust.
2. **Main Engine Horizontal Inertia:** Action 2 introduces horizontal displacement ($x\_vel$), but the engine has limited capacity to attenuate existing high horizontal velocities; high $x\_vel$ tends to persist throughout the descent regardless of vertical thrust application.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$); an engine's ability to stabilize or destabilize rotation is contingent upon whether the resulting torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Momentum Dominance:** High angular velocity ($\dot{\theta}$) is a critical failure driver; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively small or near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Rotational Reinforcement via Main Engine:** In non-upright orientations ($\theta \neq 0$), the main engine (2) acts as a rotational driver; its thrust vector can exacerbate angular displacement by increasing the magnitude of both $\theta$ and $\dot{\theta}$.
7. **Failure via Uncoordinated Oscillation:** Rapidly switching between the main engine (2) and side engines (1 or 3) fails to stabilize the craft if the angular momentum is already high, often resulting in a continuous divergence of the angle.
8. **Kinetic Convergence of Failure:** Failure is characterized by the simultaneous accumulation of high vertical descent velocities ($\dot{y}$), high angular velocities ($\dot{\theta}$), and high angular displacement ($\theta$); at this point, the kinetic energy of the system exceeds the available thrust's ability to restore stability.
9. **Reward-Instability Conflict:** The reward signal's weighting toward $\dot{y}$ stabilization can create a deceptive feedback loop, where applying the main engine (2) to arrest descent yields high instantaneous rewards while simultaneously driving the craft toward terminal angular velocity ($\dot{\theta}$).
10. **Non-Linear Control Erosion:** As the magnitudes of $\theta$, $\dot{\theta}$, and $\dot{y}$ increase, the craft enters a regime of decreasing control authority where engine inputs—particularly the main engine (2)—can trigger disproportionately large and destabilizing spikes in angular velocity ($\dot{\theta}$) while failing to meaningfully arrest $\dot{y}$.

---

## 2026-07-10 05:03:26

1. **Gravity and Terminal Vertical Descent:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$). If $\dot{y}$ exceeds a critical threshold, the main engine (2) may struggle to arrest the descent, leading to a terminal velocity that makes recovery impossible.
2. **Main Engine Horizontal Inertia:** Action 2 introduces horizontal displacement ($x\_vel$), but the engine has limited capacity to attenuate existing high horizontal velocities; high $x\_vel$ tends to persist throughout the descent regardless of vertical thrust application.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$); an engine's ability to stabilize or destabilize rotation is contingent upon whether the resulting torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Momentum Dominance:** High angular velocity ($\dot{\theta}$) is a critical failure driver; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively small or near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Main Engine-Induced Angular Spikes:** The main engine (2) acts as a primary driver of angular momentum; applying action 2 can trigger disproportionately large, sudden spikes in angular velocity ($\dot{\theta}$), particularly when the craft is not perfectly upright ($\theta \neq 0$).
7. **Side Engine Divergence Threshold:** Once angular velocity ($\dot{\theta}$) or displacement ($\theta$) exceeds a specific threshold, side engines (1 and 3) frequently cease to act as corrective forces and instead act as accelerators of angular momentum, causing rapid and uncontrolled divergence.
8. **Kinetic Convergence of Failure:** Failure is characterized by the simultaneous accumulation of high vertical descent velocities ($\dot{y}$), high angular velocities ($\dot{\theta}$), and high angular displacement ($\theta$); at this point, the kinetic energy of the system exceeds the available thrust's ability to restore stability.
9. **The Main Engine Reward Trap:** The reward signal's heavy weighting toward $\dot{y}$ stabilization creates a deceptive feedback loop; the main engine (2) can produce massive instantaneous rewards by successfully arresting descent, even while simultaneously injecting the catastrophic $\dot{\theta}$ spikes that lead to terminal instability.
10. **Non-Linear Control Erosion:** As the magnitudes of $\theta$, $\dot{\theta}$, and $\dot{y}$ increase, the craft enters a regime of decreasing control authority where engine inputs—particularly the main engine (2)—can trigger disproportionately large and destabilizing spikes in angular velocity ($\dot{\theta}$) while failing to meaningfully arrest $\dot{y}$.

---

## 2026-07-10 05:07:31

1. **Gravity and Terminal Vertical Descent:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $\dot{y}$ exceeds a critical threshold, the main engine (2) may fail to arrest the descent, leading to a terminal velocity that makes recovery impossible.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent; the main engine has limited capacity to attenuate existing high horizontal velocities regardless of vertical thrust application.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$); their ability to stabilize or destabilize rotation is contingent upon whether the resulting torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Momentum Dominance:** High angular velocity ($\dot{\theta}$) is a critical failure driver; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively small or near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Main Engine-Induced Angular Spikes:** The main engine (2) acts as a primary driver of angular momentum; applying action 2 can trigger disproportionately large, sudden spikes in angular velocity ($\dot{\theta}$), particularly when the craft is not perfectly upright ($\theta \neq 0$).
7. **Side Engine Divergence Threshold:** Once angular velocity ($\dot{\theta}$) or displacement ($\theta$) exceeds a specific threshold, side engines (1 and 3) frequently cease to act as corrective forces and instead act as accelerators of angular momentum, causing rapid divergence.
8. **The Main Engine Reward Trap:** The reward signal's heavy weighting toward $\dot{y}$ stabilization creates a deceptive feedback loop; the main engine (2) can produce massive instantaneous rewards by successfully arresting descent, even while simultaneously injecting the catastrophic $\dot{\theta}$ spikes that lead to terminal instability.
9. **Critical Angular Landing Constraint:** Achieving leg contact (leg_contact=1) does not guarantee a successful landing; if the angular displacement ($\theta$) or angular velocity ($\dot{\theta}$) is outside a narrow stability window at the moment of contact, the system transitions immediately to a failure state.
10. **Kinetic Convergence of Failure:** Failure is characterized by the simultaneous accumulation of high vertical descent velocities ($\dot{y}$), high angular velocities ($\dot{\theta}$), and high angular displacement ($\theta$); at this point, the kinetic energy of the system exceeds the available thrust's ability to restore stability.

---

## 2026-07-10 05:11:40

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) is near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Main Engine-Induced Angular Spikes:** The main engine (2) acts as a primary driver of angular momentum; applying action 2 can trigger disproportionately large spikes in $\dot{\theta}$, particularly when $\theta \neq 0$.
7. **Side Engine Destabilization:** Side engines (1 and 3) can act as accelerators of angular momentum; in certain states, applying a side engine can induce massive, sudden spikes in $\dot{\theta}$ that exacerbate rotation rather than correcting it.
8. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; the main engine (2) can produce high instantaneous rewards by arresting descent while simultaneously injecting catastrophic $\dot{\theta}$ spikes.
9. **Triple-Constraint Landing Window:** A successful landing (leg_contact=1) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$). Failure to meet any one of these windows at the moment of contact results in a failure state.
10. **Kinetic Convergence of Failure:** Failure is characterized by the simultaneous accumulation of high vertical descent velocities ($\dot{y}$), high angular velocities ($\dot{\theta}$), and high angular displacement ($\theta$); at this point, the system's total kinetic energy exceeds the available thrust's ability to restore stability.

---

## 2026-07-10 05:14:21

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) is near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** Both the main engine (2) and side engines (1 and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often exacerbating existing rotation rather than correcting it.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce high instantaneous rewards by arresting descent while simultaneously injecting catastrophic $\dot{\theta}$ spikes.
8. **Deceptive Terminal Rewards:** The reward function can produce exceptionally high positive values (e.g., $>15$) during the final steps of a descent by successfully minimizing $\dot{y}$, even if the craft's orientation or contact state is insufficient for a stable landing.
9. **Triple-Constraint Landing Window:** A successful landing (leg_contact=1) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Contact-Induced Angular Instability:** The transition to a leg contact state (`leg_contact=1`) can trigger massive, sudden spikes in angular velocity ($\dot{\theta}$), potentially inducing a failure state even if the pre-contact state appeared relatively stable.

---

## 2026-07-10 05:18:36

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) is near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often exacerbating existing rotation rather than correcting it.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce high instantaneous rewards by arresting descent while simultaneously injecting catastrophic $\dot{\theta}$ spikes.
8. **Deceptive Terminal Rewards:** The reward function can produce exceptionally high positive values (e.g., $>10$) during the final steps of a descent by successfully minimizing $\dot{y}$, even if the craft's orientation or contact state is insufficient for a stable landing.
9. **Triple-Constraint Landing Window:** A successful landing (leg_contact=1) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Contact-Phase Torque Volatility:** The transition to a leg contact state (`leg_contact=1`) renders the craft hyper-sensitive to torque; side-engine actions (1 or 3) taken during the contact phase can trigger immediate, massive spikes in angular velocity ($\dot{\theta}$), even when attempting corrective maneuvers.

---

## 2026-07-10 05:22:20

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) is near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often exacerbating existing rotation rather than correcting it.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce massive instantaneous rewards (e.g., $>20$) by attempting to arrest descent, even when it injects catastrophic $\dot{\theta}$ spikes.
8. **Deceptive Terminal Rewards:** The reward function can produce exceptionally high positive values during the final steps of a descent by successfully minimizing $\dot{y}$, even if the craft's angular velocity ($\dot{\theta}$) is high or the contact state is insufficient (e.g., only one leg making contact).
9. **Triple-Constraint Landing Window:** A successful landing (leg_contact=1) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Contact-Phase Torque Volatility:** The transition to a leg contact state (`leg_contact=1`) renders the craft hyper-sensitive to torque; side-engine actions (1 or 3) taken during the contact phase can trigger immediate, massive spikes in angular velocity ($\dot{\theta}$), often leading to immediate failure.

---

## 2026-07-10 05:24:53

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) is near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce massive instantaneous rewards (e.g., $>15$) by attempting to arrest descent, even when it injects catastrophic $\dot{\theta}$ spikes.
8. **Deceptive Terminal Rewards:** The reward function can produce exceptionally high positive values during the final steps of a descent by successfully minimizing $\dot{y}$, even if the craft's angular velocity ($\dot{\theta}$) is high or the contact state is insufficient.
9. **Triple-Constraint Landing Window:** A successful landing (leg_contact=1) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Contact-Phase Torque Volatility:** The transition to a leg contact state (`leg_contact=1`) renders the craft hyper-sensitive to torque; while the main engine (2) may be used for vertical stabilization, side-engine actions (1 or 3) during contact trigger immediate, massive spikes in $\dot{\theta}$ that lead to rapid terminal failure.

---

## 2026-07-10 05:29:19

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) is near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce massive instantaneous rewards by attempting to arrest descent, even when it injects catastrophic $\dot{\theta}$ spikes.
8. **Deceptive Terminal Rewards:** The reward function can produce exceptionally high positive values during the final steps of a descent by successfully minimizing $\dot{y}$, even if the craft's angular velocity ($\dot{\theta}$) is high or the contact state is insufficient.
9. **Triple-Constraint Landing Window:** A successful landing (leg_contact=1) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Contact-Phase Rotational Instability:** The transition to a leg contact state (`leg_contact=1`) initiates a regime of extreme angular volatility; during this phase, inaction (action 0) fails to arrest $\dot{\theta}$ growth, and side-engine actions (1 or 3) often trigger massive, unrecoverable angular velocity spikes that lead to rapid terminal failure.

---

## 2026-07-10 05:31:50

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) is near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce massive instantaneous rewards by attempting to arrest descent, even when it injects catastrophic $\dot{\theta}$ spikes.
8. **Deceptive Terminal Rewards:** The reward function can produce exceptionally high positive values (e.g., >7.0) during the final steps of a descent by successfully minimizing $\dot{y}$ or managing $\theta$, immediately preceding a catastrophic terminal penalty (-100).
9. **Triple-Constraint Landing Window:** A successful landing (`leg_contact=1`) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Contact-Phase Stability Threshold:** The onset of leg contact (`leg_contact=1`) initiates a high-sensitivity regime where the terminal penalty (-100) is triggered by excessive $\dot{\theta}$ or $\theta$. During this phase, inaction (action 0) can lead to rapid $\dot{\theta}$ divergence, and side-engine actions (1 or 3) are highly likely to induce unrecoverable angular velocity spikes.

---

## 2026-07-10 05:34:25

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) is near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce massive instantaneous rewards by attempting to arrest descent, even when it injects catastrophic $\dot{\theta}$ spikes.
8. **Deceptive Terminal Rewards:** The reward function can produce exceptionally high positive values (e.g., >7.0) during the final steps of a descent by successfully minimizing $\dot{y}$ or managing $\theta$, immediately preceding a catastrophic terminal penalty (-100).
9. **Triple-Constraint Landing Window:** A successful landing (`leg_contact=1`) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Contact-Phase Reward Volatility:** The transition to $y \le 0$ and leg contact (`leg_contact=1`) initiates a high-sensitivity regime characterized by extreme reward volatility. The reward can oscillate violently between high positive values and heavy penalties as it responds to minute changes in $\theta$ and $\dot{\theta}$. During this phase, side-engine actions (1 or 3) are highly likely to trigger unrecoverable angular velocity spikes.

---

## 2026-07-10 05:38:15

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) is near zero.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce massive instantaneous rewards by attempting to arrest descent, even when it injects catastrophic $\dot{\theta}$ spikes.
8. **Extreme Deceptive Terminal Rewards:** The reward function can produce exceptionally high positive values (exceeding 10.0) during the final steps of a descent or immediately upon leg contact, masking the imminent catastrophic terminal penalty (-100) caused by a subsequent loss of angular stability.
9. **Triple-Constraint Landing Window:** A successful landing (`leg_contact=1`) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Contact-Phase Side-Engine Instability:** Once `leg_contact=1` is achieved, the application of side engines (1 or 3) acts as a high-magnitude catalyst for unrecoverable angular velocity ($\dot{\theta}$) spikes. These actions can trigger rapid, terminal rotation even if the reward signal remains temporarily positive due to vertical velocity management.

---

## 2026-07-10 05:41:31

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively low.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce massive instantaneous rewards by attempting to arrest descent, even when such actions are taken during or after leg contact.
8. **Extreme Deceptive Terminal Rewards:** The reward function can produce exceptionally high positive values (exceeding 10.0) during the final steps of a descent or immediately upon leg contact, masking the imminent catastrophic terminal penalty (-100) caused by a subsequent loss of stability.
9. **Triple-Constraint Landing Window:** A successful landing (`leg_contact=1`) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Post-Contact Side-Engine Instability:** Once `leg_contact=1` is achieved, the application of side engines (1 or 3) acts as a high-magnitude catalyst for unrecoverable angular velocity ($\dot{\theta}$) spikes, which can trigger rapid, terminal rotation even if the reward signal remains temporarily positive.

---

## 2026-07-10 05:44:13

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively low.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce massive instantaneous rewards by attempting to arrest descent, even when such actions are taken during or after leg contact.
8. **Extreme Deceptive Terminal Rewards:** The reward function can produce exceptionally high positive values (exceeding 10.0) during the final steps of a descent or immediately upon leg contact, masking the imminent catastrophic terminal penalty (-100) caused by a subsequent loss of stability.
9. **Triple-Constraint Landing Window:** A successful landing (`leg_contact=1`) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Post-Contact Stability Fragility:** Once `leg_contact=1` is achieved, the craft enters a critical state where angular velocity ($\dot{\theta}$) becomes hyper-sensitive; the application of side engines (1 or 3) or even the persistence of existing angular momentum acts as a catalyst for unrecoverable $\dot{\theta}$ spikes, triggering rapid terminal rotation.

---

## 2026-07-10 05:46:53

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively low.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce massive instantaneous rewards by attempting to arrest descent, even when such actions are taken during or after leg contact.
8. **Extreme Post-Contact Reward Deception:** The reward function can produce exceptionally high positive values (exceeding 10.0) immediately after leg contact is achieved, masking an imminent catastrophic terminal penalty (-100) caused by unrecoverable rotational instability.
9. **Triple-Constraint Landing Window:** A successful landing (`leg_contact=1`) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Post-Contact Rotational Volatility:** Once `leg_contact=1` is achieved, the craft enters a hyper-sensitive state where existing angular momentum or side-engine corrections (1 or 3) act as catalysts for unrecoverable $\dot{\theta}$ spikes, triggering rapid terminal rotation.

---

## 2026-07-10 05:47:53

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively low.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce massive instantaneous rewards by attempting to arrest descent, even when such actions are taken during or after leg contact.
8. **Extreme Post-Contact Reward Deception:** The reward function can produce exceptionally high positive values (exceeding 13.0) during or immediately after leg contact, which can mask an imminent catastrophic terminal penalty (-100) caused by unrecoverable rotational instability.
9. **Triple-Constraint Landing Window:** A successful landing (`leg_contact=1`) requires the simultaneous satisfaction of three stability constraints: low angular displacement ($\theta$), low angular velocity ($\dot{\theta}$), and low vertical velocity ($\dot{y}$).
10. **Post-Contact Rotational Volatility:** Once `leg_contact=1` is achieved, side-engine actions (1 and 3) are highly volatile and frequently act as the direct catalyst for unrecoverable $\dot{\theta}$ spikes, leading to rapid terminal rotation even when the craft appears stabilized.

---

## 2026-07-10 05:50:35

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively low.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce massive instantaneous rewards (often exceeding 13.0) by attempting to arrest descent, even when such actions fail to stabilize the craft's rotation.
8. **Extreme Post-Contact Reward Deception:** The reward function can produce exceptionally high positive values during or immediately after leg contact, which can mask an imminent catastrophic terminal penalty (-100) caused by unrecoverable rotational instability.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact (`leg_contact=1`) can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action (action 0) is taken.
10. **Post-Contact Rotational Volatility:** Once `leg_contact=1` is achieved, side-engine actions (1 and 3) are highly volatile and frequently act as the direct catalyst for escalating unrecoverable $\dot{\theta}$ spikes, leading to rapid terminal rotation.

---

## 2026-07-10 05:52:29

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively low.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce very high instantaneous rewards (e.g., >15.0) by attempting to arrest descent, even when such actions fail to stabilize the craft's rotation.
8. **Post-Contact Reward-Outcome Disparity:** Achieving leg contact (`leg_contact=1`) can trigger exceptionally high positive rewards, but these may only signify a "PARTIAL" outcome rather than a "SUCCESS," indicating that contact alone is insufficient for a successful mission.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Immediate Terminality of Unstable Contact:** If leg contact is achieved while angular velocity ($\dot{\theta}$) is high, the system can transition from high positive rewards to an immediate terminal penalty (-100) almost instantaneously, leaving no window for corrective action.

---

## 2026-07-10 05:54:05

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively low.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce high instantaneous rewards by attempting to arrest descent, even when such actions fail to stabilize the craft's rotation.
8. **Contact Maintenance Requirement:** While achieving leg contact (`leg_contact=1`) triggers high positive rewards, contact is not a permanent state; losing contact (e.g., via a "bounce") incurs significant negative penalties, even if angular stability is maintained.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Immediate Terminality of Unstable Contact:** If leg contact is achieved while angular velocity ($\dot{\theta}$) is high, the system can transition from high positive rewards to an immediate terminal penalty (-100) almost instantaneously, leaving no window for corrective action.

---

## 2026-07-10 06:01:48

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is a primary driver of failure; extreme $\dot{\theta}$ can induce a crash even when the angular displacement ($\theta$) remains relatively low.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Engine-Induced Angular Spikes:** All engine types (1, 2, and 3) can act as primary drivers of sudden, massive increases in angular velocity ($\dot{\theta}$), often overriding previous stabilization efforts and exacerbating existing rotation.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce high instantaneous rewards by attempting to arrest descent, even when such actions fail to stabilize the craft's rotation or exacerbate $\dot{\theta}$.
8. **Contact Maintenance Requirement:** While achieving leg contact (`leg_contact=1`) triggers high positive rewards, contact is not a permanent state; losing contact (e.g., via a "bounce") incurs significant negative penalties.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Contact-Phase Velocity Sensitivity:** Even after achieving stable contact, high vertical velocity ($\dot{y}$) or angular velocity ($\dot{\theta}$) can trigger severe negative rewards and induce "bouncing" (loss of leg contact), disrupting the continuous accumulation of positive contact rewards.

---

## 2026-07-10 06:02:52

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is the primary driver of failure; extreme $\dot{\theta}$ can induce an immediate terminal crash (massive negative reward) even when the craft is already in a contact state.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Side-Engine Instability Post-Contact:** Once contact is achieved (`leg_contact=1`), the use of side engines (1 and 3) becomes extremely high-risk, as they can trigger massive, uncontrolled spikes in $|\dot{\theta}|$ that lead to immediate bouncing or crashing.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce high instantaneous rewards by attempting to arrest descent, even when such actions fail to stabilize the craft's rotation or exacerbate $\dot{\theta}$.
8. **Contact Fragility and Bouncing:** Contact is a fragile state; excessive angular velocity or sudden engine-induced torque can cause the craft to "bounce" (transition from `leg_contact=1` back to `leg_contact=0`), disrupting reward accumulation.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Terminal State Thresholds:** The simulation enforces strict stability limits; exceeding critical thresholds for $|\dot{y}|$ or $|\dot{\theta}|$ triggers an immediate terminal failure, often overriding any positive rewards accumulated during the descent or contact phase.

---

## 2026-07-10 06:04:45

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance:** High angular velocity ($\dot{\theta}$) is the primary driver of failure; extreme $\dot{\theta}$ can induce an immediate terminal crash (massive negative reward, e.g., -100) even when the craft is already in a contact state.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Side-Engine Instability Post-Contact:** Once contact is achieved (`leg_contact=1`), the use of side engines (1 and 3) is extremely high-risk; while used for orientation control, they can trigger massive, rapid spikes in $|\dot{\theta}|$ that threaten to induce immediate bouncing or crashes.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce high instantaneous rewards by attempting to arrest descent, even when such actions fail to stabilize the craft's rotation or exacerbate $\dot{\theta}$.
8. **Contact Fragility and Bouncing:** Contact is a fragile state; excessive angular velocity or sudden engine-induced torque can cause the craft to "bounce" (transition from `leg_contact=1` to `leg_contact=0`), a transition often marked by a sudden reversal of vertical velocity ($\dot{y}$) from negative to positive.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Terminal State Thresholds:** The simulation enforces strict stability limits; exceeding critical thresholds for $|\dot{y}|$ or $|\dot{\theta}|$ triggers an immediate terminal failure, often overriding any positive rewards accumulated during the descent or contact phase.

---

## 2026-07-10 06:06:26

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance and Terminal Failure:** High angular velocity ($\dot{\theta}$) is the primary driver of failure; extreme $\dot{\theta}$ can induce an immediate terminal crash (massive negative reward, e.g., -100) even when the craft is already in a contact state.
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Post-Contact Engine Volatility:** Once contact is achieved (`leg_contact=1`), applying any engine thrust (1, 2, or 3) is extremely high-risk; even if the craft is grounded, engine use can trigger massive, sudden negative rewards (e.g., -10 to -20), likely due to rapid angular oscillations or ground-rebound effects.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce high instantaneous rewards by attempting to arrest descent, even when such actions fail to stabilize the craft's rotation or exacerbate $\dot{\theta}$.
8. **Contact Fragility and Bouncing:** Contact is a fragile state; excessive angular velocity or sudden engine-induced torque can cause the craft to "bounce" (transition from `leg_contact=1` to `leg_contact=0`), a transition often marked by a sudden reversal of vertical velocity ($\dot{y}$) from negative to positive.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Terminal State Thresholds:** The simulation enforces strict stability limits; exceeding critical thresholds for $|\dot{y}|$ or $|\dot{\theta}|$ triggers an immediate terminal failure, often overriding any positive rewards accumulated during the descent or contact phase.

---

## 2026-07-10 06:11:43

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance and Terminal Failure:** High angular velocity ($\dot{\theta}$) is the primary driver of failure; extreme $\dot{\theta}$ can induce an immediate terminal crash (massive negative reward) even when the craft is in a contact state (`leg_contact=1`).
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Post-Contact Engine Volatility:** Once contact is achieved (`leg_contact=1`), applying side engine thrust (1 or 3) is highly penalized and frequently triggers negative rewards, even if the craft is otherwise stable on the ground.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce high instantaneous rewards by attempting to arrest descent, even when such actions induce high $\dot{\theta}$ that leads to terminal instability.
8. **Grounded Stability via Inaction:** Once the craft achieves a landed state with low angular velocity ($\dot{\theta} \approx 0$), it can maintain a stable, high-reward state indefinitely by utilizing action 0.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Contact Configuration Transitions:** The simulation allows for transitions in contact states, such as moving from single-leg contact to dual-leg contact (`leg_contact` transitioning from `[1, 0]` or `[0, 1]` to `[1, 1]`), which is necessary for a stable landing.

---

## 2026-07-10 06:14:04

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance and Terminal Failure:** High angular velocity ($\dot{\theta}$) is the primary driver of failure; extreme $\dot{\theta}$ can induce immediate, massive terminal penalties even when the craft is in a contact state (`leg_contact=1`).
5. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Post-Contact Engine Volatility:** Once contact is achieved (`leg_contact=1`), applying side engine thrust (1 or 3) is highly penalized and frequently triggers large negative rewards, even if the craft appears otherwise stable.
7. **The Main Engine Reward Trap:** The reward signal's weighting toward $\dot{y}$ stabilization creates a deceptive loop; applying the main engine (2) can produce high instantaneous rewards by attempting to arrest descent, even when such actions induce the high $\dot{\theta}$ that leads to terminal instability.
8. **Grounded Stability via Inaction:** Once the craft achieves a landed state with low angular velocity ($\dot{\theta} \approx 0$), it can maintain a stable, high-reward state by utilizing action 0.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Contact-State Penalty Magnification:** Applying any engine thrust (1, 2, or 3) while in a contact state (`leg_contact=1`) triggers disproportionately large negative rewards (e.g., values exceeding -10.0), indicating that thrust-induced tipping or bouncing is a critical failure mode.

---

## 2026-07-10 06:16:54

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Angular Velocity Dominance and Terminal Failure:** High angular velocity ($\dot{\theta}$) is the primary driver of failure; extreme $\dot{\theta}$ can induce immediate, massive terminal penalties even when the craft is in a contact state (`leg_contact=1`).
5. **Inaction-Induced State Decay:** During descent, prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Post-Contact Side Engine Volatility:** Once contact is achieved (`leg_contact=1`), side engine thrust (1 or 3) is extremely volatile; it can either provide critical orientation stabilization or trigger massive negative rewards (often $<-10.0$) by inducing tipping or bouncing.
7. **Post-Contact Main Engine Volatility:** In a contact state, the main engine (2) is a high-risk action that can either facilitate stabilization through upward thrust or cause catastrophic bouncing and tipping with extreme negative rewards.
8. **The Inaction Stability Paradox:** While action 0 is the optimal way to maintain a stable, landed state, it becomes a failure mode if the lander enters the contact state with a significant tilt, as gravity and impact torque will cause the craft to tip over without active correction.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Contact-State Reward Sensitivity:** The reward signal in the contact state is hypersensitive to state variables; minute variations in orientation ($\theta$) and angular velocity ($\dot{\theta}$) at the moment of thrust determine whether an action results in extreme positive stabilization rewards or massive negative penalties.

---

## 2026-07-10 06:18:22

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Catastrophic Terminal Failure:** Extreme angular velocity ($\dot{\theta}$) or orientation ($\theta$) during the contact state (`leg_contact=1`) can trigger a massive terminal penalty (e.g., $-100.0$), signifying a complete crash or tip-over.
5. **Inaction-Induced State Decay:** During descent, prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Side-Engine Volatility in Contact:** Once contact is achieved, side engine thrust (1 or 3) is extremely volatile; it can provide critical orientation stabilization or trigger massive negative rewards (e.g., $<-20.0$) by inducing tipping.
7. **Main Engine Utility in Contact:** In the contact state, the main engine (2) is a high-risk/high-reward action that can facilitate significant stabilization rewards (e.g., $>10.0$) or cause catastrophic bouncing and tipping.
8. **The Inaction Stability Paradox:** While action 0 is the optimal way to maintain a stable, landed state, it becomes a failure mode if the lander enters the contact state with a significant tilt, as gravity and impact torque will cause the craft to tip over without active correction.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Contact-State Reward Bimodality:** The reward signal in the contact state is highly sensitive to state variables; minute variations in orientation ($\theta$) and angular velocity ($\dot{\theta}$) at the moment of thrust determine whether an action results in high positive stabilization rewards or massive terminal penalties.

---

## 2026-07-10 06:20:08

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Catastrophic Terminal Failure:** Extreme angular velocity ($\dot{\theta}$) or orientation ($\theta$) during the contact state (`leg_contact=1`) triggers a massive terminal penalty (e.g., $-100.0$), signifying a complete crash or tip-over.
5. **Inaction-Induced State Decay:** During descent, prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
6. **Side-Engine Volatility in Contact:** Once contact is achieved, side engine thrust (1 or 3) is extremely volatile; it can provide critical orientation stabilization (e.g., rewards $>20.0$) or trigger massive negative rewards (e.g., $<-10.0$) by inducing tipping.
7. **Main Engine Risk in Contact:** In the contact state, the main engine (2) is a high-risk/high-reward action that can facilitate significant stabilization rewards or cause catastrophic bouncing and tipping if not precisely timed with the craft's angular momentum.
8. **The Inaction Stability Paradox:** While action 0 is the optimal way to maintain a stable, landed state once equilibrium is reached, it becomes a failure mode if the lander enters the contact state with insufficient damping, as gravity and impact torque will cause the craft to tip over without active correction.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Contact-State Reward Bimodality:** The reward signal in the contact state is extremely sensitive to the precise state variables; minute variations in orientation ($\theta$) and angular velocity ($\dot{\theta}$) at the moment of thrust determine whether an action results in high positive stabilization rewards or massive terminal penalties.

---

## 2026-07-10 06:25:15

1. **Gravity-Driven Vertical Acceleration:** Gravity continuously increases the magnitude of negative vertical velocity ($\dot{y}$); if $|\dot{y}|$ exceeds a critical threshold, the descent becomes unrecoverable regardless of thrust capacity.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) tends to persist throughout the descent, and the main engine has limited capacity to attenuate existing horizontal momentum.
3. **Orientation-Dependent Side Engine Torque:** The corrective capacity of side engines (1 and 3) is coupled to the craft's orientation ($\theta$), where their ability to stabilize rotation is contingent upon whether the torque opposes or reinforces the current angular velocity ($\dot{\theta}$).
4. **Contact-State Volatility and Bouncing:** The transition to the contact state (`leg_contact=1`) is not necessarily a terminal equilibrium; incorrect thrusting can induce significant bouncing, causing the lander to lose contact (`leg_contact=0`) and enter a highly unstable, high-velocity state.
5. **High-Stakes Bimodality in Contact:** During contact, the reward signal is extremely sensitive to the precise state variables; precise thrusting can facilitate significant stabilization rewards ($>10.0$), while miscalculated actions can trigger massive negative penalties ($<-10.0$) through tipping or bouncing.
6. **Main Engine Risk in Contact:** In the contact state, the main engine (2) is a high-risk/high-reward action that can either facilitate rapid stabilization or cause catastrophic bouncing and loss of contact if not perfectly timed with the craft's angular momentum.
7. **Catastrophic Tip-Over Penalties:** Extreme angular velocity ($\dot{\theta}$) or orientation ($\theta$) during or immediately following a contact event triggers massive terminal penalties, signifying a complete crash, tip-over, or loss of control.
8. **Inaction-Induced State Decay:** During both descent and contact, prolonged periods of action 0 (nothing) cause both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for effective recovery.
9. **Impact-Induced Angular Instability:** The physical transition to leg contact can induce sudden, significant spikes in angular velocity ($\dot{\theta}$) through impact-related torque, even when no engine action is taken.
10. **Micro-State Sensitivity of Rewards:** The reward signal is hypersensitive to minute variations in $\theta$ and $\dot{\theta}$ at the moment of thrust; small deviations in these variables determine whether an action results in high stabilization rewards or massive terminal penalties.

---

## 2026-07-10 06:27:02

1. **Gravity-Driven Vertical Acceleration:** Continuous increase in the magnitude of negative vertical velocity ($\dot{y}$) is the primary driver of unrecoverable descent; exceeding a critical threshold makes landing impossible regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) is highly persistent throughout the descent, and the main engine provides minimal capacity to attenuate existing horizontal momentum.
3. **Orientation-Coupled Side Engine Torque:** The corrective capacity of side engines (1 and 3) is contingent upon whether the applied torque opposes or reinforces the current angular velocity ($\dot{\theta}$); misapplication leads to rapid angular divergence.
4. **Contact-State Volatility:** Achieving leg contact is not a terminal equilibrium; incorrect thrusting or impact can induce significant bouncing or high-velocity instability, even after contact is established.
5. **Asymmetric Contact Reward Potential:** The reward signal can be highly positive even during asymmetric contact (one leg), provided the craft's orientation ($\theta$) and angular velocity ($\dot{\theta}$) are successfully stabilized.
6. **Main Engine Risk in Contact:** The main engine (2) is a critical tool for managing vertical velocity during contact but carries a high risk of triggering catastrophic bounces or tip-overs if not perfectly synchronized with the craft's rotation.
7. **Extreme Terminal Tip-Over Penalties:** Catastrophic loss of orientation control (tip-over) results in massive terminal penalties (up to -100.0), which can occur even when both legs are in a contact state.
8. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) during both descent and contact allow both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for recovery.
9. **Impact-Induced Angular Spikes:** The physical transition to a contact state induces sudden, significant spikes in angular velocity ($\dot{\theta}$) due to impact-related torque, requiring immediate corrective action.
10. **Micro-State Reward Sensitivity:** The reward signal is hypersensitive to the interplay between the contact state and the craft's rotational state ($\theta, \dot{\theta}$); minute deviations determine whether an action results in high stabilization rewards or massive terminal penalties.

---

## 2026-07-10 06:28:43

1. **Gravity-Driven Vertical Acceleration:** Continuous increase in the magnitude of negative vertical velocity ($\dot{y}$) is the primary driver of unrecoverable descent; exceeding a critical threshold makes landing impossible regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) is highly persistent throughout the descent; side engines provide minimal capacity to attenuate existing horizontal momentum, often requiring the craft to manage descent while drifting.
3. **Orientation-Coupled Side Engine Torque:** The corrective capacity of side engines (1 and 3) is highly sensitive to the current angular velocity ($\dot{\theta}$); misapplication of side engines during a descent or contact phase leads to rapid angular divergence and immediate negative reward accumulation.
4. **Contact-State Volatility:** Achieving leg contact is not a terminal equilibrium; the transition to contact can induce significant bouncing (returning to 0.0 contact states) or high-velocity angular instability that persists after the initial impact.
5. **Asymmetric Contact Reward Potential:** The reward signal can experience massive positive spikes (e.g., Step 314, Episode 1) during the initial transition to contact, even if the craft's orientation or angular velocity is not yet fully stabilized.
6. **Main Engine Risk in Contact:** The main engine (2) is essential for managing vertical velocity during the contact phase but carries a high risk of triggering catastrophic tip-overs or bounces if applied while the craft's rotational state ($\theta, \dot{\theta}$) is uncontrolled.
7. **Extreme Terminal Tip-Over Penalties:** Catastrophic loss of orientation control (tip-over) results in massive terminal penalties (up to -100.0), which can occur even after successful leg contact has been established.
8. **Inaction-Induced State Decay:** Prolonged periods of action 0 (nothing) during both descent and contact allow both vertical velocity ($\dot{y}$) and angular instability ($\theta, \dot{\theta}$) to accumulate, rapidly narrowing the window for recovery.
9. **Impact-Induced Angular Spikes:** The physical transition to a contact state induces sudden, significant spikes in angular velocity ($\dot{\theta}$) due to impact-related torque, necessitating immediate and precise corrective thrust to prevent a tip-over.
10. **Post-Contact Rotational Dominance:** Upon leg contact, the reward landscape undergoes a fundamental phase shift; the primary driver of reward (and failure) shifts from managing vertical velocity ($\dot{y}$) to the immediate suppression of impact-induced angular velocity ($\dot{\theta}$).

---

## 2026-07-10 06:31:46

---
1. **Gravity-Driven Vertical Acceleration:** Continuous increase in the magnitude of negative vertical velocity ($\dot{y}$) is the primary driver of unrecoverable descent; exceeding a critical threshold makes landing impossible regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) is highly persistent throughout the descent; side engines provide minimal capacity to attenuate existing horizontal momentum, often requiring the craft to manage descent while drifting.
3. **Orientation-Coupled Side Engine Torque:** The corrective capacity of side engines (1 and 3) is highly sensitive to the current angular velocity ($\dot{\theta}$); misapplication of side engines during a descent or contact phase leads to rapid angular divergence and immediate negative reward accumulation.
4. **Contact-State Volatility:** Achieving leg contact is not a terminal equilibrium; the transition to contact can induce significant bouncing (returning to 0.0 contact states) or high-velocity angular instability that persists after the initial impact.
5. **Asymmetric Contact Reward Potential:** The reward signal can experience massive positive spikes during the initial transition to a contact state, even if the craft's orientation or angular velocity is not yet fully stabilized.
6. **Impact-Induced Angular Spikes:** The physical transition to a contact state induces sudden, significant spikes in angular velocity ($\dot{\theta}$) due to impact-related torque, necessitating immediate and precise corrective thrust to prevent a tip-over.
7. **Extreme Post-Contact Stability Penalties:** Once leg contact is established, the magnitude of negative rewards for engine application is significantly higher than during the descent phase, heavily penalizing thrust that fails to perfectly stabilize the craft's current state.
8. **Angle-Magnitude Scaling of Penalties:** During the contact phase, the severity of negative rewards incurred from engine actions (1, 2, or 3) scales with the absolute magnitude of the current angle ($\theta$).
9. **Main Engine Risk in Contact:** The main engine (2) is essential for managing vertical velocity during the contact phase but carries a high risk of triggering catastrophic penalties if applied while the craft's orientation ($\theta, \dot{\theta}$) is not near zero.
10. **Post-Contact Rotational Dominance:** Upon leg contact, the reward landscape undergoes a fundamental phase shift; the primary driver of reward (and failure) shifts from managing vertical velocity ($\dot{y}$) to the immediate suppression of both angular velocity ($\dot{\theta}$) and angular deviation ($\theta$).

---

## 2026-07-10 06:36:24

1. **Gravity-Driven Vertical Acceleration:** Continuous increase in the magnitude of negative vertical velocity ($\dot{y}$) is the primary driver of unrecoverable descent; exceeding a critical threshold makes landing impossible regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) is highly persistent throughout the descent; side engines provide minimal capacity to attenuate existing horizontal momentum, often requiring the craft to manage descent while drifting.
3. **Orientation-Coupled Side Engine Torque:** The corrective capacity of side engines (1 and 3) is highly sensitive to the current angular velocity ($\dot{\theta}$); misapplication of side engines during descent or contact leads to rapid angular divergence.
4. **Impact-Induced Angular Spikes:** The physical transition to a contact state induces sudden, significant spikes in angular velocity ($\dot{\theta}$) due to impact-related torque, which can immediately trigger unrecoverable rotational instability.
5. **Asymmetric Contact Reward Spikes:** The reward signal experiences massive positive spikes during the initial transition to a contact state, which can temporarily mask the immediate onset of post-impact angular divergence.
6. **Post-Contact Rotational Dominance:** Upon leg contact, the reward landscape undergoes a fundamental phase shift; the primary driver of reward (and failure) shifts from managing vertical velocity ($\dot{y}$) to the immediate suppression of both angular velocity ($\dot{\theta}$) and angular deviation ($\theta$).
7. **Extreme Post-Contact Penalty Scaling:** During the contact phase, the severity of negative rewards incurred from any engine action (1, 2, or 3) scales aggressively with the absolute magnitude of the current angle ($\theta$).
8. **Main Engine Instability Risk:** The main engine (2) carries extreme risk during the contact phase; its application can trigger massive negative rewards even when vertical velocity is near zero, likely due to torque-induced instability or orientation mismatch.
9. **Angular Divergence as Failure Driver:** In the contact phase, the primary mechanism of failure is a rapid increase in $\theta$ driven by $\dot{\theta}$ spikes; once $\theta$ deviates significantly, the resulting penalties become catastrophic and often unrecoverable.
10. **Contact-State Equilibrium Volatility:** Achieving leg contact is not a terminal equilibrium; maintaining a stable landing requires high-precision suppression of all rotational components ($\theta, \dot{\theta}$) to prevent the craft from entering a high-penalty divergent state.

---

## 2026-07-10 06:38:30

---
1. **Gravity-Driven Vertical Acceleration:** Continuous increase in the magnitude of negative vertical velocity ($\dot{y}$) is the primary driver of unrecoverable descent; exceeding a critical threshold makes landing impossible regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) is highly persistent throughout the descent; side engines provide minimal capacity to attenuate existing horizontal momentum, often requiring the craft to manage descent while drifting.
3. **Side-Engine Torque Sensitivity:** The corrective capacity of side engines (1 and 3) is highly sensitive to the current angular velocity ($\dot{\theta}$); applying side engines while the craft possesses significant angular momentum or angular deviation frequently results in immediate, substantial negative rewards.
4. **Post-Contact Reward Volatility:** Upon transitioning to a contact state, the reward landscape becomes extremely volatile; the environment produces massive positive spikes for successful contact but can immediately pivot to catastrophic negative rewards if stability is not maintained.
5. **High-Variance Main Engine Utility:** The main engine (2) serves as a high-stakes stabilization tool during the contact phase; it can provide the highest positive rewards for managing descent/orientation (e.g., Step 325, Ep 2) but also carries an extreme risk of triggering massive negative rewards if it induces torque-related instability.
6. **Penalty of Inaction during Contact:** During the contact phase, taking no action (Action 0) is often a high-penalty behavior; if the craft is not in a perfect state of rotational equilibrium, inaction leads to rapid divergence and significant negative rewards.
7. **Post-Contact Rotational Dominance:** Once leg contact is established, the primary driver of reward (and failure) shifts from managing vertical velocity ($\dot{y}$) to the immediate and continuous suppression of both angular velocity ($\dot{\theta}$) and angular deviation ($\theta$).
8. **Angular Divergence as Failure Driver:** In the contact phase, the primary mechanism of failure is a rapid increase in $\theta$ driven by $\dot{\theta}$ spikes; once $\theta$ deviates significantly, the resulting penalties become catastrophic and often unrecoverable.
9. **Orientation-Dependent Penalty Scaling:** The severity of negative rewards incurred from any engine action (1, 2, or 3) during the contact phase scales aggressively with the absolute magnitude of the current angle ($\theta$) and angular velocity ($\dot{\theta}$).
10. **Contact-State Equilibrium Fragility:** Achieving leg contact is not a terminal state but a high-entropy equilibrium; maintaining a stable landing requires constant, high-precision corrective thrust to prevent the craft from entering a high-penalty divergent state.

---

## 2026-07-10 06:41:02

---
1. **Gravity-Driven Vertical Acceleration:** Continuous increase in the magnitude of negative vertical velocity ($\dot{y}$) is the primary driver of unrecoverable descent; exceeding a critical threshold makes landing impossible regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) is highly persistent throughout the descent; side engines provide minimal capacity to attenuate existing horizontal momentum, often requiring the craft to manage descent while drifting.
3. **Side-Engine Torque Sensitivity during Descent:** The corrective capacity of side engines (1 and 3) is highly sensitive to the current angular velocity ($\dot{\theta}$); applying side engines while the craft possesses significant angular momentum or angular deviation frequently results in immediate, substantial negative rewards.
4. **Extreme Post-Contact Reward Volatility:** Upon transitioning to a contact state, the reward landscape becomes extremely volatile; the environment produces massive positive spikes (e.g., +12.0) for successful stabilization but can immediately pivot to catastrophic negative rewards (e.g., -17.0) if contact is lost or stability is breached.
5. **Main Engine Utility in Contact Stabilization:** The main engine (2) serves as the primary high-stakes tool for managing vertical velocity ($\dot{y}$) during the contact phase; it is the most frequent driver of the highest positive rewards but carries extreme risk if it induces torque-related instability.
6. **Massive Inaction Penalty during Contact:** During the contact phase, taking no action (Action 0) is a high-penalty behavior; if the craft is not in a perfect state of rotational or vertical equilibrium, inaction leads to rapid divergence and massive negative rewards (e.g., -16.5).
7. **Contact-State Variable Dominance:** Once leg contact is established, the primary driver of reward shifts from managing altitude to the immediate and continuous suppression of both angular velocity ($\dot{\theta}$) and angular deviation ($\theta$), alongside the management of vertical velocity ($\dot{y}$).
8. **Angular Divergence as a Rapid Failure Mechanism:** In the contact phase, the primary mechanism of failure is a rapid increase in $\theta$ driven by $\dot{\theta}$ spikes; once $\theta$ deviates significantly, the resulting penalties become catastrophic and often unrecoverable.
9. **Action-State Non-Linearity in Contact:** The sign and magnitude of rewards for engine actions (1, 2, or 3) during contact are non-linearly coupled to the instantaneous state; an engine action that provides massive positive rewards in one step can trigger a massive negative reward in the next if it causes a slight angular or vertical drift.
10. **Active Equilibrium Maintenance:** Achieving leg contact is not a terminal state but a high-entropy equilibrium; maintaining a stable landing requires constant, high-frequency, and high-precision corrective thrust to prevent the craft from entering a high-penalty divergent state.

---

## 2026-07-10 06:42:42

1. **Gravity-Driven Vertical Acceleration:** Continuous increase in the magnitude of negative vertical velocity ($\dot{y}$) is the primary driver of unrecoverable descent; exceeding a critical threshold makes landing impossible regardless of thrust.
2. **Horizontal Momentum Persistence:** High horizontal velocity ($x\_vel$) is highly persistent throughout the descent; side engines provide minimal capacity to attenuate existing horizontal momentum, often requiring the craft to manage descent while drifting.
3. **Side-Engine Torque Sensitivity during Descent:** The corrective capacity of side engines (1 and 3) is highly sensitive to the current angular velocity ($\dot{\theta}$); applying side engines while the craft possesses significant angular momentum or angular deviation frequently results in immediate, substantial negative rewards.
4. **Extreme Post-Contact Reward Volatility:** Upon transitioning to a contact state, the reward landscape becomes extremely volatile; the environment produces massive positive spikes for successful stabilization but can immediately pivot to catastrophic negative rewards if stability is breached.
5. **Main Engine Utility in Vertical Management:** The main engine (2) serves as the primary tool for managing vertical velocity ($\dot{y}$); it is the most frequent driver of the highest positive rewards during both the final descent and the initial contact phase.
6. **Catastrophic Inaction Penalty during Contact:** During the contact phase, taking no action (Action 0) is a terminal failure mechanism; if the craft is not in a state of perfect rotational or vertical equilibrium, inaction can trigger a massive, terminal -100 penalty.
7. **Contact-State Variable Dominance:** Once leg contact is established, the primary driver of reward shifts from managing altitude to the immediate and continuous suppression of both angular velocity ($\dot{\theta}$) and angular deviation ($\theta$), alongside the management of vertical velocity ($\dot{y}$).
8. **Angular Divergence as a Rapid Failure Mechanism:** In the contact phase, the primary mechanism of failure is a rapid increase in $\theta$ driven by $\dot{\theta}$ spikes; once $\theta$ deviates significantly, the resulting penalties become catastrophic and often unrecoverable.
9. **Action-State Non-Linearity in Contact:** The sign and magnitude of rewards for engine actions (1, 2, or 3) during contact are non-linearly coupled to the instantaneous state; an engine action that provides massive positive rewards in one step can trigger a massive negative reward in the next if it causes a slight angular or vertical drift.
10. **Dual-Path Terminal Failure:** Terminal failure is achieved through two distinct modes: a high-energy impact (crash) at the moment of contact, or a failure of active equilibrium maintenance during the post-contact stabilization phase.
