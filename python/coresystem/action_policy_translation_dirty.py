#!/usr/bin/env python3

action_policy_translation = ( 7, 31, 56, 81, 106, 131, 156, 180, 204, 230, 259, 288,
317, 346, 374, 400, 425, 453, 485, 518, 551, 584, 615, 642,
667, 695, 727, 761, 796, 830, 861, 888, 913, 941, 973, 1007,
1042, 1076, 1107, 1134, 1159, 1187, 1219, 1252, 1285, 1318, 1349, 1376,
1401, 1428, 1457, 1486, 1515, 1544, 1572, 1597, -1, -1, -1, -1,
-1, -1, -1, -1, 10, 35, 61, 86, 111, 136, 160, 183,
207, 234, 264, 293, 322, 351, 378, 403, 428, 457, 490, 523,
556, 589, 619, 645, 670, 699, 732, 766, 801, 835, 865, 891,
916, 945, 978, 1012, 1047, 1081, 1111, 1137, 1162, 1191, 1224, 1257,
1290, 1323, 1353, 1379, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, 13, 38, 64, 90,
115, 140, 163, 185, 210, 237, 267, 297, 326, 355, 381, 405,
431, 460, 493, 527, 560, 593, 622, 647, 673, 702, 735, 770,
805, 839, 868, 893, 919, 948, 981, 1016, 1051, 1085, 1114, 1139,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
15, 40, 66, 92, 118, 142, 165, 187, 212, 239, 269, 299,
329, 357, 383, 407, 433, 462, 495, 529, 563, 595, 624, 649,
675, 704, 737, 772, 808, 841, 870, 895, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, 17, 42, 68, 94, 119, 144, 167, 189,
214, 241, 271, 301, 330, 359, 385, 409, 435, 464, 497, 531,
564, 597, 626, 651, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, 19, 44, 70, 95,
120, 145, 169, 191, 216, 243, 273, 302, 331, 360, 387, 411,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
21, 46, 71, 96, 121, 146, 170, 193, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, 8, 32, 57, 82, 107, 132, 157, -1,
205, 231, 260, 289, 318, 347, 375, -1, 426, 454, 486, 519,
552, 585, 616, -1, 668, 696, 728, 762, 797, 831, 862, -1,
914, 942, 974, 1008, 1043, 1077, 1108, -1, 1160, 1188, 1220, 1253,
1286, 1319, 1350, -1, 1402, 1429, 1458, 1487, 1516, 1545, 1573, -1,
-1, -1, -1, -1, -1, -1, -1, -1, 12, 37, 63, 88,
113, 138, -1, -1, 209, 236, 266, 295, 324, 353, -1, -1,
430, 459, 492, 525, 558, 591, -1, -1, 672, 701, 734, 768,
803, 837, -1, -1, 918, 947, 980, 1014, 1049, 1083, -1, -1,
1164, 1193, 1226, 1259, 1292, 1325, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
14, 39, 65, 91, 116, -1, -1, -1, 211, 238, 268, 298,
327, -1, -1, -1, 432, 461, 494, 528, 561, -1, -1, -1,
674, 703, 736, 771, 806, -1, -1, -1, 920, 949, 982, 1017,
1052, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, 16, 41, 67, 93, -1, -1, -1, -1,
213, 240, 270, 300, -1, -1, -1, -1, 434, 463, 496, 530,
-1, -1, -1, -1, 676, 705, 738, 773, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, 18, 43, 69, -1,
-1, -1, -1, -1, 215, 242, 272, -1, -1, -1, -1, -1,
436, 465, 498, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
20, 45, -1, -1, -1, -1, -1, -1, 217, 244, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, 22, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, 0, 24, 49, 75,
101, 127, 153, -1, 197, 223, 252, 282, 312, 342, 371, -1,
418, 446, 478, 512, 546, 580, 612, -1, 660, 688, 720, 755,
791, 826, 858, -1, 906, 934, 966, 1001, 1037, 1072, 1104, -1,
1152, 1180, 1212, 1246, 1280, 1314, 1346, -1, 1394, 1421, 1450, 1480,
1510, 1540, 1569, -1, 1614, 1639, 1665, 1691, 1717, 1743, 1768, -1,
1, 25, 50, 76, 102, 128, -1, -1, 198, 224, 253, 283,
313, 343, -1, -1, 419, 447, 479, 513, 547, 581, -1, -1,
661, 689, 721, 756, 792, 827, -1, -1, 907, 935, 967, 1002,
1038, 1073, -1, -1, 1153, 1181, 1213, 1247, 1281, 1315, -1, -1,
1395, 1422, 1451, 1481, 1511, 1541, -1, -1, 1615, 1640, 1666, 1692,
1718, 1744, -1, -1, 2, 26, 51, 77, 103, -1, -1, -1,
199, 225, 254, 284, 314, -1, -1, -1, 420, 448, 480, 514,
548, -1, -1, -1, 662, 690, 722, 757, 793, -1, -1, -1,
908, 936, 968, 1003, 1039, -1, -1, -1, 1154, 1182, 1214, 1248,
1282, -1, -1, -1, 1396, 1423, 1452, 1482, 1512, -1, -1, -1,
1616, 1641, 1667, 1693, 1719, -1, -1, -1, 3, 27, 52, 78,
-1, -1, -1, -1, 200, 226, 255, 285, -1, -1, -1, -1,
421, 449, 481, 515, -1, -1, -1, -1, 663, 691, 723, 758,
-1, -1, -1, -1, 909, 937, 969, 1004, -1, -1, -1, -1,
1155, 1183, 1215, 1249, -1, -1, -1, -1, 1397, 1424, 1453, 1483,
-1, -1, -1, -1, 1617, 1642, 1668, 1694, -1, -1, -1, -1,
4, 28, 53, -1, -1, -1, -1, -1, 201, 227, 256, -1,
-1, -1, -1, -1, 422, 450, 482, -1, -1, -1, -1, -1,
664, 692, 724, -1, -1, -1, -1, -1, 910, 938, 970, -1,
-1, -1, -1, -1, 1156, 1184, 1216, -1, -1, -1, -1, -1,
1398, 1425, 1454, -1, -1, -1, -1, -1, 1618, 1643, 1669, -1,
-1, -1, -1, -1, 5, 29, -1, -1, -1, -1, -1, -1,
202, 228, -1, -1, -1, -1, -1, -1, 423, 451, -1, -1,
-1, -1, -1, -1, 665, 693, -1, -1, -1, -1, -1, -1,
911, 939, -1, -1, -1, -1, -1, -1, 1157, 1185, -1, -1,
-1, -1, -1, -1, 1399, 1426, -1, -1, -1, -1, -1, -1,
1619, 1644, -1, -1, -1, -1, -1, -1, 6, -1, -1, -1,
-1, -1, -1, -1, 203, -1, -1, -1, -1, -1, -1, -1,
424, -1, -1, -1, -1, -1, -1, -1, 666, -1, -1, -1,
-1, -1, -1, -1, 912, -1, -1, -1, -1, -1, -1, -1,
1158, -1, -1, -1, -1, -1, -1, -1, 1400, -1, -1, -1,
-1, -1, -1, -1, 1620, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, 195, 220, 248, 277,
306, 335, 364, -1, 416, 443, 474, 507, 540, 573, 605, -1,
658, 685, 716, 750, 785, 819, 851, -1, 904, 931, 962, 996,
1031, 1065, 1097, -1, 1150, 1177, 1208, 1241, 1274, 1307, 1339, -1,
1392, 1418, 1446, 1475, 1504, 1533, 1562, -1, 1612, 1636, 1661, 1686,
1711, 1736, 1761, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, 414, 440, 470, 503,
536, 569, -1, -1, 656, 682, 712, 746, 781, 815, -1, -1,
902, 928, 958, 992, 1027, 1061, -1, -1, 1148, 1174, 1204, 1237,
1270, 1303, -1, -1, 1390, 1415, 1442, 1471, 1500, 1529, -1, -1,
1610, 1633, 1657, 1682, 1707, 1732, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, 653, 678, 707, 741,
776, -1, -1, -1, 899, 924, 953, 987, 1022, -1, -1, -1,
1145, 1170, 1199, 1232, 1265, -1, -1, -1, 1387, 1411, 1437, 1466,
1495, -1, -1, -1, 1607, 1629, 1652, 1677, 1702, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, 897, 922, 951, 984,
-1, -1, -1, -1, 1143, 1168, 1197, 1229, -1, -1, -1, -1,
1385, 1409, 1435, 1463, -1, -1, -1, -1, 1605, 1627, 1650, 1674,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, 1141, 1166, 1195, -1,
-1, -1, -1, -1, 1383, 1407, 1433, -1, -1, -1, -1, -1,
1603, 1625, 1648, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, 1381, 1405, -1, -1,
-1, -1, -1, -1, 1601, 1623, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, 1599, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
194, 219, 247, 276, 305, 334, 363, 390, 415, 442, 473, 506,
539, 572, 604, 632, 657, 684, 715, 749, 784, 818, 850, 878,
903, 930, 961, 995, 1030, 1064, 1096, 1124, 1149, 1176, 1207, 1240,
1273, 1306, 1338, 1366, 1391, 1417, 1445, 1474, 1503, 1532, 1561, 1587,
1611, 1635, 1660, 1685, 1710, 1735, 1760, 1784, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
412, 438, 468, 501, 534, 567, 600, 629, 654, 680, 710, 744,
779, 813, 846, 875, 900, 926, 956, 990, 1025, 1059, 1092, 1121,
1146, 1172, 1202, 1235, 1268, 1301, 1334, 1363, 1388, 1413, 1440, 1469,
1498, 1527, 1557, 1584, 1608, 1631, 1655, 1680, 1705, 1730, 1756, 1781,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
652, 677, 706, 740, 775, 810, 843, 872, 898, 923, 952, 986,
1021, 1056, 1089, 1118, 1144, 1169, 1198, 1231, 1264, 1298, 1331, 1360,
1386, 1410, 1436, 1465, 1494, 1524, 1554, 1581, 1606, 1628, 1651, 1676,
1701, 1727, 1753, 1778, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
896, 921, 950, 983, 1019, 1054, 1087, 1116, 1142, 1167, 1196, 1228,
1262, 1296, 1329, 1358, 1384, 1408, 1434, 1462, 1492, 1522, 1552, 1579,
1604, 1626, 1649, 1673, 1699, 1725, 1751, 1776, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
1140, 1165, 1194, 1227, 1260, 1294, 1327, 1356, 1382, 1406, 1432, 1461,
1490, 1520, 1550, 1577, 1602, 1624, 1647, 1672, 1697, 1723, 1749, 1774,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
1380, 1404, 1431, 1460, 1489, 1518, 1548, 1575, 1600, 1622, 1646, 1671,
1696, 1721, 1747, 1772, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
1598, 1621, 1645, 1670, 1695, 1720, 1745, 1770, -1, -1, -1, -1,
-1, -1, -1, -1, -1, 218, 246, 275, 304, 333, 362, 389,
-1, 441, 472, 505, 538, 571, 603, 631, -1, 683, 714, 748,
783, 817, 849, 877, -1, 929, 960, 994, 1029, 1063, 1095, 1123,
-1, 1175, 1206, 1239, 1272, 1305, 1337, 1365, -1, 1416, 1444, 1473,
1502, 1531, 1560, 1586, -1, 1634, 1659, 1684, 1709, 1734, 1759, 1783,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, 466, 499, 532, 565, 598, 627,
-1, -1, 708, 742, 777, 811, 844, 873, -1, -1, 954, 988,
1023, 1057, 1090, 1119, -1, -1, 1200, 1233, 1266, 1299, 1332, 1361,
-1, -1, 1438, 1467, 1496, 1525, 1555, 1582, -1, -1, 1653, 1678,
1703, 1728, 1754, 1779, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, 739, 774, 809, 842, 871,
-1, -1, -1, 985, 1020, 1055, 1088, 1117, -1, -1, -1, 1230,
1263, 1297, 1330, 1359, -1, -1, -1, 1464, 1493, 1523, 1553, 1580,
-1, -1, -1, 1675, 1700, 1726, 1752, 1777, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, 1018, 1053, 1086, 1115,
-1, -1, -1, -1, 1261, 1295, 1328, 1357, -1, -1, -1, -1,
1491, 1521, 1551, 1578, -1, -1, -1, -1, 1698, 1724, 1750, 1775,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, 1293, 1326, 1355,
-1, -1, -1, -1, -1, 1519, 1549, 1576, -1, -1, -1, -1,
-1, 1722, 1748, 1773, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1547, 1574,
-1, -1, -1, -1, -1, -1, 1746, 1771, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1769,
-1, 23, 48, 74, 100, 126, 152, 177, -1, 222, 251, 281,
311, 341, 370, 397, -1, 445, 477, 511, 545, 579, 611, 639,
-1, 687, 719, 754, 790, 825, 857, 885, -1, 933, 965, 1000,
1036, 1071, 1103, 1131, -1, 1179, 1211, 1245, 1279, 1313, 1345, 1373,
-1, 1420, 1449, 1479, 1509, 1539, 1568, 1594, -1, 1638, 1664, 1690,
1716, 1742, 1767, 1791, -1, -1, 47, 73, 99, 125, 151, 176,
-1, -1, 250, 280, 310, 340, 369, 396, -1, -1, 476, 510,
544, 578, 610, 638, -1, -1, 718, 753, 789, 824, 856, 884,
-1, -1, 964, 999, 1035, 1070, 1102, 1130, -1, -1, 1210, 1244,
1278, 1312, 1344, 1372, -1, -1, 1448, 1478, 1508, 1538, 1567, 1593,
-1, -1, 1663, 1689, 1715, 1741, 1766, 1790, -1, -1, -1, 72,
98, 124, 150, 175, -1, -1, -1, 279, 309, 339, 368, 395,
-1, -1, -1, 509, 543, 577, 609, 637, -1, -1, -1, 752,
788, 823, 855, 883, -1, -1, -1, 998, 1034, 1069, 1101, 1129,
-1, -1, -1, 1243, 1277, 1311, 1343, 1371, -1, -1, -1, 1477,
1507, 1537, 1566, 1592, -1, -1, -1, 1688, 1714, 1740, 1765, 1789,
-1, -1, -1, -1, 97, 123, 149, 174, -1, -1, -1, -1,
308, 338, 367, 394, -1, -1, -1, -1, 542, 576, 608, 636,
-1, -1, -1, -1, 787, 822, 854, 882, -1, -1, -1, -1,
1033, 1068, 1100, 1128, -1, -1, -1, -1, 1276, 1310, 1342, 1370,
-1, -1, -1, -1, 1506, 1536, 1565, 1591, -1, -1, -1, -1,
1713, 1739, 1764, 1788, -1, -1, -1, -1, -1, 122, 148, 173,
-1, -1, -1, -1, -1, 337, 366, 393, -1, -1, -1, -1,
-1, 575, 607, 635, -1, -1, -1, -1, -1, 821, 853, 881,
-1, -1, -1, -1, -1, 1067, 1099, 1127, -1, -1, -1, -1,
-1, 1309, 1341, 1369, -1, -1, -1, -1, -1, 1535, 1564, 1590,
-1, -1, -1, -1, -1, 1738, 1763, 1787, -1, -1, -1, -1,
-1, -1, 147, 172, -1, -1, -1, -1, -1, -1, 365, 392,
-1, -1, -1, -1, -1, -1, 606, 634, -1, -1, -1, -1,
-1, -1, 852, 880, -1, -1, -1, -1, -1, -1, 1098, 1126,
-1, -1, -1, -1, -1, -1, 1340, 1368, -1, -1, -1, -1,
-1, -1, 1563, 1589, -1, -1, -1, -1, -1, -1, 1762, 1786,
-1, -1, -1, -1, -1, -1, -1, 171, -1, -1, -1, -1,
-1, -1, -1, 391, -1, -1, -1, -1, -1, -1, -1, 633,
-1, -1, -1, -1, -1, -1, -1, 879, -1, -1, -1, -1,
-1, -1, -1, 1125, -1, -1, -1, -1, -1, -1, -1, 1367,
-1, -1, -1, -1, -1, -1, -1, 1588, -1, -1, -1, -1,
-1, -1, -1, 1785, -1, 30, 55, 80, 105, 130, 155, 179,
-1, 229, 258, 287, 316, 345, 373, 399, -1, 452, 484, 517,
550, 583, 614, 641, -1, 694, 726, 760, 795, 829, 860, 887,
-1, 940, 972, 1006, 1041, 1075, 1106, 1133, -1, 1186, 1218, 1251,
1284, 1317, 1348, 1375, -1, 1427, 1456, 1485, 1514, 1543, 1571, 1596,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 59, 84,
109, 134, 158, 181, -1, -1, 262, 291, 320, 349, 376, 401,
-1, -1, 488, 521, 554, 587, 617, 643, -1, -1, 730, 764,
799, 833, 863, 889, -1, -1, 976, 1010, 1045, 1079, 1109, 1135,
-1, -1, 1222, 1255, 1288, 1321, 1351, 1377, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, 89, 114, 139, 162, 184, -1, -1, -1, 296,
325, 354, 380, 404, -1, -1, -1, 526, 559, 592, 621, 646,
-1, -1, -1, 769, 804, 838, 867, 892, -1, -1, -1, 1015,
1050, 1084, 1113, 1138, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, 117, 141, 164, 186,
-1, -1, -1, -1, 328, 356, 382, 406, -1, -1, -1, -1,
562, 594, 623, 648, -1, -1, -1, -1, 807, 840, 869, 894,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, 143, 166, 188, -1, -1, -1, -1, -1, 358, 384, 408,
-1, -1, -1, -1, -1, 596, 625, 650, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, 168, 190, -1, -1, -1, -1,
-1, -1, 386, 410, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 192,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, 11, 36, 62, 87,
112, 137, 161, -1, 208, 235, 265, 294, 323, 352, 379, -1,
429, 458, 491, 524, 557, 590, 620, -1, 671, 700, 733, 767,
802, 836, 866, -1, 917, 946, 979, 1013, 1048, 1082, 1112, -1,
1163, 1192, 1225, 1258, 1291, 1324, 1354, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
9, 33, 58, 83, 108, 133, -1, -1, 206, 232, 261, 290,
319, 348, -1, -1, 427, 455, 487, 520, 553, 586, -1, -1,
669, 697, 729, 763, 798, 832, -1, -1, 915, 943, 975, 1009,
1044, 1078, -1, -1, 1161, 1189, 1221, 1254, 1287, 1320, -1, -1,
1403, 1430, 1459, 1488, 1517, 1546, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
196, 221, 249, 278, 307, 336, -1, -1, 417, 444, 475, 508,
541, 574, -1, -1, 659, 686, 717, 751, 786, 820, -1, -1,
905, 932, 963, 997, 1032, 1066, -1, -1, 1151, 1178, 1209, 1242,
1275, 1308, -1, -1, 1393, 1419, 1447, 1476, 1505, 1534, -1, -1,
1613, 1637, 1662, 1687, 1712, 1737, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
413, 439, 469, 502, 535, 568, 601, -1, 655, 681, 711, 745,
780, 814, 847, -1, 901, 927, 957, 991, 1026, 1060, 1093, -1,
1147, 1173, 1203, 1236, 1269, 1302, 1335, -1, 1389, 1414, 1441, 1470,
1499, 1528, 1558, -1, 1609, 1632, 1656, 1681, 1706, 1731, 1757, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, 437, 467, 500, 533, 566, 599, 628,
-1, 679, 709, 743, 778, 812, 845, 874, -1, 925, 955, 989,
1024, 1058, 1091, 1120, -1, 1171, 1201, 1234, 1267, 1300, 1333, 1362,
-1, 1412, 1439, 1468, 1497, 1526, 1556, 1583, -1, 1630, 1654, 1679,
1704, 1729, 1755, 1780, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, 245, 274, 303, 332, 361, 388, -1, -1, 471, 504,
537, 570, 602, 630, -1, -1, 713, 747, 782, 816, 848, 876,
-1, -1, 959, 993, 1028, 1062, 1094, 1122, -1, -1, 1205, 1238,
1271, 1304, 1336, 1364, -1, -1, 1443, 1472, 1501, 1530, 1559, 1585,
-1, -1, 1658, 1683, 1708, 1733, 1758, 1782, -1, -1, 54, 79,
104, 129, 154, 178, -1, -1, 257, 286, 315, 344, 372, 398,
-1, -1, 483, 516, 549, 582, 613, 640, -1, -1, 725, 759,
794, 828, 859, 886, -1, -1, 971, 1005, 1040, 1074, 1105, 1132,
-1, -1, 1217, 1250, 1283, 1316, 1347, 1374, -1, -1, 1455, 1484,
1513, 1542, 1570, 1595, -1, -1, -1, -1, -1, -1, -1, -1,
-1, 34, 60, 85, 110, 135, 159, 182, -1, 233, 263, 292,
321, 350, 377, 402, -1, 456, 489, 522, 555, 588, 618, 644,
-1, 698, 731, 765, 800, 834, 864, 890, -1, 944, 977, 1011,
1046, 1080, 1110, 1136, -1, 1190, 1223, 1256, 1289, 1322, 1352, 1378,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, 1799, 1808, 1817, 1826, 1835, 1844, 1853,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, 1800, 1809, 1818,
1827, 1836, 1845, 1854, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, 1798, 1807, 1816, 1825, 1834, 1843, 1852, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, 1793, 1802, 1811, 1820, 1829, 1838, 1847, 1856,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, 1794, 1803, 1812, 1821,
1830, 1839, 1848, 1857, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
1792, 1801, 1810, 1819, 1828, 1837, 1846, 1855, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, 1796, 1805, 1814, 1823, 1832, 1841, 1850, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, 1797, 1806, 1815, 1824,
1833, 1842, 1851, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
1795, 1804, 1813, 1822, 1831, 1840, 1849, -1, -1, -1, -1, -1,
-1, -1, -1, -1 )