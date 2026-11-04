import React from "react";
import {
  AbsoluteFill,
  Audio,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

// ---------------------------------------------------------------------------
// Design Tokens & Constants
// ---------------------------------------------------------------------------
const BG_COLOR = "#EDE9FE"; // Pastel lavender as specified
const CARD_BG = "#0F172A"; // Dark slate card surface
const CARD_BORDER = "rgba(255, 255, 255, 0.12)";
const TEXT_DARK = "#0F172A";
const TEXT_MUTED = "#64748B";
const GREEN_ACCENT = "#10B981";
const GREEN_DARK = "#047857";

// Helper Spring
function getSpring(frame: number, fps: number, delayFrames: number = 0, damping = 15, stiffness = 120) {
  return spring({
    frame: Math.max(0, frame - delayFrames),
    fps,
    config: { damping, stiffness, mass: 0.8 },
  });
}

// ---------------------------------------------------------------------------
// SVG Icons
// ---------------------------------------------------------------------------
const CursorPointer: React.FC<{ x: number; y: number; clicking?: boolean }> = ({
  x,
  y,
  clicking = false,
}) => {
  return (
    <div
      style={{
        position: "absolute",
        left: x,
        top: y,
        pointerEvents: "none",
        zIndex: 100,
        transform: `translate(-4px, -4px) scale(${clicking ? 0.88 : 1})`,
        transition: "transform 0.08s ease",
      }}
    >
      <svg width="44" height="44" viewBox="0 0 24 24" fill="none">
        <path
          d="M5.5 3.2L18.8 11.5L12.5 13.5L16.2 20.8L13.2 22.3L9.5 15L5.5 18.8V3.2Z"
          fill="#1E293B"
          stroke="#FFFFFF"
          strokeWidth="2"
          strokeLinejoin="round"
        />
      </svg>
      {clicking && (
        <div
          style={{
            position: "absolute",
            left: 2,
            top: 2,
            width: 28,
            height: 28,
            borderRadius: "50%",
            border: "3px solid #10B981",
            animation: "pulse 0.4s ease-out forwards",
          }}
        />
      )}
    </div>
  );
};

// ---------------------------------------------------------------------------
// Subcomponents
// ---------------------------------------------------------------------------

// Global Persistent Header & Progress
const HeaderBar: React.FC<{ currentStep: number; progress: number }> = ({
  currentStep,
  progress,
}) => {
  return (
    <div
      style={{
        position: "absolute",
        top: 60,
        left: 60,
        right: 60,
        display: "flex",
        flexDirection: "column",
        gap: 16,
        zIndex: 50,
      }}
    >
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <div
          style={{
            display: "inline-flex",
            alignItems: "center",
            gap: 10,
            padding: "8px 18px",
            borderRadius: 999,
            backgroundColor: "#FFFFFF",
            boxShadow: "0 4px 16px rgba(109, 40, 217, 0.08)",
            border: "1px solid #DDD6FE",
          }}
        >
          <span style={{ fontSize: 20 }}>⚡</span>
          <span
            style={{
              fontFamily: "system-ui, -apple-system, sans-serif",
              fontSize: 22,
              fontWeight: 800,
              color: "#6D28D9",
              letterSpacing: 0.5,
            }}
          >
            SOLOPRENEUR STACK
          </span>
        </div>

        <div
          style={{
            display: "inline-flex",
            alignItems: "center",
            gap: 8,
            padding: "8px 18px",
            borderRadius: 999,
            backgroundColor: "#DCFCE7",
            border: "1.5px solid #86EFAC",
          }}
        >
          <div
            style={{
              width: 10,
              height: 10,
              borderRadius: "50%",
              backgroundColor: GREEN_ACCENT,
            }}
          />
          <span
            style={{
              fontFamily: "system-ui, -apple-system, sans-serif",
              fontSize: 22,
              fontWeight: 800,
              color: GREEN_DARK,
            }}
          >
            {currentStep === 0
              ? "$0 / MO"
              : currentStep === 5
              ? "BILL: $0"
              : `BƯỚC ${currentStep}/4`}
          </span>
        </div>
      </div>

      {/* Progress Line */}
      <div
        style={{
          width: "100%",
          height: 6,
          backgroundColor: "#DDD6FE",
          borderRadius: 4,
          overflow: "hidden",
        }}
      >
        <div
          style={{
            width: `${Math.min(100, Math.max(2, progress * 100))}%`,
            height: "100%",
            backgroundColor: "#7C3AED",
            borderRadius: 4,
            transition: "width 0.1s linear",
          }}
        />
      </div>
    </div>
  );
};

// Counter Badge (1/4, 2/4, 3/4, 4/4)
const StepPillBadge: React.FC<{
  current: number;
  total: number;
  title: string;
  accentColor: string;
}> = ({ current, total, title, accentColor }) => {
  return (
    <div
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: 14,
        padding: "12px 26px",
        borderRadius: 999,
        backgroundColor: "#FFFFFF",
        border: `2px solid ${accentColor}`,
        boxShadow: "0 8px 24px rgba(0, 0, 0, 0.06)",
        marginBottom: 24,
      }}
    >
      <div
        style={{
          padding: "4px 12px",
          borderRadius: 999,
          backgroundColor: accentColor,
          color: "#FFFFFF",
          fontFamily: "system-ui, -apple-system, sans-serif",
          fontSize: 22,
          fontWeight: 800,
        }}
      >
        {current} / {total}
      </div>
      <span
        style={{
          fontFamily: "system-ui, -apple-system, sans-serif",
          fontSize: 24,
          fontWeight: 700,
          color: "#1E293B",
          textTransform: "uppercase",
          letterSpacing: 0.5,
        }}
      >
        {title}
      </span>
    </div>
  );
};

// ---------------------------------------------------------------------------
// Scene 1: Hook ('App AI Full-stack 0đ')
// ---------------------------------------------------------------------------
const Scene1Hook: React.FC<{ frame: number; fps: number }> = ({
  frame,
  fps,
}) => {
  const enterSpring = getSpring(frame, fps, 0);
  const cardSpring = getSpring(frame, fps, 10);
  const badgeSpring = getSpring(frame, fps, 25);
  const cursorSpring = getSpring(frame, fps, 40);

  const cursorX = interpolate(cursorSpring, [0, 1], [900, 680]);
  const cursorY = interpolate(cursorSpring, [0, 1], [1400, 1150]);
  const isClicking = frame > 80 && frame < 100;

  return (
    <AbsoluteFill
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        padding: 60,
      }}
    >
      {/* Headlines */}
      <div
        style={{
          textAlign: "center",
          marginBottom: 44,
          transform: `translateY(${interpolate(enterSpring, [0, 1], [40, 0])}px)`,
          opacity: enterSpring,
        }}
      >
        <div
          style={{
            display: "inline-block",
            padding: "8px 24px",
            backgroundColor: "#EDE9FE",
            border: "2px solid #8B5CF6",
            borderRadius: 999,
            color: "#6D28D9",
            fontSize: 24,
            fontWeight: 800,
            marginBottom: 20,
            letterSpacing: 1,
          }}
        >
          DEV & SOLOPRENEUR GUIDE
        </div>
        <h1
          style={{
            fontFamily: "system-ui, -apple-system, sans-serif",
            fontSize: 72,
            fontWeight: 900,
            color: TEXT_DARK,
            margin: "0 0 12px 0",
            lineHeight: 1.15,
            letterSpacing: -1,
          }}
        >
          Tech Stack Làm App AI
        </h1>
        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            gap: 16,
          }}
        >
          <span
            style={{
              fontFamily: "system-ui, -apple-system, sans-serif",
              fontSize: 64,
              fontWeight: 900,
              color: "#4F46E5",
            }}
          >
            Full-Stack
          </span>
          <div
            style={{
              transform: `scale(${badgeSpring}) rotate(-2deg)`,
              backgroundColor: GREEN_ACCENT,
              color: "#FFFFFF",
              padding: "8px 24px",
              borderRadius: 20,
              fontSize: 54,
              fontWeight: 900,
              boxShadow: "0 10px 25px rgba(16, 185, 129, 0.4)",
            }}
          >
            $0 / THÁNG
          </div>
        </div>
      </div>

      {/* Browser Window Mockup */}
      <div
        style={{
          width: 960,
          backgroundColor: CARD_BG,
          borderRadius: 28,
          boxShadow: "0 25px 60px rgba(15, 23, 42, 0.25)",
          border: `2px solid ${CARD_BORDER}`,
          overflow: "hidden",
          transform: `scale(${interpolate(cardSpring, [0, 1], [0.92, 1])}) translateY(${interpolate(
            cardSpring,
            [0, 1],
            [60, 0]
          )}px)`,
          opacity: cardSpring,
        }}
      >
        {/* Browser Top Bar */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            padding: "20px 28px",
            borderBottom: "1px solid rgba(255, 255, 255, 0.08)",
            backgroundColor: "rgba(30, 41, 59, 0.8)",
          }}
        >
          <div style={{ display: "flex", gap: 10 }}>
            <div style={{ width: 14, height: 14, borderRadius: "50%", backgroundColor: "#EF4444" }} />
            <div style={{ width: 14, height: 14, borderRadius: "50%", backgroundColor: "#F59E0B" }} />
            <div style={{ width: 14, height: 14, borderRadius: "50%", backgroundColor: "#10B981" }} />
          </div>

          <div
            style={{
              display: "flex",
              alignItems: "center",
              gap: 8,
              backgroundColor: "rgba(15, 23, 42, 0.6)",
              padding: "8px 20px",
              borderRadius: 12,
              border: "1px solid rgba(255, 255, 255, 0.1)",
              color: "#94A3B8",
              fontFamily: "monospace",
              fontSize: 18,
            }}
          >
            <span>🔒 https://my-ai-startup.app</span>
          </div>

          <div
            style={{
              display: "inline-flex",
              alignItems: "center",
              gap: 8,
              padding: "6px 14px",
              borderRadius: 999,
              backgroundColor: "rgba(16, 185, 129, 0.2)",
              border: "1px solid #10B981",
              color: "#34D399",
              fontSize: 16,
              fontWeight: 700,
            }}
          >
            <div
              style={{
                width: 8,
                height: 8,
                borderRadius: "50%",
                backgroundColor: "#10B981",
                boxShadow: "0 0 8px #10B981",
              }}
            />
            • LIVE
          </div>
        </div>

        {/* Browser Body Mockup */}
        <div style={{ padding: "40px 48px" }}>
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              marginBottom: 28,
            }}
          >
            <div>
              <div style={{ color: "#F8FAFC", fontSize: 32, fontWeight: 800 }}>
                AI Content Engine
              </div>
              <div style={{ color: "#94A3B8", fontSize: 20, marginTop: 4 }}>
                Powered by Llama 3 & Serverless Architecture
              </div>
            </div>
            <div
              style={{
                backgroundColor: "#22C55E",
                color: "#FFFFFF",
                padding: "8px 20px",
                borderRadius: 14,
                fontSize: 20,
                fontWeight: 800,
              }}
            >
              FREE PLAN
            </div>
          </div>

          {/* Chat / Prompt Card Mockup */}
          <div
            style={{
              backgroundColor: "#1E293B",
              borderRadius: 20,
              padding: 24,
              border: "1px solid rgba(255, 255, 255, 0.08)",
              marginBottom: 24,
            }}
          >
            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: 12,
                color: "#CBD5E1",
                fontSize: 20,
                marginBottom: 16,
              }}
            >
              <span style={{ fontSize: 24 }}>✨</span>
              <span>Prompt: "Viết kịch bản video viral 30s với hook mạnh..."</span>
            </div>
            <div
              style={{
                backgroundColor: "rgba(15, 23, 42, 0.6)",
                padding: "16px 20px",
                borderRadius: 14,
                color: "#38BDF8",
                fontSize: 18,
                fontFamily: "monospace",
                lineHeight: 1.5,
              }}
            >
              {`> Response generated in 0.28s (320 tok/s via Groq)`}
              <br />
              {`> Saved to Postgres pgvector embeddings ✅`}
            </div>
          </div>

          {/* Action Row */}
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
            }}
          >
            <div style={{ display: "flex", gap: 16 }}>
              <span style={{ color: "#94A3B8", fontSize: 18 }}>
                ⚡ Cloudflare • Groq • Clerk • Neon
              </span>
            </div>
            <div
              style={{
                padding: "14px 32px",
                borderRadius: 14,
                backgroundColor: isClicking ? "#059669" : "#10B981",
                color: "#FFFFFF",
                fontSize: 22,
                fontWeight: 800,
                boxShadow: "0 8px 20px rgba(16, 185, 129, 0.3)",
                transform: `scale(${isClicking ? 0.95 : 1})`,
                transition: "transform 0.1s ease",
              }}
            >
              🚀 Launch Project
            </div>
          </div>
        </div>
      </div>

      <CursorPointer x={cursorX} y={cursorY} clicking={isClicking} />
    </AbsoluteFill>
  );
};

// ---------------------------------------------------------------------------
// Scene 2: Hosting & Frontend (Cloudflare Pages)
// ---------------------------------------------------------------------------
const Scene2Cloudflare: React.FC<{ frame: number; fps: number }> = ({
  frame,
  fps,
}) => {
  const enterSpring = getSpring(frame, fps, 0);
  const cardSpring = getSpring(frame, fps, 8);
  const itemsSpring = getSpring(frame, fps, 20);

  return (
    <AbsoluteFill
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        padding: 60,
      }}
    >
      <div
        style={{
          transform: `scale(${enterSpring})`,
          opacity: enterSpring,
        }}
      >
        <StepPillBadge
          current={1}
          total={4}
          title="Hosting & Frontend"
          accentColor="#F38020"
        />
      </div>

      {/* Main Feature Card */}
      <div
        style={{
          width: 960,
          backgroundColor: CARD_BG,
          borderRadius: 32,
          padding: 56,
          boxShadow: "0 25px 60px rgba(15, 23, 42, 0.25)",
          border: `2px solid rgba(243, 128, 32, 0.3)`,
          transform: `translateY(${interpolate(cardSpring, [0, 1], [60, 0])}px)`,
          opacity: cardSpring,
        }}
      >
        {/* Header with Cloudflare logo vibes */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            marginBottom: 44,
          }}
        >
          <div style={{ display: "flex", alignItems: "center", gap: 20 }}>
            <div
              style={{
                width: 80,
                height: 80,
                borderRadius: 24,
                backgroundColor: "rgba(243, 128, 32, 0.15)",
                border: "2px solid #F38020",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                fontSize: 44,
              }}
            >
              ☁️
            </div>
            <div>
              <div
                style={{
                  fontFamily: "system-ui, -apple-system, sans-serif",
                  fontSize: 44,
                  fontWeight: 900,
                  color: "#FFFFFF",
                }}
              >
                Cloudflare Pages
              </div>
              <div style={{ color: "#F38020", fontSize: 22, fontWeight: 700 }}>
                Next.js / Vite / React Full-Stack Edge
              </div>
            </div>
          </div>

          <div
            style={{
              padding: "10px 24px",
              borderRadius: 999,
              backgroundColor: "rgba(16, 185, 129, 0.2)",
              border: "2px solid #10B981",
              color: "#34D399",
              fontSize: 24,
              fontWeight: 900,
            }}
          >
            $0 / THÁNG
          </div>
        </div>

        {/* Big Highlight: Unlimited Bandwidth */}
        <div
          style={{
            backgroundColor: "#1E293B",
            borderRadius: 24,
            padding: "32px 36px",
            border: "1.5px solid rgba(243, 128, 32, 0.25)",
            marginBottom: 36,
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            transform: `scale(${itemsSpring})`,
            opacity: itemsSpring,
          }}
        >
          <div>
            <div
              style={{
                color: "#F38020",
                fontSize: 22,
                fontWeight: 800,
                textTransform: "uppercase",
                letterSpacing: 1,
              }}
            >
              Siêu Lợi Thế
            </div>
            <div
              style={{
                color: "#FFFFFF",
                fontSize: 38,
                fontWeight: 900,
                marginTop: 6,
              }}
            >
              Băng Thông Không Giới Hạn
            </div>
            <div style={{ color: "#94A3B8", fontSize: 20, marginTop: 6 }}>
              Không lo giật mình vì hóa đơn bandwidth vọt xà
            </div>
          </div>
          <div
            style={{
              fontSize: 72,
              fontWeight: 900,
              color: "#F38020",
              fontFamily: "sans-serif",
            }}
          >
            ∞
          </div>
        </div>

        {/* Feature Grid */}
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "1fr 1fr",
            gap: 24,
          }}
        >
          <div
            style={{
              backgroundColor: "rgba(30, 41, 59, 0.6)",
              padding: 24,
              borderRadius: 20,
              border: "1px solid rgba(255, 255, 255, 0.06)",
            }}
          >
            <div style={{ fontSize: 28, marginBottom: 8 }}>⚡ 310+ Edge Data Centers</div>
            <div style={{ color: "#94A3B8", fontSize: 18 }}>
              Tải trang siêu tốc tại Việt Nam & toàn cầu
            </div>
          </div>

          <div
            style={{
              backgroundColor: "rgba(30, 41, 59, 0.6)",
              padding: 24,
              borderRadius: 20,
              border: "1px solid rgba(255, 255, 255, 0.06)",
            }}
          >
            <div style={{ fontSize: 28, marginBottom: 8 }}>🔄 Git Deploy Tự Động</div>
            <div style={{ color: "#94A3B8", fontSize: 18 }}>
              Push code lên GitHub là preview link sẵn sàng
            </div>
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ---------------------------------------------------------------------------
// Scene 3: LLM Engine (Groq Cloud API)
// ---------------------------------------------------------------------------
const Scene3Groq: React.FC<{ frame: number; fps: number }> = ({
  frame,
  fps,
}) => {
  const enterSpring = getSpring(frame, fps, 0);
  const cardSpring = getSpring(frame, fps, 8);
  const gaugeSpring = getSpring(frame, fps, 18);

  const speedVal = Math.round(interpolate(gaugeSpring, [0, 1], [0, 320]));

  return (
    <AbsoluteFill
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        padding: 60,
      }}
    >
      <div style={{ transform: `scale(${enterSpring})`, opacity: enterSpring }}>
        <StepPillBadge
          current={2}
          total={4}
          title="LLM Engine"
          accentColor="#F55036"
        />
      </div>

      {/* Main Card */}
      <div
        style={{
          width: 960,
          backgroundColor: CARD_BG,
          borderRadius: 32,
          padding: 56,
          boxShadow: "0 25px 60px rgba(15, 23, 42, 0.25)",
          border: `2px solid rgba(245, 80, 54, 0.35)`,
          transform: `translateY(${interpolate(cardSpring, [0, 1], [60, 0])}px)`,
          opacity: cardSpring,
        }}
      >
        {/* Header */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            marginBottom: 44,
          }}
        >
          <div style={{ display: "flex", alignItems: "center", gap: 20 }}>
            <div
              style={{
                width: 80,
                height: 80,
                borderRadius: 24,
                backgroundColor: "rgba(245, 80, 54, 0.15)",
                border: "2px solid #F55036",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                fontSize: 44,
              }}
            >
              ⚡
            </div>
            <div>
              <div
                style={{
                  fontFamily: "system-ui, -apple-system, sans-serif",
                  fontSize: 44,
                  fontWeight: 900,
                  color: "#FFFFFF",
                }}
              >
                Groq Cloud API
              </div>
              <div style={{ color: "#F55036", fontSize: 22, fontWeight: 700 }}>
                LPU™ Inference Engine (Llama 3.3 70B & 8B)
              </div>
            </div>
          </div>

          <div
            style={{
              padding: "10px 24px",
              borderRadius: 999,
              backgroundColor: "rgba(16, 185, 129, 0.2)",
              border: "2px solid #10B981",
              color: "#34D399",
              fontSize: 24,
              fontWeight: 900,
            }}
          >
            $0 / THÁNG
          </div>
        </div>

        {/* Speed Gauge / Metric Box */}
        <div
          style={{
            backgroundColor: "#1E293B",
            borderRadius: 24,
            padding: "36px 40px",
            border: "1.5px solid rgba(245, 80, 54, 0.3)",
            marginBottom: 36,
            textAlign: "center",
          }}
        >
          <div
            style={{
              color: "#F55036",
              fontSize: 22,
              fontWeight: 800,
              textTransform: "uppercase",
              letterSpacing: 1.5,
              marginBottom: 8,
            }}
          >
            TỐC ĐỘ SIÊU ÂM
          </div>
          <div
            style={{
              fontFamily: "system-ui, -apple-system, sans-serif",
              fontSize: 88,
              fontWeight: 900,
              color: "#FFFFFF",
              letterSpacing: -2,
            }}
          >
            ⚡ {speedVal}{" "}
            <span style={{ fontSize: 36, color: "#F55036", fontWeight: 700 }}>
              TOKENS / GIÂY
            </span>
          </div>

          {/* Speed Bar */}
          <div
            style={{
              width: "100%",
              height: 14,
              backgroundColor: "rgba(15, 23, 42, 0.8)",
              borderRadius: 999,
              marginTop: 16,
              overflow: "hidden",
            }}
          >
            <div
              style={{
                width: `${gaugeSpring * 95}%`,
                height: "100%",
                background: "linear-gradient(90deg, #F55036, #FF9B26)",
                borderRadius: 999,
              }}
            />
          </div>
        </div>

        {/* Specs */}
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "1fr 1fr",
            gap: 24,
          }}
        >
          <div
            style={{
              backgroundColor: "rgba(30, 41, 59, 0.6)",
              padding: 24,
              borderRadius: 20,
              border: "1px solid rgba(255, 255, 255, 0.06)",
            }}
          >
            <div style={{ fontSize: 24, fontWeight: 800, color: "#FFFFFF", marginBottom: 6 }}>
              🎁 14,400 Requests / ngày
            </div>
            <div style={{ color: "#94A3B8", fontSize: 18 }}>
              Free tier cực kỳ hào phóng cho mọi MVP
            </div>
          </div>

          <div
            style={{
              backgroundColor: "rgba(30, 41, 59, 0.6)",
              padding: 24,
              borderRadius: 20,
              border: "1px solid rgba(255, 255, 255, 0.06)",
            }}
          >
            <div style={{ fontSize: 24, fontWeight: 800, color: "#FFFFFF", marginBottom: 6 }}>
              ⏱️ Time to First Token 0.15s
            </div>
            <div style={{ color: "#94A3B8", fontSize: 18 }}>
              Phản hồi tức thì như nói chuyện trực tiếp
            </div>
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ---------------------------------------------------------------------------
// Scene 4: Authentication (Clerk)
// ---------------------------------------------------------------------------
const Scene4Clerk: React.FC<{ frame: number; fps: number }> = ({
  frame,
  fps,
}) => {
  const enterSpring = getSpring(frame, fps, 0);
  const cardSpring = getSpring(frame, fps, 8);
  const cursorSpring = getSpring(frame, fps, 30);

  const cursorX = interpolate(cursorSpring, [0, 1], [850, 540]);
  const cursorY = interpolate(cursorSpring, [0, 1], [1300, 1020]);
  const isClicking = frame > 65 && frame < 90;
  const isAuthed = frame >= 85;

  return (
    <AbsoluteFill
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        padding: 60,
      }}
    >
      <div style={{ transform: `scale(${enterSpring})`, opacity: enterSpring }}>
        <StepPillBadge
          current={3}
          total={4}
          title="User Authentication"
          accentColor="#6C47FF"
        />
      </div>

      {/* Main Modal Card */}
      <div
        style={{
          width: 860,
          backgroundColor: CARD_BG,
          borderRadius: 32,
          padding: 52,
          boxShadow: "0 25px 60px rgba(15, 23, 42, 0.25)",
          border: `2px solid rgba(108, 71, 255, 0.35)`,
          transform: `translateY(${interpolate(cardSpring, [0, 1], [60, 0])}px)`,
          opacity: cardSpring,
        }}
      >
        {/* Header */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            marginBottom: 36,
          }}
        >
          <div style={{ display: "flex", alignItems: "center", gap: 20 }}>
            <div
              style={{
                width: 76,
                height: 76,
                borderRadius: 22,
                backgroundColor: "rgba(108, 71, 255, 0.15)",
                border: "2px solid #6C47FF",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                fontSize: 40,
              }}
            >
              🔐
            </div>
            <div>
              <div
                style={{
                  fontFamily: "system-ui, -apple-system, sans-serif",
                  fontSize: 42,
                  fontWeight: 900,
                  color: "#FFFFFF",
                }}
              >
                Clerk Auth
              </div>
              <div style={{ color: "#A78BFA", fontSize: 22, fontWeight: 700 }}>
                10,000 Monthly Active Users Free
              </div>
            </div>
          </div>

          <div
            style={{
              padding: "10px 24px",
              borderRadius: 999,
              backgroundColor: "rgba(16, 185, 129, 0.2)",
              border: "2px solid #10B981",
              color: "#34D399",
              fontSize: 24,
              fontWeight: 900,
            }}
          >
            $0 / THÁNG
          </div>
        </div>

        {/* Modal UI Mockup */}
        <div
          style={{
            backgroundColor: "#18181B",
            borderRadius: 24,
            padding: 36,
            border: "1px solid rgba(255, 255, 255, 0.1)",
          }}
        >
          <div style={{ textAlign: "center", marginBottom: 28 }}>
            <div style={{ color: "#FFFFFF", fontSize: 28, fontWeight: 800 }}>
              Đăng nhập vào AI App
            </div>
            <div style={{ color: "#71717A", fontSize: 18, marginTop: 4 }}>
              Setup trong 5 phút với Next.js SDK
            </div>
          </div>

          {/* Social Buttons */}
          <div style={{ display: "flex", flexDirection: "column", gap: 16 }}>
            {/* Google Button */}
            <div
              style={{
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                gap: 16,
                padding: "18px 24px",
                borderRadius: 16,
                backgroundColor: isClicking
                  ? "#2563EB"
                  : isAuthed
                  ? "#059669"
                  : "#27272A",
                border: isAuthed ? "2px solid #10B981" : "1px solid #3F3F46",
                color: "#FFFFFF",
                fontSize: 22,
                fontWeight: 700,
                transform: `scale(${isClicking ? 0.96 : 1})`,
                transition: "all 0.1s ease",
              }}
            >
              {isAuthed ? (
                <>
                  <span style={{ fontSize: 26 }}>✅</span>
                  <span>Đã xác thực thành công (Google OAuth)</span>
                </>
              ) : (
                <>
                  <span style={{ fontSize: 24 }}>🇬</span>
                  <span>Tiếp tục với tài khoản Google</span>
                </>
              )}
            </div>

            {/* GitHub Button */}
            <div
              style={{
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                gap: 16,
                padding: "18px 24px",
                borderRadius: 16,
                backgroundColor: "#27272A",
                border: "1px solid #3F3F46",
                color: "#FFFFFF",
                fontSize: 22,
                fontWeight: 700,
              }}
            >
              <span style={{ fontSize: 24 }}>🐙</span>
              <span>Tiếp tục với GitHub</span>
            </div>
          </div>
        </div>
      </div>

      <CursorPointer x={cursorX} y={cursorY} clicking={isClicking} />
    </AbsoluteFill>
  );
};

// ---------------------------------------------------------------------------
// Scene 5: Database (Neon Serverless Postgres)
// ---------------------------------------------------------------------------
const Scene5Neon: React.FC<{ frame: number; fps: number }> = ({
  frame,
  fps,
}) => {
  const enterSpring = getSpring(frame, fps, 0);
  const cardSpring = getSpring(frame, fps, 8);
  const codeSpring = getSpring(frame, fps, 20);

  return (
    <AbsoluteFill
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        padding: 60,
      }}
    >
      <div style={{ transform: `scale(${enterSpring})`, opacity: enterSpring }}>
        <StepPillBadge
          current={4}
          total={4}
          title="Vector Database & Storage"
          accentColor="#00E599"
        />
      </div>

      {/* Main Card */}
      <div
        style={{
          width: 960,
          backgroundColor: CARD_BG,
          borderRadius: 32,
          padding: 56,
          boxShadow: "0 25px 60px rgba(15, 23, 42, 0.25)",
          border: `2px solid rgba(0, 229, 153, 0.35)`,
          transform: `translateY(${interpolate(cardSpring, [0, 1], [60, 0])}px)`,
          opacity: cardSpring,
        }}
      >
        {/* Header */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            marginBottom: 36,
          }}
        >
          <div style={{ display: "flex", alignItems: "center", gap: 20 }}>
            <div
              style={{
                width: 80,
                height: 80,
                borderRadius: 24,
                backgroundColor: "rgba(0, 229, 153, 0.15)",
                border: "2px solid #00E599",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                fontSize: 44,
              }}
            >
              🐘
            </div>
            <div>
              <div
                style={{
                  fontFamily: "system-ui, -apple-system, sans-serif",
                  fontSize: 44,
                  fontWeight: 900,
                  color: "#FFFFFF",
                }}
              >
                Neon Postgres
              </div>
              <div style={{ color: "#00E599", fontSize: 22, fontWeight: 700 }}>
                Serverless Postgres + pgvector tích hợp sẵn
              </div>
            </div>
          </div>

          <div
            style={{
              padding: "10px 24px",
              borderRadius: 999,
              backgroundColor: "rgba(16, 185, 129, 0.2)",
              border: "2px solid #10B981",
              color: "#34D399",
              fontSize: 24,
              fontWeight: 900,
            }}
          >
            $0 / THÁNG
          </div>
        </div>

        {/* Code / Terminal Snippet */}
        <div
          style={{
            backgroundColor: "#0A0F1D",
            borderRadius: 20,
            padding: "24px 28px",
            border: "1px solid rgba(0, 229, 153, 0.2)",
            marginBottom: 32,
            fontFamily: "monospace",
            fontSize: 20,
            color: "#A7F3D0",
            lineHeight: 1.6,
            transform: `scale(${codeSpring})`,
            opacity: codeSpring,
          }}
        >
          <div style={{ color: "#64748B", marginBottom: 8 }}>-- RAG & Vector Search trực tiếp trong Postgres</div>
          <div><span style={{ color: "#F472B6" }}>CREATE EXTENSION IF NOT EXISTS</span> vector;</div>
          <div><span style={{ color: "#60A5FA" }}>SELECT</span> id, title, cosine_distance(embedding, $query)</div>
          <div><span style={{ color: "#60A5FA" }}>FROM</span> documents <span style={{ color: "#60A5FA" }}>ORDER BY</span> 3 <span style={{ color: "#F472B6" }}>LIMIT</span> 5;</div>
        </div>

        {/* Features */}
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "1fr 1fr",
            gap: 20,
          }}
        >
          <div
            style={{
              backgroundColor: "rgba(30, 41, 59, 0.6)",
              padding: 22,
              borderRadius: 18,
              border: "1px solid rgba(255, 255, 255, 0.06)",
            }}
          >
            <div style={{ fontSize: 22, fontWeight: 800, color: "#FFFFFF", marginBottom: 4 }}>
              💤 Auto Scale to Zero
            </div>
            <div style={{ color: "#94A3B8", fontSize: 17 }}>
              Khi không có traffic, DB tự ngủ → Tiết kiệm $0 hoàn hảo
            </div>
          </div>

          <div
            style={{
              backgroundColor: "rgba(30, 41, 59, 0.6)",
              padding: 22,
              borderRadius: 18,
              border: "1px solid rgba(255, 255, 255, 0.06)",
            }}
          >
            <div style={{ fontSize: 22, fontWeight: 800, color: "#FFFFFF", marginBottom: 4 }}>
              🌿 Database Branching
            </div>
            <div style={{ color: "#94A3B8", fontSize: 17 }}>
              Tạo nhánh DB thử nghiệm ngay tức thì như Git branch
            </div>
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ---------------------------------------------------------------------------
// Scene 6: Outro & Payoff (10,000 Users, Bill: $0)
// ---------------------------------------------------------------------------
const Scene6Outro: React.FC<{ frame: number; fps: number }> = ({
  frame,
  fps,
}) => {
  const enterSpring = getSpring(frame, fps, 0);
  const counterSpring = getSpring(frame, fps, 10);
  const billSpring = getSpring(frame, fps, 25);
  const pulseScale = 1 + Math.sin(frame * 0.15) * 0.03;

  const usersCount = Math.round(
    interpolate(counterSpring, [0, 1], [0, 10000])
  ).toLocaleString("en-US");

  return (
    <AbsoluteFill
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        padding: 60,
      }}
    >
      {/* Metric Badge */}
      <div
        style={{
          textAlign: "center",
          marginBottom: 32,
          transform: `translateY(${interpolate(enterSpring, [0, 1], [40, 0])}px)`,
          opacity: enterSpring,
        }}
      >
        <div
          style={{
            fontSize: 24,
            fontWeight: 800,
            color: "#6D28D9",
            textTransform: "uppercase",
            letterSpacing: 1.5,
            marginBottom: 8,
          }}
        >
          KẾT QUẢ THỰC TẾ
        </div>
        <div
          style={{
            fontFamily: "system-ui, -apple-system, sans-serif",
            fontSize: 84,
            fontWeight: 900,
            color: TEXT_DARK,
            letterSpacing: -2,
          }}
        >
          🚀 {usersCount} <span style={{ fontSize: 44, color: "#7C3AED" }}>USERS</span>
        </div>
      </div>

      {/* Invoice Card */}
      <div
        style={{
          width: 920,
          backgroundColor: CARD_BG,
          borderRadius: 32,
          padding: "48px 56px",
          boxShadow: "0 30px 70px rgba(15, 23, 42, 0.3)",
          border: `2px solid rgba(16, 185, 129, 0.4)`,
          transform: `scale(${interpolate(billSpring, [0, 1], [0.92, 1])})`,
          opacity: billSpring,
        }}
      >
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            paddingBottom: 24,
            borderBottom: "1px dashed rgba(255, 255, 255, 0.15)",
            marginBottom: 24,
          }}
        >
          <div style={{ color: "#F8FAFC", fontSize: 28, fontWeight: 800 }}>
            HÓA ĐƠN HÀNG THÁNG
          </div>
          <div
            style={{
              padding: "6px 16px",
              borderRadius: 8,
              backgroundColor: "rgba(16, 185, 129, 0.2)",
              color: "#34D399",
              fontSize: 18,
              fontWeight: 800,
            }}
          >
            STATUS: PAID ($0.00)
          </div>
        </div>

        {/* Itemized List */}
        <div style={{ display: "flex", flexDirection: "column", gap: 16 }}>
          <div style={{ display: "flex", justifyContent: "space-between", fontSize: 22, color: "#CBD5E1" }}>
            <span>☁️ Cloudflare Pages (Frontend & Edge)</span>
            <span style={{ fontWeight: 800, color: "#34D399" }}>$0.00</span>
          </div>
          <div style={{ display: "flex", justifyContent: "space-between", fontSize: 22, color: "#CBD5E1" }}>
            <span>⚡ Groq Cloud (Llama 3 Inference)</span>
            <span style={{ fontWeight: 800, color: "#34D399" }}>$0.00</span>
          </div>
          <div style={{ display: "flex", justifyContent: "space-between", fontSize: 22, color: "#CBD5E1" }}>
            <span>🔐 Clerk Authentication (10k MAU)</span>
            <span style={{ fontWeight: 800, color: "#34D399" }}>$0.00</span>
          </div>
          <div style={{ display: "flex", justifyContent: "space-between", fontSize: 22, color: "#CBD5E1" }}>
            <span>🐘 Neon Postgres (Serverless DB + Vector)</span>
            <span style={{ fontWeight: 800, color: "#34D399" }}>$0.00</span>
          </div>
        </div>

        {/* Total Payoff */}
        <div
          style={{
            marginTop: 32,
            paddingTop: 24,
            borderTop: "2px solid rgba(255, 255, 255, 0.12)",
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
          }}
        >
          <div>
            <div style={{ color: "#94A3B8", fontSize: 20 }}>TỔNG CHI PHÍ THỰC TẾ</div>
            <div style={{ color: "#FFFFFF", fontSize: 32, fontWeight: 900 }}>BILL CUỐI THÁNG</div>
          </div>
          <div
            style={{
              padding: "16px 36px",
              borderRadius: 20,
              backgroundColor: GREEN_ACCENT,
              color: "#FFFFFF",
              fontSize: 48,
              fontWeight: 900,
              boxShadow: "0 10px 30px rgba(16, 185, 129, 0.4)",
              transform: `scale(${pulseScale})`,
            }}
          >
            $0 / THÁNG
          </div>
        </div>
      </div>

      {/* Call to action */}
      <div
        style={{
          marginTop: 36,
          textAlign: "center",
          color: "#475569",
          fontSize: 24,
          fontWeight: 700,
        }}
      >
        🚀 Bắt đầu build app AI của bạn ngay hôm nay!
      </div>
    </AbsoluteFill>
  );
};

// ---------------------------------------------------------------------------
// Main AiStackZeroDollar Composition
// ---------------------------------------------------------------------------
export const AiStackZeroDollar: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  // Scene timing markers (frame boundaries)
  // Total: 1122 frames (~37.4s)
  const SCENE_1_END = 165;  // 0 - 165 (5.5s)
  const SCENE_2_END = 355;  // 165 - 355 (6.3s)
  const SCENE_3_END = 545;  // 355 - 545 (6.3s)
  const SCENE_4_END = 735;  // 545 - 735 (6.3s)
  const SCENE_5_END = 925;  // 735 - 925 (6.3s)
  // Scene 6: 925 - 1122 (6.5s)

  let currentStep = 0;
  if (frame >= SCENE_1_END && frame < SCENE_2_END) currentStep = 1;
  else if (frame >= SCENE_2_END && frame < SCENE_3_END) currentStep = 2;
  else if (frame >= SCENE_3_END && frame < SCENE_4_END) currentStep = 3;
  else if (frame >= SCENE_4_END && frame < SCENE_5_END) currentStep = 4;
  else if (frame >= SCENE_5_END) currentStep = 5;

  const progress = frame / durationInFrames;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: BG_COLOR,
        // Dot grid background texture
        backgroundImage: "radial-gradient(#CBD5E1 2px, transparent 2px)",
        backgroundSize: "32px 32px",
        overflow: "hidden",
        fontFamily: "system-ui, -apple-system, sans-serif",
      }}
    >
      {/* Background Audio */}
      <Audio src={staticFile("ai-stack-audio.mp3")} volume={1} />

      {/* Top persistent header */}
      <HeaderBar currentStep={currentStep} progress={progress} />

      {/* Scene Layers */}
      {frame < SCENE_1_END && (
        <Scene1Hook frame={frame} fps={fps} />
      )}

      {frame >= SCENE_1_END && frame < SCENE_2_END && (
        <Scene2Cloudflare frame={frame - SCENE_1_END} fps={fps} />
      )}

      {frame >= SCENE_2_END && frame < SCENE_3_END && (
        <Scene3Groq frame={frame - SCENE_2_END} fps={fps} />
      )}

      {frame >= SCENE_3_END && frame < SCENE_4_END && (
        <Scene4Clerk frame={frame - SCENE_3_END} fps={fps} />
      )}

      {frame >= SCENE_4_END && frame < SCENE_5_END && (
        <Scene5Neon frame={frame - SCENE_4_END} fps={fps} />
      )}

      {frame >= SCENE_5_END && (
        <Scene6Outro frame={frame - SCENE_5_END} fps={fps} />
      )}
    </AbsoluteFill>
  );
};
