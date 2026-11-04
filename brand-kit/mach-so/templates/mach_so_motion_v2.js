/**
 * MẠCH SỐ 2.0 — Reusable Developer Motion Suite (GSAP + HyperFrames)
 * 
 * Standardized motion primitives for high-tech vertical explainers:
 * 1. Snappy Card Reveal: cubic-bezier(0.16, 1, 0.3, 1) in 280ms
 * 2. Continuous Camera Slow-Drift: 1.0 -> 1.025x
 * 3. Token-Aware Terminal & Line Spotlight: active line scale 1.02x & mint glow, others dim 40%
 * 4. SVG Bus & Data Packet Pulse: stroke-dashoffset + packet travel + node bounce 1.06x
 * 5. Mechanical Odometer: expo.out deceleration to exact value
 * 6. Stamp Slam: mechanical stamp impact at -3deg rotation
 */

export const MACH_SO_EASINGS = {
  snappy: "cubic-bezier(0.16, 1, 0.3, 1)",
  odometer: "expo.out",
  stamp: "back.out(2.2)",
  bus: "power2.out",
  packet: "power2.inOut",
  wipe: "power3.in"
};

/**
 * Animate snappy bento card entry
 */
export function applySnappyCardReveal(target, tl, startTime = 0.2, yOffset = 35) {
  return tl.from(target, {
    scale: 0.97,
    y: yOffset,
    opacity: 0,
    duration: 0.28,
    ease: MACH_SO_EASINGS.snappy
  }, startTime);
}

/**
 * Apply continuous slow camera drift to maintain scene momentum
 */
export function applyCameraSlowDrift(cameraWrapSelector, durationSeconds, tl, startTime = 0) {
  return tl.to(cameraWrapSelector, {
    scale: 1.025,
    duration: durationSeconds,
    ease: "none"
  }, startTime);
}

/**
 * Line Spotlight: Highlight active code line and dim surrounding lines to 40%
 */
export function applyLineSpotlight(activeLineSelector, surroundingLinesSelector, tl, triggerTime) {
  tl.to(surroundingLinesSelector, {
    opacity: 0.40,
    duration: 0.35,
    ease: "power2.out"
  }, triggerTime);

  tl.to(activeLineSelector, {
    scale: 1.02,
    backgroundColor: "rgba(16, 185, 129, 0.20)",
    borderColor: "#10B981",
    duration: 0.35,
    ease: MACH_SO_EASINGS.snappy
  }, triggerTime);
}

/**
 * SVG Bus Draw & Accelerated Data Packet travel with destination node bounce
 */
export function applySvgBusAndPacket(busPathSelector, packetSelector, targetNodeSelector, tl, startTime, travelDuration = 0.45) {
  tl.to(busPathSelector, {
    strokeDashoffset: 0,
    duration: travelDuration,
    ease: MACH_SO_EASINGS.bus
  }, startTime);

  tl.set(packetSelector, { opacity: 1, y: 0 }, startTime + 0.05);
  tl.to(packetSelector, {
    y: 80,
    duration: travelDuration,
    ease: MACH_SO_EASINGS.packet
  }, startTime + 0.05);
  tl.to(packetSelector, { opacity: 0, duration: 0.1 }, startTime + travelDuration);

  // Micro-bounce reaction on destination node
  tl.to(targetNodeSelector, {
    scale: 1.06,
    duration: 0.12,
    ease: "power2.out"
  }, startTime + travelDuration);
  tl.to(targetNodeSelector, {
    scale: 1.0,
    duration: 0.18,
    ease: "power2.in"
  }, startTime + travelDuration + 0.12);
}

/**
 * Mechanical Odometer: Roll counter to target value and brake with expo.out
 */
export function applyMechanicalOdometer(counterElementId, targetNumber, duration, tl, startTime, suffix = "+") {
  const counterObj = { val: 0 };
  return tl.to(counterObj, {
    val: targetNumber,
    duration: duration,
    ease: MACH_SO_EASINGS.odometer,
    onUpdate: () => {
      const el = document.getElementById(counterElementId);
      if (el) {
        el.innerText = Math.round(counterObj.val).toLocaleString() + suffix;
      }
    }
  }, startTime);
}

/**
 * Mechanical Stamp Slam with -3deg rotation and physical overshoot
 */
export function applyStampSlam(stampSelector, tl, startTime) {
  return tl.fromTo(stampSelector, {
    opacity: 0,
    scale: 1.6,
    rotation: 12
  }, {
    opacity: 1,
    scale: 1.0,
    rotation: -3,
    duration: 0.32,
    ease: MACH_SO_EASINGS.stamp
  }, startTime);
}
