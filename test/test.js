// win : choco install k6
// mac : brew install k6
// linux : sudo apt install k6

import http from 'k6/http';
import { check } from 'k6';
import { Rate } from 'k6/metrics';

export const errorRate = new Rate('errors');

export default function () {
  const url = 'http://localhost:8000/v1/gen';
  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };
  check(http.get(url, params), {
    'status is 200': (r) => r.status == 200,
  }) || errorRate.add(1);
}
