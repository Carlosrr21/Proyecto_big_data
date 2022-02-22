select 
	pp.entityid as ID,
	pp.attrvalue as valor,
	pp.attrname as campo,
	pp2.attrvalue as entidad,
	pp.recvtime as time
from 
	postgres.smartindustry.prensadora01_prensadora pp 
	left outer join 
	postgres.smartindustry.prensadora01_prensadora pp2
	on 
	pp.entitytype = pp2.entitytype 
	and 
	pp.entityid =pp2.entityid 
where
	pp.attrname in ('fuerza','temperatura')
	and 
	pp2.attrname='name'
	