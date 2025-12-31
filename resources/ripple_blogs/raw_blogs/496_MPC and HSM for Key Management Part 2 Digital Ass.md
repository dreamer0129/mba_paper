# MPC and HSM for Key Management Part 2: Digital Asset Custody Design Considerations

**发布日期**: December 16, 2025
**作者**: 未知
**来源**: [https://ripple.com/insights/mpc-and-hsm-for-key-management-part-2-digital-asset-custody-design-considerations/](https://ripple.com/insights/mpc-and-hsm-for-key-management-part-2-digital-asset-custody-design-considerations/)

## 支付相关度评估
**评级**: 🟡 中度相关
**关键词匹配数**: 2

## 摘要
Tokenization unlocks asset liquidity and secure ownership. Learn the types of technologies banks must evaluate to offer trusted digital asset custody solutions.

## 核心内容

Team Ripple

Tokenization, not merely as a technological marvel but as a change catalyst, can dissolve friction of ownership, value, and participation, even from the world’s most illiquid traditional assets. Beyond cryptocurrencies, digital assets can represent mutual funds, real estate, carbon credits, art, precious metals or even fine wine on a blockchain. The applications and implications are enormous, with Boston Consulting Group predicting tokenized assets will grow into a $16 trillion business opportunity by 2030.

As the number of digital asset use cases grows, sophisticated institutional investors and enterprises are increasingly seeking trusted custody options to protect their portfolios, creating an opening for banks and financial institutions to expand their custody offerings and meet this need.

In part one of this series, we examined the types of technologies banks and financial institutions must evaluate when developing a digital asset custody solution, including hot or cold wallets, Hardware Security Modules (HSM) versus Multiparty Computation (MPC), and on-premise (on-prem) or third-party hosted solutions.

Part two of this series looks at the different considerations that inform the optimal design and execution of an institutional crypto custody solution.

As this popular maxim implies, custodians must design solutions using robust technologies and governance policies that maximize private key protection and control.

Just because a security solution makes it more difficult to take control of keys does not mean it’s impregnable. Even Multi-party Computation (MPC) solutions that split the vault or wallet keys into key fractions or “shards” are vulnerable if hackers can compromise multiple accounts or signatories.

Institutional custodians and regulated entities cannot afford to simply default to the most widely-adopted solutions. Instead, they must be rigorous in their evaluation and deploy, maintain and audit a layered digital asset custody service that incorporates proper storage, access and governance protocols that fully comply with rigorous risk management and compliance requirements.

Institutional custody solutions are much more than just technology protections for crypto assets and their private keys. Custodians and clients must also jointly develop detailed internal policies and access controls that outline a framework and control hierarchy that reduces if not eliminates single points of failure.

A robust policy engine will include strong technology controls, data encryption, network security, and limits on individual access so that no one person performs sensitive transactions in isolation or some individuals collude to do so with malevolent intention. Of course, this vital layer is also a point of vulnerability, offering hackers that gain access to it a way to modify the policies and control the flow of funds.

An effective policy engine is one that combines controls, audits and monitoring to reinforce security at every step of the control and approval hierarchy.

When designing a custodial service, financial service institutions must account for expected transaction throughput and scalability. Each component of a solution – wallet type, key protection and hosting – has strengths and weaknesses relative to speed and volume that, in aggregate, can significantly impact the viability of an intended use case.

For example, HSM solutions can handle up to 10,000 transactions per second while an MPC wallet is limited to roughly 20 or less transactions per second. So, while an HSM solution may be slower to access than a MPC wallet, it offers more room for transaction volumes to scale over time.

Understanding how environments might change is also important when designing the optimal system. One custody architecture may work well within a limited pilot or proof of concept, but quickly become obsolete as throughput grows within a production environment. Designers must have a grasp on the continuum of client needs to build optimal, future-proofed solutions.

Each choice within a custody solution comes with different cost and resource commitments that must be weighed against client needs and use cases.

While a MPC wallet adds extra layers of security and peace of mind, it requires additional computational resources. Despite this performance tax, it still retains the edge over HSMs when protecting against single points of failure, making it more useful in a hot wallet. Of course, that hot wallet also comes with tradeoffs, providing greater access and enabling faster transactions but sacrificing some level of security.

Similarly, institutional providers must weigh cost and resource requirements when choosing a Software-as-a-Service (SaaS) provider versus building an on-prem solution. The on-prem path comes with much higher up-front costs and ongoing maintenance and resource requirements relative to a SaaS option, but it provides a compelling advantage for those providers who need custom setups or that must maintain complete control.

Ultimately, banks and financial institutions seeking to capitalize on the fast-growing market for institutional digital asset custody solutions must consider all these pros and cons at every step in their build. The key to designing a strong, multi-tiered solution is combining layers of technology with processes. Institutional crypto custodians that can offer robust, secure and adaptable solutions are best able to safeguard client assets and therefore most likely to capture market share over competitors.

Contact us to learn more about MPC and HSM for key management technology.

---
*此文档由爬虫自动生成，发布时间: 2025-12-23 19:41:33*
