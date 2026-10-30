# 34句逐句表达复核

原句全文、事实包链接与输入哈希见[sentence-review.json](sentence-review.json)。Z为锌段落，S为固态段落；数字依次为段号和句号。对照编号表示同功能的表达参照，不是句子事实来源或强配母句；事实仍据原练习输入，编辑判断由本次审读作出。

- **N-MD**：Read PDF page 4, left column, first paragraph under Ligand-channel-facilitated mechanism; Fig. 2 caption on page 3. 模型身份、具体量、比较及局部解释的顺序；不能迁移其锂体系机制。
- **N-IF**：Read PDF page 6, body below Fig. 4, interphase-analysis paragraph and corresponding caption. 测量/计算分工和观察与解释的相邻放置；不照搬来源因果强度。
- **A-IMG**：Published PDF page 4, paragraph below Fig. 2 introducing LiCl comparison; continuation on right; Fig. 3 on page 5. 对象、条件、时间序列及形貌对照；不能把来源原位条件移植给非原位XR-CT。
- **A-SPEC**：Published PDF page 9, lower left, Raman/solvation paragraph associated with Fig. 5i,j; preceding context. 峰归属、定量比较与解释分层；不同谱带不可被虚设为同分母。

| 句ID | 编辑判断 | 表达参照 | 具体依据 |
|---|---|---|---|
| Z1.1 | 拆分 | A-SPEC | 三种配方与molality定义同句，读者需同时保存多个对象；按SE/DE与HDE分句。原数值和水质量基准均保留。 |
| Z1.2 | 保留 | A-SPEC | 测量对象、谱段、拟合身份、对照和最小值齐全；句长来自必要比较，不必机械切短。 |
| Z1.3 | 保留 | A-SPEC | 将氢键环境与水活度/析氢测量区分，限制紧贴相应推断，不能为了流畅删除。 |
| Z2.1 | 合并 | A-SPEC | 只宣布Raman提供信息，下一句才给结果；可与下一句合并为直接描述拟合所得量。 |
| Z2.2 | 保留内容 | A-SPEC | 两类阴离子及对应比例清楚；与前句合并时仍保留归属和不同统计对象。 |
| Z2.3 | 保留 | A-SPEC | 不同谱带分母不可混算，是关键比较边界，不是空泛的谨慎话术。 |
| Z2.4 | 保留 | A-SPEC | 明确HDE谱学定量缺口，不能用MD占比填成Raman实测。 |
| Z2.5 | 收紧 | N-IF | XANES edge重复；可用Shifts in the Zn K-edge XANES spectra，并明确EXAFS的变换域。几何不唯一的限制保留。 |
| Z3.1 | 合并 | N-MD | 通用的structural interpretation没有具体信息，可让MD直接引出下一句的粒子分布趋势。 |
| Z3.2 | 保留内容 | N-MD | 三体系间的下降方向及具体值清楚；并入MD句后仍标明模型身份。 |
| Z3.3 | 拆分 | N-MD | 同句同时解释AGG非单调变化和CIP变化，按两个物种拆句，保留所有数字与对象。 |
| Z3.4 | 保留 | N-MD | 已将原先模糊的重新分布写成HDE相对DE的具体差异，是清楚的局部综合。 |
| Z3.5 | 可合并 | N-MD | 模型与Raman口径不同需保留；可随MD结果首次出现说明，不必在后面再作泛化提醒。 |
| Z3.6 | 保留 | N-MD | 0.19明确为平均配位数，模型中参与配位的表述有界，不应改成19%。 |
| Z3.7 | 可收紧 | N-MD | 贡献与唯一机制分开得当；可与相邻限定统筹压缩，不能改成已经证明抑制副反应的唯一原因。 |
| Z3.8 | 保留 | N-MD | 盐浓度共同变化直接限制DMF单因果归属，必须可见。 |
| Z3.9 | 保留内容 | N-MD | 同时很高电流密度和面容量的边界会改变外推；不得省去同时成立或补造阈值。 |
| S1.1 | 保留 | A-IMG | 来源身份、材料和研究对象明确；这是已发表事实练习，第三人称不应作为风格错误。 |
| S1.2 | 保留 | A-IMG | 压力值对应器件构型，明确无外加压力并非零压力，信息有用。 |
| S1.3 | 可合并 | A-IMG | 连续监测与独立测压不同，若压缩应并入测量范围说明，而不能写成全程恒压已实测。 |
| S1.4 | 保留 | A-IMG | 虽较长，但单一平行比较包含20圈、非原位、两体系和两种压力，理解关系清楚。 |
| S1.5 | 保留 | A-IMG | 将亮条纹作为作者判定的伪影，而非独立认证，避免形貌误读。 |
| S1.6 | 保留 | A-IMG | 条件与定量缺口对应这次结构比较，属于结论所需限定。可与本段已有条件去重，但不能隐去。 |
| S2.1 | 合并 | N-MD | 只说支持mechanical interpretation，具体预测在下一句；与下一句合并更直接。 |
| S2.2 | 保留内容 | N-MD | 模型假设、应力量、比较方向均有科学作用；并句时保留随机球、线弹性和膨胀情景。 |
| S2.3 | 保留 | N-MD | 从模拟应力过渡到接触解释，consistent with保持合理证据强度。 |
| S2.4 | 保留 | N-MD | 非共价键断裂不是XR-CT直接可见结果，限制具有针对性。 |
| S2.5 | 保留 | N-MD | 配方、工艺及对电极差异妨碍唯一弹性因果归属，不能当作语言冗余删除。 |
| S3.1 | 替换并去重 | N-IF | place this interpretation within specific cell configurations过于抽象；可前置S3.5中具体的接触—循环稳定性关系。 |
| S3.2 | 收紧 | N-IF | showed a reported capacity retention套叠；直接写reported capacity retention was即可，保留温度、倍率和圈数。 |
| S3.3 | 收紧 | N-IF | 与上一句同类冗余，可统一为reported retention；LFP质量基准及独立全电池构型不能省略。 |
| S3.4 | 保留 | N-IF | 全电池装配前预循环关系影响性能理解，指代清楚。 |
| S3.5 | 合并去重 | N-IF | 实质关系有用；若移到段首，就删除此处重复表达，不能仅新增一条更漂亮的首句。 |
| S3.6 | 保留 | N-IF | 20圈结构证据与长循环性能之间的时间外推限制应保留。 |
