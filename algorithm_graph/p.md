당신은 좌표 (-10, A) 에서 (10, B)로 가려고 한다. 좌표는 키로미터 단위이며, 당신의 보트는 시간 당 1키로미터의 속도로 일정하게 간다. 당신은 보트가 이동하는 경로를 완전히 제어 할 수 있습니다. 보트를 하나의 점으로 생각하기로 하겠습니다.

영역 안에는 N개의 섬이 있습니다. 우리는 각 섬을 하나의 점으로 생각하기로 하겠습니다. i번째 섬의 좌표는 (0, Ci) 입니다.

영역은 방사능으로 오염되었습니다. 당신은 영역 내의 어디에 존재하건 매시간마다 일정하게 1 microsievert 의 방사능을 받게 됩니다. 거기에 더해서, 섬들 또한 방사능으로 오염이 되어 i번째 섬에서는 매 시간당 (Di)-2microsieverts의 방사능을 추가적으로 얻게 됩니다. Di는 당신으로부터 i번째 섬의 거리(키로미터)를 의미합니다. (Formally: let Di(t) be your distance from the i-th island as a function of time t, and X be the total time your journey takes. Then the total radiation received from the i-th island is the definite integral from 0 to X of Di(t)-2.) 당신은 섬에 얼마든지 근접할 수 있지만 도달할 수는 없습니다.

만약 당신이 -10에서 10으로 갈 때 얻게되는 최소 방사선 량을 구하시오.