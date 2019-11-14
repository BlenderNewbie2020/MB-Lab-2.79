# MB-Lab 2.79

MB-Lab 2.79 is initially intended to be a solo project, base on animate1978's reboot of ManuelBastioniLAB, reset to 1.6.5b

## Blender 2.79 Only

For use with the latest version of Blender 2.79 from the Arch Linux repositories, or other recent source.

TODO:

Backport to 2.79
Is it possible to maintain a single codebase that works for both Blender 2.7 and 2.8? (Yes).

c.f. https://theduckcow.com/2019/update-addons-both-blender-28-and-27-support/

https://www.youtube.com/watch?v=W8PxOFA6AFo




# Previous ReadMe

# MB-Lab

MB-Lab is an attempt to keep the ManuelBastioniLAB Blender addon alive through community efforts.

## Contributors wanted! Python programmers needed!

Manuel Bastioni is active in open source projects since 1999.

Member of Blender Artist community since 2002.

He was one of the authors of "The Official Blender 2.3 guide, the open 3D creation suite", writing the chapter "From Blender to YafRay Using YableX"

In 2000 he started Makehuman Project, a free and open source software for the modelling of 3d photo-realistic characters, winner of "Suzanne Award" as the best python script for Blender 3D in 2004. He left the MakeHuman project in 2016.

He is the author of Manuel Bastioni Laboratory, a free and open source add-on for Blender to create 3d humanoids. It includes the results of years of prototyping and studies realized by him during the development of his 3d graphics projects.

## MB-Lab 1.6.5 Notes

    New shader network based on Principled BSDF for skin, eyes and teeth
    New texture maps for specular and sub dermal
    Additional code to load new texture maps into right image texture node
    Added references to new texture maps in the character config JSON file for all character types
    Changed Skin Editor values to reflect new PBR shading network


## Release notes for ManuelBastioniLAB 1.6.1

The version 1.6.1 of ManuelbastioniLAB, the free and open source character editor for Blender, is still available for download at http://www.manuelbastioni.com

## New features

    Assets library, with four hair models
    Automatic transfer of rigging weights from body to proxy
    Improvement of human base models
    Improvement of proxy fitting process using a subset of polygons
    Human hair shader for Cycles
    Toon hair shader for Cycles
    Custom name for finalized characters
    Expressions parameter for eyes rotations

## Bug fixed

    Less restrictive version check to run in Blender vers. > 2.79.0
    Fixed bug in hidden IK control
    Fixed bug in save custom poses
    Fixed bug in rest pose loading
    Fixed bug in proxy reset
    Fixed "red eyes" bug
    Fixed a bug in expressions with multiple characters in the same scene

