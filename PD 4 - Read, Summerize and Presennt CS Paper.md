# Reading Research Papers

## Introduction
In this document, we will discuss the process of reading, summarizing, and presenting research papers. This is a crucial skill for staying up-to-date with the latest developments in your field and effectively sharing knowledge with your teammates.

## The Main Structure of a Paper
When we want to read a research paper, we should first understand the standard structure of a paper, especially in the field of computer science and AI, and the role of each section.

### Abstract
As the name suggests, this part is the summary and condensed result of the article, divided into the following sections:
- Background and Value Explanation: This part explains the value of the problem being solved (e.g., how important music retrieval is) and the application scenarios of the problem this paper aims to solve (e.g., 3D object detection providing solutions and technical support for autonomous driving).
- Main Challenge: This part explains the main challenges of the problem the paper aims to solve. Research is an exploration of unresolved issues, and only areas with ongoing challenges are worth researching.
- Mainstream Approaches: This part explains the mainstream approaches and solutions in the field. These solutions have certain limitations, which is where the value of this paper lies—it aims to be better than existing methods.
- Approach of This Paper: This part transitions from other works to the author's own work, logically explaining the key points and advantages of the proposed method.
- Novelty and Results of This Paper: This part shows the value and results of the paper, such as stating that the proposed method ranks first on the same dataset.

When reading the abstract, it's the easiest place to understand the value of an unfamiliar paper. From the abstract, you can determine if the paper is in your field and if it is worth referencing. You can quickly filter a batch of papers for in-depth reading through the abstract.

### Introduction
This part can be seen as a further expansion of the first half of the abstract. The name "Introduction" indicates that it introduces the entire article. In this section, the article explains its idea and motivation, leading to the explanation of the method. For example, proposers of some neural networks might cite some neural theories and psychological theories here to complete the introduction and transition.

The structure of this part is:
- Discuss the significance of the research problem and the mainstream solutions from a broad perspective. This part often cites related works and categorizes them.
- Discuss the problems encountered in the research field to which this paper belongs (often corresponding to the paper's motivation). Based on previous work, what are the key conclusions? (For example, feature extraction is important, with citations attached. This part is often the foundation and inspiration of the paper.)
- Based on the above problems or a specific starting point, this paper proposes... (Common phrasing: "We propose a novel (task name) framework, xxx, which...") Then, briefly introduce each sub-structure.
- State the main contributions of this paper, usually around three points. Some papers also consider achieving SOTA (State Of The Art) on a dataset as a contribution.

For readers, a well-written introduction can lead them to think from the inventor's perspective and understand the necessary background information. Usually, after reading this part, readers can judge whether the paper is valuable for their research and decide whether to continue reading.

### Related Work
This section is usually written with bold subheadings. For example, if the research involves A, B, and C aspects, it will have A, B, and C as bold headings at the beginning of each paragraph, explaining the progress in these three fields.

In the related work section, you need to organize previous work and try to find multiple threads. For readers, a good related work section can show where the article's general idea comes from and whether it is tenable. This part is like a mini literature review, helping readers understand the article's relative position in the entire field. In the research system, traditional methods and initial problems are the roots of a big tree, gradually growing different leaves and nodes over time. The related work section explains which leaves and nodes inspired the authors.

### Approach & Experiments & Discussion
- The Approach section explains the technical details, usually following a workflow to introduce and explain different parts and the innovations of the article. Typically, a framework diagram is presented first, which is crucial for readers to modularly understand each part of the method.
- The Experiments section verifies the results and effectiveness of the previous ideas, usually by comparing them with baselines and other methods to prove the effectiveness of the proposed method. After that, the discussion section supplements additional information, such as whether there were any doubts in the experiments or limitations of the method.

### Conclusion
This section summarizes the entire paper, essentially rewriting the abstract. Ideally, after thoroughly reading the paper, the reader's understanding should align closely with the conclusions drawn in the conclusion section.

## Steps

### 1. Selecting Relevant Papers
- Identify the research topic or area of interest.
- Search for relevant papers using academic databases, search engines, or specialized platforms.
- Evaluate the credibility and relevance of each paper before proceeding.

In this stage, readers can extensively search for resources to understand the field and establish an overall framework. There is no limit to the number of resources at this stage. Gather any materials you find important, but be sure to create a useful shortlist of papers, videos, and articles. In the second step, delve into any resources you find relevant to the topic.

### 2. Reading and Understanding
- Skim through the paper to get an overview of the content.
- Read the abstract, introduction, and conclusion to understand the main objectives and findings.
- Dive deeper into the methodology, results, and discussion sections to grasp the details.
- Take notes, highlight important points, and mark any questions or areas that require further clarification.

A good approach here is to continually ask yourself several questions:
1. Describe what the authors of the paper aim to accomplish or perhaps did achieve.
2. If a new approach/technique/method was introduced in a paper, what are the key elements of the newly proposed approach?
3. What content within the paper is useful to you?
4. What other references do you want to follow?

### 3. Summarizing
- After reading the paper, summarize the key points in your own words.
- Include the research problem, methodology, main findings, and implications.
- Use bullet points or headings to organize the information logically.
- Be concise and focus on the most important aspects.

Summarize the paper by reciting it with your eyes closed, then repeatedly browse the paper and refine your summary. This way, you can quickly recall a paper in the future through your summary. A crucial point is to understand the motivation of a paper: from the results, look at what problems others are solving and why they are doing it.

### 4. Presenting to Teammates
- Prepare a presentation or document to share the summarized research with your teammates.
- Start with an introduction to the research topic and its relevance.
- Present the key points and findings in a clear and structured manner.
- Use visuals, such as graphs or diagrams, to enhance understanding.
- Encourage discussion and address any questions or concerns raised by your teammates.

In this process, the Feynman learning method is very effective: try to teach yourself what you've learned to gain a deeper understanding. From personal experience, this presentation usually takes place during the regular weekly team meetings. You can divide the presentation into several parts: 1. Framework 2. Content 3. Analysis of strengths and innovations 4. Limitations of the paper and your thoughts 5.

## Conclusion
By following these steps, you can effectively read, summarize, and present research papers. This will help you stay informed, contribute to your team's knowledge base, and foster meaningful discussions.