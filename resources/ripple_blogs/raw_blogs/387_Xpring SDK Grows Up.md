# Xpring SDK Grows Up

**发布日期**: December 16, 2025
**作者**: 未知
**来源**: [https://ripple.com/insights/xpring-sdk-more-than-just-xrp-2/](https://ripple.com/insights/xpring-sdk-more-than-just-xrp-2/)

## 支付相关度评估
**评级**: 🟡 中度相关
**关键词匹配数**: 3

## 摘要
Ripple is the leading blockchain payments company.

## 核心内容

Team Ripple

In October 2019, Xpring announced an effort to produce a multi language software development kit (SDK) that would simplify and unify Xpring’s offerings across our suite of protocols and products. Predictably, the first product in our SDK was integration with the XRP Ledger (XRPL), the most mature technology that Xpring works on.

While XRPL was a good place to start, the goal of Xpring has always been to create the internet of value and enable developers to make money a MIME type. To deliver on this promise, Xpring SDK needs to support not just XRP, but all the money. New versions of the Xpring SDK, available today (JavaScript, Java, Swift) have added functionality to support Interledger Protocol (ILP). ILP enables interoperability among different ledgers and expands the SDK’s functionality beyond XRP. This feature addition marked our first step in delivering on our ultimate vision for the SDK: A one stop show for any developer who wants to move value. As we continue to deliver on our promise, we expect our SDK to expand to offer support for additional protocols and compose complex interactions between existing ones.

Past the delivery of ILP, we’re proud to showcase improvements to our XRPL components. In October 2019, we delivered Javascript, Java and Swift libraries, which worked on a common codebase and exposed similar APIs. Xpring decided to use code generation and code sharing to simplify the internals of the SDK, an approach with high initial overhead but long-term benefits. Our initial version of the code worked, but provided minimal functionality (checking balances and sending XRP). The APIs weren’t great, the documentation left a lot to be desired and the SDK needed to talk to a modified rippled node that only Xpring had access to. As Xpring SDK matured and we responded to developer feedback, we made breaking API changes to the codebase.

Since October, we’ve invested significant effort in maturing and building our XRPL support. Today, our libraries contain stable APIs and additional functionality (most notably: payment status and payment history). More notably, these libraries now connect directly to any rippled node, which lets dApp developers decentralize themselves from Xpring’s infrastructure and rely on their own nodes. Lastly, Xpring SDK also continues to power the entirety of our web based wallet. This includes functionality for both ILP and XRPL.

Beyond the headlines above, this post serves to take a deeper dive into the technical aspects of the SDK’s surface area that go beyond the shallows of our recent launch announcement. We will also look at what’s new in both the Xpring SDK and the community.

If you’re excited about writing code to interact with Xpring Services read on!

As my previous post suggested, Xpring employs a unique technical architecture to enable us to build libraries scalably across languages. Xpring uses interface description languages (IDLs) and code generation to easily create and validate our network layer. For XRPL and ILP, we employ gRPC for its ease of use, wide language availability, backwards compatibility, and performance benchmarks.

Additionally, we created a common JavaScript library which encapsulates core functionality. We use this for tasks like encoding / decoding between formats, binary serialization of transactions, wallet derivation and similar low level tasks relating to XRPL.

Let’s take a look at some of the new features of the SDK, and how they use these libraries:

Xpring SDK has incorporated ILP. The ILP team has delivered code that lets users connect to a remote ILP node and interact with the ILP protocol. The functionality makes heavy use of gRPC’s code generation which helped the team get code working, tested, QA’ed and delivered quickly in all variants of the SDK. ‌‌

We’ve delivered several additional features in our XRPL components. New features, like payment history and account existence checks make use of gRPC code which we get for free via code generation.

Under the hood, we’ve made a bunch of improvements including support for flags attached to transactions, bucketing of payment statuses and many smaller performance improvements. As with our other work, these smaller features benefit greatly from having a common core library that enforces similar behavior across our libraries.

In addition to the original JSON-based API, rippled 1.5 (the software that powers XRP Ledger nodes and validators) introduced support for a native gRPC interface. Prior to this support, Xpring SDK had to use a modified codebase to connect to a node via gRPC. This shimming layer worked as a proof of concept, but the resulting architecture was centralized at Xpring.

After the hard work by our rippled team to build gRPC support natively into rippled, the daemon now offers gRPC support for the API endpoints that Xpring SDK requires. From a performance perspective, our initial internal benchmarks of our wallet software have indicated that gRPC calls perform better and faster than their analogs in the JSON API.

In practice, this development means that anyone can run a rippled node and connect to it via the Xpring SDK, removing Xpring as a centralized point of failure. Xpring continues to encourage users to properly decentralize the network and practice self-reliance by running their own nodes, but we also recognize that developers will want to get started right away. You can access a node maintained by Xpring by pointing the SDK at:

# Testnettest.xrp.xpring.io:50051# Mainnetmain.xrp.xpring.io:50051

Xpring SDK’s architecture was built with modularity and code reuse in mind. As such, Xpring is proud to highlight additional community-created SDKs that are produced outside of Xpring. In all cases, these SDKs make heavy use of our core libraries and architectures which greatly simplify the developer’s life. ‌‌

We believe in an open source ecosystem and are delighted to see enthusiasm to continue producing Xpring SDK in additional languages. We’d like to highlight:

Xpring is thrilled by the outpouring of support from these developers. Xpring will work with these developers and support them in order to help them bring all the features of the Xpring SDK to the languages of their choice.

Today’s announcement underscores what Xpring SDK is all about. Xpring SDK is more than just another XRPL SDK. Xpring SDK is built to connect developers to the internet of value and make money a MIME type regardless of their language, asset or protocol of choice.

This release ties together contributions from nearly every team at Xpring, whether it’s the rippled XRP Ledger team, the InterLedger Team, or the developer tooling teams. Xpring is harnessing the synergy of all components executing together on a similar paradigm. All members of these teams are excited to see the vision of a unified programming model for these protocols take shape and we can’t wait to see what developers will build and do with it.

Want to get started? Head on over to our documentation or take a look at our demos. Have a question about working with Xpring SDK or a feature request? Head on over to the Xpring Forum and get in touch.

---
*此文档由爬虫自动生成，发布时间: 2025-12-23 19:41:33*
