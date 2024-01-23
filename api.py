from dotenv import load_dotenv

from gpt import parse_response
from article import ArticleProcessor


# Usage:
article_processor = ArticleProcessor()
article_content = """Summarise this article in 3 to 4 sentences and also give me a translation of the summary in italian:
# EDF's nuclear project in Britain pushed back to 2029, may cost up to $34 bln
# January 23, 20247:49 PM GMTUpdated 15 min ago
# Workers at the nuclear reactor area under construction, are seen at Hinkley Point C nuclear power station site, near Bridgwater
# PARIS, Jan 23 (Reuters) - French utility EDF said on Tuesday it was pushing back the start date on its Hinkley Point C reactor project in Britain to 2029, with a new estimated cost of between 31 billion and 34 billion pounds ($43.06 billion) in 2015 values.

# The plant, in southern England, was previously expected to start operations in June 2027, with an estimated cost of 25 billion to 26 billion pounds.

# The delay marks the latest blow to the project which is part of Britain's efforts to increase its nuclear energy capacity. The plant was initially scheduled to open in 2025 at a cost then estimated at 18 billion pounds.

# Advertisement · Scroll to continue
# EDF said that the new target date is based on current productivity goals as the company shifts to the ramp-up of electromechanical work, following the installment of the dome on unit one in December.

# The electromechanical work follows the basic building phase, where the contractor switches from tasks like pouring concrete to wiring and setting up the reactor.

# There are two other possible scenarios, EDF said, with the first seeing a delay until 2030 with the same cost. The other scenario envisages that the project will be postponed until 2031 and cost around an additional 1 billion pounds to 35 billion pounds in 2015 values.

# Advertisement · Scroll to continue
# The group said that 70% of the equipment that is expected to be installed in the first unit has been delivered to the site.

# Other similar projects in Flamanville, France, and Olkiluoto, Finland were also delayed and faced big increases in costs.

# ($1 = 0.7895 pounds)

# Advertisement · Scroll to continue
# Reporting by Forrest Crellin and Benjamin Mallet. Editing by Jane Merriman

# Our Standards: The Thomson Reuters Trust Principles.

# Acquire Licensing Rights"""

api_response = article_processor.summarize_and_translate(article_content)
parsed_response = parse_response(api_response)
for choice in parsed_response.choices:
    print(choice.message.content)
