本文件为合成事实上的局部英文写作练习，不代表真实实验。本轮依据 skill-r2 续改已见的 run-b.md，另存修订稿；不属于独立新运行。

# Stack-pressure dependence of the cycling advantage of thin-layer-modified layered-oxide composite cathodes

## Abstract

The cycling benefit of a cathode modification needs to be assessed under the stack pressures at which it is used. Here, we compare layered-oxide composite cathodes with a thin-layer modification (C) and unmodified controls (U) in cells with Li–In counter electrodes at 4 and 12 MPa. After 100 cycles at 25 °C and 0.2 C, mean capacity retention relative to the first discharge was 88% for C and 72% for U at 4 MPa, compared with 90% and 87% at 12 MPa. The difference between the three-cell means therefore narrowed from 16 to 3 percentage points. At 4 MPa, C also had a lower post-cycling cross-sectional pore-area fraction and a lower fitted interface-related resistance at 50% state of charge. These observations are consistent with a contribution from geometric contact to the low-pressure benefit, but do not distinguish it from chemical effects.

## Introduction

Here, we test whether the cycling advantage of a thin-layer modification persists when stack pressure increases from 4 to 12 MPa. We compare modified layered-oxide composite cathodes (C) with unmodified controls (U) in cells with Li–In counter electrodes, holding the cathode active-material mass, electrode area and sulfide-electrolyte proportion constant. Post-cycling cross-sectional imaging and impedance measurements at 4 MPa examine how the larger low-pressure advantage relates to morphology and interface-related resistance.

## Results

### The retention advantage narrows at higher stack pressure

The modified cathodes showed a larger mean capacity-retention advantage over the unmodified controls at 4 MPa than at 12 MPa (Fig. 1a). In cells with Li–In counter electrodes cycled at 25 °C and 0.2 C, C and U retained 88% and 72%, respectively, of their first-discharge capacities after 100 cycles at 4 MPa. At 12 MPa, the corresponding means were 90% and 87%, narrowing the C–U difference from 16 to 3 percentage points. Each value is the mean of three independent cells for the specified sample and pressure. This narrowing mainly reflected the higher mean retention of U at 12 MPa; C differed by only 2 percentage points between pressures.

At 4 MPa, the larger retention difference was accompanied by a lower pore-area fraction and a lower fitted interface-related resistance for C after cycling. Analysis of four cross-sectional SEM fields from one cell per sample after 100 cycles gave pore-area fractions of 3% for C and 10% for U, using the same segmentation threshold; representative images are shown in Fig. 1b. At 50% state of charge after 100 cycles at 4 MPa, fitting the impedance spectra with the same equivalent circuit gave interface-related resistances of 80 Ω cm² for C and 140 Ω cm² for U (Fig. 1c).

## Discussion

The coexistence of a smaller pore-area fraction and a lower fitted interface-related resistance at 4 MPa is consistent with a contribution from geometric contact to the retention advantage of C. Without pre-cycling pore fractions, the morphology comparison cannot distinguish an initial difference from one that developed during cycling; the fitted resistance also leaves geometric and chemical contributions unresolved. Corresponding measurements at 12 MPa would test whether the narrowing retention gap accompanies a smaller difference in interfacial state. Evaluating the modification therefore requires pressure-matched controls, while the present mean differences remain descriptive because cell-to-cell dispersion is unavailable.

## Conclusion

For the tested layered-oxide composite cathodes, thin-layer modification yielded a mean capacity-retention advantage at both pressures, with a larger difference at 4 MPa than at 12 MPa.

## Methods

Layered-oxide composite cathodes with a thin-layer modification (C) were compared with unmodified cathodes (U). The two sample types had the same cathode active-material mass, electrode area and sulfide-electrolyte proportion, with a cathode active-material loading of 4 mg cm⁻². Cells with Li–In counter electrodes were cycled for 100 cycles at 25 °C and 0.2 C using the same voltage window under stack pressures of 4 or 12 MPa. Three independent cells were tested for each sample–pressure combination. Capacity retention was calculated for each cell relative to its first discharge capacity, and the reported values are the means of the three cells. After 100 cycles at 4 MPa, cells were disassembled for cross-sectional SEM. The pore-area fraction for each sample was obtained from four fields of view from one cell, using a common segmentation threshold. Impedance spectra were collected after 100 cycles at 4 MPa at 50% state of charge, over 1 MHz to 10 mHz with a perturbation amplitude of 10 mV. Spectra for C and U were fitted with the same equivalent circuit to obtain the interface-related resistance.

## Figure caption

**Fig. 1 | Stack-pressure-dependent capacity retention and characterization after cycling at 4 MPa.** C and U denote the thin-layer-modified and unmodified layered-oxide composite cathodes, respectively. **a,** Capacity retention after 100 cycles at 4 and 12 MPa for cells with Li–In counter electrodes, cycled at 25 °C and 0.2 C. Retention is referenced to each cell’s first discharge capacity; values are means from three independent cells for each sample–pressure combination. **b,** Representative cross-sectional SEM images of C and U after 100 cycles at 4 MPa. Pore-area analysis used four fields from one cell per sample and a common segmentation threshold. **c,** Impedance spectra and equivalent-circuit fits obtained after 100 cycles at 4 MPa at 50% state of charge, using a frequency range of 1 MHz–10 mHz and a perturbation amplitude of 10 mV.

---

## 本轮续改记录

本轮从 run-b.md 接续，使用 skill-r2，保持原有“压力比较 → 低压下形貌与阻抗 → 有限解释”的主线。摘要保留四个容量保持率及 16、3 个百分点的核心对照，将孔隙和电阻的完整数值留在 Results，删除重复收束；引言删去对研究设计的重复概括。Results 第一段将重复数移到解释之前，第二段删去重述段首的关联总结。循环前基线缺失与几何/化学归因的限制集中在 Discussion；结论直接回答两个压力下的均值优势。题名、Results 小标题、Methods 和图注保留。此记录只说明本次可见稿件的修改，不据此判断技能的泛化效果。

## 必要待补资料

- **材料与循环复现：** 薄层组成、厚度及制备配方；活性材料、电解质身份、复合正极配方与组装过程；电极面积、电压窗口及电位基准、0.2 C 的容量/电流基准、堆压施加与保持方式。
- **形貌与阻抗复现：** 截面制备、取样荷电状态、转移与成像条件、标尺；视野选择、分割阈值及四视野汇总方式；等效电路与元件归属、拟合流程、面积归一化、阻抗测量温度与静置条件、独立重复数。
- **统计与成图：** 各独立电池保持率及离散度、孔隙与阻抗结果的变异信息；Fig. 1 原图、图例和线型，以及实际采用的误差线定义。未替作者设定均值之外的统计量或显著性检验。
- **解释范围与正式成稿：** 如需加强归因，应补循环前孔隙、12 MPa 对应形貌与阻抗，以及区分接触几何和化学变化的证据；未提供原位观察、直接应力测量或完整电芯能量数据，正文未写入相应结论。背景还需可核验文献。上述缺口未作为完成本次局部续改的前置条件。

## 实际核对范围

已对修订后的全部英文片段进行事实、句段衔接和片段间一致性复核，重点检查删并后是否仍保留样品顺序、压力与循环条件、首次放电分母、百分点、二维孔隙量、SEM 单电池四视野、阻抗的拟合身份和 50% SOC 条件。循环的三个独立电池未外推为 SEM 或阻抗重复数；未将较小孔隙分数写成循环中孔隙生成受抑制，也未将低压关联写成已验证的压力机制。Methods 和图注沿用后重新核对了任务事实。

核对依据限于 task.md、已有 run-b.md 和本轮所读 skill-r2 文件。未读其他运行或评审产物，未联网、未新编事实或引文，未建立 60 篇文献库。未获得真实图像、原始数据、完整方法或全稿，未完成图像定量复核、实验复现、整篇论文审查、同功能原文句段对照或篇级结构对照；指南中的文献阅读记录不计为本轮亲读。本轮为已见案例续改，不作评分或期刊录用判断。

## 本轮实际读取文件的相对路径

- `SKILL.md`
- `../task.md`
- `../run-b.md`
- `references/context-and-mappings.md`
- `references/section-writing.md`
- `references/english-workflow.md`
- `references/sentence-craft.md`
- `references/paragraph-craft.md`
- `references/review-protocol.md`
