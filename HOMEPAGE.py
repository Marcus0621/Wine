# HOMEPAGE.py

import streamlit as st
from PIL import Image

def display_homepage():
    welcome_title = st.title("WELCOME TO THE WORLD OF WINE!")
    first_image = Image.open('WineIntro.jpg')
    image_placeholder = st.empty()
    caption_placeholder = st.empty()
    image_placeholder.image(first_image, caption='Image by 1Zoom', use_column_width=True)

def what_is_wine():
    st.title("WHAT IS WINE?")
    st.write("Wine is an alcoholic beverage that is made from fermented grapes or other fruits. The fermentation process involves the conversion of sugars present in the fruit into alcohol and carbon dioxide, typically through the action of yeast. Wine has been produced and enjoyed by various cultures for thousands of years and holds cultural, social, and culinary significance in many societies.")
    st.write("The process of making wine including: Harvesting, Crushing, Pressing, Fermentation, Racking, Aging, Blending, Clarification, Bottling, Labeling and Packaging")
    
def making_process():
    st.title("1. Harvesting")
    harvest_image = Image.open('harvest.jpg')
    image_placeholder = st.empty()
    caption_placeholder = st.empty()
    image_placeholder.image(harvest_image, caption='Image by BELL WINE CELLAR', use_column_width=True)
    st.write("Harvesting in winemaking is a precise moment when grapes attain peak ripeness, a juncture that holds the key to the quality and character of the eventual wine. The decision of when to harvest is pivotal, shaping critical components such as sugar levels, acidity, and flavor intricacies within the grapes.")
    st.write("The process is a delicate dance between various factors. The grape variety serves as a foundational element, each type boasting its unique maturation timeline. Climate conditions, encompassing temperature, sunlight exposure, and precipitation patterns, exert a significant influence on the grapes' development trajectory. This interaction with the terroir, coupled with the desired style of the wine, drives the timing of the harvest. Grapes harvested earlier maintain heightened acidity, yielding wines with vivacity and brightness, while delayed harvests result in higher sugar content, fostering full-bodied wines with elevated alcohol potential.")
    st.write("Guided by intuition and expertise, winemakers ensure that the grapes are gathered precisely when all elements coalesce to achieve the desired flavor profile. The harmony between grape variety, climate, and wine style orchestrates this temporal intersection, underscoring the crucial role of timing in translating the vineyard's essence into the forthcoming vinification journey.")
    

    st.title("2. Crushing")
    crush_image = Image.open('crush.png')
    image_placeholder = st.empty()
    caption_placeholder = st.empty()
    image_placeholder.image(crush_image, caption='Image by WineMaker', use_column_width=True)
    st.write("Crushing, an essential facet of winemaking, involves gently breaking harvested grapes to extract their juice, initiating the transformation from grape to wine. In modern practices, mechanical crushers are prevalent, gently rupturing grape skins to release juice while minimizing undesirable tannin extraction. This mechanization ensures controlled and efficient juice extraction, a key consideration for large-scale production.")
    st.write("Yet, traditional methods like foot stomping retain allure. This tactile approach allows for nuanced extraction, potentially enhancing wine quality through gentler juice release. However, irrespective of the method, the core purpose of crushing is to unleash a harmonious interplay between grape solids and juice. This interaction contributes color, aroma, flavor compounds, and structural elements that shape the wine's identity.")
    st.write("The choice between modern efficiency and traditional artistry, along with decisions regarding stem inclusion, impacts the final wine's character. From this initial phase, the grape's potential comes to light, laying the foundation for subsequent stages like fermentation and aging. Crushing, in its humble beginnings, sets the stage for the captivating journey of winemaking.")

    st.title("3. Pressing")
    press_image = Image.open('press.jpg')
    image_placeholder = st.empty()
    caption_placeholder = st.empty()
    image_placeholder.image(press_image, caption='Image by NATURAL VINE', use_column_width=True)
    st.write("Building upon the initial crushing of grapes to extract their precious juice. After the grapes have been gently crushed, pressing involves the deliberate application of pressure to further extract the remaining juice from the grape solids. This step significantly impacts the quality, quantity, and style of the resulting wine.")
    st.write("During pressing, the must, a mixture of juice, skins, seeds, and pulp, is subjected to pressure to release additional juice. The amount of pressure applied, along with the number of pressings performed, varies according to the winemaker's vision and the desired characteristics of the wine. The first pressings yield the highest-quality juice, known as 'free-run juice', which is often separated from subsequent pressings due to its superior purity.")
    st.write("The decision of how much pressure to exert and which press fractions to use requires careful consideration. While gentle pressing can minimize the extraction of bitter tannins, prolonged or intense pressing can introduce undesirable astringency. Pressing also influences the wine's color, as pigments from the grape skins are released. The skilled winemaker employs pressing as an artful balance between optimizing juice extraction and preserving the delicate flavors, aromas, and structural components that define the wine's identity.")


    st.title("4. Fermentation")
    ferment_image = Image.open('ferment.jpeg')
    image_placeholder = st.empty()
    caption_placeholder = st.empty()
    image_placeholder.image(ferment_image, caption='Image by brewsy', use_column_width=True)
    st.write("Fermentation stands as a transformative cornerstone in winemaking, where grape juice evolves into wine under the influence of yeast. This intricate process converts sugars within the juice into alcohol and carbon dioxide, unlocking a symphony of flavors and aromas. The magic of fermentation unfolds as yeast, both naturally occurring or deliberately added, consumes sugars, releasing heat and metabolic byproducts that shape the wine's character.")
    st.write("During fermentation, grape juice—referred to as 'must'—is transferred into specialized vessels, such as tanks or barrels. Yeast is introduced to the must, commencing the fermentation journey. As yeast consumes sugars, alcohol levels rise, and carbon dioxide gas is released as a delightful byproduct. The temperature at which fermentation occurs plays a pivotal role, influencing the speed of fermentation and the resulting wine's flavor profile. Cooler temperatures might retain vibrant fruitiness, while warmer temperatures can encourage more robust flavors and aromas.")
    st.write("Fermentation's complexities go beyond the chemical transformation. Winemakers often monitor and adjust variables like temperature, yeast strains, and nutrient levels to guide the process toward desired outcomes. A skillful balance of science and artistry shapes the fermentation process, leading to wines with unique nuances that carry the fingerprint of both the grapes and the winemaker's careful choices.")

    st.title("5. Racking")
    rack_image = Image.open('rack.jpg')
    image_placeholder = st.empty()
    caption_placeholder = st.empty()
    image_placeholder.image(rack_image, caption='Image by Sonoma Wine Garden', use_column_width=True)
    st.write("Racking is a refining step in winemaking, occurring after fermentation, that contributes to a wine's clarity, purity, and overall quality. This process involves transferring the wine from one vessel to another, leaving sediment and unwanted particles behind. Racking plays a crucial role in clarifying the wine, eliminating impurities, and preparing it for further maturation or bottling.")
    st.write("Once fermentation concludes, the wine often contains sediments, spent yeast cells, and other solids that can cloud the liquid and affect its taste. Racking addresses this by carefully siphoning the clear wine off the sediments, allowing the wine's natural brilliance to shine. It not only clarifies the wine but also helps mitigate off-flavors associated with decomposing yeast.")
    st.write("Winemakers may choose to rack the wine multiple times to ensure thorough clarification. The timing and frequency of racking depend on the wine's style and the winemaker's preference. While modern filtration methods can achieve similar outcomes, racking is often favored for its gentler treatment of the wine. This meticulous process underscores the commitment to crafting wines that showcase purity and finesse, creating a foundation for the wine's journey toward maturation and, eventually, enjoyment.")

    st.title("6. Aging (Optional)")
    age_image = Image.open('age.jpg')
    image_placeholder = st.empty()
    caption_placeholder = st.empty()
    image_placeholder.image(age_image, caption="Image by Winemaker's Academy", use_column_width=True)
    st.write("Aging is a transformative journey that shapes a wine's complexity, character, and depth over time. This patient process occurs after fermentation, allowing the wine to mature and evolve. Wines can be aged in various vessels, such as oak barrels, stainless steel tanks, or even the bottle itself. Each container imparts distinct qualities to the wine.")
    st.write("Oak aging, a common method, infuses wines with flavors, aromas, and textures from the wood. The type of oak and its toasting level influence the degree of influence on the wine. Stainless steel tanks maintain freshness, preserving the wine's primary fruit flavors. Throughout aging, chemical reactions continue, refining tannins, melding flavors, and enhancing aromatic nuances.")
    st.write("The duration of aging varies based on factors like grape variety, intended style, and the winemaker's vision. Shorter aging may retain fruit-forward characteristics, while extended aging can foster tertiary aromas and a velvety texture. The artistry of aging lies in knowing when to bottle the wine, capturing the perfect moment to share a crafted masterpiece that reflects the interplay between time, grape, and vessel.")

    st.title("7. Blending (Optional)")
    blend_image = Image.open('blend.jpg')
    image_placeholder = st.empty()
    caption_placeholder = st.empty()
    image_placeholder.image(blend_image, caption='Image by Winemaker Matt', use_column_width=True)
    st.write("Blending in winemaking is not mandatory but is often employed as a valuable technique to enhance the final product. The decision to blend wines is contingent upon several factors, including the winemaker's intent, the grape varieties involved, the vintage, and the desired style of the wine.")
    st.write("This process involves carefully combining wines made from various grape varieties, vineyards, or vintages to craft a final product that surpasses the sum of its parts. Winemakers leverage blending to achieve a desired flavor profile, balance, and consistency.")
    st.write("The art of blending offers winemakers a palette to create wines that possess complexity, depth, and unique identities. This practice is particularly prevalent in regions where multiple grape varieties are cultivated, allowing winemakers to marry different qualities to create a cohesive and enchanting experience. Blending provides flexibility to enhance wine attributes, tempering bold elements with subtleties, and rectifying any imbalances that may have arisen during the winemaking process.")

    st.title("8. Clarification (Optional)")
    clarify_image = Image.open('clarify.jpg')
    image_placeholder = st.empty()
    caption_placeholder = st.empty()
    image_placeholder.image(clarify_image, caption='Image by Grapes & Grains', use_column_width=True)
    st.write("Clarification is a refining process in winemaking aimed at enhancing a wine's visual clarity, stability, and overall sensory experience. After fermentation and other early stages, wines often contain particles, sediment, and haze that can impact appearance and flavor. Clarification methods, such as fining and filtration, address these issues.")
    st.write("Fining involves introducing fining agents, such as bentonite or egg whites, into the wine. These agents attract and bind to unwanted particles, causing them to settle and be removed. Filtration, on the other hand, physically removes particles by passing the wine through a series of filters. Both methods result in a clearer, visually appealing wine.")
    st.write("Clarification not only improves aesthetics but also ensures the wine's stability and reduces the risk of spoilage or off-flavors. While these processes can modify the wine's composition slightly, skillful application helps maintain the wine's intended flavor and aromatic profile. Winemakers carefully balance the benefits of clarification with the desire to preserve the wine's unique qualities, ultimately aiming for a visually appealing and satisfying final product.")

    st.title("9. Bottling")
    bottle_image = Image.open('bottle.jpg')
    image_placeholder = st.empty()
    caption_placeholder = st.empty()
    image_placeholder.image(bottle_image, caption='Image by Karissa', use_column_width=True)
    st.write("Bottling, the culmination of the winemaking journey, involves transferring the finished wine into bottles for distribution and consumption. This crucial stage requires meticulous care to maintain the wine's integrity. Prior to bottling, winemakers may add a small amount of sulfur dioxide to preserve freshness and prevent spoilage. Bottles are sealed with corks, screw caps, or other closures.")

    st.title("10. Labeling and Packaging")
    pack_image = Image.open('pack.jpg')
    image_placeholder = st.empty()
    caption_placeholder = st.empty()
    image_placeholder.image(pack_image, caption='Image by 43oz', use_column_width=True)
    st.write("Labels and packaging materials are applied, conveying essential information about the wine's origin, vintage, and winemaker. Bottling marks the transformation from liquid potential to a tangible embodiment of the winemaker's artistry, ready to delight enthusiasts and tell the story of its creation., and the wine is ready for distribution and consumption.")
