import bpy, os

def Load_F(filename):
    tmp_data = []
    with open(filename) as f:
        tmp_data = f.readlines()
    class dmd_model:
        class __dmd_mesh: vertnum = 0; facenum = 0; verts = []; faces = []; normals = []
        class __dmd_material: diff_col = []; amb_col = []; spec_col = []; gloss = 0; opa = 0; diff = ""; bump = ""; spec = ""
        class __dmd_texture: vertnum = 0; facenum = 0; verts = []; faces = []
        mesh = __dmd_mesh(); material = __dmd_material(); texture = __dmd_texture()
    model = dmd_model()
    print("OK")
    mesh_inited, mat_inited, normals_inited, texture_inited    = False, False, False, False
    for i in range(len(tmp_data)):
        if not mesh_inited      and "TriMesh"       in tmp_data[i]: mesh_inited = i
        if not normals_inited   and "Smooth normals:"       in tmp_data[i]: normals_inited = i
        if not mat_inited       and "Material"      in tmp_data[i]: mat_inited = i
        if not texture_inited   and "New Texture"   in tmp_data[i]: texture_inited = i
    if mesh_inited:
        model.mesh.vertnum, model.mesh.facenum = [int(i) for i in (tmp_data[mesh_inited + 2]).split()]
        for i in range(model.mesh.vertnum):
            model.mesh.verts.append(tuple([float(i) for i in (tmp_data[mesh_inited + 4 + i]).split()]))
        for i in range(model.mesh.facenum):
            model.mesh.faces.append(tuple([int(i)-1 for i in (tmp_data[mesh_inited + 3 + model.mesh.vertnum + 3 + i]).split()]))
        if normals_inited:
            for i in range(model.mesh.vertnum):
                model.mesh.normals.append(tuple([float(i) for i in (tmp_data[normals_inited + 1 + i]).split()]))
    if mat_inited:
        for i in (range(len(tmp_data)))[mat_inited:] :
            if "diffuse color" in tmp_data[i]: model.material.diff_col = [int(i) for i in (tmp_data[i + 1]).split()]
            if "ambient color" in tmp_data[i]: model.material.amb_col = [int(i) for i in (tmp_data[i + 1]).split()]
            if "specular color" in tmp_data[i]: model.material.spec_col = [int(i) for i in (tmp_data[i + 1]).split()]
            if "glossiness" in tmp_data[i]: model.material.gloss = int(tmp_data[i+1])
            if "opacity" in tmp_data[i]: model.material.opa = int(tmp_data[i+1])
            if "diffuse map" in tmp_data[i]: model.material.diff = tmp_data[i+1]
            if "bump map" in tmp_data[i]: model.material.bump = tmp_data[i+1]
            if "specular map" in tmp_data[i]: model.material.spec = tmp_data[i+1]
            if "end material" in tmp_data[i]:  break
    if texture_inited:
        model.texture.vertnum, model.texture.facenum = [int(i) for i in (tmp_data[texture_inited + 2]).split()]
        for i in range(model.texture.vertnum):
            tmp_uv_tuple = [float(i) for i in(tmp_data[texture_inited + 4 + i]).split()]
            trimmed_uv = tuple((tmp_uv_tuple[0], tmp_uv_tuple[1])) # Cut_off 3-th coordinate
            model.texture.verts.append(trimmed_uv)
        for i in range(model.texture.facenum):
            model.texture.faces.append(tuple([int(i)-1 for i in (tmp_data[texture_inited + 3 + model.texture.vertnum + 3 + i]).split()]))
    return model
            
filename = r"C:\tmp\zdsim\routes\Шевченко-Пятихатки_2_0\models\tracks\1track.dmd"
#filename = r"D:\Program Files\ZDSimulator\routes\Москва-Калуга2_1_0\models\tracks\1track.dmd"
mesh_name = os.path.splitext(os.path.basename(filename))[0]
dmd_raw = Load_F(filename)
me = bpy.data.meshes.new(mesh_name)
me.from_pydata(dmd_raw.mesh.verts, [], dmd_raw.mesh.faces)
me.update(False, True)
ob = bpy.data.objects.new(mesh_name, me)
bpy.context.scene.objects.link(ob)

texFaces = []
for i in dmd_raw.texture.faces:
    texFaces.append(dmd_raw.texture.verts[i[0]])
    texFaces.append(dmd_raw.texture.verts[i[1]])
    texFaces.append(dmd_raw.texture.verts[i[2]])
me.uv_textures.new('uv')
for i in range(len(me.uv_layers.active.data)):
    me.uv_layers.active.data[i].uv = texFaces[i]
me.update(False, True)
