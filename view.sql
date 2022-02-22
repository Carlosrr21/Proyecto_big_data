CREATE OR REPLACE VIEW public.prensadoras
AS SELECT mm.entityid AS id,
    cast(mm.attrvalue as integer) AS valor,
    mm.attrname AS campo,
    mm2.attrvalue AS entidad,
    mm.recvtime AS "time"
   FROM smartindustry.prensadora01_prensadora mm
     LEFT JOIN smartindustry.prensadora01_prensadora mm2 
     ON mm.entitytype = mm2.entitytype AND mm.entityid = mm2.entityid
     LEFT JOIN smartindustry.prensadora01_prensadora mm3
     ON mm.entitytype = mm3.entitytype AND mm.entityid = mm3.entityid
  WHERE mm.attrname = ANY (ARRAY['fuerza'::text]) AND mm2.attrname = 'name'::text 
  AND mm.attrname = ANY (ARRAY['temperatura'::text])