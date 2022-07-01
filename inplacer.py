import bpy


def main(context):
    print(bpy.data.collections['animations'].name)
    for obj in bpy.data.collections['animations'].all_objects:
        print("obj: ", obj.name)
        print(obj.pose.bones["mixamorig:Hips"])
        
        #get frame range of the animation
        first_frame = obj.animation_data.action.frame_range[0]
        first_frame = int(first_frame)
        frame_range = obj.animation_data.action.frame_range[1]
        frame_range = int(frame_range)
        frame_range +=1
        
        for i in range(first_frame, frame_range):

            #set current frame
            bpy.context.scene.frame_current = i

            #set Z location 0 for every keyframe

            obj.pose.bones["mixamorig:Hips"].location[2] = 0
            obj.pose.bones["mixamorig:Hips"].keyframe_insert(data_path="location", frame=i, index=2)
            obj.pose.bones["mixamorig:Hips"].location[2] = 0
            
            
            obj.pose.bones["mixamorig:Hips"].location[0] = 0
            obj.pose.bones["mixamorig:Hips"].keyframe_insert(data_path="location", frame=i, index=0)
            obj.pose.bones["mixamorig:Hips"].location[0] = 0
    
            #insert keyframe to make it permenant
#            bpy.ops.anim.keyframe_insert_menu(type='Location')

                            
            #go back to the first frame    
            bpy.context.scene.frame_current = first_frame


class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Simple Object Operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(SimpleOperator.bl_idname, text=SimpleOperator.bl_label)


# Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access).
def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(SimpleOperator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.simple_operator()
