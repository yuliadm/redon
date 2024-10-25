from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from papers.models import Paper

app = FastAPI()

origins = [
    "http://localhost:4200",  # Allow your Angular app
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


papers: dict[str, Paper] = {
    "1104.3379v1": Paper(
            doi = "http://arxiv.org/abs/1104.3379v1",
            title = "Advanced Asymmetrical Supercapacitors Based on Graphene Hybrid Materials",
            authors=  ["Hailiang Wang", "Yongye Liang", "Tissaphern Mirfakhrai", "Zhuo Chen", "Hernan Sanchez Casalongue", "Hongjie Dai"],
            publication= "2011-04-18T04:42:30Z",
            summary ="Supercapacitors operating in aqueous solutions are low cost energy storage devices with high cycling stability and fast \
            Rcharging and discharging capabilities, but have suffered from low energy densities. Here, we grow Ni(OH)2 nanoplates and RuO2 \
            nanoparticles on high quality graphene sheets to maximize the specific capacitances of these materials. We then pair up a Ni(OH)2/\
            graphene electrode with a RuO2/graphene electrode to afford a high performance asymmetrical supercapacitor with high energy and \
            power densities operating in aqueous solutions at a voltage of ~1.5V. The asymmetrical supercapacitor exhibits significantly \
            higher energy densities than symmetrical RuO2-RuO2 supercapacitors and asymmetrical supercapacitors based on either \
            RuO2-carbon or Ni(OH)2-carbon electrode pairs. A high energy density of ~48Wh/kg at a power density of ~0.23kW/kg, \
            and a high power density of ~21kW/kg at an energy density of ~14Wh/kg have been achieved with our Ni(OH)2/graphene\
            and uO2/graphene asymmetrical supercapacitor. Thus, pairing up metal-oxide/graphene and metal-hydroxide/graphene hybrid materials for \
            asymmetrical supercapacitors represents a new approach to high performance energy storage."
    ), 
    "2301.01023":Paper(
            doi= 'http://arxiv.org/abs/2301.01023v1',
            title=' Performance investigation of supercapacitors with PEO-based gel polymer amp; ionic liquid electrolytes: Molecular Dynamics Simulation ',
            authors= ['Nasrin Eyvazi', 'Davood Abbaszadeh', 'Morad Biagooi', 'SeyedEhsan Nedaaee Oskoee'],
            publication= '2023-01-03T09:48:12Z',
            summary= '  Due to the importance of using supercapacitors in electronic storage devices, improving their efficiency is one of the topics that has attracted the attention of many researchers. Choosing the proper electrolyte for supercapacitors is one of the most significant factors affecting the performance of supercapacitors. In this paper, two classes of electrolytes, i.e. liquid electrolyte (ionic liquid electrolyte) and solid electrolyte (polymer electrolyte) are compared by molecular dynamics simulation. We consider the polymer electrolyte in linear and network configurations. The results show that although ionic liquid-based supercapacitors have a larger differential capacitance, since they have a smaller operation voltage, the amount of energy stored is less than polymer electrolyte-based supercapacitors. Also, our investigations indicate that polymer electrolyte-based supercapacitors have more mechanical stability. Therefore, they can be considered a very suitable alternative to liquid electrolyte-based supercapacitors that do not have known liquid electrolyte problems and display better performance.',
        ), 
    "1908.10494": Paper(
            doi= 'http://arxiv.org/abs/1908.10494v1',
            title=' A Systematic Study to Improve the Performance of SrCoO3 as anAnion-Intercalation-Type Electrode for Supercapacitors Through Interface,Oxygen Vacancies, and Doping ',
            authors= ['Sadhana Lolla', 'Xuan Luo'],
            publication= '2019-08-27T23:22:20Z',
            summary= '  Supercapacitors have recently gained popularity as possible energy storage systems due to their high cycling ability and increased power density. However, one of the major drawbacks of supercapacitors is that they have a low energy density, which makes them less effective than batteries. Herein, we explore different methods of increasing the supercapacitor performance of the perovskite SrCoO3. We carry out first-principles calculations to systematically study how SrCoO3/graphene interface, oxygen vacancies, and doping improve the performance of strontium cobaltite as an anion-intercalation-type supercapacitor. The results show that the SrCoO3/graphene interface is relatively stable with a formation energy of 1.3 eV and is highly conductive, which makes it a promising material for supercapacitors. We also find that inducing oxygen vacancies in SrCoO3 significantly increases the conductivity of this material. Results of doping calculations reveal that doping with Mo, V, P, and Nb all increase the stability and conductivity of SrCoO3. We find that niobium is the most stable and most conductive of all four dopants. In addition, we find that vanadium is a very promising novel dopant for SrCoO3 as an anion-intercalation-type supercapacitor electrode material. ',
            ), 
    "2006.01989": Paper(
        doi= 'http://arxiv.org/abs/2006.01989v1',
        title=' Suppressed self-discharge of an aqueous supercapacitor using Earth-abundant materials ',
        authors= ['Samuel Devese', 'Thomas Nann'],
        publication= '2020-06-03T00:16:19Z',
        summary= '  Supercapacitors (aka electrostatic double-layer capacitors -- EDLCs) offer excellent power storage capacity and kinetics, but suffer under rapid self-discharge. We introduced a zeolite framework into the active capacitor electrode, with the goal to tailor the free desorption energy and thus the self-discharge rate of supercapacitors. Low-cost carbonaceous materials and benchtop production methods were used to create supercapacitor electrodes with a measured specific capacitance of 17.25 F g$^{-1}$, a coulombic efficiency of 100%, and charge retention of over 25% over 24 hours determined by galvanostatic charge/discharge curve measurements. This charge retention was an enhancement of $\sim$350 compared with electrodes without zeolite coating. ',
    ),
    "2001.07429":Paper(
        doi= 'http://arxiv.org/abs/2001.07429v1',
        title=' One-step fabrication of flexible, cost/time effective and high energy storage graphene-based supercapacitor ',
        authors= ['Katayoon Gholami laelabadi', 'Rostam Moradian', 'Iraj Manouchehri'],
        publication= '2020-01-21T10:19:22Z',
        summary= '  The advances in micro-size and in-plane supercapacitors lead to produce the miniaturizing energy storage devices in portable and bendable electronics. Micro-supercapacitors have unique electrochemical performance, such as high power density, fast charging, long cycle life, and high safety. The reduction time and cost in the fabrication processes of micro-supercapacitors are important factors in micro-fabrication technology. In this work, a simple, scalable and cost-effective fabrication of interdigitated reduced graphene oxide@polyaniline flexible micro-supercapacitors is presented. We found that in fabricating the interdigitated microelectrode patterns on PET substrate; the reduction of graphene oxide and growth of conducting polymer are rapidly performed simultaneously in one step by laser irradiation. The capacitance was 72 mF/cm2 at 0.035mA/cm2 current density. These high capacitance micro-supercapacitors demonstrate good stability and more than 93.5 of the capacitance retain after 1000 cycles at 0.7 mA/cm2 current density. ',
    )

}

@app.get("/")
def root():
    return {"message": "My papers"}


# Route to add a item
@app.post("/papers/{doi}")
def add_paper(paper_doi: str, paper_authors: list[str], paper_title: str, paper_pub: str, paper_summary:str):
    doi = paper_doi
    papers[doi] = Paper(
        doi=paper_doi, title=paper_title, authors=paper_authors, publication = paper_pub, summary=paper_summary
    )
    return {"item": papers[doi]}



# Route to list a specific item by ID
@app.get("/papers/{doi}")
def list_paper(doi: str) -> dict[str, Paper]:
    if doi not in papers:
        raise HTTPException(status_code=404, detail="Paper not found.")
    return {"item": papers[doi]}


# Route to list all items
@app.get("/papers")
def list_papers() -> dict[str, dict[str, Paper]]:
    return {"items": papers}


# Route to delete a specific item by ID
@app.delete("/papers/{doi}")
def delete_paper(doi: str) -> dict[str, str]:
    if doi not in papers:
        raise HTTPException(status_code=404, detail="Item not found.")
    del papers[doi]
    return {"result": "Item deleted."}

