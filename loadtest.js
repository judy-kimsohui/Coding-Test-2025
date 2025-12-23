import http from "k6/http";
import { sleep, check } from "k6";

export const options = {
  stages: [
    { duration: "30s", target: 20 },  // 20명
    { duration: "30s", target: 50 },  // 50명
    { duration: "30s", target: 100 }, // 100명
    { duration: "30s", target: 0 },   // 내려오기
  ],
  thresholds: {
    http_req_failed: ["rate<0.01"],   // 실패율 1% 미만
    http_req_duration: ["p(95)<1000"] // 95%가 1초 이내
  }
};

export default function () {
  const url = "https://mtris.site//"; 
// const url = "https://mtris.site/api/ranks";
  const res = http.get(url, { timeout: "10s" });

  check(res, {
    "status is 200": (r) => r.status === 200,
  });

  sleep(0.2);
}
