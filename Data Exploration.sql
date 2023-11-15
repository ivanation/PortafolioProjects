
-- Select Data that we are going to be using

SELECT location, DATE, total_cases, new_cases, total_deaths, population
FROM coviddeaths
WHERE continent IS NULL 
ORDER BY 1,2

-- Looking at total cases vs total deaths

SELECT location, DATE, total_cases, total_deaths, (total_deaths / total_cases)*100 AS DeathPercentage
FROM coviddeaths
WHERE location LIKE '%states%'

-- Looking at total cases vs population

SELECT location, DATE, total_cases, population, (total_cases / population )*100 AS PopulationPercentage
FROM coviddeaths
WHERE location LIKE '%states%'
ORDER BY 1,2

-- Looking at country with highest infection rate compared to population

SELECT location, population, MAX(total_cases) AS HighestInfectionCount, MAX((total_cases / population )*100) AS PopulationInfectedPorcent
FROM coviddeaths
GROUP BY location, population
ORDER BY PopulationInfectedPorcent DESC

-- Looking at countries with highest death count per population

SELECT location, population, MAX(total_deaths) AS HighestDeathsCount, MAX((total_deaths / population )*100) AS PopulationDeathsPorcent
FROM coviddeaths
GROUP BY location, population
ORDER BY PopulationDeathsPorcent DESC

-- Looking at countries and continents with highest death count

SELECT location, MAX(cast(total_deaths AS INT)) AS HighestDeathsCount
FROM coviddeaths
WHERE continent IS NOT null
GROUP BY location
ORDER BY HighestDeathsCount DESC

-- Looking at continents with highest death count

SELECT continent, MAX(cast(total_deaths AS INT)) AS HighestDeathsCount
FROM coviddeaths
WHERE continent IS NOT NULL
GROUP BY continent
ORDER BY HighestDeathsCount DESC

-- global numbers

Select SUM(new_cases) as total_cases, SUM(cast(new_deaths as int)) as total_deaths, SUM(cast(new_deaths as int))/SUM(New_Cases)*100 as DeathPercentage
FROM coviddeaths
WHERE continent IS NOT NULL

-- looking at the population vs vaccinations

Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
From coviddeaths dea
Join covidvaccinations vac
On dea.location = vac.location
and dea.date = vac.date
where dea.continent is not null

-- use cte

With PopvsVac (Continent, Location, Date, Population, New_Vaccinations, RollingPeopleVaccinated)
as
(
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(int,vac.new_vaccinations)) OVER (Partition by dea.Location Order by dea.location, dea.Date) as RollingPeopleVaccinated
--, (RollingPeopleVaccinated/population)*100
From coviddeaths dea
Join covidvaccinations vac
	On dea.location = vac.location
	and dea.date = vac.date
where dea.continent is not null 
--order by 2,3
)
Select *, (RollingPeopleVaccinated/Population)*100
From PopvsVac



-- Using Temp Table to perform Calculation on Partition By in previous query

DROP Table if exists #PercentPopulationVaccinated
Create Table #PercentPopulationVaccinated
(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric
)

Insert into #PercentPopulationVaccinated
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(int,vac.new_vaccinations)) OVER (Partition by dea.Location Order by dea.location, dea.Date) as RollingPeopleVaccinated
From coviddeaths dea
Join covidvaccinations vac
	On dea.location = vac.location
	and dea.date = vac.date

Select *, (RollingPeopleVaccinated/Population)*100
From #PercentPopulationVaccinated




-- Creating View to store data for later visualizations

Create View PercentPopulationVaccinated as
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(int,vac.new_vaccinations)) OVER (Partition by dea.Location Order by dea.location, dea.Date) as RollingPeopleVaccinated
From coviddeaths dea
Join covidvaccinations vac
	On dea.location = vac.location
	and dea.date = vac.date
where dea.continent is not null 







