# Research & Development Optimization and Navigation (ReDON) System
ReDON is a virtual assistant designed to streamline the discovery and analysis of available research re-sources devoted to a narrow high-tech topic. It incorporates state-of-the-art web crawling, NLP, and graph-based NNs to find, filter, and organize vast quantities of information from scholarly articles, pa-tents, and online sources. 

## Motivation

The field of high-tech research has seen rapid growth. Researchers and engineers are often faced with the challenge of sifting through vast amounts of scientific literature, patents, and technical blogs to extract relevant, high-quality insights. The time-consuming nature of this process hinders innovation and decision-making. An effective solution for navigating inventors seamlessly through all stages of R&D process by equipping them with the most relevant, verified and precise information and to the point reccomendations will allow to reduce the time and effort required for literature review, allowing researchers to focus on practical experimentation.

## Description

ReDON is a virtual assistant designed to streamline the discovery and analysis of available research re-sources devoted to a narrow high-tech topic. It incorporates state-of-the-art web crawling, natural lan-guage processing (NLP), and graph-based neural networks to find, filter, and organize vast quantities of information from scholarly articles, patents, and online sources. The assistant will be equipped with ad-vanced filtering capabilities (e.g. filtering out articles with weak grammar or low-quality writing, citation and reputation checks, time decay factor) to remove low-quality or outdated sources, ensuring that only the most relevant and reliable materials are considered. By leveraging graph attention networks (GATs) and citation-based ranking mechanisms, the assistant will not only categorize information by topics (such as materials, assembly techniques, and practical applications) but also highlight connections between dif-ferent research areas, visualizing their influence and relevance to the user's specific query. Researchers can use the assistant to receive an ordered selection of the most relevant papers and practical schemes, enabling faster, more informed decision-making. This VA has the potential to accelerate the design and development of new high-tech devices by providing a systematic, structured approach to navigation through the complex landscape of scientific knowledge. Ultimately, the virtual assistant can serve as a critical aid for researchers, reducing the time spent on literature reviews, improving research quality, and enhancing innovation.

## Data

The prototype version will be based on the ArXiv papers. 
At the second development stage the database will be expanded to include Google Scholar and Google Patents.
At later stages it will also incorporate information from technical blogs and websites (for these, the rate-limiting and legal aspects of web scraping should be taken into consideration).

## Tools

Devtools: VSCode, Flask, BeautifulSoup, API Access: Google Patents, ArXivGoogle Scholar API keys, Hugging Face Transformers, NLTK, word2vec, TF-IDF, PyTorch Geometric (PyG), NetworkX, Pandas, NumPy, Matplotlib
Models: Graph Neural Networks, Transformers, BERT
Technologies: Heroku, Google Cloud Storage, AWS S3

## Computing Platform 

Renku

## Further Development, Support, Availability, Communication

1. Enhance and Expand Features
	• Refinement of AI models: Expand the capabilities of GNN (Graph Neural Network) models or use other AI architectures like transformer models for more accurate content extraction and analysis, improve language understanding and natural language processing (NLP) for handling more detailed user requests and returning more accurate results.
	• Domain expansion: Initially focused on supercapacitors, your assistant could be adapted to cover other areas of energy storage, materials science, or electrical engineering (Batteries, Fuel Cells and Energy Harvesting).
	• Automated experiment suggestion: Once your tool has built enough knowledge of the research landscape, you could integrate functionality to suggest new experiments, designs, or prototypes based on the latest research trends, patents, and materials science advancements.
	• Visualization and interface improvements: Improve how your virtual assistant displays data, such as interactive citation graphs, knowledge maps, develop a straightforward user-friendly customizable interface.

2. Open-Source Contributions and Community Building
	• Create an Open-Source Community: encourage developers to contribute, extend the capabilities, and build a larger community around your project, develop a feedback loop , engage with users via forums, blogs, or social media.
	• Public outreach: publish papers, case studies, blog posts, describing the architecture, model development, and real-world applications, present at engineering and ML conferences.
	• Educational application: adding features and enhancing explainability to use ReDON as a tool for educational institutions (for students studying energy storage or materials science).


3. Scaling Up and Industrial Application
	• Enterprise version: develop a larger-scale version with extended features that can handle larger datasets, integrate with proprietary company databases, and provide advanced analytics on specific supercapacitor-related R&D projects.
	• Data-driven prototyping: integrate your assistant into prototyping platforms for providing real-time recommendations during the design and production phases, suggesting the most optimal materials and configurations.
	• Industry collaboration: reach out to supercapacitor manufacturers, automotive companies, and battery manufacturers.
	• Government initiatives: collaborate with government energy initiatives or national labs.
