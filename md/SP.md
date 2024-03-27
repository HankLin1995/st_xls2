
#### 一、計算依據

:link:[內政部建築物基礎構造設計規範(112年)--7.5.3]("https://www.nlma.gov.tw/filesys/file/EMMA/L1120811.pdf")

#### 二.基本參數設定

φ = {phi}°

主動土壓力係數（Ka）的計算公式如下：

$$ K_a = \frac{{1 - \sin(\phi)}}{{1 + \sin(\phi)}} $$

Ka = {Ka}

被動土壓力係數（Kp）的計算公式如下：

$$ K_p = \frac{{1 + \sin(\phi)}}{{1 - \sin(\phi)}} $$

Kp = {Kp}

---

#### 三.O點上部計算

(1) 假設 O 點為不動點，將擋土牆分為上下兩部分。下圖之牆後被動
土壓力與牆前主動土壓力的差值，以一集中力 R 作用於上圖 O 點。

(2) 對上圖之 O 點取彎矩平衡，取適當的彎矩安全係數 FS，可求得 d0；
取水平力平衡，可得 R 值。

$$ P_A = \frac{{1}}{{2}} \cdot \gamma \cdot (H + d_0)^2 \cdot K_a  $$

$$ P_p = \frac{{1}}{{2}} \cdot \gamma  \cdot (d_0)^2 \cdot K_p $$

$$ L_a=\frac{{(H + d_0)}}{{3}} $$

$$ L_p=\frac{{d_0}}{{3}} $$

$$ M_A = P_A \cdot L_a= \frac{{1}}{{2}} \cdot \gamma \cdot (H + d_0)^2 \cdot K_a \cdot \frac{{(H + d_0)}}{{3}}  $$  

$$ M_p = P_p \cdot L_p = \frac{{1}}{{2}} \cdot \gamma \cdot d_0^2 \cdot K_p \cdot \frac{{d_0}}{{3}} $$

$$ FS = \frac{{M_p}}{{M_A}} $$

**對上圖之 O 點取彎矩平衡，FS按規範取1.5。**

計算得到的d0為2：{d0_sol}M

**對上圖取力平衡**

$$ R = P_p- P_A $$

計算得到的R值為：{R_value}

---

#### 四.O點下部計算

**計算目的:至少須滿足  S >= R**

根據經驗  D=1.1~1.2d0

$$ P_{{Al}} = \frac{{1}}{{2}}(\gamma \cdot d_0 \cdot K_a + \gamma \cdot D \cdot K_a)(D - d_0) $$

$$ P_{{pl}} = \frac{{1}}{{2}}(\gamma \cdot (H + d_0) \cdot K_p + \gamma \cdot (H + D) \cdot K_p)(D - d_0) $$

$$ S = P_{{pl}}- P_{{Al}} $$

當i={i_value}時，S={S_test_value}

此時滿足  S >= R，試誤法求解得D=**{D}**

---

#### 五.計算成果

計算所得之H+D={H_D}M

#### :heavy_check_mark: 建議採用懸臂式板樁長度為 *{H_D_ceil}* M
